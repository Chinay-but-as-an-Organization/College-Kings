define config.enable_steam = True
define config_debug = True # Automatic Testing

define config.version = "1.4.0"

label path_builder:
    $ quick_menu = False
    
    call screen path_builder_starting_location
    return


# The game starts here.
label start:
    if config.developer:
        show screen debug_overlay

    call screen real_life_mode
