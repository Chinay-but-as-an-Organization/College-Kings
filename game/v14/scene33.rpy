# SCENE 33: MC heads back to his room
# Locations: Wolves/Apes room.
# Characters: MC (Outfit: 2), Lauren (Outfit: Nude)
# Time: Evening


label v14s33:
    if joinwolves:
        scene v14s33_1 # TPP. Show MC showering, slight smile, mouth closed
        with dissolve

        pause 0.5

        scene v14s33_2 # TPP. Show MC looking at his phone while sitting on the bed in his Wolves Room, slight smile, mouth closed.
        with dissolve

        if not laurenrs:
            scene v14s33_2a # TPP. Same as v14s33_2, Mc in a different pose looking at his phone in his wolves room, slight smile, mouth closed.
            with dissolve

            pause 0.75

            if v11s23_penelope_date:
                jump v14s34
            else:
                jump v14s35
        else:
            pause 0.75

            play sound "sounds/call.mp3"

            scene v14s33_2a
            with dissolve

            pause 0.5

            play sound "sounds/answercall.mp3"

            scene v14s33_2b # TPP. Same as v14s33_2a. MC with the phone to his ear, slight smile, mouth open. 
            with dissolve
            
            u "Hello?"

            scene v14s33_3 # TPP. Show Lauren nude in her bed with the phone up to her ear, her other hand rubbing to the left of her vagina, slight smile, mouth open.
            with dissolve

            la "Hey, babe. Did I wake you?"

            scene v14s33_3a # TPP. Same as v14s33_3, Laurens hand now rubbing to the right of her vagina, slight smile, mouth closed. 
            with dissolve

            u "Nope. What's up?"

            scene v14s33_3
            with dissolve

            la "Not much, I just miss you. *Chuckles* I've been thinking about you all night..."

            menu:
                "Want me to come over?":
                    scene v14s33_3a
                    with dissolve

                    u "Want me to come over?"

                    scene v14s33_3
                    with dissolve

                    la "Haha, I wish."

                "I miss you too":
                    scene v14s33_3a
                    with dissolve

                    u "I miss you too."

                    scene v14s33_3
                    with dissolve

                    la "I wish you could come over..."

            la "But sadly, I have an early meeting with the Deers tomorrow."

            scene v14s33_3a
            with dissolve

            u "Oh, haha."

            scene v14s33_3
            with dissolve

            la "Well... I was thinking about trying something."

            scene v14s33_3a
            with dissolve

            u "Oh? What's that?"

            scene v14s33_3
            with dissolve

            la "I mean..."

            la "I'm in bed naked, all alone, and I'm thinking I should try to watch some porn and..."

            la "*Chuckles* I don't know... See what it does for me?"

            menu:
                "Laugh":
                    scene v14s33_3a
                    with dissolve

                    u "*Laughs* You've never watched porn before?"

                    scene v14s33_3
                    with dissolve

                    la "Oh my gosh, don't laugh!"

                    la "And no, I haven't ever felt the need to but... I've been really curious."

                    scene v14s33_3a
                    with dissolve

                    u "Well, be sure to tell me how it goes. *Chuckles*"

                    scene v14s33_3
                    with dissolve

                    la "I don't know if I want to now..."

                    la "Kinda embarrassed, ha."

                    scene v14s33_3a
                    with dissolve

                    u "No need to be embarrassed, haha. Enjoy yourself."

                    scene v14s33_3
                    with dissolve

                    la "I will. Just, um..."

                    la "Just go back to whatever you were doing."

                    scene v14s33_3a
                    with dissolve

                    u "Will do. *Chuckles*"

                    play sound "sounds/rejectcall.mp3"

                    scene v14s33_2a
                    with dissolve

                    u "(Lauren watching porn for the first time? Haha! I hope she didn't take that the wrong way... But, damn...)"

                    pause 0.75

                    if v11s23_penelope_date:
                        jump v14s34
                    else:
                        jump v14s35

                "Get excited":
                    scene v14s33_3a
                    with dissolve

                    u "Oh shit, now I really wish I was there."

                    scene v14s33_3
                    with dissolve

                    la "*Chuckles* We think a lot alike."

                    scene v14s33_3a
                    with dissolve

                    u "Do you know what you wanna watch?"

                    scene v14s33_3
                    with dissolve

                    la "Plenty!"

                    scene v14s33_3a
                    with dissolve

                    u "O-Oh! *Chuckles* Well shit, I guess I'll let you go handle your biz."

                    scene v14s33_3
                    with dissolve

                    la "When we get together again, I wanna talk about it. *Chuckles*"

                    scene v14s33_3a
                    with dissolve

                    u "Okay, sure. I'd like that."

                    scene v14s33_3
                    with dissolve

                    la "Good Night!"

                    pause 0.75

                    play sound "sounds/rejectcall.mp3"

                    scene v14s33_2a
                    with dissolve

                    u "(Lauren is watching porn for the first time...)"

                    pause 0.75
                    
                    if v11s23_penelope_date:
                        jump v14s34
                    else:
                        jump v14s35
    if joinapes:
            scene v14s33_1 # TPP. Show MC showering, slight smile, mouth closed
            with dissolve

            pause 0.5

            scene v14s33_4 # TPP. Show MC looking at his phone while sitting on the bed in his Apes room, slight smile, mouth closed.
            with dissolve

            if not laurenrs:
                scene v14s33_4a # TPP. Same as v14s33_4, Mc in a different pose looking at his phone in his Apes room, slight smile, mouth closed.
                with dissolve

                pause 0.75

                if v11s23_penelope_date:
                    jump v14s34
                else:
                    jump v14s35
            else:
                pause 0.75

                play sound "sounds/call.mp3"

                scene v14s33_2a
                with dissolve

                pause 0.5

                play sound "sounds/answercall.mp3"

                scene v14s33_4b # TPP. Same as v14s33_4a. MC with the phone to his ear, slight smile, mouth open. 
                with dissolve
                
                u "Hello?"

                scene v14s33_3 # TPP. Show Lauren nude in her bed with the phone up to her ear, her other hand rubbing to the left of her vagina, slight smile, mouth open.
                with dissolve

                la "Hey, babe. Did I wake you?"

                scene v14s33_3a # TPP. Same as v14s33_3, Laurens hand now rubbing to the right of her vagina, slight smile, mouth closed. 
                with dissolve

                u "Nope. What's up?"

                scene v14s33_3
                with dissolve

                la "Not much, I just miss you. *Chuckles* I've been thinking about you all night..."

                menu:
                    "Want me to come over?":
                        scene v14s33_3a
                        with dissolve

                        u "Want me to come over?"

                        scene v14s33_3
                        with dissolve

                        la "Haha, I wish."

                    "I miss you too":
                        $ add_point(KCT.BOYFRIEND)
                        scene v14s33_3a
                        with dissolve

                        u "I miss you too."

                        scene v14s33_3
                        with dissolve

                        la "I wish you could come over..."

                la "But sadly, I have an early meeting with the Deers tomorrow."

                scene v14s33_3a
                with dissolve

                u "Oh, haha."

                scene v14s33_3
                with dissolve

                la "Well... I was thinking about trying something."

                scene v14s33_3a
                with dissolve

                u "Oh? What's that?"

                scene v14s33_3
                with dissolve

                la "I mean..."

                la "I'm in bed naked, all alone, and I'm thinking I should try to watch some porn and..."

                la "*Chuckles* I don't know... See what it does for me?"

                menu:
                    "Laugh":
                        scene v14s33_3a
                        with dissolve

                        u "*Laughs* You've never watched porn before?"

                        scene v14s33_3
                        with dissolve

                        la "Oh my gosh, don't laugh!"

                        la "And no, I haven't ever felt the need to but... I've been really curious."

                        scene v14s33_3a
                        with dissolve

                        u "Well, be sure to tell me how it goes. *Chuckles*"

                        scene v14s33_3
                        with dissolve

                        la "I don't know if I want to now..."

                        la "Kinda embarrassed, ha."

                        scene v14s33_3a
                        with dissolve

                        u "No need to be embarrassed, haha. Enjoy yourself."

                        scene v14s33_3
                        with dissolve

                        la "I will. Just, um..."

                        la "Just go back to whatever you were doing."

                        scene v14s33_3a
                        with dissolve

                        u "Will do. *Chuckles*"

                        play sound "sounds/rejectcall.mp3"

                        scene v14s33_4a
                        with dissolve

                        u "(Lauren watching porn for the first time? Haha! I hope she didn't take that the wrong way... But, damn...)"

                        pause 0.75

                        if v11s23_penelope_date:
                            jump v14s34
                        else:
                            jump v14s35

                    "Get excited":
                        $ add_point(KCT.BOYFRIEND)
                        scene v14s33_3a
                        with dissolve

                        u "Oh shit, now I really wish I was there."

                        scene v14s33_3
                        with dissolve

                        la "*Chuckles* We think a lot alike."

                        scene v14s33_3a
                        with dissolve

                        u "Do you know what you wanna watch?"

                        scene v14s33_3
                        with dissolve

                        la "Plenty!"

                        scene v14s33_3a
                        with dissolve

                        u "O-Oh! *Chuckles* Well shit, I guess I'll let you go handle your biz."

                        scene v14s33_3
                        with dissolve

                        la "When we get together again, I wanna talk about it. *Chuckles*"

                        scene v14s33_3a
                        with dissolve

                        u "Okay, sure. I'd like that."

                        scene v14s33_3
                        with dissolve

                        la "Good Night!"

                        pause 0.75

                        play sound "sounds/rejectcall.mp3"

                        scene v14s33_4a
                        with dissolve

                        u "(Lauren is watching porn for the first time...)"

                        pause 0.75
                        
                        if v11s23_penelope_date:
                            jump v14s34
                        else:
                            jump v14s35