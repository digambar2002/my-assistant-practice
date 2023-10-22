import eel
from playsound import playsound

@eel.expose
def playAssisatntSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


