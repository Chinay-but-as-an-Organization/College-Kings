init python:
    class KCT(Enum):
        BRO = _("bro")
        BOYFRIEND = _("boyfriend")
        TROUBLEMAKER = _("troublemaker")


    def add_point(var, value=1):
        # Don't update kct if kct is locked
        if locked_kct or _in_replay:
            return

        if pb_kct_notification:
            renpy.show_screen("popup", message=_("{} point added".format(var.value.capitalize())))

        # Update the KCT variables
        setattr(store, var.value, getattr(store, var.value) + value)
        
        old_kct = kct

        # Sort KCT values
        kct_dict = {
            "popular": bro * troublemaker / float(boyfriend),
            "confident": boyfriend * troublemaker / float(bro),
            "loyal": bro * boyfriend / float(troublemaker)
        }
        
        # Update KCT
        store.kct = max(kct_dict, key=lambda k: kct_dict[k])

        # Notify user on KCT change
        if kct != old_kct:
            renpy.notify(_("Your KCT has changed to " + kct))


# KCT Screens
screen kct_choice_hint():
    style_prefix "kct_choice"

    frame:
        xalign 1.0
        xoffset -100

        background "gui/kct/background_{}.webp".format(kct)

        hbox:
            spacing 5
            align (0.5, 0.5)
            xoffset 20

            add Transform("gui/kct/logo.webp", zoom=0.2382) yalign 0.5

            text kct.upper() yalign 0.5

style kct_choice_text is syne_extra_bold_22


screen kct_popup(required_kct=None):
    modal True
    zorder 300

    if required_kct is None or required_kct == kct:
        $ message = _("Congratulations! Your Key Character Trait {b}[kct]{/b} has just changed the outcome of a decision someone was making.")
    else:
        $ message = _("Unfortunately, your Key Character Trait {b}[kct]{/b} did not change the outcome of this decision.")

    use alert_template(message):
        textbutton _("OK"):
            align (0.5, 1.0)
            action Return()

    if config_debug:
        timer 0.1 action Return()