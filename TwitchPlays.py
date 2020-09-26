import time, subprocess, ctypes, random, string, re, sys, os, TwitchPlays_Connection, pyautogui, pydirectinput, pynput
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN
from pynput.mouse import Button, Controller
SendInput = ctypes.windll.user32.SendInput
reg = re.compile('[^0-9a-z\s]')
reg2 = re.compile('[WASD\*]\s')
reg3 = re.compile('[A-Z]')
def nothing():
    os.system('cls')
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)
mouse = Controller()
Q=0x10
W=0x11
E=0x12
R=0x13
T=0x14
Y=0x15
U=0x16
I=0x17
O=0x18
P=0x19
A=0x1E
S=0x1F
D=0x20
F=0x21
G=0x22
H=0x23
J=0x24
K=0x25
L=0x26
Z=0x2C
X=0x2D
C=0x2E
V=0x2F
B=0x30
N=0x31
M=0x32
ESC=0x01
ONE=0x02
TWO=0x03
THREE=0x04
FOUR=0x05
FIVE=0x06
SIX=0x07
SEVEN=0x08
EIGHT=0x09
NINE=0x0A
ZERO=0x0B
MINUS=0x0C
EQUALS=0x0D
BACKSPACE=0x0E
SEMICOLON=0x27
TAB=0x0F
CAPS=0x3A
ENTER=0x1C
LEFT_CONTROL=0x1D
LEFT_ALT=0x38
LEFT_SHIFT=0x2A
SPACE=0x39
DELETE=0x53
COMMA=0x33
PERIOD=0x34
BACKSLASH=0x35
NUMPAD_0=0x52
NUMPAD_1=0x4F
NUMPAD_2=0x50
NUMPAD_3=0x51
NUMPAD_4=0x4B
NUMPAD_5=0x4C
NUMPAD_6=0x4D
NUMPAD_7=0x47
NUMPAD_8=0x48
NUMPAD_9=0x49
NUMPAD_PLUS=0x4E
NUMPAD_MINUS=0x4A
LEFT_ARROW=0xCB
RIGHT_ARROW=0xCD
UP_ARROW=0xC8
DOWN_ARROW=0xD0
LEFT_MOUSE=0x100
RIGHT_MOUSE=0x101
MIDDLE_MOUSE=0x102
MOUSE3=0x103
MOUSE4=0x104
MOUSE5=0x105
MOUSE6=0x106
MOUSE7=0x107
MOUSE_WHEEL_UP=0x108
MOUSE_WHEEL_DOWN=0x109
Ffour=0x3E
RIGHT_SHIFT=0x36
RIGHT_CONTROL=0xA3
RIGHT_ALT=0xA5
L_WIN=0x5d
R_WIN=0x5C
t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);
while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        nothing()
        continue
    else:
        try:
                for message in new_messages:
                    msg = message['message'].lower()
                    msg_preserve_caps = message['message']
                    username = message['username'].lower()
                    usr = username.decode()
                def obs():
                    print (msg_preserve_caps + ' (' + usr + ')')                   
                if msg in ['left', 'l']:
                    obs()
                    pydirectinput.move(-100,0)
                if msg in ['light left', 'light l']:
                    obs()
                    pydirectinput.move(-25,0)
                if msg in ['right', 'r']:
                    obs()
                    pydirectinput.move(100,0)
                if msg in ['light right', 'light r']:
                    obs()
                    pydirectinput.move(25,0)
                if msg in ['up', 'u']:
                    obs()
                    pydirectinput.move(0, -100)
                if msg in ['light up', 'light u']:
                    obs()
                    pydirectinput.move(0, -25)
                if msg in ['down', 'd']:
                    obs()
                    pydirectinput.move(0, 100)
                if msg in ['light down', 'light d']:
                    obs()
                    pydirectinput.move(0, 25)              
                if msg in ['rightclick', 'right click', 'click right', 'right cl', 'rightcl']:
                    obs()
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                if msg in ['hold left click']:
                    obs()
                    mouse.press(Button.left)
                if msg in ['hold right click']:
                    obs()
                    mouse.press(Button.right)
                if msg in ['click', 'cl']:
                    obs()
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                if msg in ['doubleclick', 'double click', 'double cl', 'doublecl']:
                    obs()
                    mouse.press(Button.left)
                    time.sleep(0.04)
                    mouse.release(Button.left)
                    mouse.press(Button.left)
                    time.sleep(0.04)
                    mouse.release(Button.left)
                if msg in ['tab']:
                    obs()
                    PressKeyPynput(TAB)
                    ReleaseKeyPynput(TAB)
                if msg in ['enter', 'en']:
                    obs()
                    PressKeyPynput(ENTER)
                    ReleaseKeyPynput(ENTER)
                if msg in ['space', 'spc']:
                    obs()
                    PressKeyPynput(SPACE)
                    ReleaseKeyPynput(SPACE)
                if msg in ['where?', 'where']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    time.sleep(0.004)
                    ReleaseKeyPynput(LEFT_CONTROL)
                if msg in ['win', 'windows key', 'win key', 'windows']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    PressKeyPynput(ESC)
                    ReleaseKeyPynput(LEFT_CONTROL)
                    ReleaseKeyPynput(ESC)
                if msg in ['win s', 'windows s']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    PressKeyPynput(ESC)
                    ReleaseKeyPynput(LEFT_CONTROL)
                    ReleaseKeyPynput(ESC)
                    time.sleep(0.004)
                    PressKeyPynput(SPACE)
                    ReleaseKeyPynput(SPACE)
                if msg in ['stop all keys', 'stop keys', '!stop', '!end', 'end keys', 'end all keys', 'release key', 'release keys', 'release all keys', 'stop' , 'end']:
                    obs()
                    ReleaseKeyPynput(RIGHT_CONTROL)
                    ReleaseKeyPynput(RIGHT_ALT)
                    ReleaseKeyPynput(TAB)
                    ReleaseKeyPynput(LEFT_SHIFT)   
                if msg in ['hold ctrl', 'hold control', 'hold ctrl key', 'hold control key']:
                    obs()
                    PressKeyPynput(RIGHT_CONTROL)
                if msg in ['hold alt', 'hold alt key']:
                    obs()
                    PressKeyPynput(RIGHT_ALT)
                if msg in ['hold tab', 'hold tab key']:
                    obs()
                    PressKeyPynput(TAB)
                if msg in ['hold shift', 'hold shift key']:
                    obs()
                    PressKeyPynput(LEFT_SHIFT)
                if msg in ['control t', 'ctrl t']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    time.sleep(0.004)
                    PressKeyPynput(T)
                    ReleaseKeyPynput(LEFT_CONTROL)
                    ReleaseKeyPynput(T)
                if msg in ['control w', 'ctrl w']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    time.sleep(0.004)
                    PressKeyPynput(W)
                    ReleaseKeyPynput(LEFT_CONTROL)
                    ReleaseKeyPynput(W)
                if msg in ['drag mouse up', 'drag up mouse']:
                    obs()
                    pydautogui.drag(0, -50, 0.25, button='left')
                if msg in ['drag mouse down', 'drag down mouse']:
                    obs()
                    pyautogui.drag(0, 50, 0.25, button='left')
                if msg in ['drag mouse right', 'drag right mouse']:
                    obs()
                    pydautogui.drag(50, 0, 0.25, button='left')
                if msg in ['drag mouse left', 'drag left mouse']:
                    pyautogui.drag(-50, 0, 0.25, button='left')
                if msg in ['backspace', 'back space']:
                    obs()
                    PressKeyPynput(BACKSPACE)
                    ReleaseKeyPynput(BACKSPACE)
                if msg in ['arrow up', 'up arrow']:
                    obs()
                    PressKeyPynput(UP_ARROW)
                    time.sleep(1)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['arrow down', 'down arrow']:
                    obs()
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(1)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['arrow left', 'left arrow']:
                    obs()
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(1)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['alt tab', 'alt-tab']:
                    obs()
                    PressKeyPynput(LEFT_ALT)
                    time.sleep(0.004)
                    PressKeyPynput(TAB)
                    ReleaseKeyPynput(LEFT_ALT)
                    ReleaseKeyPynput(TAB)
                if msg in ['arrow right', 'right arrow']:
                    obs()
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(1)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['quit', 'exit']:
                    obs()
                    PressKeyPynput(LEFT_ALT)
                    PressAndHoldKey(Ffour, 0.004)
                    ReleaseKeyPynput(LEFT_ALT)
                if msg in ['its stuck', 'it is stuck']:
                    obs()
                    mouse.position = (500, 500)
                if msg in ['escape', 'esc']:
                    obs()
                    PressKeyPynput(ESC)
                    ReleaseKeyPynput(ESC)
                if msg in ['close tab', 'close the tab']:
                    obs()
                    PressKeyPynput(LEFT_CONTROL)
                    PressAndHoldKey(W, 0.004)
                    ReleaseKeyPynput(LEFT_CONTROL)
                if msg in ['hold mouse', 'hold the mouse']:
                    obs()
                    mouse.press(Button.left)
                    time.sleep(3)
                    mouse.release(Button.left)
                if msg == "hold mouse long":
                    obs()
                    mouse.press(Button.left)
                    time.sleep(9)
                    mouse.release(Button.left)
                if msg.startswith('type '): 
                    try:
                        typeMsg = msg_preserve_caps[5:]
                        lengg= len(typeMsg)
                        if reg3.search(typeMsg) and lengg==1:
                            obs()
                            pydirectinput.typewrite(typeMsg.lower())
                        elif reg2.findall(typeMsg) and lengg!=1:
                            obs()
                            pydirectinput.typewrite(typeMsg.lower())
                        elif reg.search(typeMsg):
                            obs()
                            pydirectinput.typewrite(typeMsg)
                        else:
                            obs()
                            pydirectinput.typewrite(typeMsg)
                    except:
                        print("Typing this particular message didn't work: " + msg)
                if msg.startswith("go to "): 
                    try:
                        obs()
                        coord = msg[6:]
                        xval,yval = coord.split(' ',1)
                        xval = int(xval)
                        yval = int(yval)
                        pydirectinput.moveTo(xval, yval) 
                    except:
                        print("Typing this particular message didn't work: " + msg)
                if msg in ['select all', 'control all', 'ctrl all', 'ctrl a']:
                        obs()
                        PressKeyPynput(LEFT_CONTROL)
                        PressAndHoldKey(A, 0.004)
                        ReleaseKeyPynput(LEFT_CONTROL)
                if msg.startswith('d for '): 
                    try:
                        timee = msg[6:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(D,timee)
                    except:
                        print('error')
                if msg.startswith('a for '): 
                    try:
                        timee = msg[6:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(A,timee)
                    except:
                        print('error')
                if msg.startswith('s for '): 
                    try:
                        timee = msg[6:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(S,timee)
                    except:
                        print('error')
                if msg.startswith('w for '): 
                    try:
                        timee = msg[6:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(W,timee)
                    except:
                        print('error')
                if msg.startswith('up arrow for '): 
                    try:
                        timee = msg[13:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(UP_ARROW,timee)
                    except:
                            print('er')   
                if msg.startswith('left arrow for '): 
                    try:
                        timee = msg[15:]
                        timee = float(timee)
                        if timee<=10:
                            obs()
                            PressAndHoldKey(LEFT_ARROW,timee)
                    except:
                            print('er')    
                if msg.startswith('right arrow for '): 
                    try:
                        timee = msg[16:]
                        timee = float(timee)
                        if timee<=10 and time>=0:
                            obs()
                            PressAndHoldKey(RIGHT_ARROW,timee)
                    except:
                            print('er')
                if msg.startswith('down arrow for '): 
                    try:
                        timee = msg[15:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            obs()
                            PressAndHoldKey(DOWN_ARROW,timee)
                    except:
                        print('er')
        except:
            print('Encountered an exception while reading chat.')
