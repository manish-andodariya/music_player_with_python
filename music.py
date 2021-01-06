from pygame import mixer

mixer.init()
mixer.music.load("music.mp3")
volume = 0.5
mixer.music.set_volume(volume)
mixer.music.play();

while True:
    print("Press P to Pause || Press R to resume || Press Q to Quit || Press + to Volume up || Press - to Volume down ")//user enter inputs in small case
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


main 1 code
main no code
switch main 1
merge main 1
git push main
both are same
both`s head diff
checkout main
main merge
2 times merge


