import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
time.sleep(10) #wait 10 seconds before executing the script - gives you time to open the game window


while True:
    pyautogui.hotkey('tab') #selects nearest mob
    time.sleep(0.05)

    pyautogui.hotkey('alt', '1') #sends pet into battle
    time.sleep(0.5)

    pyautogui.press('1') #basic melee attack is bound to key 1 in game
    time.sleep(5.5)

    for i in range (3):         #repeat below loop X times - easy to adjust depending on how long it takes you to kill a mob
        pyautogui.press('2')    #druid starting damage skill bound to key 2 in game
        time.sleep(1.5)         #wait for cast time

        pyautogui.press('f4')  # pick up is bound to key F4 in came. If mob is still alive, skill will be casting and won't interrupt for pickup. If mob is dead, character will collect loot
        time.sleep(1)

        pyautogui.press('2')    #druid starting damage skill bound to key 2 in game
        time.sleep(1.5)         #wait for cast time

        pyautogui.press('f4')  # pick up is bound to key F4 in came. If mob is still alive, skill will be casting and won't interrupt for pickup. If mob is dead, character will collect loot
        time.sleep(1)

        pyautogui.press('f2')  # pet heal is bound to key F2 in game
        time.sleep(2.5)

    pyautogui.press('~')    # in game this hotkey cycles through the skill bars
    time.sleep(0.05)

    pyautogui.press('8')   # on all each bar I have different utility skills bound to key 8 - heal(druid skill that cds 300 seconds); mana regen, skill that swaps HP and Mana
    time.sleep(0.05)

    pyautogui.press('9')   # pet food is bound to key 9 on one of the bars
    time.sleep(0.05)

    pyautogui.press('7')   # on each bar a different weapon is bound to key 7, this way script swaps weapon after each mob. Helps avoid weapon breaking due to low durability.
    time.sleep(0.05)

    # RETURN TO POSITION:
    pyautogui.click(1900, 111)         #opens the 'added points' menu in game - make sure do adjust to your screen size
    time.sleep(0.25)
    pyautogui.doubleClick(204, 740)
    time.sleep(0.25)
    pyautogui.click(1900, 111)
    time.sleep(0.25)
    pyautogui.moveTo(1192, 185)

    pyautogui.keyDown('Space')      #useful when fighting flying mobs - maintains height so that characted doesn't start attaching ground mobs
    time.sleep(3)
    pyautogui.keyUp('Space')

    pyautogui.hotkey('esc')
    time.sleep(0.5)





