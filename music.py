from pygame import mixer

mixer.init()
mixer.music.load("music.mp3")
volume = 0.5
mixer.music.set_volume(volume)
mixer.music.play();

