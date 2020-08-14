import turtle
import time
import json
import re
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
awnser.goto(300  ,-300)
dictturtle.goto(-300  ,-300)
word.ht()
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
            max_alternatives=1,
            inactivity_timeout=5,
            profanity_filter=True,
            background_audio_suppersion=0.5
        ).get_result()
    results=json.dumps(speech_recognition_results, indent=2)
    rawdata  = json.loads(results)
    print(results)
    rawdata=rawdata["results"]
    rawdata=rawdata[0]
    rawdata=rawdata['alternatives']
    rawdata=rawdata[0]
    data=rawdata['transcript']
    data2=rawdata['confidence']
    print(data)
    data=[data,data2]
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
