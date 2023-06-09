---
Title: Learning Rust
summary: Why I'm learning Rust and how I'm doing it.
date: 2023-04-29
Modified: 2023-06-23
Category: Rust, Software Engineering
---

## But why...?

Its always good to make decision based on data.

![Graph from Stackoverflow Trends. Extrapolate the lines...]({attach}images/cpp_vs_rust_2023.svg)

I'm interested in Rust as I predict it will overtake C++ in popularity within the next 1-2 years if the trends in the above graph from [Stackoverflow Trends](https://insights.stackoverflow.com/trends?tags=c%2B%2B%2Crust) continues. Rust is growing in popularity exponentially and C++ seems to have a linear decline.

There is also the results of the [Stackoverflow Annual Survey for 2023 Admired and Desired section](https://survey.stackoverflow.co/2023/?utm_source=banner&utm_medium=display&utm_campaign=dev-survey-results-2023&utm_content=survey-results#section-admired-and-desired-programming-scripting-and-markup-languages)

> Rust is the most admired language, more than 80% of developers that use it want to use it again next year

The reasons for this, I think, are many.

Rust has a built in package manager which also handles compilation and makes the developer experience easy. Easy always trumps difficult, every time[^everytime]. This is a huge boon to productivity and also a huge breath of fresh air after C++. It took me about 6 weeks to get started with C++ (finding a package manager amongst many, trying to understand CMake). I think what is happening is young[^young], C++ developers are trying Rust and then being won over by this after struggling through C++.

Rust has a lot of modern language features like the Monads Option(Maybe) and Result(Either) which tackle uncertainty up front. They are used consistently and everywhere within the standard lib.

![C++ vs Rust meme]({attach}images/cpp_vs_rust_meme.png)

Some C++ people say that the syntax is horrible, but I find it quite a contrary. I've studied C++ for a year and I still can't open a C++ project and understand it. For example compare a tokenizer written in C++, Google's [sentencepiece](https://github.com/google/sentencepiece) written in a modern C++ style and following the conventions of Google's C++ guideline (presumably), verse OpenAI's [TikToken](https://github.com/openai/tiktoken) which are both [BPE](https://www.wikiwand.com/en/Byte_pair_encoding) tokeniser. I know what they both do so it should be easy to interpret the code, right?

To start with I have no idea where to begin with the C++ project. There are no conventions for project layout or naming stuff. I know CMake is the de facto build tool for C++ but the [CMakeLists.txt](https://github.com/google/sentencepiece/blob/master/CMakeLists.txt) file is long and cryptic. It imperative unlike the declarative Cargo.toml of TiKToken which is much shorter (21 lines vs 170!). I know exactly where to look for the entry point in any Rust project in ether the `src/lib.rs` if it a library or the `src/main.rs` if its an executable.

The splitting of C++ code into header files and implementation files is bananas. No other language does this, is laborious to write and painful to read.

But I guess the real genius of Rust is that it ditched Object Oriented Programming while keeping its best feature: polymorphism.

## Current problems with Rust

The main thing Rust suffers from right now is being young. A lot of the ecosystem is immature. This is changing rapidly and there are opportunities for keen, young developers to get in there and become a major part of the ecosystem.

No native linear algebra libraries or [Scientific/High-Performance Computing](https://www.reddit.com/r/rust/comments/smdl3m/rust_and_scientifichighperformance_computing/) (HPC). It does have bindings for OpenBLAS a C++ lib but its apparently a nightmare to get working cross platform. This holds it back from deep learning and general data science which both rely heavily on matrix operations. [But this is changing](https://www.reddit.com/r/rust/comments/obghx7/fast_linear_algebra_library_for_rust/).

But its still early days and I think these issues will be address in time.

[^young]: The average age of C++ devs is over 40 these days, see [Q2 and Q3](https://isocpp.org/files/papers/CppDevSurvey-2022-summary.pdf), also Q6 notes the major pain point is "Managing libraries my application depends on".

[^everytime]: This is why Netflix and Spotify are unicorns despite the fact that you can download everything they publish on torrents for free.

# But How?

Here are some materials I've been using:

- [The Rust Lang Book video series](https://www.youtube.com/playlist?list=PLai5B987bZ9CoVR-QEIN9foz4QCJ0H2Y8) is quite handy to get up to speed on Rust quickly. Its basically going over the official [The Rust Programming Language Book](https://doc.rust-lang.org/book/) which takes you through all the features of Rust in a systematic way. I find someone going over the material (at double speed) seems to be easier than reading the material directly. But its not enough by itself. Need to apply what I've learning quickly or else it doesn't sink in.
    - There is also an interactive [quiz based](https://rust-book.cs.brown.edu/) leaning aid that I just discovered while writing this. I have never been into puzzels that much but I know if you don't try to apply what you have just learnt
- [Learn Bevy Engine 0.10 Beginner Tutorial Series](https://www.youtube.com/playlist?list=PLVnntJRoP85JHGX7rGDu6LaF3fmDDbqyd) [Bevy](https://bevyengine.org/) is an [ECS](https://www.wikiwand.com/en/Entity_component_system) game system. ECS are all the range in game development because they are fast because they take advantage of CPU caching. This tutorial series takes you from zero to build a basic interactive game and give you a template for your own project. Although I'm not familiar will all of Rust's syntax I find learning by doing the best strategy. I've just finished the first 10 episodes which is all there is at this time. Time to make my first game with this template.

## First steps

Some projects I'm thinking of starting or have started in current order of enthusiasm:

<!-- - [Alphabetica Game]({filename}/alphabetica.md) - My son is learning to read at the moment and I think a game to help him match letters to sounds might help. Repetition is the key. I'm going to build it off the back of the Bevy tutorial I've been going through. -->
- [Online Machine Learning]({filename}/online_learning.md) - I've seen some simple simulations on YouTube where people evolve neural networks (NN) to operate, embodied in a simple simulated environment. I want to do something similar but I want to do online/real-time training of the NN. I think this will lead to a more aware AI.
- [Chess engine](https://github.com/awhillas/check) - or now I'm thinking, rather a general purpose discreet, game engine. Create an interface to some set of rules which generate moves for a given position (and also indicate a winning move/position) it should be able to learn via self-play. I guess replicating AlphaZero would be the first step?
- [Solid Pod Server]({filename}/solid-pod-server.md) - all in one identity/public+private content server with built in authorization (OAuth+). The hard part of Solid, because it was very boring, was trying to understand the standards which are verbose and incomplete. It also uses OAuth + OpenID Connect at the core of its authorization protocol which in itself was the hardest part, because its complicated and I found it hard to find a [straight forward explanation](https://www.youtube.com/results?search_query=oauth2+flow).
- **Cave Boy**, a kids, open-world, adventure game. I've started [prototyping in Python](https://github.com/awhillas/caveboy). I'm thinking something like Don't Starve (but less scary), or Stardew valley (with less detail) with a Captain Underpants sense of humour (i.e. potty). I'm thinking to aim it for 4-8 year olds, full touch screen and very simple mechanics. Everything is visually displayed at all times (no hidden menus or state i.e. inventory). TODO: break this out into a full blog post (i will as I get more into it). I have some concept art already!

This list is getting long...