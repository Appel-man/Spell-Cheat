print("Loading Spell Cheat...")


### [ INFORMATION ] ###
#
####
#
# Made By: Abeloos/Abeloser
# Roblox Profile: https://www.roblox.com/users/246043225/profile
# YouTube Channel: https://www.youtube.com/channel/UCyv3T6e_IgU2ZdPk686XX-Q
# GitHub Profile: https://github.com/Abeloser
# This GitHub Page: https://github.com/Abeloser/Spell-Cheat
#
# File Version: 1.1.3
# Language: Python
# Language Version: 3.11.1
#
# Setup:
## Download Python: https://www.python.org/downloads/release/python-3111/
## Open the setup and complete it, add Python to the path (It's a checkbox)
## Open CMD (WINDOWS + R, Type cmd in the textbox and press Enter)
## Enter this command: "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
## Enter this command: "python get-pip.py"
## Enter this command: "pip install pynput"
## SETUP COMPLETE!
#
# How To Use:
## When you did the setup, you only need to do one thing, you have two options.
##
## OPTION 1:
## Open CMD (WINDOWS + R, Insert "cmd" and press Enter)
## Enter this command: "python FILELOCATION"
## Example: "python C:\Users\USERNAME\Downloads\Spell-Cheat.py"
## You can see the file location in explorer (WINDOWS + E)
##
## OPTION 2:
## Use the "Run Spell-Cheat.cmd" file.
## Don't have it? Go to this github page on the top of this information and
## download it.
## Can't find it? Save this text as a .cmd file "python Spell-Cheat.py" and put
## it in the same location/folder/map/directory (all the same)
##
## !! NOTE !!
## !! THE "Run Spell-Cheat.cmd" MUST ALWAYS BE IN THE SAME LOCATION/FOLDER/MAP/
## DIRECTORY OR THAT FILE WONT OPEN/WORK !!
#
# File Name: Spell-Cheat
# File Description:
## This is a Python script for a Roblox Harry Potter game called Magic Training.
## With this script you can cast spells very quicky by using keyboard shortcuts.
## You can block spells, cast spells, autoshoot spells, enable and disable the
## script, switch spell library, change your settings however you would like
## them to be, AI walk when casted a spell, see the logs, and more!
##
## !! I AM NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS !!
##
## This script is smart and s very handy to use!
## If there are any bugs or glitches or updates that you know just let me know!
##
## The Harry Potter game: https://www.roblox.com/games/527730528/Magic-Training
#
####


