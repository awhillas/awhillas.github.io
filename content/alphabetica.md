---
Title: Alphabetica Game Dev Log
summary: A new game I'm working on to help kids learn to read.
date: 2023-06-11
Category: Rust, Software Engineering, Game Development
---

## 15th June, 2023 - Sound problems

SO I have the button on the screen and it makes a sound when you press it. If you smash the button, which 5yos will do, it triggers so much that I fear the app will crash. I thought to try and fix this by installing a Bevy Kira extension but it very difficult to install. Will ask on some forums how to get it going. Don't want to lose momentum so I'll just use the built in stuff. Sound always plays second fiddle to graphics in games.

Next I need to investigate evens in Bevy and get the letters spawning when the button is pressed. I'm thinking SVG for letters so I can go crazy with fonts.

## 13th June, 2023 - First steps

So after watching a few game dev videos on YouTube about indie success stories, they seem to recommend keeping a game dev log to help with motivation. So here I am.

My son is five and a half and beginning to learn to read. Tonight actually he spelt out the word 'wash' in a Sesame Street book I was reading him to my amazement. I wanted to make a game for him to help him with the sounding out of letters and ultimately help him to sound out letters. My only fear is that it will take too long and he wont need it by the time I finish.

I did start to look into phonetics and phenomes, there are 44 in the English language.

> Phonemes are taught as part of the Phonics Phases 1-6 and are a key method in helping children learn how to read. Phonics links phonemes, or the sounds, with the graphemes, or letters, they represent.
> [cite](https://www.twinkl.co.nz/teaching-wiki/phoneme)

### Sound

I found this great video of a woman sounding out each of them.

<iframe width="560" height="315" src="https://www.youtube.com/embed/XUCUhHUDZIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

I downloaded the video, extracted the sound, converted it to WAV, used Audacity to cut it up into individual voicings and then had to convert them to Ogg Vorbis audio format because I couldn't find any documentation on what audio types Bevy accepts out of the box other than the example of `.ogg` files. I still have to go through all of them and name them something useful. There are 4 soundings of each phoneme and a word example for each.

### Fonts!

I'd forgotten how much fun fonts can be! Its going to be easy to give letters character using different fonts.

### Follow the fun

But how to make it fun? I have a very basic idea of what I'm going to start with and hope by getting my son to play test it I can figure out what he likes about it a follow that. I saw a video by [Sid Meier](https://www.wikiwand.com/en/Sid_Meier) (Sim City, The Sims) on Master Class about making games and his advise was to prototype ideas fast and test them for fun. You wont always know until you play what mechanic/dynamic will be the fun part. "Follow the fun!".