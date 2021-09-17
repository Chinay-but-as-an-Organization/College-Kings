screen v13s20_room():
    tag free_roam

    imagemap:
        idle "images/v13/Scene20/Screens/v13s20_room.webp"
        hover "images/v13/Scene20/Screens/v13s20_room_hover.webp"

        hotspot (39, 81, 515, 773) action Show("v13s20_bathroom")

        hotspot (573, 434, 445, 420) action Show("endFreeRoamConfirm", continueLabel="v13s20_end")

        hotspot (1018, 103, 546, 711) action Jump("v13s20_closet")


screen v13s20_bathroom():
    tag free_roam

    imagemap:
        idle "images/v13/Scene20/Screens/v13s20_bathroom.webp"
        hover "images/v13/Scene20/Screens/v13s20_bathroom_hover.webp"
    
        hotspot (1417, 303, 301, 224) action Jump("v13s20_toothbrush")

        hotspot (465, 630, 1103, 450) action Jump("v13s20_bleach")

        hotspot (307, 0, 1390, 284) action Show("v13s20_room")