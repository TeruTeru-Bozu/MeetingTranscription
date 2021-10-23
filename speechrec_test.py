#!/usr/bin/env python

import speech_recognition as sr 

rec = sr.Recognizer()
mic = sr.Microphone()
while True:
  with mic as source:
    #ノイズ対策
    rec.adjust_for_ambient_noise(source) 
    audio = rec.listen(source)
  
  try:
    print(rec.recognize_google(audio, language='ja-JP'))
  except sr.UnknownValueError:
    print("音声を認識できません")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
