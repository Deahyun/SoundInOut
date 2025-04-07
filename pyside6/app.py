import sys
import random
import time

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from demo import Ui_MainWindow

# Whisper 라이브러리를 불러옵니다
#import whisper
from faster_whisper import WhisperModel
import torch
import time
import speech_recognition as sr

from gtts import gTTS
import pyglet

r = sr.Recognizer()

# 마이크를 오디오 소스로 사용
mic = sr.Microphone()

# 저장할 오디오 파일의 이름
file_name = "recorded_audio.wav"


def extract_text_from_file(file_path: str) -> dict:
    #model_size = "small"
    model_size = "large-v3"
    #
    # Run on GPU with FP16
    # model = WhisperModel(model_size, device="cuda", compute_type="float16")
    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(file_path, language='ko', beam_size=5)
    for segment in segments:
        print('[%.2fs -> %.2fs] %s' % (segment.start, segment.end, segment.text))
    return segments

def record_audio():
    with mic as source:
        print("녹음 시작...")
        # 녹화 종료 판단을 위한 시간간격 설정. 무음구간의 시간 간격.
        r.pause_threshold = 1.5
        audio_data = r.listen(source)
        print("녹음 완료!")
        return audio_data

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #
        self.btnSay.clicked.connect(self.say)
        self.btnListen.clicked.connect(self.listen)
        #
        self.device = torch.device('cpu')
        #self.device = torch.device('cuda')
        #self.model = whisper.load_model("small").to(self.device)
        # tiny.en, tiny, base.en, base, small.en, small, medium.en, medium, large-v1, large-v2
        self.model = WhisperModel('small', device="cpu", compute_type="int8")

    @QtCore.Slot()
    def say(self):
        strSay = self.edSay.text()
        if len(strSay) == 0:
            return
        #self.edListen.setText(strSay)
        #self.edSay.setText('아무말 대잔치')
        tts = gTTS(text=strSay, lang='ko')
        filename = 'output.mp3'
        tts.save(filename)
        sound = pyglet.media.load(filename, streaming=False)
        sound.play()

    def listen(self):
        # 음성 녹음
        audio_data = record_audio()

        # 오디오 파일로 저장
        with open(file_name, "wb") as f:
            f.write(audio_data.get_wav_data())

        start_time = time.time()
        # audio_file = 'sample2.m4a'
        audio_file = 'recorded_audio.wav'
        #result = self.model.transcribe(audio_file, fp16=False)
        segments, info = self.model.transcribe(audio_file, language='ko', beam_size=5)
        infer_time = time.time() - start_time
        print('infer_time', round(infer_time, 3))
        #strResult = result["text"]
        #
        strResult = ''
        for segment in segments:
            strResult += segment.text
        #
        self.edListen.setText(strResult)


app = QApplication()
window = MainWindow()
window.show()
app.exec()
