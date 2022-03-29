# SCENE 36: Transition Mc gets dressed up
# Locations: MC's Wolves/Apes room
# Characters: MC: (Outfit: Date/Suit)
# Time: Morning

label v16s36:
# -MC gets dressed. Quick shots of different stages of dress. He ends up smiling, looking very smart for his date-
    if joinwolves:
        scene v16s36_1 # TPP. In wolves room. Show MC in his underwear putting on a black shirt, MC neutral face, mouth closed.
    else:
        scene v16s36_3 # TPP. In apes room. Show MC in his underwear putting on a black shirt, MC neutral face, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s36_1a # TPP. In wolves room. Show MC putting on a pair of pants, MC neutral face, mouth closed.
    else:
        scene v16s36_3a # TPP. In apes room. Show MC putting on a pair of pants, MC neutral face, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s36_2 # TPP. In wolves room. Show MC looking in the mirror, MC slight frown, mouth closed.
    else:
        scene v16s36_4 # TPP. In apes room. Show MC looking in the mirror, MC slight frown, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s36_1b # TPP. In Wolves room. MC in his underwear again putting on a nice button up shirt, MC visibly stressed, mouth closed.
    else:
        scene v16s36_3b # TPP. In apes room. MC in his underwear again putting on a nice button up shirt, MC visibly stressed, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s36_1c # TPP. In Wolves Room. MC wearing his nice button up shirt, putting on a pair of pants that match nicely, MC only slightly stressed, mouth closed.
    else:
        scene v16s36_3c # TPP. In apes Room. MC wearing his nice button up shirt, putting on a pair of pants that match nicely, MC only slightly stressed, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s36_2a # TPP In wolves room. MC in his new nice outfit looking at himself in the mirror, MC slight smile, mouth closed.
    else:
        scene v16s36_4a # TPP In apes room. MC in his new nice outfit looking at himself in the mirror, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

# SCENE 37: Transition Mc walking to restaurant
# Locations: Sidewalk
# Characters: MC (Outfit: Suit)
# Time: Evening

    scene v16s37_1 # TPP. MC walks along the street, slight smile, mouth is closed
    with fade

    u "(This is going to be a special night, I can already feel it. Just don't fuck it up, [name]. *Laughs*)"

    jump v16s38 # -Transition to Scene 38-