---
Title: Realtime Machine Learning
summary: Experiments in online/real-time Machine learning.
date: 2023-04-29
Modified: 2023-06-14
Category: Machine Learning
---

In the Machine Learning Street Talk podcast's episode on 'Consciousness In The [Chinese Room](https://www.wikiwand.com/en/Chinese_room)', Francois Chollet's [criticism of the thought experiment](https://youtu.be/_KVAzAzO5HU?t=979) struck me

> of course the person executing the rules does not understand Chinese, that's not where you would expect understanding to be located in the system. Understanding is an imagined property of the information processing system as a whole. Understanding is not in the instructions themselves it's not in the processor that executes the instructions it's in the functional dynamics of how the input information is being processed by the instructions.

He goes on to say that he believes the Chinese Room does not understand even if you are looking at the information processing system as a whole its because the book is static, or a crystallized skill, it can not adapt to changing circumstances

> skill at a task is not sufficient to assert understanding of a task... intelligence is characterized by the ability to learn and adapt and efficiently pick up new skills from experience

> If you understand what you're doing then you can adapt what you're doing when the world changes you can learn and adapt and improve and if you don't understand what you're doing then you're stuck with a static skill and that's really how you tell the difference between understanding and not understanding

This made me think of what used to be called "online learning" or real-time learning[^online].

[^online]: "Real-time" might be a better term as "online" implies the internet these days.

So now I'm interested in doing some experiments with basic simulations, with neural networks that update their weights in real time and see where that leads. This is why I'm [learning Rust]({filename}/a-new-hope.md) incidentally.

## Predator and Prey

The first experiment I'm going to try is a simple hunter-prey simulation like this

<iframe width="560" height="315" src="https://www.youtube.com/embed/tVNoetVLuQg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

What [Pezzza](https://www.youtube.com/@PezzzasWork) is doing here is to take a fixed architecture neural network (NN) with input from a visual field, lines that trace out from the agent and detect the presence of ether friend or foe, and fully connect them to two outputs: speed and direction.

![Pezzza's agent Neural Network]({static}/images/Pezzzas_NN.png)

Then, instead of using backpropagation to tune the NN's weights he is choosing them randomly and letting natural selection kill off the bad ones[^mutation] while the ones that survive long enough to multiply propagate. This allows him to train a NN without an objective function.

[^mutation]: Possibly he's also mutating the offspring in order to get variation into the population. There might be crossover, the splicing of genes, by randomly selecting one of the other survivors to mate/share-genes with.

I want to take this basic setup and introduce real-time learning via backpropagation (BP). The problem with BP is that you need an objective function, which says how to update the weights. Its not obvious how to do this in this setup where the output is not the same as the objective function. This is where Reinforcement Learning traditionally.

There is also [this very similar approch](https://www.reddit.com/r/bevy/comments/1464kcq/i_built_a_self_driving_car_ai_using_rust_and_bevy/), in [Rust and using the Bevy framework](https://github.com/bones-ai/rust-drive-ai) which is exactly where I wanted to go with it.
[AI learns to play retro game road fighter (Reinforcement learning)](https://www.youtube.com/watch?v=H7RWcNgE-6s&t=1s&ab_channel=BonesAI)

## In search of an objective

[AlphaZero](https://www.deepmind.com/blog/alphazero-shedding-new-light-on-chess-shogi-and-go) they seem to have trained a NN to rate chess board positions without the needing of an immediate objective, sort of.

From the paper [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/pdf/1712.01815.pdf)

## Predictive Models

[Filip Piekniewski](http://blog.piekniewski.info/) has this idea of [predictive vision models](http://blog.piekniewski.info/2016/11/04/predictive-vision-in-a-nutshell/) which basically try to guess the next frame of video and there by model the world. One might look at this as the [language modelling](https://en.wikipedia.org/wiki/Language_model) task of vision. He's also suggesting adding online learning to this mix so the model trains and predicts at the same time, thus, according to Francois Chollet's thesis would make it adaptive and thus conscious? And he's got feedback from top back to bottom. He carries on about [Associate Memory](https://www.tutorialspoint.com/artificial_neural_network/artificial_neural_network_associate_memory.htm) which is a type of NN (I need to look into)

to be continued...[^wip]

[^wip]: This whole page is a work-in-progress and is just to document, and help me work through my ideas