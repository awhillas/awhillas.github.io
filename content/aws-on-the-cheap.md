---
Title: AWS on the Cheap(ish)
slug: aws-on-the-cheap
summary: Remember when it was still cheap to have a side web project and it cost you a pittance so you could experiment and the web was a lot more diverse? I do. But those days are gone since we all moved to the cloud. Here is an experiment in deploying to AWS for as little as possible in the hopes of keeping the web weird.
date: 2024-05-06
Modified: 2024-05-20
Category: Software Engineering, Web Development
---

**TL;DR**: You can't do a dynamic website on AWS on the cheap. I op'ed for a K3s cluster on a Raspberry Pi instead on my local network. Cheap and I can scape it up if the projects go anywhere as it will not require much compute or storage.

# AWS on the Cheap(ish), A Journey

Since Heroku is was bought by Salesforce, I've been looking for a new place to host my side projects. Surely in the age of the cloud it must be cheaper than ever to host a small web app, right? This is my experiment in deploying to AWS for as little as possible in the hopes of keeping the web weird.

## But why a "journey"?

Well i thought it might be useful to people to see my decision processes instead of just the final result. This might be useful to junior engineers and training LLMs. Why do I care about the latter? I guess I realise that the future is LLMs and I hope they get better.

## Approach 1: ECS with Fargate

So my first attempt was using ECS with Fargate deployments and an application load balancer (ALB). This was a bit of a disaster. The ALB alone was going to cost me $20 a month! Its not wonder they are featured in every ECS example setup you find. _EVERYONE SINGLE ONE_. But they are completely unnecessary. The ECS service, which is a rip off of Kubernetes does exactly the same thing. So the hard part was figuring how to point a Route 53 domain to an ECS service.

I found Aidan Steele's blog post [Cheap serverless containers using API Gateway](https://awsteele.com/blog/2022/10/15/cheap-serverless-containers-using-api-gateway.html) which is genius (he even suggests Fargate spot instances for even cheaper deployments)! ...if not unfortunate in that he outlines the whole setup in a CloudFormation template. I'm not a fan of CloudFormation. I prefer CDK. So I set out to replicate his setup in CDK.

But CDK is tedious! Thank god for LLMs! They can convert a CloudFormation template to CDK code. I have 4 at my disposal but which one(s) should I choose. I don't have all day and based on the [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html) and [CanAiCode Leaderboard](https://huggingface.co/spaces/mike-ravkine/can-ai-code-results) (at this time 20/5/24) GPT-4-Turbo (April 2024) and [CodeLlama-Instruct](https://www.meta.ai/) respectively are the bast at this point in time. Given that OpenAI seems to be the best most of the time (somehow) and Meta just finished training their latest Llama 3 model its what I'd expect. Actually, GPT-4o is just out and supposedly better, faster and cheaprer than vanilla GPT-4 I'll use that one instead.


### The prompts

Here are the prompts I gave to the LLMs:

#### The infrastructure stack
```
I need a CDKv2 stack, written in python, that sets up the infrastructure for a second stack. This first stack should:

- A VPC and its associated subnets, route tables, etc.
- A Route 53 hosted zone for your DNS records
- An ACM-managed TLS certificate (used by API Gateway later)
- An API Gateway VPC Link and its security group. This is how API GW “reaches in” to the container running in your VPC.
- A Cloud Map namespace.

Import from . import VPC_ID, and HOSTED_ZONE_ID and use them instead of createing a VPC and a new hosted zone.
```
# The project stack
```
Create a second stack that is passed the infrastructure stack to deploy a containerized web app. This second stack contains everything specific to a single application hosted on example.com. You would deploy multiple stacks from this template, one for each serverless app you have developed. It contains:

- An ECS task definition
- IAM roles for your ECS task definition
- A CloudMap service. This holds the IP addresses of your running containers
- An ECS service. This runs one copy of your task and registers/deregisters Fargate IPs with the CloudMap service when tasks start and stop.
- A security group for your ECS service that only allows the VPC link to make requests to it.
- An API gateway that forwards all requests to the CloudMap service via the VPC link.
- An API Gateway API mapping and Route 53 record to make your API accessible at my-app.example.com.

Note that the ECS task definition contains a health check. This is because API Gateway itself doesn’t perform health, have ECS run curl inside the container.
```

## Results: Too hard

