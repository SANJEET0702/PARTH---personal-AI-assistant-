import os

import eel

from engine.features import *

eel.init("www")

playassistantsound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')
//designig phase
eel.start('index.html',mode=None,host='localhost', block=True)
