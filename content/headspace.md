---
Title: Project: Headspace
summary: A new type of interface to data and media which takes ideas from Pure-data/Max-MSP and online whiteboard spaces like Miro while at the same time leveraging linked-data
date: 2024-03-31
Modified: 2024-04-01
Category: Software Engineering
---

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