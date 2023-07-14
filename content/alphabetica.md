---
Title: Phonetica Game Dev Log
slug: reading-video-game-dev-log
summary: A new game I'm working on to help kids learn to read.
date: 2023-06-11
Modified: 2023-07-14
Category: Rust, Software Engineering, Game Development, Linguistics
---


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