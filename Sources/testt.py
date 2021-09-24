# # # import speech_recognition as sr
# # # import pyttsx3 as tts
# # # import os
# # # filename = r"C:\Users\Admin\Downloads\audio.mp3"
# # # import subprocess
# # #
# # # subprocess.call(["ffmpeg", "-i", filename, os.path.join(os.getcwd(), "audio.wav")])
# # #
# # # filename = os.path.join(os.getcwd(), "audio.wav")
# # # def genereate_mp3(filename):
# # #
# # #
# # #
# # #     engine = tts.init()
# # #
# # #     engine.save_to_file(text="text", filename=filename)
# # #
# # #     engine.runAndWait()
# # #
# # #
# # #
# # #
# # #
# # # # initialize
# # # genereate_mp3(filename)
# # # engine = sr.Recognizer()
# # #
# # # with sr.AudioFile(filename) as mp3:
# # #     print("start")
# # #     audio_data = engine.record(mp3)
# # #
# # # try:
# # #     text = engine.recognize_google(audio_data)
# # #     print(f"text: {text}")
# # # except Exception as e:
# # #     print(e)
# #
# #
# #
# #
# #
# # # ----------------------------------------------------------------------
# import speech_recognition as sr
# import os
# from pydub import AudioSegment
# # filename = r"C:\Users\Admin\Downloads" + "\\audio.mp3"
# # print("filename: ", filename)
#
# from pydub import AudioSegment
# # AudioSegment.ffmpeg = os.getcwd()
#
# sound = AudioSegment.from_mp3("audio1.mp3")
#
# sound.export(os.getcwd() + "\\audio.wav", format="wav")
#
# audio_file = os.getcwd() + "\\audio.wav"
#
# r = sr.Recognizer()
#
# with sr.AudioFile(audio_file) as mp3:
#     audio_data = r.record(mp3)
#     print("extract text: ", r.recognize_google(audio_data))
# #
# #
# # # ====================================================================================================================
# # import requests
# #
# # r = requests.get("https://recaptcha.net/recaptcha/api2/payload/audio.mp3?p=06AGdBq25Fwd6dteMuABGCxuvkEVyBXkLv9dGs2SPHq4dpF7c9Tux506X9Ydlgtu_Xg3mMEGGZmfXJ0MNlnZ1b8MxPHHtQ_SFoK1qhk4Ck_FsQkl_yIclVqxebDh0NOnDCgGChSKtQq29D1WieVlr_4jdNvfMHj1SvJNGVrEnBXbml0P8QixvvHLn5RjnWUPbGSqXKLSe6RBMd&k=6Ld7XBgTAAAAABhqMs0avEPpilCq3w8FsocJLK_n")
# # content = r.content
# # with open("audio1.mp3", "wb") as audio:
# #     audio.write(content)
import schedule
import time


def printHi():
    print("Hi")

schedule.every(3).seconds.do(printHi)

while True:
    schedule.run_pending()
    time.sleep(1)
