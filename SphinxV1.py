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
dictionary=PyDictionary()
r = sr.Recognizer()
wordsComplete=0
inccorectWords=[]
wordlist=['wage','wait','wake','walk','wall','wallet','want','ward','warehouse','warfare','warm','warmer','warn','warrant','warranty','wary','wash','waste','watch','watchdog','water','waterproof','waters','wave','weak','weaken','weaker','weakest','weakness','wealth','wealthiest','wealthy','weapon','wear','wearable','wearables','weather','website','websites','week','weekend','weekly','weigh','weight','weird','welcome','welcomed','welcoming','welfare','well','wells','west','western','whale','whales','what','whatever','wheat','wheel','wheelchair','when','whenever','where','whereabouts','whereas','wherever','whether','which','while','white','whoever','whole','wholesale','wholly','whom','whopping','whose','wide','widely','wider','widespread','widgets','widow','width','wife','wild','wildfire','wildlife','wildly','will','willingness','wind','winding','window','wine','wing','winner','winter','wipe','wire','wired','wireless','wirelessly','wisdom','wise','wish','with','withdraw','withdrawal','within','without','withstand','witness','woke','woman','wonder','wonderful','wood','wooden','word','work','worker','workflow','workflows','workforce','workload','workout','workplace','workstation','world','worldwide','worm','worry','worse','worst','worth','worthwhile','worthy','would','wound','wounded','wounding','wrap','wreck','wreckage','wrist','write','writer','wrong','vacant ','vacation ','vaccination ','vaccine ','vacuum ','vague ','vaguely ','vain ','valid ','validate ','validation ','validity ','valley ','valuable ','valuation ','value ','valued ','valuing ','valve ','vampire ','vanilla ','vantage ','vapor ','variable ','variables ','variant ','variation ','variety ','various ','vast ','vastly ','vault ','vector ','vegan ','vegetable ','vegetation ','vehemently ','vehicle ','vein ','velocity ','vending ','vendor ','venerable ','venom ','vent ','ventilation ','venture ','ventured ','venturing ','venue ','verbal ','verdict ','verge ','verifiable ','verification ','verify ','veritable ','versa ','versatile ','versatility ','version ','versus ','vertebrate ','vertical ','vertically ','verticals ','very ','vessel ','vest ','vested ','veteran ','veto ','vetoed ','viability ','viable ','vibrant ','vibration ','vice ','vicinity ','vicious ','victim ','victory ','video ','videogame ','videotaped ','view ','viewable ','viewed ','viewer ','viewfinder ','viewing ','viewpoint ','vigil ','vigilance ','vigilant ','vigilante ','vigorous ','vigorously ','villa ','village ','villagers ','vintage ','vinyl ','violate ','violation ','violence ','violent ','violently ','viral ','virtual ','virtually ','virtue ','virus ','visa ','visibility ','visible ','visibly ','vision ','visionary ','visit ','visitor ','visual ','visualize ','visually ','visuals ','vital ','vivid ','vocal ','vodka ','voice ','voicemail ','void ','volatile ','volatility ','volcanic ','volcano ','voltage ','volume ','voluntarily ','voluntary ','volunteer ','volunteered ','vortex ','vote ','voter ','vowed ','vowing ','voyage ']
chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 3
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
        try:

            # using google speech recognition
            data = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(data)

        except:
             print('Sorry.. run again...')
    return data


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
    currentword=wordlist[random.randrange(0,len(wordlist))]
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
    result=result.replace(" ", "")
    currentword=currentword.replace(" ", "")
    result.lower()
    #print('a',result,'b')
    if currentword in result:
        print('correct')
        awnser.color('green')
    if not currentword in result:
        print('incorrect')
        awnser.color('red')
        #inccorectWords.append(currentword)
        getRecording(currentword,True)
        playAudio()
        recordAudio()
        result=getResult()
        result=result[0]
        #print('a',result,'b')
        result=result.replace(" ", "")
        currentword=currentword.replace(" ", "")
        result.lower()
        #print('a',result,'b')
        if currentword in result:
            print('correct')
            awnser.color('green')
        if not currentword in result:
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
