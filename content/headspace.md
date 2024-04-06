---
Title: Project: Headspace
summary: A new type of interface to data and media which takes ideas from Pure-data/Max-MSP and online whiteboard spaces like Miro while at the same time leveraging linked-data
date: 2024-03-31
Modified: 2024-04-06
Category: Software Engineering
---

# 6th April, 2024 - My Kingdom for a Hypermedia backend!

I realised that if I'm going to the hypermedia route I'm going to be doing a lot of backend again like the good old days. It also occurred to me that FastAPI is not really optimised for hypermedia but instead JSON APIs. So ether I go back to [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/), but Django is very heave and mainly for setups with a database as the main driver of the content. I'm mainly using the file system(s), until I have to start to manage logins that is, which I should perhaps just think about from the begging since collaboration is going to be a big part of Headspace.

By hypermedia doesn't care what your backend is written in so I was flirting with the idea of using Rust? Most of these opinions I git from [a Reddit post](https://www.reddit.com/r/rust/comments/18ogwtl/which_web_framework_do_you_use_in_rust/).

- Rust web frameworks:
    - [Poem](https://docs.rs/poem/latest/poem/): "sits somewhere between a focused micro-framework and a full-featured "batteries included" framework. I like the API design, it uses strong typing well to increase correctness and ergonomics, but without getting too crazy to keep things simple." & "it just doesn't get enough love and fast enough bugfixes" also "hard-to-google name"
    - [Rocket](https://rocket.rs/): "Rocket is great with all of the bells and whistles but it's heavy use of macros, while it makes things easy, requires you to jump into the documentation more to look up the correct way to do things."
    - [Axum][https://docs.rs/axum/latest/axum/] "Axum is light and flexible, you can usually guess correctly how to do things without popping into the docs too often because it just works how you'd expect. But that is also because how you expect it to work is usually "build the thing yourself or use another crate".
        - [Loco](https://loco.rs/) - Loco follows Rails. There, I said it. Rails concepts are carefully adapted to modern Rust development. (I don't like Rails, convention over configuration :@ Try remebering convention after 6 months!)
- HTML Templating in Rust:
    - [maud](https://maud.lambda.xyz/): light weight macro, Pug like, for writing html templates
    - [minijinja](https://docs.rs/minijinja/latest/minijinja/) jinja templates in Rust!

But I'm kidding myself. Using Rust for this will just slow me down... Flask it is...

## Now using htmx Boosting

So if you include the htmx CDN file in your page and then turn bosting by putting `hx-boost="true"` in the body tag of your page all the links on you page go AJaX and your page body is swapped out instead of a page reload. No extra work required!


# 4th April, 2024 - The revolution is televised

Found this great talk that breaks down the kind of API that I want to build which is a [Hypermedia Maturity Model](https://8thlight.com/insights/the-hypermedia-maturity-model) level 3 me thinks

<iframe width="560" height="315" src="https://www.youtube.com/embed/zM5t6DaYrqM?si=dkAb8PhJP1zngC5B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Which I found in the videos section of the [FastAPI HyperModel resources page](https://jtc42.github.io/fastapi-hypermodel/resources/).

## htmx?

> htmx gives you access to AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext

I got a little side tracked with [htmx](https://htmx.org/) in combo with this type of hypermedia in which the server is rendering HTML snippets and sending them after in this video. This means ditching React and having simple HTML+HTMLx as the frontend. What gave me pause to seriously consider this was the results of doing this on a [real system](https://www.youtube.com/watch?v=3GObi93tjZI&t=493s&ab_channel=DjangoConEurope) or at least their reported stats which look like:

![Refactoring from SPA to hypermedia system]({static}/images/savings_with_hypermedia.png)
(From [Back to the Future of Hypermedia in Django with Mario Munoz](https://www.youtube.com/watch?v=LwH4ifjt3Y4&ab_channel=DjangoConUS))

Performance over thousands of elements is a factor (2nd last point above) because its just rendered HTML at the end of the day, which React struggles with. Performance being one of the biggest complaints of Miro. It also seems to reduce the frontend by about 90%, which if your a lone developer is huge!

He also claims that their product velocity has increased dramatically and the team is smaller.

Checkout:

- [PyHAT: Awesome Python htmx](https://github.com/PyHAT-stack/awesome-python-htmx) - PyHAT is more than just a snake with a hat 🐍🤠. It stands for Python htmx ASGI Tailwind—a web stack that allows you to build powerful web applications using nothing more than... drumroll... Python, htmx, and Tailwind.
- [Hypermedia Systems](https://hypermedia.systems/) book by the htmlx guys with an example using Flask and htmlx and Jinja2 for rendering HTML fragments.

# 2nd April, 2024 - Hypermodel

Going to go with a Level 2 hypermodel using `[fastapi-hypermodel](https://jtc42.github.io/fastapi-hypermodel/)` which is...

> FastAPI-HyperModel is a FastAPI + Pydantic extension for simplifying hypermedia-driven API development.
> Hypermedia consist of enriching API responses by providing links to other URIs within the services to fetch related resources or perform certain actions. There are several levels according to the [Hypermedia Maturity Model Levels](https://8thlight.com/insights/the-hypermedia-maturity-model). Using Hypermedia makes APIs reach Level 3 of the [Richardson Maturity Model (RMM)](https://en.wikipedia.org/wiki/Richardson_Maturity_Model), which involves leveraging [Hypertext As The Engine Of Application State (HATEOAS)](https://en.wikipedia.org/wiki/HATEOAS), that is, Hypermedia.

This basically allows me to define media types and exposed hyperlinks (URIs) to perform all the actions on those media types. It has the equivalent of HTML forms but in JSON if those actions or mutations need more information. This should allow me to keep the React FE fairly generic which was the idea of the REST principles. If I take it all the way to RMM Level 3 it even has all the RDF stuff so people can expose the data to the public and do real linked data.

*[FE]: frontend

# 1st April, 2024 - No Fooling

I've been working on, what I call Headspace[^headspace] (working tittle), for about 3 months. I imagine it as a virtual space in which you can organise your ideas, various types of data and interface with AI models on the backend with a click of a button. Kind of a cross between a virtual whiteboard and a database knitted together with RDF metadata.gi

[^headspace]: Yes I'm aware of the mental health app and the Australia’s National Youth Mental Health Foundation, thanks. Its not related to mental health.

## Brief history of the idea

I've had this idea knocking around inside my head for about... 20 years. At first it wasn't feasible with the SoTA[^sota] in frontend development being JQuery and SVG being a standard that perhaps one browser supported (Flash was what everyone was using for vector graphics).

*[SoTA]: State of The Art
[^sota]: hey, there are no real rules to acronym capitalisation or even what makes the acronym i.e. 'for' is randomly dropped such as in FBI. I'm going with Proper Nouns (PN) get capitalised ('the' is part of the PN) and everything else is lowercase

## REST is HATEOAS?

I've known about [REST](https://en.wikipedia.org/wiki/REST)ful APIs for awhile, or at least I thought I did. REST actually has a few constraints, according to its originator [Roy Fielding](https://en.wikipedia.org/wiki/Roy_Fielding) in his [PhD thesis](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm) (he gets to the crunch in chapter 5 and 6), that are about long term think:

*[REST]: Representational State Transfer

> REST is software design on the scale of decades: every detail is intended to promote software longevity and independent evolution. Many of the constraints are directly opposed to short-term efficiency. Unfortunately, people are fairly good at short-term design, and usually awful at long-term design. - [cite](https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)


So [Hypertext as The Engine of Application State](https://en.wikipedia.org/wiki/HATEOAS#:~:text=Hypermedia%20as%20the%20engine%20of,provide%20information%20dynamically%20through%20hypermedia.) (HaTEoAS) "is a constraint of the REST application architecture that distinguishes it from other network application architectures." according to Roy Fielding its creator, which he outlines in his doctorial thesis. This gives us

> The strong decoupling of client and server together with the text-based transfer of information using a uniform addressing protocol provided the basis for meeting the requirements of the Web: robustness (anarchic scalability), independent deployment of components, large-grain data transfer, and a low entry-barrier for content readers, content authors and developers alike.

So the long and short of it is: have hyperlinks (URIs related to the thing/data you are looking at) accompany media. These URIs are for navigating and mutating the state of the media you are looking at. The links can be labelled with relations. The only problems with this last part is that those are domain specific and so you need a human to interpret them, well until LLM. There has been an attempt to make some standard relations. But this is all good as this is exactly what I need for Headspace as the relations need only have good human readable descriptions for the React client/frontend/Code-on-Demand to display to the user, and these relations are going to be different of each media type, as Mr Fielding intended!

*[URIs]: Uniform Resource Identifiers

[^cod]: [Code on Demand](https://en.wikipedia.org/wiki/Code_on_demand) seems to be the old way of saying "frontend"?

*[LLM]: Large Language Models, i.e ChatGPT, M$'s Copilot etc