#Everything In A "try" Block To Catch Errors:
try:
    from pynput.keyboard import Key, Listener
    from pynput.keyboard import Controller as Keyboard
    from pynput.mouse import Button
    from threading import Thread
    from time import sleep as Wait
    import traceback
    
    #Script Setup:
    Keyboard = Keyboard()

    #Script Settings:
    Enabled = True
    lastDirection = ""
    autoShoot = False
    AIMoveCharacter = False
    toggleSpellRank = 0
    Typing = False
    Loop = False
    Chatting = False
    blockDb = False
    
    #All Spells:
    Spells = ["duro", "ebublio", "glacius", "impedimenta", "incarcerous",
              "levicorpus", "locomotor wibbly", "petrificus totalus",
              "pruina tempestatis", "stupefy", "tarantallegra", "avada kedavra",
              "defodio", "deletrius", "infernum","sectumsempra",
              "alarte ascendare", "baubillious", "bombarda", "confringo",
              "crucio", "depulso", "diffindo", "everte statum", "expulso",
              "flare", "incendio", "reducto", "tonitro", "verdimillious",
              "carpe retractum","confundo", "expelliarmus", "flipendo",
              "rictusempra", "obliviate", "obscuro", "protego diabolica",
              "protego totalum", "appa", "ascendio", "episkey",
              "finite incantatem", "relashio", "rennervate", "vulnera sanetur",
              "lumos", "nox", "melofors", "engorgio skullus", "diminuendo",
              "calvorio", "accio", "aboleo"]

    ### [ User Settings ] ###
    ##
    # Leave A Setting Empty To Disable It ( Like this "" ) #
    ##
    keyboardSpells = {"é":["Avada Kedavra", "Episkey"],
                      "\"":["Protego Totalum", "Rennervate"],
                      "'":["Bombarda", "Vulnera Sanentur"],
                    "(":["Appa", "Finite Incantatem"],
                      "§":["Expelliarmus", "Aboleo"]} #Key for spell keybinds
    #
    currentBlockKey = "a" #Current key to block spells
    newBlockKey = "e" #Replacement key to block
    #
    enableKey = "2" #Enable/Disable spell cheat key
    chatKey = "/" #Chat key to disable spell cheat
    #
    autoShootKey = "4" #Enable/Disable autoshoot key
    autoShootSpeed = 1 #Autoshoot speed in seconds
    #
    toggleSpellsKey = "3" #Use next keyboard spell key
    #
    AIMoveCharacterKey = "5" #Moves the character at the last direction key
    characterMovingKeys = ["q", "d", "z", "s"] #Movement keys, now: AZERTY
    ##
    ####

    #Execute Spell Function:
    def typeWordThread(word):
        global Enabled, lastDirection, AIMoveCharacter, Typing
        Wait(0.01)
        Keyboard.type("/")
        Wait(0.01)
        Keyboard.type(str(word))
        Wait(0.01)
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
        Typing = False
        print("Spell Used: {}".format(word))
        if AIMoveCharacter:
            Keyboard.press(lastDirection)
            Wait(0.25)
            Keyboard.release(lastDirection)

    def loopTypeWord(Spell):
        global Enabled, autoShoot, Typing, autoShootSpeed, Loop
        Loop = True
        while Enabled and autoShoot:
            Typing = True
            thread = Thread(target = typeWordThread, args = [Spell])
            thread.daemon = True
            thread.start()
            Wait(autoShootSpeed)
        Loop = False
    
    def typeWord(Spell):
        global autoShoot, Typing
        if autoShoot:
            thread = Thread(target = loopTypeWord, args = [Spell])
            thread.daemon = True
            thread.start()
        else:
            Typing = True
            thread = Thread(target = typeWordThread, args = [Spell])
            thread.daemon = True
            thread.start()

    def blockSpell():
        global currentBlockKey, blockDb
        blockDb = True
        Keyboard.type(currentBlockKey)
        print("Blocked Spell!")
        Wait(0.5)
        blockDb = False
 
    #Key Pressed Function:
    def on_press(key):
        global Enabled, keyboardSpells, enableKey, autoShoot, disableOnChatKey
        global characterMovingKeys, lastDirection, AIMoveCharacter, autoShootKey
        global autoShootSpeed, AIMoveCharacter, disableOnChat, Typing, Loop
        global toggleSpellsKey, toggleSpellRank, currentBlockKey, newBlockKey
        global chatKey, Chatting, blockDb
        
        if key and hasattr(key, "char"):
            Character = str(key.char)
            if lastDirection == "" and AIMoveCharacter:
                lastDirection = characterMovingKeys[0]
            if (keyboardSpells.get(Character) and
                len(keyboardSpells[Character]) >= toggleSpellRank and not Loop):
                if not Enabled:
                    print("Spell Denied: spell cheat is disabled")
                    return
                Spell = keyboardSpells.get(Character)[toggleSpellRank]
                typeWord(Spell)
            elif Typing:
                return
            elif Character == newBlockKey and not Chatting and not blockDb:
                thread = Thread(target = blockSpell)
                thread.daemon = True
                thread.start()
            elif Character == enableKey:
                if Enabled:
                    Enabled = False
                    print("Spell Cheat Disabled!")
                else:
                    Enabled = True
                    Chatting = False
                    print("Spell Cheat Enabled!")
            elif Character == chatKey:
                Enabled = False
                Chatting = True
                print("Spell Cheat Disabled: player is chatting!")
            elif Character in characterMovingKeys and AIMoveCharacter:
                lastDirection = Character
            elif Character == autoShootKey:
                if autoShoot:
                    autoShoot = False
                    print("AutoShoot Disabled!")
                else:
                    autoShoot = True
                    print("AutoShoot Enabled!")
            elif Character == AIMoveCharacterKey:
                if AIMoveCharacter:
                    AIMoveCharacter = False
                    print("AIMoveCharacter Disabled!")
                else:
                    AIMoveCharacter = True
                    print("AIMoveCharacter Enabled!")
            elif Character == toggleSpellsKey:
                Higher = False
                currentSpells = {}
                for Spell in keyboardSpells:
                    if (Spell and
                        len(keyboardSpells[Spell]) - 1 > toggleSpellRank):
                        Higher = True
                        currentSpells[Spell] = (
                            keyboardSpells[Spell][toggleSpellRank + 1])
                if Higher:
                    toggleSpellRank += 1
                    print("\nThe Spell Rank Is Now: " + str(toggleSpellRank))
                    print("Current Spell Scope:")
                    for key in currentSpells:
                        print(key + " = " + currentSpells[key])
                else:
                    toggleSpellRank = 0
                    print("\nThe Spell Rank Is Now: " + str(toggleSpellRank))
                    print("Current Spell Scope:")
                    for Spell in keyboardSpells:
                        if Spell and len(keyboardSpells[Spell]) - 1 >= 1:
                            print(Spell + " = " + keyboardSpells[Spell][0])

    #Key Pressed Listener:
    with Listener(on_press=on_press) as listener:
        print("Spell Cheat Loaded! \n")
        print("Press '" + enableKey + "' to toggle spell cheat!")
        print("Press '" + autoShootKey + "' to toggle autoshoot!")
        print("Press '" + AIMoveCharacterKey + "' to toggle AIMoveCharacter!")
        print("Press '" + toggleSpellsKey + "' to change spell scope!")
        print("\nSpells:")
        for key in keyboardSpells:
            print(key + " = " + str(keyboardSpells[key]))
        print("\n")
        listener.join()
except Exception as error:
    print("Oops!")
    print("An error happened!")
    print("Report the error to the maker or anyone who can fix it!")
    print("Restart the file to try again!")
    print("\nError:\n")
    print("###")
    print(error)
    print("###")
    print(traceback.format_exc())
    print("###")
    print("\nPress enter to close this window!")
    input()
