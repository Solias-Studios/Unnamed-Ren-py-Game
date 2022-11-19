label splashscreen:

    scene black
    $ renpy.pause (1.0, hard=True)

    show text "Project SOLIAS Presents..." with dissolve
    $ renpy.pause (2.0, hard=True)

    hide text with dissolve
    $ renpy.pause (2.0, hard=True)
    
    ## Plays introductory cutscene the first time the game is run. After that, it will simply skip to the main menu.
    if persistent.first_run == False:
        play movie "assets/testy.webm"
        $ renpy.pause(35, hard=True) ## prevents user from skipping
        pause 1
        stop movie
        $ persistent.first_run = True
        return
    else:
        return