screen v11s1_hallway1():
    tag free_roam

    # Background
    if not "riley" in freeroam7:
        # add "images/v11/scene 1/hall1.webp"

        imagemap:
            idle "images/v11/scene 1/v11s1HallIdle.webp"
            hover "images/v11/scene 1/v11s1Hall1Hover.webp"
            ground "images/v11/scene 1/hall1.webp"
            
            alpha False

            hotspot (379, 179, 332, 704) action Jump("v11s1_riley") # Speak to Riley

            if not "delib" in freeroam7:
                hotspot (18, 25, 282, 1049) action Jump("v11s1_delib") # Check door
            else:
                hotspot (18, 25, 282, 1049) action Call("freeRoamSpokenToo", backgroundImg="hall1", returnScreen="v11s1_hallway1")

            hotspot (1324, 201, 134, 406) action Show("v11s1_hallway2") # Hallway 2
        
    else:
        # add "images/v11/scene 1/hall1a.webp"

        imagemap:
            idle "images/v11/scene 1/v11s1HallIdle.webp"
            hover "images/v11/scene 1/v11s1Hall1aHover.webp"
            ground "images/v11/scene 1/hall1a.webp"

            alpha False
            if not "jenny" in freeroam7:
                hotspot (1443, 264, 216, 488) action Jump("v11s1_jenny") # Speak to Jenny
            else:
                hotspot (1443, 264, 216, 488) action Show("confirm", message="Are you sure you want to end free roam?", yes_action=[Hide("confirm"), Jump("v11_case_verdict")])
            if not "delib" in freeroam7:
                hotspot (18, 25, 282, 1049) action Jump("v11s1_delib") # Check door
            else:
                hotspot (18, 25, 282, 1049) action Call("freeRoamSpokenToo", backgroundImg="hall1a", returnScreen="v11s1_hallway1")
            hotspot (1324, 201, 134, 406) action Show("v11s1_hallway2") # Hallway 2

screen v11s1_hallway2():
    tag free_roam

    # add "images/v11/scene 1/hall2.webp"

    imagemap:
        idle "images/v11/scene 1/v11s1HallIdle.webp"
        hover "images/v11/scene 1/v11s1Hall2Hover.webp"
        ground "images/v11/scene 1/hall2.webp"

        alpha False
        if not "mr rose" in freeroam7:
            hotspot (182, 221, 253, 555) action Jump("v11s1_mrrose") # Speak to Mr. Rose
        else:
            hotspot (182, 221, 253, 555) action Call("freeRoamSpokenToo", backgroundImg="hall2", returnScreen="v11s1_hallway2")
        hotspot (246, 891, 1401, 188) action Show("v11s1_hallway1") # Hallway 1