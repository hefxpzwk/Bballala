import sys
import os

# src 디렉토리를 파이썬 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from stt.whisper_stt import WhisperSTT

def test_stt():
    stt = WhisperSTT("small")
    text = stt.transcribe("sample.wav", language="ko")
    print("인식 결과:", text)

if __name__ == "__main__":
    test_stt()
