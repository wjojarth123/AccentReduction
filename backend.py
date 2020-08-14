import json
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


wordsComplete=0
inccorectWords=[]
wordlist=['wage','wait','wake','walk','wall','wallet','want','ward','warehouse','warfare','warm','warmer','warn','warrant','warranty','wary','wash','waste','watch','watchdog','water','waterproof','waters','wave','weak','weaken','weaker','weakest','weakness','wealth','wealthiest','wealthy','weapon','wear','wearable','wearables','weather','website','websites','week','weekend','weekly','weigh','weight','weird','welcome','welcomed','welcoming','welfare','well','wells','west','western','whale','whales','what','whatever','wheat','wheel','wheelchair','when','whenever','where','whereabouts','whereas','wherever','whether','which','while','white','whoever','whole','wholesale','wholly','whom','whopping','whose','wide','widely','wider','widespread','widgets','widow','width','wife','wild','wildfire','wildlife','wildly','will','willingness','wind','winding','window','wine','wing','winner','winter','wipe','wire','wired','wireless','wirelessly','wisdom','wise','wish','with','withdraw','withdrawal','within','without','withstand','witness','woke','woman','wonder','wonderful','wood','wooden','word','work','worker','workflow','workflows','workforce','workload','workout','workplace','workstation','world','worldwide','worm','worry','worse','worst','worth','worthwhile','worthy','would','wound','wounded','wounding','wrap','wreck','wreckage','wrist','write','writer','wrong','vacant ','vacation ','vaccination ','vaccine ','vacuum ','vague ','vaguely ','vain ','valid ','validate ','validation ','validity ','valley ','valuable ','valuation ','value ','valued ','valuing ','val','ve ','vampire ','vanilla ','vantage ','vapor ','variable ','variables ','variant ','variation ','variety ','various ','vary ','vast ','vastly ','vault ','vector ','vegan ','vegetable ','vegetation ','vehemently ','vehicle ','vein ','velocity ','vending ','vendor ','venerable ','venom ','vent ','ventilation ','venture ','ventured ','venturing ','venue ','verbal ','verdict ','verge ','verifiable ','verification ','verify ','veritable ','versa ','versatile ','versatility ','version ','versus ','vertebrate ','vertical ','vertically ','verticals ','very ','vessel ','vest ','vested ','veteran ','veto ','vetoed ','viability ','viable ','vibrant ','vibration ','vice ','vicinity ','vicious ','victim ','victory ','video ','videogame ','videotaped ','view ','viewable ','viewed ','viewer ','viewfinder ','viewing ','viewpoint ','vigil ','vigilance ','vigilant ','vigilante ','vigorous ','vigorously ','villa ','village ','villagers ','vintage ','vinyl ','violate ','violation ','violence ','violent ','violently ','viral ','virtual ','virtually ','virtue ','virus ','visa ','visibility ','visible ','visibly ','vision ','visionary ','visit ','visitor ','visual ','visualize ','visually ','visuals ','vital ','vi','vid ','vocal ','vodka ','voice ','voicemail ','void ','volatile ','volatility ','volcanic ','volcano ','voltage ','volume ','voluntarily ','voluntary ','volunteer ','volunteered ','vortex ','vote ','voter ','vowed ','vowing ','voyage ']
chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 3
filename = "output.wav"
p = pyaudio.PyAudio()

def recordAudio():
    print('Recording')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    #p.terminate()
    print("recording complete")
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
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
            keywords=[word],
            keywords_threshold=0.5,
            max_alternatives=20
        ).get_result()
    results=json.dumps(speech_recognition_results, indent=2)
    # rawdata  = json.loads(results)
    # rawdata=rawdata["results"]
    # rawdata=rawdata[0]
    # rawdata=rawdata['alternatives']
    # rawdata=rawdata[0]
    # data=rawdata['transcript']
    # data2=rawdata['confidence']
    # print(data)
    # data=[data,data2]
    return results

def playAudio():
    p = vlc.MediaPlayer("text.mp3")
    p.play()
    time.sleep(3)
    p.stop()
    print("complete")
def getRecording(text):
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save('text.mp3')

wordsComplete+=1
word=wordlist[random.randrange(0,len(wordlist))]
#getRecording(word)
#playAudio()
#print(word)
recordAudio()
print(getResult())
