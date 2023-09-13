import os

# GUI Library
import eel 

#Frontend
eel.init('www')


# Use MS Edge default browser
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# Staring Index Page
eel.start('index.html', mode=None, host='localhost', block=True)

