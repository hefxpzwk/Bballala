import whisper

class WhisperSTT:
    def __init__(self, model_name="small"):
        """
        Whisper STT 초기화
        모델 이름: tiny, base, small, medium, large
        """
        print(f"Loading Whisper model: {model_name}")
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str, language="ko"):
        """
        음성 파일을 텍스트로 변환하는 함수
        """
        print(f"Transcribing audio: {audio_path}")
        result = self.model.transcribe(audio_path, language=language)
        return result["text"]
