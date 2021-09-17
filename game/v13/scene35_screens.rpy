screen v13s35_adult_shop():
    modal True

    add "images/v13/Scene35/sex_shop/background.webp"

    text "Money: €{}".format(mc.money) xpos 20 size 50

    vbox:
        align (0.5, 0.5)
        spacing 50

        hbox:
            spacing 50

            imagebutton:
                idle honey.idle_image
                hover honey.hover_image
                insensitive honey.insensitive_image
                sensitive (honey not in mc.inventory.items) or (mc.money < honey.cost)
                action Call("v13s35_buy_item_dialog", honey)

            imagebutton:
                idle butt_plug.idle_image
                hover butt_plug.hover_image
                insensitive butt_plug.insensitive_image
                sensitive (butt_plug not in mc.inventory.items) or (mc.money < butt_plug.cost)
                action Call("v13s35_buy_item_dialog", butt_plug)

            imagebutton:
                idle spankers.idle_image
                hover spankers.hover_image
                insensitive spankers.insensitive_image
                sensitive (spankers not in mc.inventory.items) or (mc.money < spankers.cost)
                action Call("v13s35_buy_item_dialog", spankers)

        hbox:
            xalign 0.5
            spacing 50

            imagebutton:
                idle cuffs.idle_image
                hover cuffs.hover_image
                insensitive cuffs.insensitive_image
                sensitive (cuffs not in mc.inventory.items) or (mc.money < cuffs.cost)
                action Show("v13s35_end_shopping_confirm")

            imagebutton:
                idle feather.idle_image
                hover feather.hover_image
                insensitive feather.insensitive_image
                sensitive (feather not in mc.inventory.items) or (mc.money < feather.cost)
                action Call("v13s35_buy_item_dialog", feather)


screen v13s35_end_shopping_confirm():
    modal True

    use endfrTemplate:
        text "Are you sure you want to finish shopping?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("v13s35_end_shopping_confirm"), SetVariable("freeRoam", False), Return()]
                
            textbutton "No":
                action Hide("v13s35_end_shopping_confirm")