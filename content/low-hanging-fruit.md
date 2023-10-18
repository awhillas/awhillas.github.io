---
Title: Engineering First Business Model
slug: the-low-hanging-fruit-business-model
summary: An alternative approach to tech business development in which all product decisions are made by the developers not Product Managers with the aim of keeping engineering effort minimal.
date: 2023-10-02
Modified: 2023-10-02
Category: Business
---

I've been around the tech business for 25 years and have noticed that companies that put an MBA guy in charge usually fail (or fire them). One might also note that some of the biggest tech companies in the world have been started and lead by engineers, Facebook and Google notably.


## The VC model

The general argument for VC is that they "fund startups that drive innovation and make the world a better place" (this is not actually a quote but an attempt to steel man their argument).

[This Y Combinator talk](http://www.paulgraham.com/die.html) is drenched in their value system:

> ...our definition of success is that the founders **get rich**... If you can just avoid dying, you ***get rich***... So even in the middle of **getting rich** we were fighting off the grim reaper... you can now **get rich** by not letting your company die... If so many startups get demoralized and fail when merely by hanging on they could **get rich**... I wish every startup we funded could appear in a Newsweek article describing them as the **next generation of billionaires**...etc

You get the point, which is to "get rich", because then the VC get rich, and that is the VC talking in that quote. There is no talk about making the world a better place or the quality of the product/service, or even serving the customers, which is what motivates engineers. This is not new or surprising, but if you do do a deal with the VC[^the_devil] you should have no illusions that that is what your motivation is now to become. And there is nothing wrong with making a buck, but have no illusions, its not noble and its not for the betterment of humanity, its just a cynical money making activity. So where does it sit morally?

[^the_devil]: in the classical blues sense of [The Devil](https://en.wikipedia.org/wiki/Deal_with_the_Devil)

The basic premise of the VC is similar to a [pump-and-dump](https://en.wikipedia.org/wiki/Pump_and_dump) stock market scheme. The idea being "pump" the start-up with a some cash to get it off the ground, or at least make it appear that way with demos[^demos], which ever, and then when enough people are convinced "exit" (dump it), ideally for much more than the VC put into it. Also, ideally in the shortest space of time possible which is why antithetical to the idea of "organic growth" or "quality". If you know the [project management triangle](https://en.wikipedia.org/wiki/Project_management_triangle)[^pmt](PMT) you've fixed the time and the cost dimensions so the quality _has_ to suffer.

[^demos]: In my experience demos are _always_ [smoke and mirrors](https://en.wikipedia.org/wiki/Smoke_and_mirrors).
[^pmt]: PMT 😛 or in other words: "Good, fast, cheap. Choose two."

So the objective is to make money fast by producing low quality products. Where does this money come from? Inevitably someone has to buy the shares of the company after the VC has exited. These people are left with a low quality product (most of the time) if any at all. They have been duped. The VC will tell you this happen very rarely but my intuition tells me this can't be true[^evidence]. Where does this perpetual well spring of money come from if that is the case?

[^evidence]: The only evidence I have is the memory of looking at a successful VC's company portfolio and finding that nearly all the websites of the supposed successes were all dead links. TODO: find an updated source for this, perhaps Y Combinator?

## Enshitification!

> Amazon now feels more like a racket than an open shopping platform; you can't find posts from your friends on Facebook because it's clogged with unsolicited advertising; and Uber no longer seems like a cool, efficient taxi service, it's morphed instead into a global machine for turning gig workers into the new underclass – it's all part of a process Cory Doctorow has dubbed "enshittification".[^podcast]
[^podcast]: Cory also has [Kickstarting a book to end enshittification, because Amazon will not carry it](https://pluralistic.net/2023/07/31/seize-the-means-of-computation/#the-internet-con) which I got from [this HN post](https://pluralistic.net/2023/07/31/seize-the-means-of-computation/#the-internet-con)

So the only way that the new custodians/shareholders of company can get value out of it is the lock users and businesses:

> the platform tries to establish this equilibrium where there is as little value left as possible as is needed to keep you from going, but no more, where all the additional value can be handed off to its shareholders - [Cory Doctorow](https://pca.st/yr3hd7f9)

Is this worth spending our time on?

## But is 'Engineering First' the answer?

Engineers are adverse to making garbage. They are into making quality things or at the least, things that elegantly fix the design spec within the prism of the PMT. This can impact the business and dictate where engineering effort goes as this comment from hacker news on billing systems states:

![Comment from Hacker News on including engineers in the design process of billing systems]({static}/images/hacker_news_comment-01.png)

The trouble with organic growth is that you can't quit your job and work full time on it... in the beginning. Which is not as sexy as getting VC cash and hiring a team immediately to "work on your idea/dream" but as soon as you take that money it is no longer "yours" anymore.

But it can be done without VC as [37signals](https://37signals.com/) has proved. And their products are quality. From their manifesto:

> 01. An obligation to independence
> We have no investors, no board of directors, no eyes on an exit. We feel a moral obligation to exercise our independence. To do things no one would give us permission to do. To try things other companies would be afraid to try. To skip safe, and go for original. - [cite](https://37signals.com/01/)

As an engineer, this sounds like The Dream. And as for profits

> 04. Profit motive
> The tech industry is especially good at losing money. Growth is electric, but profits are elusive. We take an old school, economics 101 approach: Make more than you spend. That’s why we’ve been profitable every year we’ve been in business. It’s the responsible way to be reliable and take care of customers over the long haul.

Can it work in practice? [The story of Sizzy](https://www.kitze.io/posts/github-stars-wont-pay-your-rent) is a great, recent example of it coming true (once he stepped out of his own way)

> Currently, Sizzy has around 1600 users, which is crazy because the only marketing I've done so far is sponsoring one newsletter, and that was last week. Most of the marketing is just a word of mouth from people who enjoy the product. I want to improve the stability of the app even more before I start properly investing in marketing. It's still far away from my final goal. I have so many ideas about shaping Sizzy to be a tool that every developer and designer will rely on during their daily work. I want to reach a million users. It may sound crazy, but I know I'll get there. The only thing standing between me and that goal is just … me. But I won't let myself lose track again. Sizzy is my primary focus now, and everything else comes secondary. It's really hard to sleep properly when you know you have a lot of customers who depend on you. It's a weird feeling, but I love it!

He solved a problem he was having, turned out it was not just him and after dicking around for years he took time out to focus on it, and make it a SaaS, and have good quality, and it worked! Very inspiring story where he didn't have a VC standing over him with a whip saying "FASTER! FASTER!! Make me rich bitch!". Amazing! His take aways are good too, the first are very similar to 37signals advice about "Sell your by products" (which is what basecamp was):

- Solve your own problem
- Show your solution to other people as soon as possible
- Package it and distribute it as soon as possible (note to self)
- Don't be scared, ashamed, or discouraged to make it paid
- Don't let anyone tell you how much you should charge for your work

