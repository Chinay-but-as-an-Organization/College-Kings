# SCENE 32: MC's Room WOLVES OR APES (both)
# Locations: MC's WOLVEs Frat House
# Characters: MC (Outfit: 9)
# Time: Afternoon

label v16s32:
    if not joinwolves: # -if Apes
        scene v16s32_1 # TPP. MC enters his bedroom, sitting on the edge of his bed, no expression, mouth is closed
        with dissolve

        u "(This situation between Grayson and Samantha is going to explode soon. I can feel it coming...)"

        pause 0.75

        scene v16s32_1a # TPP. MC (no expression, mouth closed) sitting on his bed with back to the corner (generic white wall) looking at his phone.
        with dissolve

    else: # -if Wolves
        scene v16s32_2 # TPP. MC enters his bedroom, sitting on the edge of his bed, no expression, mouth is closed
        with dissolve

        u "*Sighs* (Damn, Imre. What's gotten into him lately, talking himself into a punch like that?)"

        u "(Maybe he's still getting over the whole Karen thing...)"

        scene v16s32_2a # TPP. MC (no expression, mouth closed) sitting on his bed with back to the corner (generic white wall) looking at his phone.
        with dissolve

        u "(I can't believe Chris actually punched him, though. He's clearly not in control of his emotions lately.)"

    # -if AubreyTamed and having date

        scene v16s32_3 # TPP. Show just Mc looking at his phone, slight smile, mouth is closed, (generic white wall) for the background
        with dissolve

        u "(Hmm, now would be a good time to sort out everything for my date with Aubrey.)"

        u "(First, the restaurant.)"

        scene v16s32_3a # TPP. Show just Mc tapping on his phone, slight smile, mouth is closed, same position and background as v16s32_3
        with dissolve

        u "(Hmm... Live grill... Too risky.)"

        u "(Live band... Too loud...)"

        scene v16s32_3
        with dissolve

        u "(Ah, here we go. Something fancy and calm.)"

        scene v16s32_3a
        with dissolve

        u "(Oh, last step: Special occasion package or standard date reservation?)"

        scene v16s32_3
        with dissolve

        u "(I know it's not Aubrey's birthday, or our anniversary... *Chuckles* But, we'll get a free dessert if we pretend...)"

        scene v16s32_3a
        with dissolve

        u "(Or should I keep it as a standard date reservation?)"

        scene v16s32_3a
        with dissolve

        menu:

            "Standard reservation":

                scene v16s32_3
                with dissolve

                u "(Standard it is. I've done some sneaky things, but lying about a birthday at a high-class restaurant? That's just evil...)"

            "Birthday reservation":
                $ v16birthday_reservation = True

                scene v16s32_3
                with dissolve

                u "(Who doesn't love free dessert? The birthday girl is not going to see this coming, haha!)"

        scene v16s32_3a
        with dissolve

        u "(I can book her a cab too, and just meet her at the restaurant...)"

        scene v16s32_3
        with dissolve

        u "(I'm sure she can get there on her own though...)"

        scene v16s32_3
        with dissolve

        menu:

            "Book her a cab":

                scene v16s32_3a
                with dissolve

                u "Okay so the cab is going to cost twenty dollars..."

                scene v16s32_3b # TPP. Show just Mc slightly holding his finger away from his phone, slight smile, mouth is closed, same position and background as v16s32_3
                with dissolve

                u "Oh, the cab driver will bring your date a bouquet of flowers for an additional twenty."

                scene v16s32_3
                with dissolve

                u "(Hmm, that's a total of forty dollars for a cab and flowers.)"

                scene v16s32_3
                with dissolve

                menu:

                    "Just the cab":
                        $ v16aubrey_cab = True

                        scene v16s32_3a
                        with dissolve

                        u "(Yeah, I don't think the flowers are necessary. Let's save the money.)"

                    "Cab/Flower Combo":
                        $ v16aubrey_flower_cab = True

                        scene v16s32_3a
                        with dissolve

                        u "(Now that I've seen the option, I can't stop thinking about how happy it'd make her... Flowers, yes.)"

                scene v16s32_3b
                with dissolve

                u "(Oh, shit. It says I have to pay the driver in cash. Can't use my card.)"

                # -if helping Chloe with Spa day

                scene v16s32_3b
                with dissolve

                u "(I can't spend any of the money Chloe gave me for spa supplies.)"

                scene v16s32_3
                with dissolve

                u "(The only cash I can really use is the fifty dollars that Lindsey gave me to donate to the animal shelter. Should I use that money for my date with Aubrey?)"

                scene v16s32_3b
                with dissolve

                menu:

                    "Use the money":

                        scene v16s32_3a
                        with dissolve

                        u "(What Lindsey doesn't know won't hurt her, right? Surely....)"

                    "Cancel the booking":
                        $ v16aubrey_cab = False
                        $ v16aubrey_flower_cab = False

                        scene v16s32_3a
                        with dissolve

                        u "(I can't use someone else's money for my date, haha. I think Aubrey would understand."

            "She can manage":

                scene v16s32_3
                with dissolve

                u "(She can find her own way there, ha. She's a tough girl.)"

        scene v16s32_3a
        with dissolve

        u "And... Done."

    # -Regardless of AubreyTamed-

    # -if MC is not helping Chloe

        scene v16s32_3b
        with dissolve

        u "..."

        scene v16s32_3
        with dissolve

        u "(Hang on...)"

        scene v16s32_3c # TPP. MC looks around, confused, still holding his phone, mouth is closed
        with dissolve

        u "(What's that smell?)"

        scene v16s32_3d # TPP. MC turns his head to his armpit for a sniff, with a slightly disgusted expression
        with dissolve

        u "(Oh, fuck! I need a shower...)"

        jump v16s33 # -Transition to Scene 33-

    # -if MC is helping Chloe with newspaper cover

        # -MC's phone vibrates. He checks it and sees a text from Chloe-

        scene v16s32_5 # FPP. Close up shot of MC's phone in his hand, with a new message text appearing on his phone
        with dissolve

        $ chloe.messenger.newMessage("Elijah is available rn, let's go meet with him?.")
        $ chloe.messenger.addReply("Okay. OMW")
        $ chloe.messenger.newMessage("Hurry up :)")
        $ chloe.messenger.addReply("Running all the way, boss :P")

        scene v16s32_3
        with dissolve

        u "(Hope this goes according to plan. A happy Chloe is much easier to be around! *Laughs*)"

        jump v16s34 # -Transition to Scene 34-

    # -if MC is helping Chloe with spa night

        # -MC checks his phone-

        scene v16s32_3
        with dissolve

        u "(Oh shit, I need to get started on shopping... Chloe would kick my ass if she knew what I was doing right now, haha."

        scene v16s32_6 # TPP. Show a close-up shot of Mc's face, slight smile, mouth is closed, same position and background as v16s32_3
        with dissolve

        u "Spa shit, here I come!"

        jump v16s35 # -Transition to Scene 35-