from pygame import mixer

mixer.init()
mixer.music.load("music.mp3")
volume = 0.5
mixer.music.set_volume(volume)
mixer.music.play();

while True:
    print("Press p to Pause || Press r to resume || Press q to Quit || Press + to Volume up || Press - to Volume down ")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == '+':
        volume+=0.2
        mixer.music.set_volume(volume)
    elif query == '-' and volume>=0.1 :
        volume-=0.2
        mixer.music.set_volume(volume)
    elif query == 'e':
        mixer.music.stop()
        break
