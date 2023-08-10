---
Title: Phonetica Game Dev Log
slug: reading-video-game-dev-log
summary: A new game I'm working on to help kids learn to read.
date: 2023-06-11
Modified: 2023-08-07
Category: Rust, Software Engineering, Game Development, Linguistics
---

## 10 August, 2023 - First play test

So I gave it to my son this morning and he played through it a bit. Some notes:

- Was too fast. One second between words dropping was too short, especially at beginning. Perhaps increment as go.
- Didn't get the idea of spelling out the word. Need to somehow be explained? Perhaps 3 phoneme words were too hard to start with, try 2. Will make discovery easier.
- Found the explosions fun and laughed when they happened.
- Once all the letters filled the screen it became a challenge. He had to know the order of the letters.
- He found blowing up his own name a kick :)

### Going forward

- [ ] The selection order mechanic was confusing. Should clear as soon as the wrong letter is chosen.
- [ ] Make the selection more obvious i.e. rotate colour of selected?
- [ ] Have the word written somewhere, perhaps on the background
- [ ] Change background with word.
- [ ] Announce the number of words left to explode.
- [ ] Should track what he has played and what took him a long time vs what was easy and took less time.
- [ ] Bug in which the first word is repeated.

### New material

![Word list from Sons's school]({static}images/word_list_from_sons_school.jpg)

I too the kid to school this morning and while I was waiting for the teacher to show up I found a phonetic chart. On the back were lists of words in **alphabetical order**! Looping through the alphabet can make up a level! Seems obvious now, but I guess since I'm using phonemes not letters maybe its not. Though some letters have limited number of 2 and 3 words... still, will be easy for 3 letter words.

## 7th August, 2023 - The need for bling

So I have the basics of the game setup with simple level progressions. I'm not sure if it is fun yet? Time for some play testing with Asher?

TODO:

- [x] Empty scene transition between word
- [ ] Rest of the words
    - [ ] Sound recordings of words being said, get from?
    - [ ] Update the syllabus file, checking phonemes against OED
- [ ] Bling Effects when!
    - [ ] the countdown time is updated
    - [ ] word changes
    - [ ] background?


## 5th August, 2023 - "-er"?

So I ran into an issue with translating "Asher" into phonemes. [IPA-dict](https://github.com/open-dict-data/ipa-dict) says its /'æʃɐ/ but I was unsure about the 'ɐ' sound/phone for UK English as it's the same as vowel in fox /fˈɒks/ (according to the same dictionary, but now that I look at it, its a different upside-down 'a'). According to the video ['er' Ending Words and the Schwa Phoneme](https://www.youtube.com/watch?v=ZyULNC_8SNw&ab_channel=EnglishLanguageClub) it should be the Schwa 'ə' sound. Anyway, I found this chart which is a better translation from IPA to all grapheme forms

![Phoneme to Grapheme chart]({static}/images/phonetica/phonetics_chart.webp)

Although there is no 'ɐ' in that chart only 'ɒ'? According to the [IPA interactive chart](https://www.ipachart.com/) it seems that 'ə' is in fact correct, but all three could be correct depending on which part of the UK your from? The [OED](https://www.oed.com/dictionary/basher_n1?tab=factsheet#26849264) says 'ə' so I guess I'll go with that. I'm not sure how one decides what is the official phoneme for a pronunciation for a dialect. Maybe the OED is it?

## 3rd August, 2023 - Explosions!

Got the explosions working. Had to improvise with pymunk as it doesn't have a built in explosion effect. I replace the block to blow up with a circle for ~200ms and then make it disappear. I also made the explosion weightless so it wouldn't roll down.

I got the explosions sounds [here](https://www.freesoundeffects.com/free-sounds/explosion-10070/) and the image from [wikimedia](https://commons.wikimedia.org/wiki/File:Explosion-153710_icon.svg). Good bless creative commons!

## 25th July, 2023 - First demo

![First Demo]({static}/images/phonetica/mvp01.gif)

So I've started to code up the demo of the idea. Still much to do:

- [x] Sound phenome when clicking box
- [x] Play word sound when phonemes appear
- [x] Track order that letters are selected in
- [x] Letters explode when right order is chosen
- [ ] Compile rest of the words Content. (I just choose words I had voice recordings for)

### Side note

It was pretty cool to get the first(ish) version working, and actually it was very easy with python. When I first saw the thing I've had in my head for weeks appear on screen and start to work(ish) there was a buzz of gratification. Its a cool feeling.

I watched a short video of [Trevor Noah talking about how he loves stand up comedy](https://www.youtube.com/shorts/K1JsNyEHrso) and giving the life advice of:

> Live in a space where you are doing what you love.

I think that games could be that space for me.


## 23 July, 2023 - Physics is fun

![pymunk demp / animated logo]({static}/images/pymunk_logo_animation.gif)

So I have a basic concept for the game. Its going to involve blocks dropping and using a physics engine to simulate that. I found a simple 2D physics engine called [pymunk](http://www.pymunk.org/) which is an interface to the C library [Chipmunk2D](http://chipmunk-physics.net/). pymunk is under active development while Chipmunk2D seems to be feature complete. There is heaps of tutorials with pygame and pymunk so getting up-to-speed is quite easy and fun! There was a lot of low hanging fruit! To list what I went through:

    - [Python Physics Simulation. Galton Board. Pymunk Tutorial](https://www.youtube.com/watch?v=-q_Vje2a6eY&t=15s&ab_channel=CoderSpace) I watched this and used the code as a starting point. Great template for getting pygame and pymunk talking to each other.
    - [Using mouse and keyboard](https://pymunk-tutorial.readthedocs.io/en/latest/mouse/mouse.html) helped me create the touch/click interaction I need for interacting with the blocks.

I did give up on trying to rotate the images to the same angle as the physics block.


## 14th July, 2023 - Just graphemes to phonemes

Phonetics is quite the rabbit hole. I just need English spellings, or graphemes, and their related phonemes. I found this chart for Australian English (I think)

![alphabetic-code-chart]({static}/images/alphabetic-code-chart.png)

> In order to represent the 44 phonemes of Australian English we use a range of graphemes (letters or letter combinations).  Children need to know 150 - 200 of these phoneme/grapheme correspondences in order to read a reasonably complex text and these need to be taught explicitly and systematically. - [cite](https://www.jocelynseamereducation.com/blog/46913-phonemes-and-graphemes)

This two part video series about [helping children sounding out words](https://www.youtube.com/watch?v=yxIrK5R8n0g) I found quite helpful. The [second part](https://www.youtube.com/watch?v=5ID2fMAjx94) mentions some recent research[^reading] on the topic and apparently the current approach to looking at the pictures and guessing the words is poor or "inefficient". She recommends a problem solving approach of breaking the word up by underlining the phonemes and helping them with phonemes that the don't know but letting them sound out the word phoneme by phoneme until they get the word.

[^reading]:
    [National Inquiry into the Teaching of Literacy (Australia) – The Rowe Report](https://ldaustralia.org/research-papers/national-inquiry-into-the-teaching-of-literacy-australia-the-rowe-report/), Ken Rowe - December, 2005

    [Read about it: Scientific evidence for effective teaching of reading](https://www.deb.co.nz/content/uploads/2023/04/Read-About-It.pdf), K Hempenstall, J Buckingham - 2016

### An Idea!

This has given me the idea to have words broken up into their respective phonemes, with different colours, but written correctly and then slowly drift apart. The player then has to hit the phonemes in the order they were originally, sounding out the word. This then multiplied into many examples of the same thing with the letters getting mixed up, like soup, and the challenge is to put them all back together, click-on/touch them in the right order to clear the level.

### How to start

There is a great set of documents which outline the Australian reading syllabus at [Firefly Education](https://www.fireflyeducation.com.au/series/soundwaves/features/).

*[CVC]: Consonant-Vowel-Consonant e.g mat, sat, did, nap

I'm going to base my syllabus on the [Sound Waves NSW Early Stage 1 Syllabus](https://www.fireflyeducation.com.au/downloads/Sound_Waves_NSW_Syllabus_Match_Early_Stage_1.pdf). From that document:

> In Sound Waves Foundation, phoneme–grapheme relationships are introduced in a very specific order. This minimises confusion for students and ensures they are up and running quickly with reading and spelling. The order begins with m, a, t, s, i, d, f, n and p so students can read and spell CVC words such as mat, sat, did, nap etc.

![Sound Waves Foundation principles]({static}/images/sound_wave_foundation_princibles.png)

They have a system of pairing graphical icons for phonemes with the graphemes which is a good idea but stems from using print as a medium. I hope that I can just relate the sound of the phoneme directly with the graphemes by playing the sound when they touch the grapheme. This is the advantage of using an interactive medium (I hope).

### Tracking learning

Also, I want to track the learning of a child. At the very minimum I'm going to need keep track of which part of the syllabus they are up to. The video game way is to just make them start from the beginning every time. Perhaps they unlock levels as they progress which gives them new icons at the start of they game so they can jump start at the latest or revisit previous levels?

Also, some sort of report for for parents and teachers would be good. Not sure what they would like it see? Perhaps what they are good and bad at in terms of grapheme-phoneme mapping?


## 14th July, 2023 - Deep diving into Phonemes

So I'm trying to build the game content/levels aka the syllabus. The general structure is going to be:

    Phonemes/Phones -> Words -> Texts

I'm focusing on the first step, but would like to incorporate some of the second. To begin with I need a list of the phonemes in English and grouped into vowels and consonants. I also need a list of short words (2-3 letters/phonemes) starting with the simple consonants, one vowel sound only. I combined the word frequencies with the word->phoneme dictionary and then filtered to a list of words with one-to-one mapping of letters to phonemes (was a crude estimate will update the Gruut IPA module [see bellow])

### Gruut IPA module

![International Phonetic Alphabet code diagram]({static}/images/ipa.png)

I found a great python module for working with phonemes called [Gruut IPA](https://github.com/rhasspy/gruut-ipa). It has some [data](https://github.com/rhasspy/gruut-ipa/tree/master/gruut_ipa/data) for different languages (I'm keeping this in the back of my mind). I might try and do Russian in parallel so I can use the game for learning Russian and use myself as a test subject, but don't want to get too side tracked for now. The [British English file](https://github.com/rhasspy/gruut-ipa/blob/master/gruut_ipa/data/en-gb/phonemes.txt) has phonemes grouped which is handy. There are 42 phonemes. I don't know where the 44 came from?.

I tried to install the module and use the "print" function but it seems to only spit out 33 phonemes? I'm just going to write my own parser for its data files and move on. Lost a day to digging around it's code. Its got way more info than I need.

### Elsewhere

This is all good research for doing Text-to-Speech which I want to get back into. I might train a model to convert text to IPA phonemes as I think I have an idea of how to do that now.


## 9th July, 2023 - Chat with a Speech Pathologist

Had a chat with my old friend Khye who is a speech pathologist.

Her advice was to start on the simple one letter to one sound i.e. one-to-one mappings between glyphs and phonemes. Once they are confident with that start them on simple words. Then with words that do not have consonant clusters i.e. /brick/ where the "ck" are acting as one sound, better is /dog/ where each letter is a single sound and those are constant

The words should be two to three letters and also only use one-to-one, one glyph to one phoneme sounds. There are some texts with this goal in mind released by the NSW government called [decodable texts](https://education.nsw.gov.au/teaching-and-learning/curriculum/literacy-and-numeracy/teaching-and-learning-resources/literacy/effective-reading-in-the-early-years-of-school/decodable-texts)

>  Decodable texts are specifically written for beginning readers as they are developing their blending and segmenting skills and their knowledge of the alphabetic code. Decodable texts support students as they practise by using a continuous meaningful text.
> Decodable texts contain a very large percentage of words that incorporate the letter-sound relationships that students have been taught. Decodable texts increase in complexity as the student learns more of the phonetic code.

These texts are behind a login so not accessible to the general public (for some reason?), but with the [ipa-dict](https://github.com/open-dict-data/ipa-dict) I should be able to make my own: Filter words that have matching number of letters and phonemes, sort by [word frequency](https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download), filter by number of letters/phonemes i.e. start with 2 and 3 letter words and go up from there. I guess the next step would be to make narratives out of these words.


## 8th July, 2023 - Building a Syllabus

I finished organising the English phonetic sounds I gathered from the [phonic letter sounds video](https://www.youtube.com/watch?v=XUCUhHUDZIY). It has both the English and American pronunciations but seemingly only for 42 out of 44 phonemes for some reason.

But now what?

### Data driven syllabus

I was thinking of taking a data driven approach to building a syllabus. Look at word frequencies in large corpus which I found for download on Kaggle's [English Word Frequency: ⅓ Million Most Frequent English Words on the Web](https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download). So I can get the most frequent 2, 3 and 4 letter words. But what I really need is frequency of 2-4 letter phonemes. So I need a dictionary that can translate the orthography into IPA phonemes. Fortunately someone has compiled such a dictionary: [ipa-dict](https://github.com/open-dict-data/ipa-dict) - Monolingual wordlists with pronunciation information in IPA.

![Storybooks Speech and Hearing]({static}/images/african_stories.jpg)
I also found a great [collection of African stories](https://global-asp.github.io/storybooks-sah/stories/en/#) for different reading levels which might come in handy with IPA versions.

*[IPA]: International Phonetic Alphabet
*[orthography]: the conventional spelling system of a language

### Name change

Change the project name to "Phonetica"! Maybe that can be the name of a fantasy kingdom and the phonemes that inhabit it can anthropomorphised?

### Side note on Rust

I found this really great [online synth called Ironfish](https://makepad.nl/makepad/examples/ironfish/src/index.html) written in Rust as a demo for a UI lib called [makepad](https://github.com/makepad/makepad) ([RustNL 2023 talk](https://www.youtube.com/watch?v=rC4FCS-oMpg&t=1298s&ab_channel=RustNederland%28RustNL%29)). Making the game in Rust will mean that a web version will easy(er) to make. Worth considering.


## 6th July, 2023 - working memory and games

This book review came up on [Hacker News](https://news.ycombinator.com/item?id=36605085) today:

> He devotes an entire chapter to the issue of computer games and the question of whether they are a negative influence or a positive one (in terms of cognitive ability --- he sidesteps the 'violence debate') . He points out that there is no general answer, referring back to the earlier discussion: some types of training are more effective than others, and it is critical that the working memory be pushed to its limit repeatedly. Thus it is critical to consider particular computer games, instead of trying to make a general statement about computer games as a whole. He describes a variety of studies that show some types of computer games as having a positive influence on cognitive skills. - [Book Review: 'The Overflowing Brain' by Torkel Klingberg](https://tertulia-moderna.blogspot.com/2010/12/overflowing-brain-by-torkel-klingberg.html)

I should look into the reference he uses for the game stuff. I haven't thought about how how games can help train and improve working memory. Could be an interesting direction.

He also goes into Flow which is another topic I need to investigate in regards to education

> Klingberg concludes with a short chapter on the "information flood" that exists today and studies of its effects on cognitive ability. The results of some of these studies point to a kind of 'sweet spot' of information flow --- we perform best when the challenge presented is just at the limits of our skill. He refers to a diagram developed by Mihály Csíkszentmihályi, who defines 'flow' as "characterized by a high level of challenge and skill, in which the capacity of the doer exactly matches the demands of the task being done.... [W]hen challenge exceeds skill, we get stress. When skill exceeds challenge, we get a sense of control, which becomes boredom as the level of challenge drops." (p. 168)

## 29 June, 2023 - Research time

So, I've hit the point in which I've run out of things to code and need to do some research and design.

> phonemic awareness performance can predict literacy performance more accurately than variables such as intelligence, vocabulary knowledge, and socioeconomic status[^1] The good news is that phonological awareness is one of the few factors that teachers are able to influence significantly through instruction—unlike intelligence, vocabulary, and socioeconomic status [^2]. [cite](https://www.readnaturally.com/research/5-components-of-reading/phonological-awareness#:~:text=Phonological%20Awareness%20Skills,onset%2Drime%2C%20and%20phoneme.)

![Phonological Awareness Skills]({static}/images/Phonological_Awareness_Skills.png)

> Blending phonemes into words and segmenting words into phonemes contribute directly to learning to read and spell well. In fact, these two phonemic awareness skills contribute more to learning to read and spell well than any of the other activities under the phonological awareness umbrella. [^3]

So blending phonemes into words and segmenting words into phonemes are the main objectives of this project.

[^1]: Gillon, G. T. (2004). Phonological awareness: From research to practice. New York: The Guilford Press.

[^2]: Lane, H. B., and P. C. Pullen. (2004). A sound beginning: Phonological awareness assessment and instruction. Boston: Allyn & Bacon.

[^3]:
    National Reading Panel. (2000). Teaching children to read: An evidence-based assessment of the scientific research literature on reading and its implications for reading instruction. Washington, DC: National Institute of Child Health and Human Development.

    Snider, V. A. (1995). A primer on phonemic awareness: What it is, why it’s important, and how to teach it. School Psychology Review, 24(3), pp. 443-456.


## 26 June, 2023 - Pivot (again) to Kivy

So while setting up pygame, which is really going back to basics, I was reminded of [Kivy](https://kivy.org/) which is designed to make user interfaces. Another issue with pygame is that it is difficult to compile for iOS, and that is a target of this project i.e. touch screens are what I'm designing for, and Kivy makes his easy out of the box.

The only problem with Kivy is that its model is a but opaque and the documentation is in various stages of freshness. The API documentation seems up to date but doesn't have so many examples of common use cases and the tutorials are over a decade old. There are [examples](https://github.com/kivy/kivy/tree/master/examples) that I have yet to delve into, most of them are pushing a decade old as well.

### On the Bevy front

I did a little experiment on Friday. I had a question that I posted in three places, the [bevy github discussion](https://github.com/bevyengine/bevy/discussions/8919), [Stack Overflow](https://stackoverflow.com/questions/76527423/how-to-get-the-actual-pixel-size-of-a-transformed-sprite-in-bevy) and [r/rust_gamedev](https://www.reddit.com/r/rust_gamedev/comments/14fkzwk/how_to_get_the_actual_pixel_size_of_a_transformed/?sort=new). The only one that got a reply and indeed and answer was Reddit (took 3 days). I think that Reddit works so well because developers go there for many reasons, news; gossip; ideas and help, all mixed together. So if you need help you have the highest chance the person with the answer's eyeballs will see your post. Since the other two are just help support, people are less likely to look there. There is a threaded Help channel in the Discord that I didn't look at which seems active, I'll try that next time.

So anyway the answer was you have to figure out scaling stuff yourself but you can get the info in the Transform:
```rust
fn print_sprite_bounding_boxes(
    mut sprite_query: Query<(&Transform, &Handle<Image>), With<Sprite>>,
    assets: Res<Assets<Image>>,
) {
    for (transform, image_handle) in sprite_query.iter_mut() {
        let image_dimensions = assets.get(image_handle).unwrap().size();
        let scaled_image_dimension = image_dimensions * transform.scale.truncate();
        let bounding_box = Rect::from_center_size(transform.translation.truncate(), scaled_image_dimension);

        println!("bounding_box: {:?}", bounding_box);
    }
}
```

So since I got an answer I might persevere with it a bit longer.

### New Strategy

I might do two versions of the project at the same time. Since it takes soooooo loooong to get Bev answers I'll work in Bevy until I hit a blocker, ask a question and then swtich to Kivy until I hot a blocker and then switch back again. I really want to learn Rust and I don't have the bandwidth to learn it separately from the one side project I do have time for so I'll keep tyring to shoehorn it in.


## 23 June, 2023 - Pivot to pygame

So as much as I like the setup of Bevy's ECS I hit a major road block and can't get any help on it. I basically want to get the pixel size of a scaled image and there doesn't seem to be any way to do that in Bevy. I think because transforms are in WebGPU (WGPU) and Bevy its a one way street with from Bevy to WGPU.

I found a hard time getting help with this as the Bevy subreddit has been taken down due the the [Reddit hullabaloo](https://www.eff.org/deeplinks/2023/06/what-reddit-got-wrong?utm_source=pocket_saves) that is going on. The moderator didn't bother with a transition period so there is nowhere to ask questions. I tried posting the same question on the [bevy's github discussion board](https://github.com/bevyengine/bevy/discussions/8919), [/r/rust_gamedev](https://www.reddit.com/r/rust_gamedev/comments/14fkzwk/how_to_get_the_actual_pixel_size_of_a_transformed/) and [Stack Overflow](https://stackoverflow.com/questions/76527423/how-to-get-the-actual-pixel-size-of-a-transformed-sprite-in-bevy) to see which one would get a response but so far nada.

In the mean time my son needs some help with reading so I'm going to pivot to pygame as I know I can bag out something fast.

I'll learn Rust on one of my other side projects. I think approaching it from the other side, see what low hanging fruit there is a and make a game around it rather than fighting Bevy to do something specific. There is a [fluid simulation lib](https://github.com/dimforge/salva) I found (which is based on a good, [pure Rust linear algebra lib](https://nalgebra.org/)) which would be fun for kids as they love water parks especially sandpits with water!

### Starting at the end

So the first thing I want to do is figure out how to make a n executable from my python script so I can CI/CD all the time and have it playable on 3 OSes (not sure if i get it working on MacOS if that will work on an iPad as that would be a great market). There are two options I can see [pyInstaller](https://pyinstaller.org/en/stable/) and [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/). In both cases you need to run their build on the target OS.

## 15th June, 2023 - Sound problems

SO I have the button on the screen and it makes a sound when you press it. If you smash the button, which 5yos will do, it triggers so much that I fear the app will crash. I thought to try and fix this by installing a Bevy Kira extension but it very difficult to install. Will ask on some forums how to get it going. Don't want to lose momentum so I'll just use the built in stuff. Sound always plays second fiddle to graphics in games.

Next I need to investigate [events](https://bevy-cheatbook.github.io/programming/events.html) in Bevy and get the letters spawning when the button is pressed. I'm thinking SVG for letters so I can go crazy with fonts.

### Bevy Events

There are pretty simple. Four steps

1. Create a plain public struct for the event

```rust
pub struct MyEvent {};
```

2. Register it on your main app

```rust
fn main() {
    App::new()
        .add_event::<MyEvent>()
        ...
}
```

3. Trigger events in a system using an EventWriter

```rust
fn some_system(
    mut somthing_happened_event: EventWriter<MyEvent>,
) {
    somthing_happened_event.send(MyEvent{});
}
```

4. Then receive the event in as many systems as you like

```rust
fn debug_system(
    mut somthing_happened_events: EventReader<MyEvent>,
) {
    for event in somthing_happened_events.iter() {
        println!("Somthing did indeed happen...");
    }
}
```

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