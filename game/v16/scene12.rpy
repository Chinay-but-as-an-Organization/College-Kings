# SCENE 12: Mc & Chloe in planning room
# Locations: Planning board room
# Characters: CHLOE (Outfit: 2), MC (Outfit: 5)
# Time: Afternoon

label v16s12:
    scene v16s12_1 # TPP. Show Chloe and MC walking into the planning board room, both slight smiles, mouths closed, Chloe walking in in front of MC
    with dissolve

    pause 1

    if (v15_chloe_lindseysabotage and not v15_chloe_postkiwii) and v15_lindsey_recording > 0: # if PA announcement 
        scene v16s12_2 # FPP. MC and Chloe in planning board room, standing in front of the board, next to each other, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open
        with dissolve

        cl "Phew! Now that we're in private, we can finally talk about how the announcement went, and..."

        if chloe.relationship >= Relationship.GIRLFRIEND:
            scene v16s12_3 # TPP. Show Chloe giving MC a kiss
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 1.5

        scene v16s12_2a # FPP. Same as v16s12_2, Chloe smiling, mouth open
        with dissolve

        cl "It was perfect!"

        scene v16s12_2b # FPP. Same as v16s12_2a, Chloe smiling, mouth closed
        with dissolve

        u "Haha, I know! As soon as everyone heard those words..."

        scene v16s12_2a
        with dissolve

        cl "I could practically feel her votes coming over to me. *Laughs*"

        scene v16s12_2b
        with dissolve

        u "Haha, it was a good plan."

        scene v16s12_2a
        with dissolve

        cl "You did great, seriously. Thank you."

        scene v16s12_2b
        with dissolve

        u "Sure thing. What's next?"

        scene v16s12_2
        with dissolve

        cl "Phase three!"

        scene v16s12_2e
        with dissolve

    elif (v15_chloe_lindseysabotage and not v15_chloe_postkiwii): # if tried PA announcement but couldn't record anything useful
        scene v16s12_2c # FPP. Same as v16s12_2, Chloe slightly sad, mouth open
        with dissolve

        cl "Okay, just a quick review of phase two. It sucked that you didn't manage to record anything I could use."

        scene v16s12_2d # FPP. Same as v16s12_2c, Chloe slightly sad, mouth closed
        with dissolve

        u "Yeah, I'm sorry. I tried, but I couldn't get her drunk enough."

        scene v16s12_2c
        with dissolve

        cl "We need to succeed this time. We have no choice."

        scene v16s12_2
        with dissolve

        cl "I think you'll like these ideas too."

        scene v16s12_2e
        with dissolve

    if v15s22_meeting_points >= 1:
        scene v16s12_2
        with dissolve

        cl "Oh, I haven't gotten the chance to tell you, but we had the Chicks meeting this morning."

        scene v16s12_2e # FPP. Same as v16s12_2, Chloe slight smile, mouth closed
        with dissolve

        u "Oh yeah?"

        scene v16s12_2
        with dissolve

        cl "Yeah, I announced that we were successful in getting lower tuition fees and they freaked, haha."

        scene v16s12_2b
        with dissolve

        u "That's great! I wish I could've been there."

        scene v16s12_2a
        with dissolve

        cl "Me too, but... They were all in tears. *Chuckles*"

        scene v16s12_2e
        with dissolve

        u "Even Lindsey?"

        scene v16s12_2
        with dissolve

        cl "Ha, um... She kinda just stood up and walked out."

        scene v16s12_2e
        with dissolve

        u "Ouch..."

        scene v16s12_2a
        with dissolve

        cl "Yeah, this is perfect. We need to keep on the offensive for phase three."

        scene v16s12_2
        with dissolve

        cl "I want to make sure I win with no contest."

        scene v16s12_2f # FPP. Same as v16s12_2, Chloe looking at the board, Chloe slight smile, hand on chin (as if she's thinking deeply), mouth closed
        with dissolve

        u "(I can't tell if this competitive side of Chloe is scary hot or just scary.)"

    u "Okay, show me what you've got."

    python:
        chloe_board = PlanningBoard("images/v16/planning_boards/chloe_background.webp", money=chloe_board.money) ### to be replaced with v16 board

        chloe_board.add_approach("Newspaper",
            "Decide the cover of the new student newspaper",
            opinion="\"Elijah is starting a school newspaper, and for the first edition, I NEED to have control over what or who is on the cover. We just have to convince him somehow to let us decide what goes on front.\"")
        
        chloe_board.add_approach("Sparty",
            "Chicks spa day",
            opinion="\"I really want to treat the girls, and sadly... I mean all of them. I wanna put the drama aside for one night and have a relaxing Sparty! Get it? Spa party? No? Okay, anyway! They're gonna love it and they're gonna love me after it.\"")

        chloe_board.add_task("Newspaper",
            "Convince Elijah to let us decide over the cover",
            opinion="\"Convincing Elijah really shouldn't be too hard. We can set up a meeting with him and see what he thinks, and maybe we can work out some sort of deal.\"",
            people=[elijah,chloe,mc])

        v16s12_chloe_on_cover = chloe_board.add_subtask("Newspaper",
            "Promote Chloe on the cover",
            opinion="\"For the cover, promoting myself is the obvious choice I can get a good headshot, I already have a few, haha. Then we just have to decide what we want it to say, and what might be a good look.\"")

        chloe_board.add_subtask("Newspaper",
            "Embarrass Lindsey on the cover",
            opinion="\"Instead of putting myself on the cover, we could use this to our advantage and really screw with Lindsey's campaign. Maybe we can find an interesting photo or even photoshop one.\"")
            
        chloe_board.add_task("Newspaper",
            "Design cover",
            opinion="\"The final step is to design it the way we want. As long as it looks perfect, we just give the final image to the newspaper team.\"")

        chloe_board.add_task("Sparty",
            "Buy items for spa day",
            opinion="\"Shopping for the items we want is the first step, we need to make sure we pick things that smell nice, aren't cheap, and are going to be fun to use during the party.\"",
            cost=100)

        v16s12_chloe_real_masseuse = chloe_board.add_subtask("Sparty",
            "Hire professional masseuse",
            opinion="\"Massages are key and we want them to be mesmerized by professional hands. It costs a pretty dollar, but it means that you and I get to focus on the Sparty and the Sparty people.\"",
            cost=100)

        chloe_board.add_subtask("Sparty",
            "[name] does the massages",
            opinion="\"If we wanna save some dime, you can be our masseuse for the night...? It's up to you, haha.\"")

        chloe_board.add_task("Sparty",
            "Host spa day",
            opinion="\"Last but not least, we host the Sparty! Remember, I'm going to be on my best behavior and avoid drama at all costs, so please help me follow through with that, haha.\"",
            people=[chloe,nora,aubrey,lindsey,jenny])

    call screen planning_board(chloe_board)

    if chloe_board.approach is not None:
        $ v16_chloe_newspaper = chloe_board.approach.id == "Newspaper"

    if chloe_board.selected_task is not None:
        $ v16_chloe_on_cover = chloe_board.selected_task == v16s12_chloe_on_cover
        $ v16_chloe_real_masseuse = chloe_board.selected_task == v16s12_chloe_real_masseuse

    # End planning board (screen disappears)

    scene v16s12_4 # TPP. Show MC pointing at something on the board (show the board from behind so we don't have to draw anything on the board), MC serious expression, other hand on chin, mouth open
    with dissolve

    u "Both great ideas, but... I think this is the smartest move."

    if v16_chloe_newspaper:
        scene v16s12_2e
        with dissolve

        u "The cover of the first SVC newspaper is going to be very influential."

        scene v16s12_2
        with dissolve

        cl "Yeah, that's what I was thinking. I just hope Elijah is easy to persuade."

        scene v16s12_2e
        with dissolve

        u "I'm sure it'll be fine. We're both charming, attractive... smart?"

        scene v16s12_2a
        with dissolve

        cl "Mmm... You lost me at smart"

        scene v16s12_2g # FPP. Same as v16s12_2, Chloe laughing
        with dissolve

        cl "*Laughs*"

        scene v16s12_2 
        with dissolve

        cl "Okay, now go. I'll text you when I need you. Have fun!"
    
    else:
        scene v16s12_2e
        with dissolve

        u "Getting the girls on your side with a spa day? That's genius."

        scene v16s12_2
        with dissolve

        cl "Yeah, I love it too. The girls are going to get completely pampered."

        scene v16s12_2b
        with dissolve

        u "Just the girls?"

        scene v16s12_2a
        with dissolve

        cl "Haha, shut up. Ladies first, you can have the leftovers."

        scene v16s12_2e
        with dissolve

        u "Even Lindsey... That might make things interesting, you know. Can you keep her happy all night?"

        scene v16s12_2c
        with dissolve

        cl "*Sighs* Right. Let's just keep a positive attitude, yeah? Yeah."

        scene v16s12_2d
        with dissolve

        u "Yeah... (I'll think about it.)"

        scene v16s12_2h # FPP. Same as v16s12_2, Chloe handing MC money, Chloe slight smile, mouth open
        with dissolve

        cl "Here's some cash for the supplies. I don't need any change so spend it all. This is going to be well worth it."

        scene v16s12_2b
        with dissolve

        u "Okay, I'll get some nice girl-smelly things."

        scene v16s12_2a
        with dissolve

        cl "Haha, have fun!"
    
    menu:
        "Always do!":
            $ add_point(KCT.BOYFRIEND)
            scene v16s12_2b
            with dissolve

            u "Always do!"

            scene v16s12_2a
            with dissolve

            cl "Haha, I'm so happy you're doing this with me."

        "I'll try...":
            $ add_point(KCT.TROUBLEMAKER)
            scene v16s12_2d
            with dissolve

            u "I'll try... Hopefully nothing bad happens."

            scene v16s12_2c
            with dissolve

            cl "Why would you even say that? Are you trying to jinx me?"

            scene v16s12_2e
            with dissolve

            u "No, I'm just saying that-"

            scene v16s12_2
            with dissolve

            cl "We need to always keep a positive mindset, [name]!"

    scene v16s12_2a
    with dissolve

    cl "Now get out there and get to work."

    if chloe.relationship >= Relationship.GIRLFRIEND:
        scene v16s12_3
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 1.5

    scene v16s12_2b
    with dissolve

    u "Aye, aye, Captain!"

    scene v16s12_5 # TPP. Show MC walking out, smiling, mouth closed, Chloe in background watching him walk out, mouth closed, smiling
    with dissolve

    pause 1

    jump v16s13