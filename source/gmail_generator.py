#! python3

#   Author      : Altify
#   Updated    : blactorio
#   GitHub      : https://github.com/Altify-Development
#   GitHub      : https://github.com/Altify-Developing
#   Year        : 2022
#   Description : [Updated] Script that generates random Gmail account. Still stalls at phone verification.

import pyautogui
import sys
import time
import random
import string

# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
def msg(
        _option_,
        _message_
        ):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')


# Exiting function
def ext():
    msg(1,'Exiting...')
    sys.exit()


# Function used to open Firefox
def open_firefox():
        
    # Printing basic message
    msg(1,'Opening Firefox...')

    # Location the start button
    _start_button_=pyautogui.locateOnScreen('images/start_button.png')
    _location_=pyautogui.center(_start_button_)

    # Clicking the start button
    if not  pyautogui.click(_location_):
        msg(1,'Opened start menu successfully!')
    else:
        msg(3,'Failed to open start menu!')
        ext()

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    
    # Print message
    msg(1,'Firefox is now open and running.')


# Function used to locate GMail
def locate_gmail():
    
    #Sleep for a while and wait for Firefox to open
    time.sleep(3)

    # Printing message
    msg(1,'Opening Gmail...')

    # Typing the website on the browser
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')
    
    # Wait for a while until the website responds
    time.sleep(6)

    # Print a simple message
    msg(1,'Locating the form...')

    # Locate the form
    pyautogui.press('tab')
 
    time.sleep(2)

    _gmail_ = pyautogui.locateOnScreen('images/gmail_form.png')
    formx, formy = pyautogui.center(_gmail_)
    pyautogui.click(formx, formy)
    
    # Check and print message
