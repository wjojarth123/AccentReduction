#for windows ONLY
import speech
import sound
from random_word import RandomWords
r = RandomWords()
playing=True
words=0
inaccuracy=0
for i in range(10):
    words+=1
    Word=True
    word=r.get_random_word()
    while Word:
        speech.say(word, 'es_ES')
        r = sound.Recorder('audio.m4a')
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print(word)
        r.record(3)
        text = speech.recognize('audio.m4a', 'en')[0][0]
        if text==word:
            Word=False
        else:
            inaccuracy+=1
            print("try again")
print(inaccuracy/words)
