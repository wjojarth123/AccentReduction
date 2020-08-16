import turtle
import time
import json
import re
from os.path import join, dirname
import speech_recognition as sr
import wave
import  vlc
import time
from gtts import gTTS
import pyaudio
import random
from PyDictionary import PyDictionary
wordlist=[]
file=open("list.txt")
a=file.read()
print(a)
wordlist=a.split('\n')
# num_lines = sum(1 for line in file)
# for line in range(0,num_lines):
#     print(file.readline(5))
#     wordlist.append(file.readline())
print(wordlist)
dictionary=PyDictionary()
r = sr.Recognizer()
wordsComplete=0
inccorectWords=[]
chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 5
filename = "output.wav"
p = pyaudio.PyAudio()



word=turtle.Turtle()
recording=turtle.Turtle()
awnser=turtle.Turtle()
dictturtle=turtle.Turtle()
awnser.shape('circle')
recording.shape('circle')
recording.hideturtle()
recording.penup()
dictturtle.penup()
awnser.penup()
recording.goto(300  ,0)
awnser.goto(300  ,-300)
dictturtle.goto(-300  ,-300)
word.ht()
def getResult():
    with sr.AudioFile('output.wav') as source:

        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        #try:

            # using google speech recognition
        results=[]
        try:
            results.append(r.recognize_google(audio_text).lower())
            #results.append(r.recognize_sphinx(audio_text).lower())
            #apikey results.append(r.recognize_wit(audio_text).lower())
            #results.append(r.recognize_api(audio_text).lower())
            #results.append(r.recognize_ibm(audio_text).lower())
            #apikey results.append(r.recognize_bing(audio_text).lower())
            id='aUqG6M26l4HhciRvcDINrQ=='
            key='hRcltnYRVunwgoPykUriDTDstwHCI4vgBDr1Bx2fkMmJ2N5egNu6gwR0XY_BCdTLZX3fPYCdIao_gNiL3Rg-uA=='
            results.append(r.recognize_houndify(audio_text,id,key).lower())
            print('Converting audio transcripts into text ...')
            print(results)

        except:
             print('Sorry.. run again...')
        return results


def recordAudio():
    print('Recording')
    recording.st()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    a=0
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
        a+=1
        if a==20:recording.ht()
        if a==40:
            recording.st()
            a=0


    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    #p.terminate()
    print("recording complete")
    recording.ht()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def playAudio():
    p = vlc.MediaPlayer("text.mp3")
    p.play()
    time.sleep(3)
    p.stop()
    print("complete")
def getRecording(text,speed):
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = speed)
    speech.save('text.mp3')

while True:
    wordsComplete+=1
    rand=random.randrange(5,40)
    print(rand)
    currentword=wordlist[rand]
    word.write(currentword, align="center",font=("Verdana", 30, "normal"))
    meaning=dictionary.meaning(currentword)
    meaningSplit=re.findall('.',str(meaning))
    a=0
    b=''
    for char in meaningSplit:
        a+=1
        if a==50:
            a=0
            b+=char+'\n'
        else:
            b+=char
    dictturtle.write(b, align="left",font=("Verdana", 15, "normal"))
    getRecording(currentword,False)
    playAudio()
    print(currentword)
    recordAudio()
    result=getResult()
    #print('a',result,'b')
    print(result)
    currentword=currentword.replace(" ", "")
    currentword=currentword.replace("\n", "")
    print(result)
    #print('a',result,'b')
    if any(currentword in s for s in result):
        print('correct')
        awnser.color('green')
    if not any(currentword in s for s in result):
        print('incorrect')
        awnser.color('red')
        #inccorectWords.append(currentword)
        getRecording(currentword,True)
        playAudio()
        recordAudio()
        result=getResult()
        #print('a',result,'b')
        #print('a',result,'b')
        if any(currentword in s for s in result):
            print('correct')
            awnser.color('green')
        if not any(currentword in s for s in result):
            print('incorrect')
            awnser.color('red')
            inccorectWords.append(currentword)
    word.clear()
    dictturtle.clear()




# word.write("hello", align="center",font=("Verdana", 30, "normal"))
# time.sleep(5)
# word.clear()
# word.write("bye", align="center",font=("Verdana", 30, "normal"))
# time.sleep(5)
