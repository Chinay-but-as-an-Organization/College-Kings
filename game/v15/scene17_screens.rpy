screen v15s17_gift_selection():
    modal True

    fixed:
        xalign 0.5
        xysize (1190, 127)

        add "images/v15/Scene 17/gift_picking_screen/header_box.png" xalign 0.5
        text "Lauren Halloween Birthday Party" align (0.5, 0.5) yoffset -10

    vbox:
        align (0.5, 0.5)
        yoffset 50
        spacing 50

        hbox:
            spacing 50

            for item in (gift_card_50, emerald_bracelet, ruby_choker_necklace):
                vbox:
                    spacing 10

                    fixed:
                        xysize (225, 350)

                        add "images/v15/Scene 17/gift_picking_screen/item_box.png"
                        text item.name xalign 0.5 ypos 25 style "item_name_text"
                        add item.idle_image align (0.5, 0.5)
                    
                    imagebutton:
                        idle "images/v15/Scene 17/gift_picking_screen/pick_item_idle.png"
                        action [Function(mc.inventory.add_item, item), Return()]

        hbox:
            xalign 0.5
            spacing 50

            for item in (brown_horse_golden_mane, white_horse_black_mane):
                vbox:
                    spacing 10

                    fixed:
                        xysize (225, 350)

                        add "images/v15/Scene 17/gift_picking_screen/item_box.png"
                        text item.name xalign 0.5 ypos 15 style "item_name_text"
                        add item.idle_image align (0.5, 0.5)
                    
                    imagebutton:
                        idle "images/v15/Scene 17/gift_picking_screen/pick_item_idle.png"
                        action [Function(mc.inventory.add_item, item), Return()]


style item_name_text is text:
    xsize 185
    font "fonts/Montserrat-Bold.ttf"
    size 15
    color "#FFCC2B"
    text_align 0.5