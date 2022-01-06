screen disclaimer():
    add "splashscreen_3"

    imagebutton:
        idle "gui/splashscreen/confirm_idle.png"
        action [SetVariable("persistent.confirm_18", True), Return()]
        xalign 0.5
        ypos 551


label splashscreen:
    # Splashscreen
    scene black
    with dissolve

    scene splashscreen_1
    with dissolve
    pause 2

    scene splashscreen_2
    with dissolve
    pause 2

    if not persistent.confirm_18:
        call screen disclaimer
        with dissolve

    scene black
    with dissolve

    return