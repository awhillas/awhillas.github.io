---
Title: Engineering First Business Model
slug: the-low-hanging-fruit-business-model
summary: An alternative approach to tech business development in which all product decisions are made by the developers not Product Managers with the aim of keeping engineering effort minimal.
date: 2023-10-02
Modified: 2024-03-02
Category: Business
---

I've been around the tech business for 25 years and have noticed that companies that put an MBA guy in charge usually fail (or fire them). One might also note that some of the biggest tech companies in the world have been started and lead by engineers, Facebook, Google and Apple () notably.


## The VC model

The general argument for VC is that they "fund startups that drive innovation and make the world a better place" (this is not actually a quote but an attempt to steel man their argument). Or this is what anyone with an MBA will tell/sell you.

[This Y Combinator talk](http://www.paulgraham.com/die.html) is drenched in their value system:

> ...our definition of success is that the founders **get rich**... If you can just avoid dying, you ***get rich***... So even in the middle of **getting rich** we were fighting off the grim reaper... you can now **get rich** by not letting your company die... If so many startups get demoralized and fail when merely by hanging on they could **get rich**... I wish every startup we funded could appear in a Newsweek article describing them as the **next generation of billionaires**...etc

You get the point, which is to "get rich", because then the VC(s) get rich, and that is this VC, talking in that quote, is on about. There is no talk about _making the world a better place_ or the _quality_ of the product/service, or even _serving the customers_, all of which is the main motivation of engineers.

This is not new or surprising, but if you do do a deal with the VC/devil[^the_devil] you should have no illusions that that is what your motivation is now to become, getting them rich. And there is nothing wrong with making a buck, but have no illusions, its not noble and its not for the betterment of humanity, its just a cynical money making activity. So where does it sit morally?

[^the_devil]: in the classical blues sense of [The Devil](https://en.wikipedia.org/wiki/Deal_with_the_Devil)

The basic premise of VC is similar to a [pump-and-dump](https://en.wikipedia.org/wiki/Pump_and_dump) stock market scheme. The idea being "pump" the start-up with a some cash to get it off the ground, or at least make it appear that way with demos[^demos], which ever, and then when enough people are convinced and the valuation goes up enough: "exit" (dump it), ideally for much more than the VC put in and in the shortest span of time possible, which is why this approach is antithetical to the idea of "organic growth" or "quality" or "socially responsible".

[^demos]: In my experience demos are _always_ [smoke and mirrors](https://en.wikipedia.org/wiki/Smoke_and_mirrors).

If you know the [project management triangle](https://en.wikipedia.org/wiki/Project_management_triangle)[^pmt](PMT) you have fixed the _time_ and the _cost_ dimensions so the **quality has to suffer**.

[^pmt]: PMT 😛 or in other words: "Good, fast, cheap. Choose two."

So the objective is to make money fast by producing the lowest quality products that will give the highest stock valuation. Where does this money come from? Inevitably someone has to buy the shares of the company after the VC has exited. These people are left with an Minimum Viable Product (MVP[^MVP]) if they are lucky, or with nothing function at all. The investors have been duped. The VC will tell you this happen very rarely (95% of all start-ups fail in the first 5years apparently) but my intuition tells me this can't be true[^evidence]. Where does this perpetual well spring of money come from if that is the case?

[^evidence]: Weirdly I haven't been able to find stats on companies success rates after their IPOs? Funlly enough VCs don't publish those stats. TODO: ask around about this...
[^MVP]: [Minimum Viable Product](https://en.wikipedia.org/wiki/Minimum_viable_product)" is a version of a product with just enough features to be usable by early customers who can then provide feedback for future product development."

Here is a video from Elon Musk, how ever you feel about the man he is undeniably a successful business man, saying MBAs suck at running businesses. Don't spend time making power point presentations and going to meetings, get amongst the frontline workers and the customers and make the product as good as you can. Doesn't even need to be particularly innovative:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Y6P8qdanszw?si=QZ0lfWeYUDjnP243" title="'Too many MBAs ruining companies' Elon Musk explains" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Enshitification!

> Amazon now feels more like a racket than an open shopping platform; you can't find posts from your friends on Facebook because it's clogged with unsolicited advertising; and Uber no longer seems like a cool, efficient taxi service, it's morphed instead into a global machine for turning gig workers into the new underclass – it's all part of a process Cory Doctorow has dubbed "enshittification".[^podcast]
[^podcast]: Cory also has [Kickstarting a book to end enshittification, because Amazon will not carry it](https://pluralistic.net/2023/07/31/seize-the-means-of-computation/#the-internet-con) which I got from [this HN post](https://pluralistic.net/2023/07/31/seize-the-means-of-computation/#the-internet-con)

So the only way that the new custodians/shareholders of company can get value out of it is the lock users and businesses:

> the platform tries to establish this equilibrium where there is as little value left as possible as is needed to keep you from going, but no more, where all the additional value can be handed off to its shareholders - [Cory Doctorow](https://pca.st/yr3hd7f9)

## But why?

Coming from an AI background I know that if a learning algorithm is capable of representing sufficiently complex solutions it will learn shortcuts[^shortcuts] instead of the objective as intended by it's designer. I believe this is what is happening when businesses are optimising for exit profitability.

[^shortcuts]: [Shortcut Learning in Deep Neural Networks](https://arxiv.org/abs/2004.07780), 2020, Robert Geirhos et. al.

The solution might be to remove objective and open up to exploration, seeking interestingness according to the book [Why Greatness Cannot Be Planned: The Myth of the Objective](https://www.goodreads.com/book/show/25670869-why-greatness-cannot-be-planned) by the ex-OpenAI'er Kenneth O. Stanley.

## Is the VC model a good idea?

Two stats I came accross (need to verify source):

- 84% of high growth companies are not built with venture capital.
- Only 144 of the 900 fastest growing companies in America ('97-'07) had venture capital.

And the famous one:

> 95% of all start-ups fail in the first 5 years

If you knew these odds would you roll the dice for anything other than start-ups?

## But is 'Engineering First' the answer?

Engineers/domain-experts are adverse to making garbage. They are into making quality things or at the least, things that elegantly fix the design spec within the prism of the PMT. This can impact the business and dictate where engineering effort goes as this comment from hacker news on [Billing systems are a nightmare for engineers](https://news.ycombinator.com/item?id=31424450), a treasure trove of engineering nightmare stores, one that stood out to me:

> [awillen on May 18, 2022](https://news.ycombinator.com/item?id=31425390)
> Once upon a time I was the first product person at a now-decacorn, and my first task was fixing the billing system. It was quite the monster, and we ended up implementing a combination of Zuora and an internal system, as there were some parts of the billing model Zuora couldn't handle.
> I came away from this with one big lesson - if you're considering a complex billing model, consider the engineering implications first. With most products, engineering feedback gets taken into account - often product proposes something, engineering breaks it down, product realizes that feature x is vastly more complicated than they thought and not worth the effort, and the requirements are changed to simplify or remove it.
> The one thing that never seems to be true of is pricing models - that decision gets made at the very top and handed down with no chance for feedback. I think that if it the folks designing the billing system realized the costs, they might simplify things. If the complexity of your billing system means that 3% of your engineering team (plus additional folks in support and finance) is going to be working on it forever, but if you simplify it a bit you could keep 90% of it and only have 1% of engineering working on it, that might be a good tradeoff - after all, that leaves you more engineers to build features, which should drive additional sales. Unfortunately, that analysis never seems to get done up front and the cost is only understood after the billing system is deeply integrated into everything and would take an unpalatable amount of effort to change.

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

## Some more anecdotal evidence

In the spirit of all great ideas I shall create a list where this principle hold:

- Film: [Godzilla Minus One](https://www.youtube.com/watch?v=T4pi1F25sxg) - Hear from writer, director, and VFX supervisor Takashi Yamazaki and learn more about the unique approach Shirogumi took with the visual effects. A key innovation was actually the team structure; the Director cut out layers of decision makers by giving notes direct to the artists on the same floor. But that was only possible because he is a VFX artist himself.
- From [a Quora thread](https://www.quora.com/What-great-companies-did-not-raise-venture-capital) on this topic:
    - Webtrends
    - Siebel Systems
    - CraigsList
    - Survey Monkey
    - Mailchimp
    - Atlassian
    - IKEA
    - Sears
    - Campaingn Monitor
    - Vizio
    - Github