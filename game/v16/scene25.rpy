# SCENE 25: MC goes to bed WOLVES OR APES (both)
# Locations: Wolves/Apes dorm room, Wolves/Apes living room
# Characters: MC (Outfit: 5), EMILY (Robe, Lingerie1, Lingerie2)
# Time: Night

label v16s25:

    if joinwolves:
        scene v16s25_1 # TPP. Show MC entering his Wolves Frat Room, slight smile, mouth closed.
    else:
        scene v16s25_14 # TPP. Show MC entering his Apes Frat Room, slight smile, mouth closed.
    with fade

    pause 1

    if joinwolves:
        scene v16s25_1a # TPP. Show MC inside his Wolves Frat Room, closing the door now that he is inside, slight smile, mouth closed.
    else:
        scene v16s25_14a # TPP. Show MC inside his Apes Frat Room, closing the door now that he is inside, slight smile, mouth closed.
    with dissolve
    
    pause 1

    play sound "sounds/doorclose.mp3"

    if joinwolves:
        scene v16s25_2 # TPP. Show MC taking off his shirt in the middle of his Wolves Frat Room, face obscured by shirt.
    else:
        scene v16s25_15 # TPP. Show MC taking off his shirt in the middle of his Apes Frat Room, face obscured by shirt.
    with dissolve

    pause 1
    
    if joinwolves:
        scene v16s25_2a # TPP. In his Wolves Frat Room, Show MC taking off his pants about to just be in his underwear, slight smile, mouth closed.
    else:
        scene v16s25_15a # TPP. In his Apes Frat Room, Show MC taking off his pants about to just be in his underwear, slight smile, mouth closed.
    with dissolve

    pause 1

    if joinwolves:
        scene v16s25_3 # TPP. In his Wolves Frat Room, Show MC getting into bed, slight smile, mouth closed.
    else:
        scene v16s25_16 # TPP. In his Apes Frat Room, Show MC getting into bed, slight smile, mouth closed.
    with dissolve

    pause 1

    if joinwolves:
        scene v16s25_4 # TPP. In MC's Wolves Frat Room, Camera looking down from the ceiling as MC looks up at the ceiling where the camera is, *thinking* MC slight smile, mouth closed.
    else:
        scene v16s25_17 # TPP. In MC's Apes Frat Room, Camera looking down from the ceiling as MC looks up at the ceiling where the camera is, *thinking* MC slight smile, mouth closed.
    with dissolve

    pause 1

    if v14_amber_clean: # [Checkpoint 1.1]
        if amber.relationship >= Relationship.FWB:
            u "(Is Amber relationship material? Definitely something to think about...)"

            u "(I never thought Amber would be the type for a serious relationship... Maybe things have changed.)"

        else: ### if Amber Friend
            u "(Amber's still thinking about detective stuff... Haha, I think she has a fetish!)"

            # [End of Checkpoint 1.1. Continue to Checkpoint 2]

    else: # [Checkpoint 1.2]
        if amber.relationship >= Relationship.FWB: # if MC got a dance
            u "(Holy shit, I can't get Amber's body out of my mind now...)"

            u "(Maybe being a stripper is her true calling... *Laughs*)"

        elif not v16s23_support_amber: # if told Amber to quit stripping (i.e. not FWB and not supported her)
            u "(I hope Amber doesn't stay pissed at me for too long...)"

            u "(I just... I can't stand by and watch her ruin her life.)"

            u "(Especially since I'm the one who could've prevented her from getting this job in the first place.) *Sighs*"

        else:
            u "(If anyone can handle getting harassed by douchebags every night, it's Amber...)"

            u "(I'm glad she's happy.)"

        #[End of Checkpoint 1.2. Continue to Checkpoint 2]

    #[Checkpoint 2]

    if "v15_emily" in sceneList:
        play sound "sounds/vibrate.mp3"

        if joinwolves:
            scene v16s25_4
        else:
            scene v16s25_17
        with vpunch

        pause 0.75

        if joinwolves:
            scene v16s25_5 # TPP. Show MC grabbing his phone off his nightstand in his Wolves Frat Room, confused, mouth closed.
        else:
            scene v16s25_18 # TPP. Show MC grabbing his phone off his nightstand in his Apes Frat Room, confused, mouth closed.
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s25_6 # TPP. In his wolves frat room, Show MC sitting up in bed on his phone pressing a button, slight smile, mouth closed.
        else:
            scene v16s25_19 # TPP. In his Apes frat room, Show MC sitting up in bed on his phone pressing a button, slight smile, mouth closed.
        with dissolve
        
        pause 0.75

        if joinwolves:
            scene v16s25_7 # FPP. Laying down in his Wolves Frat Room bed, MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, Looking at MC on her phone. Show MC's face in the corner small like its a face time, mouth open, Emily slight smile, mouth closed.
        else:
            scene v16s25_20 # FPP. Laying down in his Apes Frat Room bed, MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, Looking at MC on her phone. Show MC's face in the corner small like its a face time, Emily slight smile, mouth closed.
        with dissolve

        u "You love these late-night sessions, huh?"

        if joinwolves:
            scene v16s25_7a # FPP. MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, looking at MC on her phone, Show MC's face in the corner small like its a face time mouth closed, Emily slight smile, mouth open.
        else:
            scene v16s25_20a # FPP. MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, looking at MC on her phone, Show MC's face in the corner small like its a face time, Emily slight smile, mouth open.
        with dissolve

        em "Haha, I do. I can't help but think about you every night when I'm getting naked and cozy."

        if joinwolves:
            scene v16s25_7
        else:
            scene v16s25_20
        with dissolve

        u "Funny, I'm always thinking about you getting naked too..."

        if joinwolves:
            scene v16s25_7b # MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, Show MC's face in the corner small like its a face time mouth closed, Emily blushing and biting her lip.
        else:
            scene v16s25_20b # MC looking at his phone, On the phone a video chat with Emily, Emily wears a robe, Show MC's face in the corner small like its a face time mouth closed, Emily blushing and biting her lip.
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s25_7
        else:
            scene v16s25_20
        with dissolve

        u "So how can I help you tonight?"

        if joinwolves:
            scene v16s25_7a
        else:
            scene v16s25_20a
        with dissolve

        em "Go get a laptop."

        if joinwolves:
            scene v16s25_7
        else:
            scene v16s25_20
        with dissolve

        u "I don't have a laptop. Why do I need a laptop?"

        if joinwolves:
            scene v16s25_7a
        else:
            scene v16s25_20a
        with dissolve

        em "You'll want to see this on a bigger screen. Trust me. *Giggles*"

        menu:
            "Find a laptop": # [Checkpoint 2.1]
                $ add_point(KCT.BOYFRIEND)

                if joinwolves:
                    scene v16s25_7
                else:
                    scene v16s25_20
                with dissolve

                u "One sec, I'll hunt one down."

                if joinwolves:
                    scene v16s25_7a
                else:
                    scene v16s25_20a
                with dissolve

                em "Hehe, okay! Be quick."

                play sound "sounds/dooropen.mp3"

                if joinwolves:
                    scene v16s25_1b # TPP. In his Wolves Frat Room, Show MC leaving his room in his underwear, slight smile, mouth closed.
                else:
                    scene v16s25_14b # TPP. In his Apes Frat Room, Show MC leaving his room in his underwear, slight smile, mouth closed.
                with dissolve

                u "(Laptop... Laptop... Let's check the living room first.)"

                if joinwolves:
                    scene v16s25_8 # TPP. Show MC walking into the Wolves Frat Living Room only in his underwear, slight smile, mouth closed.
                else:
                    scene v16s25_21 # TPP. Show MC walking into the Apes Frat Living Room only in his underwear, slight smile, mouth closed.
                with dissolve

                pause 0.75

                if joinwolves:
                    scene v16s25_9 # TPP. Close up of a laptop on the couch in the Wolves Frat Living Room.
                else:
                    scene v16s25_22 # TPP. Close up of a laptop on the couch in the Apes Frat Living Room.
                with dissolve

                u "(Yes!)"

                if joinwolves:
                    scene v16s25_10 # TPP. In the wolves frat room, Show MC. mouth closed, looking at the lock screen on the laptop.
                else:
                    scene v16s25_23 # TPP. In the Apes frat room, Show MC looking at the lock screen on the laptop.
                with dissolve

                u "(Dammit, of course it's locked. Um, let's try...)"

                scene v16s25_11 # TPP. Just the laptop password screen so we can use it for the Apes version too.
                with dissolve

                menu:
                    "boobiez123":
                        scene v16s25_11a # TPP. Just the laptop desktop screen so we can use it for the Apes version too.
                        with dissolve

                        u "(Haha, no way... I'm in! Are we really that predictable guys?)"

                    "i<3chloe":
                        scene v16s25_11b # TPP. Just the laptop password screen with a red exclamation to show the password is wrong.
                        with dissolve

                        u "(Come on...)"

                        scene v16s25_11
                        with dissolve

                        menu:
                            "boobiez123":
                                scene v16s25_11a
                                with dissolve
                                
                                u "(Haha, no way... I'm in! Are we really that predictable guys?)"

                            "696969":
                                scene v16s25_11b
                                with dissolve

                                u "(Come on...)"

                                scene v16s25_11
                                with dissolve

                                menu:
                                    "boobiez123:":
                                        scene v16s25_11a
                                        with dissolve

                                        u "(Haha, no way... I'm in! Are we really that predictable guys?)"

                    "696969":
                        scene v16s25_11b
                        with dissolve

                        u "(Come on...)"

                        scene v16s25_11 
                        with dissolve

                        menu:
                            "boobiez123":
                                scene v16s25_11a
                                with dissolve

                                u "(Haha, no way... I'm in! Are we really that predictable guys?)"

                            "i<3chloe":
                                scene v16s25_11b
                                with dissolve

                                u "(Come on...)"

                                scene v16s25_11 
                                with dissolve
                                
                                menu:
                                    "boobiez123:":
                                        scene v16s25_11a
                                        with dissolve

                                        u "(Haha, no way... I'm in! Are we really that predictable guys?)"

                play sound "sounds/doorclose.mp3"

                if joinwolves:
                    scene v16s25_1c # TPP. Show MC closing the door to his Wolves Room with the laptop in his other arm, slight smile, mouth closed.
                else:
                    scene v16s25_14c # TPP. Show MC closing the door to his Apes Room with the laptop in his other arm, slight smile, mouth closed.
                with dissolve

                pause 0.75

                if joinwolves:
                    scene v16s25_6
                else:
                    scene v16s25_19
                with dissolve

                u "(Okay, let's connect...)"

                scene v16s25_11c # TPP. Laptop screen, Video chat overlay with Emily, Emily looking at MC, mouth open, on the chat, Emily slight smile, mouth closed.
                with dissolve

                u "Should be good. Can you hear me?"

                scene v16s25_11d # TPP. Laptop screen, Video chat overlay with Emily, Emily looking at MC, mouth closed, on the chat, Emily slight smile, mouth open.
                with dissolve

                em "I hear you! And see you! Hi cutie."

                scene v16s25_11c
                with dissolve

                u "Haha, hey you."

                scene v16s25_11d
                with dissolve

                em "How do I look?"

                scene v16s25_11c
                with dissolve

                u "As hot as ever, obviously."

                scene v16s25_11d
                with dissolve

                em "Hehe, good. I wanted you to see some of my new outfits."

                scene v16s25_11e # TPP. Laptop screen, Video chat overlay with Emily, Emily stood back so MC can see her whole body, Emily's robe falls off revealing her naked, Emily slight smile/MC mouth closed, smiling, surprised.
                with dissolve

                pause 0.75

                scene v16s25_27 # TPP. Laptop screen, Video chat overlay with Emily, Emily slight smile, looking at camera, arching her back a little (pushing out chest/boobs) as she turns her body away from the camera)/MC mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_27a # TPP. Laptop screen, Video chat overlay with Emily, Emily bending over at the hips, pushing her nude ass (a slight view of her pussy is optional at Mozzart's direction) out a little towards the camera, while pulling up the bottoms of lingerie1/MC mouth closed, smiling, surprised.
                with dissolve

                pause 0.75

                scene v16s25_27b # TPP. Laptop screen, Video chat overlay with Emily, Emily slight smile, looking at camera over shoulder, while pulling the strap to her bra of lingerie1 over her shoulder/MC mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_27c # TPP. Laptop screen, Video chat overlay with Emily, Emily posing sexy for the camera, slight smile, mouth closed//MC mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_11f # TPP. Laptop screen, Video chat overlay with Emily (lingerie1), Emily close to the camera with one hand on her boob, Emily smirking, mouth open/ MC mouth closed, smiling, happy
                with dissolve

                em "Do you like it?"

                menu:
                    "Like it":
                        $ add_point(KCT.BRO)
                        
                        scene v16s25_11g # TPP. Laptop screen, Video chat overlay with Emily (lingerie1), Emily close to the camera with one hand on her boob, Emily biting her lip/ MC mouth open, smiling, happy.
                        with dissolve

                        u "Yeah, it looks great on you."

                        scene v16s25_11f
                        with dissolve

                        em "Why thank you... I like it too."

                        em "Are you touching yourself yet?"

                        scene v16s25_11g
                        with dissolve

                        u "Ha, should I be?"

                        scene v16s25_11f
                        with dissolve

                        em "Do as you please."

                    "Love it":
                        $ add_point(KCT.BOYFRIEND)
                        
                        scene v16s25_11g
                        with dissolve

                        u "I absolutely love it... You look hot as hell."

                        scene v16s25_11f
                        with dissolve

                        em "Haha, good."

                        scene v16s25_11h # TPP. Laptop screen, Video chat overlay with Emily (lingerie1), Emily slight smile, mouth open, looking into camera while both hands slightly pushing her boobs up/MC mouth closed, smiling, happy. 
                        with dissolve

                        em "Are you touching yourself yet?"

                        scene v16s25_11g
                        with dissolve

                        u "Ha, should I be?"

                        scene v16s25_11f
                        with dissolve

                        em "Do as you please."

                    "Not my favorite":
                        $ add_point(KCT.TROUBLEMAKER)
                        
                        scene v16s25_11g
                        with dissolve

                        u "Hmm, it's cute, I guess. Just not my favorite."

                        scene v16s25_11p # TPP. Laptop Screen, Video chat overlay with Emily (lingerie1), Emily looking at MC on the video chat, Emily slightly frown, mouth open/ MC, mouth closed, slight smile.
                        with dissolve

                        em "Really? I thought you'd like this one..."

                        em "I guess I can always return it."

                        scene v16s25_11i # TPP. Laptop Screen, Video chat overlay with Emily (lingerie1), Emily looking at MC on the video chat, Emily slight frown, mouth closed/ MC, mouth open, slight smile.
                        with dissolve

                        u "It's your call, it doesn't look horrible, haha."

                scene v16s25_11j # TPP. Laptop Screen, Video chat overlay with Emily, Emily, smiling, facing the camera, bra unhooked, off her bobos (as if she just took it off) but still draping on her arms/ MC, mouth closed, smiling, happy.
                with dissolve

                em "Okay, next!"

                scene v16s25_11q # TPP. Close up of MC laying in bed ,dark, looking at the laptop screen, smiling, enjoying what he sees on the screen. The light from the laptop shines on MC's face.
                with dissolve

                pause 0.75

                scene v16s25_11k # TPP. Laptop Screen, Video chat overlay with Emily, Show Emily reaching off the screen to grab her lingerie2 her boobs right in front of her laptop camera, Emily slight smile, mouth closed/ MC, mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_11r # TPP. Laptop Screen, Video Chat overlay with Emily, Emily putting on the top of lingerie2 on while winking at MC on the chat, Emily smirking, mouth closed/ MC, mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_11s # TPP. Laptop Screen, Video Chat Overlay with Emily, Emily standing a little back bent over showing her naked bottom as she pulls up the bottom part of lingerie2, Emily biting her lip/ MC, mouth closed, smiling, happy.
                with dissolve

                pause 0.75

                scene v16s25_11l # TPP. Laptop screen, Video chat overlay With Emily, Emily close to her screen using her arms to push up her boobs, Emily smirking, mouth open/ MC, mouth closed, smiling, happy.
                with dissolve

                em "What about this one?"

                menu:
                    "Like it":
                        $ add_point(KCT.BRO)
                        
                        scene v16s25_11m # TPP. Laptop Screen, Video chat overlay with Emily, Emily close to her screen using her arms to push up her boobs, Emily biting her lip/ MC, mouth open, smiling.
                        with dissolve

                        u "Yeah, that one I like. It compliments your body really well."

                        scene v16s25_11l
                        with dissolve

                        em "Yeah? Does it?"

                        scene v16s25_11n # TPP. Laptop screen, Video chat overlay with Emily, Emily stood away a bit from the screen, Emily turned around on her tip toes, her hands on her hips showing off her butt, looking over her shoulder to see the chat, Emily smirking, mouth closed/ MC mouth open, smiling, surprised.
                        with dissolve

                        u "Mm-hmm..."

                        scene v16s25_11l
                        with dissolve

                        em "*Laughs* Perfect."

                    "Love it":
                        $ add_point(KCT.BOYFRIEND)
                        
                        scene v16s25_11m
                        with dissolve

                        u "Oh, shit... I love this one."

                        scene v16s25_11l
                        with dissolve

                        em "Haha, do you?"

                        scene v16s25_11m
                        with dissolve

                        u "Hmm... Let me see the back?"

                        scene v16s25_11l
                        with dissolve

                        em "As you wish... *Giggles*"

                        scene v16s25_11n
                        with dissolve

                        u "Damn..."

                        scene v16s25_11l
                        with dissolve

                        em "Is that your final answer?"

                        scene v16s25_11m
                        with dissolve

                        u "Y-yes. Final answer, hot as fuck."

                        scene v16s25_11l
                        with dissolve

                        em "*Laughs* Perfect."

                    "Not a fan":
                        $ add_point(KCT.TROUBLEMAKER)
                        
                        scene v16s25_11m
                        with dissolve

                        u "Eh, I'm not really a fan of this one. Looks better on your floor, I think."

                        scene v16s25_11l
                        with dissolve

                        em "Haha, naughty boy."

                        em "You seriously don't like it? This one is my favorite..."

                        scene v16s25_11m
                        with dissolve

                        u "I'm sorry, I just... kind of hate it? Ha."

                        scene v16s25_11l
                        with dissolve

                        em "Well, that sucks. *Sighs* Oh well!"

                scene v16s25_11o # TPP. Laptop screen, Video chat overlay with Emily, Emily putting her robe over the lingerie2, the lingerie not visible anymore, slight smile, mouth open/MC, mouth closed, smiling, happy.
                with dissolve

                em "That's it. I hope you enjoyed the show."

                scene v16s25_11c
                with dissolve

                u "Of course, I did."

                scene v16s25_11d
                with dissolve

                em "Thanks for letting me model for you."

                scene v16s25_11c
                with dissolve

                u "I'll always be available for that, haha."

                scene v16s25_11d
                with dissolve

                em "*Chuckles* I like the feeling of you watching me..."

                scene v16s25_11c
                with dissolve

                u "Hmm, that's not weird."

                scene v16s25_11d
                with dissolve

                em "Haha, goodnight handsome."

                scene v16s25_11c
                with dissolve

                u "Night, Emily."

                if joinwolves:
                    scene v16s25_12 # TPP. In the Wolves Frat Room, Show MC sitting in bed and closing the laptop, slight smile, mouth closed.
                else:
                    scene v16s25_24 # TPP. In the Apes Frat Room, Show MC sitting in bed and closing the laptop, slight smile, mouth closed.
                with dissolve

                u "(I'd better get this laptop back before it's missed. Then it's time for sleep!)"

                play sound "sounds/dooropen.mp3"

                if joinwolves:
                    scene v16s25_1d # TPP. In his wolves frat room, MC opening the door to his room with the laptop in his arm, only in his underwear, slight smile, mouth closed.
                else:
                    scene v16s25_14d # TPP. In his Apes frat room, MC opening the door to his room with the laptop in his arm, only in his underwear, slight smile, mouth closed.
                with dissolve

                pause 0.75

                if joinwolves:
                    scene v16s25_13 # TPP. In the wolves living room, Show MC leaving the Laptop on the couch where he found it, slight smile, mouth closed.
                else:
                    scene v16s25_25 # TPP. In the Apes living room, Show MC leaving the Laptop on the couch where he found it, slight smile, mouth closed.
                with dissolve

                pause 0.75

                play sound "sounds/doorclose.mp3"

                if joinwolves:
                    scene v16s25_1e # TPP. In his wolves frat room closing the door to his room in just his underwear, slight smile, mouth closed.
                else:
                    scene v16s25_14e # TPP. In his Apes frat room closing the door to his room in just his underwear, slight smile, mouth closed.
                with dissolve

                pause 0.75

            "I'm too tired": # [Checkpoint 2.2]
                if joinwolves:
                    scene v16s25_7
                else:
                    scene v16s25_20
                with dissolve

                u "I'm super tired right now, Emily. Can we do this another time?"

                if joinwolves:
                    scene v16s25_7a
                else:
                    scene v16s25_20a
                with dissolve

                em "Aww, I was really excited to show you my sexy new outfits, though..."

                em "But okay. If you're sure."

                if joinwolves:
                    scene v16s25_7
                else:
                    scene v16s25_20
                with dissolve

                u "I'd love to, but I can barely keep my eyes open, ha."

                if joinwolves:
                    scene v16s25_7a
                else:
                    scene v16s25_20a
                with dissolve

                em "It's okay... I miss you, [name]."

                if joinwolves:
                    scene v16s25_7
                else:
                    scene v16s25_20
                with dissolve

                u "I miss you too. Night, Emily."

                if joinwolves:
                    scene v16s25_7a
                else:
                    scene v16s25_20a
                with dissolve

                em "Goodnight, baby. I love you."

                menu:
                    "I love you, too":
                        $ add_point(KCT.BOYFRIEND)

                        if joinwolves:
                            scene v16s25_7
                        else:
                            scene v16s25_20
                        with dissolve

                        u "I love you, too."

                        if joinwolves:
                            scene v16s25_7b
                        else:
                            scene v16s25_20b
                        with dissolve

                        pause 0.75

                    "Hang up":
                        $ add_point(KCT.TROUBLEMAKER)

                        play sound "sounds/hangup.mp3"

                        if joinwolves:
                            scene v16s25_7
                        else:
                            scene v16s25_20
                        with dissolve

                        pause 0.75

                        if joinwolves:
                            scene v16s25_4
                        else:
                            scene v16s25_17
                        with dissolve

                        u "*Whistles* Anyway..."

        if joinwolves:
            scene v16s25_4a # TPP. Show MC with his eyes closed as he falls asleep, neutral face, mouth closed.
        else:
            scene v16s25_17a # TPP. Show MC with his eyes closed as he falls asleep, neutral face, mouth closed.
        with fade
        
        pause 0.75
            
            # [End of Checkpoint 2.2. Continue to Checkpoint 3]
            
            # [Checkpoint 3]
            
        jump v16s25a