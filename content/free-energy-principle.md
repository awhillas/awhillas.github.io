---
Title: Free Energy Principle
slug: free-energy-principle
summary: My understanding of the Free Energy Principle and how it applies to (machine) learning agents.
date: 2023-08-08
Modified: 2023-08-08
Category: Machine Learning
---

## The basics

![Free Energy Principle, Basic outline]({static}/images/fep_simple.png)

So the Free Energy Principle (FEP) is a sort of universals objective function for cognitive agents i.e. agents with some sort of cognition or internal world representation that learns. It learns from sensory input and some actions that it can enact on the world.

    Sensation -> Internal model -> Actions -> World changes -> Sensations -> ... etc

Its a feedback loop. What they are calling free energy is the difference between the predicted (by the model) sensor(s) state and the actual sensor(s) state. The system tires to minimise this difference, or entropy, or "surprise" as its call in relation to the FEP.

## My RoboCup Experience

![Robocup Standard Platform league]({static}/images/robocup.png)

So I was vaguely involved in the [RoboCup](https://www.robocup.org/)[^robocup] at UNSW when I was doing my masters back in 2013. The control systems on the bots then was very crude. I thought that UNSW would be using some sort of reinforcement learning (RL) to control walking but they were actually hand programming every movement. I realised there where all these sensors on the "Standard Platform" bot that we were not using and my thought at the time was that if we feed these into a feedback loop into a learning algorithm like RL[^notRL] with the objective of keeping itself upright then it might be able to learn walk. Furth more, since the robots were getting damaged quite easily from falling over _a lot_ individual robots might learn how to deal with their own particular damage.

## Feedback is the key

From my days of making experimental music/noise I know that feedback is very powerful. It was what always made the most interesting results. Here too I think the feedback mechanism is a key factoring in making this work. The system balances itself.


[^robocup]: Competition between universities to make robots play soccer. I'd really like to get my hands on a simple robot I could program and try some of these ideas out on!
[^notRL]: I would obviously say a deep neural network now.