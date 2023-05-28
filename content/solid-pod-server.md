---
Title: Solid Pod Server
date: 2023-05-28
Category: Rust, Solid
---

[Solid](https://solidproject.org/) is an attempt at making standards for returning control over your data, getting it out of the big tech silos. You run your own content server called a Solid Pod that you keep all your data in and control access to third party web apps to via OAuth2.

# Some background

Tim Berners-Lee started the Solid Project which is a lose collection of standards, still in its infancy after more than a decade, which defines Solid Pod Servers, which are an online identity for you, described in Turtle/RDF and a place to keep your public and private data. The

## The idea

I was thinking this might take off more if it was easy to deploy a personal solid server on a cloud provider where storage is cheap and you could use lambda/cloud functions to do the serving i.e. your not paying for them when they are not being used. Uses OAuth2 as authentication and the server is just a web server so all the components are already available as Rust crates, just have to bring it together. I've also seen some examples of using [Rust for AWS lambda functions](https://github.com/nogibjj/rust-mlops-template/tree/main/lambdathreads) and apparently is much cheaper because of the speedup.

## Persistent storage on the cheap?

The OAuth2 server needs to some persistent state to track the sessions and their details. Persistent state can be expensive in cloud as databases are not cheap.

- DynamoDB on AWS is [aways free](https://aws.amazon.com/free/database/?p=ft&z=subnav&loc=3) under a certain amount (which it should be). There are [Rust examples](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html). Does force vendor lock in to AWS :( There are [examples using the Rust SDK](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html)
- AWS [SimpleDB](https://aws.amazon.com/simpledb/): Amazon SimpleDB is a highly available NoSQL data store that offloads the work of database administration. 25 SimpleDB Machine Hours and 1 GB of Storage for free each month. Sadlt there are no examples online for using SimpleDB and rust :(
- Keep a SQLite file in a bucket and load it for every request? Vendor agnostic but might be slow?