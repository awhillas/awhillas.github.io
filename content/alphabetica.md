---
Title: Alphabetica Game Dev Log
summary: A new game I'm working on to help kids learn to read.
date: 2023-06-11
Modified: 2023-06-23
Category: Rust, Software Engineering, Game Development
---

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