import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from nlp.intent_parser import IntentParser

parser = IntentParser(api_key="YOUR_API_KEY")

result = parser.parse("크롬 열고 네이버 접속해서 고양이 사진 검색해줘")
print(result)