I gave up. This is to esoteric and if it breaks I have no way to change or improve it. CDK has become almost as complicatd as the thing its trying to replace i.e. CloudFormation. I'm going to try a different approach.

Now that I think of it I really don't need this infrastructure-as-code thing right now. Since its a tiny side project I'm going to fight my instincts to do it the enterprise way and do the opposite:

- EC2 instance I'm setting up and running by hand. I just need something up and running fast and cheap.
- K3s to deploy with.
  - I find k8s YAML much easier to understand than CDK or CloudFormation even after coming back to it after a couple of years.
  - There are also waaaay more examples out there.
  - Need something to restart the containers if they fall over.
  - I prefer it to Docker as you can do ingress routing based on domain name which i want to do as I'll deploy multiple (side projects) apps to the same cluster.


So starting with [K3s Cluster on AWS EC2](https://subbaramireddyk.medium.com/k3s-cluster-on-aws-ec2-206893ab968a). Which worked like a charm (after an unmentioed reboot).

### Perfect Django Dockerfile

Next step is to containerize my Django app. There was a [conversation on the django subreddit](https://www.reddit.com/r/django/comments/njt7b3/the_perfect_python_dockerfile_better_performance/) about exactly this "3y ago". On that thread I found this [Dockerfile](https://github.com/nickjj/docker-django-example/blob/main/Dockerfile) which makes a good starting point (the forst half is building the frontend framework, which I'm not doing). So here is my version of it:

```Dockerfile
FROM python:3.9-slim-bookworm AS app

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean \
    && groupadd -g "${GID}" python \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
    && mkdir -p /public_collected public \
    && chown python:python -R /public_collected /app

USER python

COPY --chown=python:python requirements.txt ./

RUN pip3 install --no-warn-script-location --no-cache-dir --user -r requirements.txt

ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python" \
    DJANGO_SETTINGS_MODULE="config.production"

COPY --chown=python:python . .

RUN if [ "${DEBUG}" = "false" ]; then \
    python3 manage.py collectstatic --no-input; \
    else mkdir -p /app/public_collected; fi

EXPOSE 5555

CMD ["gunicorn", "-b", "0.0.0.0:5555", "-w", "4", "--worker-tmp-dir", "/dev/shm", "mindikatta.wsgi"]
```
which I had to remove all the special user stuff as k3s was bugging out with write permissions to the volume if it wasn't root. So
```Dockerfile
FROM python:3.9-slim-bookworm AS app

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    DJANGO_SETTINGS_MODULE="config.production"

COPY . .

EXPOSE 3000

CMD ["gunicorn", "-b", "0.0.0.0:3000", "-w", "4", "--worker-tmp-dir", "/dev/shm", "mindikatta.wsgi"]
```
So much simpler!

### k3s deployment

So I have a nice containerized Django app. Now I need to deploy it to my k3s cluster. Tricky parts are I need to make the ingress to the app only happen for a certain domain name. Also need to put the database connection string in a secret. I'll start with the secret.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: myapp-database-secret
  namespace: myapp
type: Opaque
stringData:
  database_url: "postgres://<username>:<password>@<location>:5432/postgres"
```
Also need to create a secret so k3s can access a private image on docker hub. Just do this using the kubectl command line.
```bash
kubectl create secret docker-registry dockerreg --docker-server=docker.io --docker-username=someone --docker-password=a_password --docker-email=somebody@example.com --namespace myapp
```
Finally the deployment that pulls the image to make the pod, the service and sets up the ingress.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
  namespace: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: someone/myapp
          imagePullPolicy: Always
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: myapp-service
  name: myapp-service
  namespace: myapp
spec:
  ports:
    - name: "5555-80"
      port: 5555
      protocol: TCP
      targetPort: 80
  selector:
    app: myapp
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    ingress.kubernetes.io/ssl-redirect: "false"
  namespace: myapp
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp-service
                port:
                  number: 5555
```
AAAAAAAAAAAAAAAAnd, it doesn't work 😬

Getting 502 Bad Gateway. After scratching my head for 48 hours I did a search for "k8s Django deployment" and found this heavenly repo [django-kubernetes](https://github.com/mukulmantosh/django-kubernetes/tree/main) 👼 Trick is to stick an `ngix` in front of the `gunicorn`. Even has jobs to run to do the collect static assets!