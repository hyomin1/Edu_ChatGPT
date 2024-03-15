# OpenAI API 사용하기
# 1. API-KEY 발급
# 2. 카드 등록(VISA, MASTER) + 5.5달러(보유)


# 라이브러리 관리
# 1. VENV
# 2. Anaconda



# 챗본 만들기
# - ChatGPT : 챗봇 서비스 이름(ex: 카카오톡)
#  > 인공지능 모델: GPT
#  > 무료: 3.5
#  > 유료: 4.0

# OpenAI 회사에서 GPT 관련 API 제공
# -https://openai.com/blog/openai-api

from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "모든 설명을 2줄로 요약해서 설명해주세요."},
    {"role": "user", "content": "클라우드 설명해줘."}
  ]
)

print(completion.choices[0].message)

# OpenAI사의 API를 사용ㅎ서 챗봇 문제점
# 1.개발이 어려움(난이도 상) -> 더 쉽게 개발 할 수 있는 프레임워크 필요
# 2. 챗봇 개발 완성 -> Bard 모델 변경 -> Bard API 처음부터 개발 -> 프레임워크(LLM)

# -> langChain 프레임워크(코드 동일: 모델만 바꾸면)


# git commit -m add langchain

