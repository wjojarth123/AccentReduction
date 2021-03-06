import turtle
import time
import json
import re
import fuzzy
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import RecognizeCallback, AudioSource
import wave
import  vlc
import time
from gtts import gTTS
import pyaudio
import random
variants=20
from PyDictionary import PyDictionary
dictionary=PyDictionary()
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
awnser.goto(310  ,-290)
dictturtle.goto(-300  ,-300)
word.ht()
awnser.resizemode("user")
awnser.shapesize(3, 3, 5)
authenticator = IAMAuthenticator('jdDymmXRUxB1zUTS5rTB8fH18uPo2IzCNMR0C3Sf-dvu')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/51627f25-e544-4602-9a54-00cfa7e97ad3')

def getResult():
    with open(join(dirname(__file__), './.', 'output.wav'),
                   'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            word_alternatives_threshold=0.9,
            keywords=[currentword],
            keywords_threshold=0.5,
            max_alternatives=20,
            inactivity_timeout=5,
            profanity_filter=True,
            background_audio_suppersion=0.5
        ).get_result()
    results=json.dumps(speech_recognition_results, indent=2)
    rawdata  = json.loads(results)
    print("a",results)
    rawdata=rawdata["results"]
    print("b",rawdata)
    rawdata=rawdata[0]
    rawdata=rawdata['alternatives']
    print("c",rawdata)
    #rawdata=rawdata[0]
    #data=rawdata['transcript']
    #data2=rawdata['confidence']
    data=rawdata
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
    #currentword='wateringcan'
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
    results=getResult()
    #print('a',result,'b')
    azby=0
    correct=False
    for result in results:
        print("d",result)
        result=result['transcript']
        result.lower()
        print("e",result)
        azby+=1
        if not correct:
            print("inloop")
            result=result[0]
            result=result.replace(" ", "")
            currentword=currentword.replace(" ", "")
            result.lower()
            currentword=currentword.replace(" ", "")
            #print('a',result,'b')
            if currentword in result:
                correct=True
                print("woho")
            if not currentword in result:
                correct=False

        print(correct)

        if correct:
            print('correct')
            awnser.color('green')
        elif azby==len(results)-1:
            print('incorrect')
            awnser.color('red')
            #inccorectWords.append(currentword)
            a=fuzzy.nysiis(currentword)
            b=fuzzy.nysiis(result)
            a=re.findall('.',str(a))
            b=re.findall('.',str(b))
            for char in range(len(a)):
                try:
                    if b[char-1]==a[char]:
                        a[char]=0
                    elif b[char]==a[char]:
                        a[char]=0
                    elif b[char+1]==a[char]:
                        a[char]=0
                except:
                    print("error")
            word.clear()
            word.write(a, align="center",font=("Verdana", 30, "normal"))
            time.sleep(3)
        print(azby)
    word.clear()
    dictturtle.clear()




# word.write("hello", align="center",font=("Verdana", 30, "normal"))
# time.sleep(5)
# word.clear()
# word.write("bye", align="center",font=("Verdana", 30, "normal"))
# time.sleep(5)
