import json
from openai import OpenAI


class IntentParser:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def parse(self, user_text: str) -> list:
        prompt = f"""
당신은 사용자의 명령을 분석하여 OS 자동화 실행 계획을 JSON 배열 형태로만 출력하는 모델입니다.

규칙:
- 반드시 JSON 배열만 출력한다.
- 각 항목은 action, target 또는 text를 가진다.
- 불필요한 설명은 절대 출력하지 않는다.
- JSON 외의 문자는 단 1글자라도 출력하면 안 된다.

지원 행동 예시:
- open_app
- close_app
- new_file
- write
- press
- open_browser
- go_to_url
- chatgpt_query
- copy_response
- switch_app
- paste

사용자 명령:
"{user_text}"

적절한 JSON만 출력하라.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content.strip()
        content = content.replace("```json", "").replace("```", "").strip() # ai 코드블럭까지 반환을 해주는 오류 해결을 위해 코드블럭 부분 삭제

        # print("📌 GPT Raw Output:", content)

        try:
            actions = json.loads(content)
        except json.JSONDecodeError:
            print("❌ JSON 파싱 실패")
            actions = []

        return actions
