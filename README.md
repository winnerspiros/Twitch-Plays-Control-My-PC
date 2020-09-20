# Installation
If you want to build yourself download python from https://www.python.org/downloads/ and run these in cmd:

• python -m pip install --upgrade pip
• pip install pyautogui
• pip install pynput
• pip install pydirectinput

else:

download the prebuilt pypy build I use here: https://mega.nz/file/PI1TUbYQ#kPtAjUUQJDcol5Yju4660EbvXoXerwM5KKhWi0sqwUM
extract in C:\
add new enviroment variable in path with the folder name e.x. C:\pypy
and done

# Run Script
Go to TwitchPlays_AccountInfo.py put you stream username and oauth from here http://twitchapps.com/tmi/
Then run from a cmd/powershell 'python twitchplays.py' or if you got pypy type 'pypy3 twitchplays.py'. In case 'python twitchplays.py' doesnt work try 'python3', 'py', 'py3' or add variables cause they are missing.

About forever. It's a script that reruns the code in case of a crash. I think you need to npm install it, look here https://www.npmjs.com/package/forever
If you type forever on cmd and it returns stuff you are good to go. The file .bat should be self explained, the way it works is it runs and it hides, if you want to stop script check task manager for a node.js process.
