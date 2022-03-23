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
