import demo_cli
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr
from googletrans import Translator
r=sr.Recognizer()
path=input("영어로 번역,더빙하고 싶은 한국어 음성 경로를 입력하세요. (mp3, " \
                      "wav, m4a, flac, ...):\n")
Yujin=sr.AudioFile(path)
with Yujin as source:
    audio=r.record(source)

mytext=r.recognize_google(audio, language="ko-KR")
print(mytext)
language='ko'
translator=Translator()

tr_results_ja=translator.translate(mytext, src='ko', dest='ja')
#print(tr_results_ja.text)
tr_results_ch=translator.translate(tr_results_ja.text, src='ja', dest='zh-CN')
#print(tr_results_ch.text)
tr_results_en=translator.translate(tr_results_ch.text, src='zh-CN', dest='EN')
print(tr_results_en.text)
