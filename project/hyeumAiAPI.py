import time
import openai
from openai import OpenAI

def getGPTAPI(user_content, order, alignment="", polite="", cnt=0):
    try:
        if order == 1: # 닉네임 생성
            client = openai.OpenAI(api_key='')
            contents = user_content + "\n Q는 질문이고 A는 답변이야 내용을 읽고 판단하여 {'alignment' : '이사람의 성향을 한줄로 표현', 'nickname' : '성향과 내용으로 이 사람에게 어울리는 한글닉네임 5개'}를 생성해줘"
            chat_completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text",
                             "text": contents
                             }
                        ]
                    }
                ],
                max_tokens=200,
                temperature=1
            )
            get_message = chat_completion.choices[-1].message.content
            s = ''
            for i, ch in enumerate(get_message):
                if ch == ' ' and s == '':
                    continue
                elif i+1 < len(get_message) and get_message[i] == ',' and get_message[i + 1] == '\n':
                    continue
                elif i + 1 < len(get_message) and get_message[i] == ' ' and get_message[i] == ':':
                    continue
                elif i + 2 < len(get_message) and get_message[i] == ',' and get_message[i+1] == ' ':
                    continue
                elif ch == '{' or ch == '}' or ch == '\n' or ch == '"' or ch == "'" or ch == "[" or ch == "]":
                    continue
                elif i+1 < len(get_message) and get_message[i] == 'a' and get_message[i+1] == 'l':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "alignment":
                            break
                    s += ch
                elif i+1 < len(get_message) and get_message[i] == 'n' and get_message[i+1] == 'i':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "nickname":
                            break
                    s += '\n'
                    s += ch
                else:
                    s += ch

            return s

        # 내용을 듣고 다음 질문 생성하기
        elif order == 2: # GPT 질문 문구 생성
            client = openai.OpenAI(api_key='')
            # order 2에선 alignment에 존댓말, 반말 정보가 들어가도록
            contents = user_content + "\n Q는 질문이고 A는 답변이야 내용을 읽어 보고 꼭 Q. 형식으로 출력해줘 " + f"단, 조건이 있어 \n 1. 지금부터 질문만 해야해. 유저가 다음에 말하기 편하도록 마지막에 대한 대화를 이어가줘 \n 2. '그럼요, 그럼' 같은 내가 시키는거에 대답하는 단어는 쓰면 안돼 \n 3. 자문자답 또한 금지야 \n 4. 말은 항상 {polite}로 할 것 \n 5. 질문은 평문이고, 질문 외에 다른 말은 붙이지 말 것 \n 6. 글자수는 반환 값의 글자수는 20글자로 제한할게 7. 비슷한 말 또 하지 말 것."
            chat_completion = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": contents
                        }
                    ]
                }],
                max_tokens=200,
                temperature=1
            )

            get_message = chat_completion.choices[-1].message.content

            s = ''
            for i, ch in enumerate(get_message):
                if (i-2 >= 0 and ch == ' ' and get_message[i-1] == '.' and get_message[i-2] == 'Q') or (i-2 >= 0 and ch == ' ' and get_message[i-1] == ':' and get_message[i-2] == 'Q'):
                    s = ''
                elif (i-2 >= 0 and ch == ' ' and get_message[i-1] == ':' and get_message[i-2] == 'A') or (i-2 >= 0 and ch == ' ' and get_message[i-1] == '.' and get_message[i-2] == 'A'):
                    s = ''
                elif (i-1 >= 0 and ch == '.' and get_message[i-1] == 'Q') or (i-1 >= 0 and ch == ':' and get_message[i-1] == 'Q'):
                    s = ''
                elif (i-1 >= 0 and ch == ':' and get_message[i-1] == 'A') or (i-1 >= 0 and ch == '.' and get_message[i-1] == 'A'):
                    s = ''
                elif (i - 1 >= 0 and ch == '1' and get_message[i - 1] == '.') or (i - 2 >= 0 and ch == 1 and get_message[i-1] == '.' and get_message[i-2] == ' '):
                    s = ''
                elif i + 1 < len(get_message) and get_message[i] == 'a' and get_message[i + 1] == 'n':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "answer:":
                            s = ''
                            break
                elif i + 1 < len(get_message) and get_message[i] == 'a' and get_message[i + 1] == 'n':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "answer :":
                            s = ''
                            break
                elif i + 1 < len(get_message) and get_message[i] == 'A' and get_message[i + 1] == 'n':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "Answer: ":
                            s = ''
                            break
                elif i + 1 < len(get_message) and get_message[i] == 'A' and get_message[i + 1] == 'n':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "Answer : ":
                            s = ''
                            break

                elif i + 1 < len(get_message) and get_message[i] == 'q' and get_message[i + 1] == 'u':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "question : ":
                            s = ''
                            break
                elif i + 1 < len(get_message) and get_message[i] == 'A' and get_message[i + 1] == 'n':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "question: ":
                            s = ''
                            break

                elif i + 1 < len(get_message) and get_message[i] == 'Q' and get_message[i + 1] == 'u':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "Question : ":
                            s = ''
                            break
                elif i + 1 < len(get_message) and get_message[i] == 'Q' and get_message[i + 1] == 'u':
                    for j in range(i, len(get_message)):
                        s += ch
                        if s == "Question: ":
                            s = ''
                            break
                else:
                    s += ch

            return s

        #emotion, 위로의 말 생성
        elif order == 3:
            client = openai.OpenAI(api_key='')
            contents = user_content + "\n Q는 질문이고 A는 답변이야 다음 내용을 읽고 판단하여 emotion과 consolation을 출력해줘 단, 조건이 있어 \n 1. 이 사람의 성향은 " + alignment + "이야. \n 2. 답변 형식은 {emotion : 감정(기쁨, 화남, 슬픔, 즐거움 중 내용과 관련하여 택1, consolation : 위로의 한마디 생성} 이야 꼭 형식 맞춰줘 \n 3. 답변에는 emotion과 consolation 빼고 아무 것도 출력하지 마 \n 4. 답변은 " + polite + "로 할것"
            chat_completion = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": contents
                            }
                        ]
                    }
                ],
                max_tokens=300,
                temperature=1
            )

            get_message = chat_completion.choices[-1].message.content
            s = ''
            for i, ch in enumerate(get_message):
                if ch == ' ' and s == '':
                    continue
                elif (i + 1 < len(get_message) and get_message[i] == ' ' and get_message[i] == ':') or (i + 1 < len(get_message) and get_message[i] == ',' and get_message[i + 1] == '\n'):
                    continue
                elif (i + 2 < len(get_message) and get_message[i] == ',' and get_message[i+1] == ' ') or (ch == '{' or ch == '}' or ch == '\n' or ch == '"' or ch == "'"):
                    continue
                elif i + 1 < len(get_message) and get_message[i] == 'e' and get_message[i + 1] == 'm':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "emotion":
                            break
                    s += ch
                elif i + 1 < len(get_message) and get_message[i] == 'E' and get_message[i + 1] == 'm':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "Emotion":
                            break
                    s += ch.lower()
                elif i + 1 < len(get_message) and get_message[i] == 'c' and get_message[i + 1] == 'o':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "consolation":
                            break
                    s += '\n'
                    s += ch
                elif i + 1 < len(get_message) and get_message[i] == 'C' and get_message[i + 1] == 'o':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "Consolation":
                            break
                    s += '\n'
                    s += ch.lower()
                else:
                    s += ch

            return s

    except Exception as e:
        print(e)
        if e == "context_length_exceeded":
            return "context_length_exceeded"

        if cnt>5:
            # "open ai 에러입니다. 잠시 후 다시 사용해주세요."
            return 400

        time.sleep(5)

        return getGPTAPI(user_content, cnt+1)

def getDALLE(user_content, emotion=""):
    try:
        content = user_content + " 기분은 " + emotion + "이고 " + "이 내용을 읽고 이 내용과 감정을 연관하여 그림으로 나타내줘 그림 안에 글자 넣지마"
        client = OpenAI(api_key='')


        response = client.images.generate(
            model="dall-e-3",
            prompt=content,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[-1].url
        return image_url

    except Exception as e:
        print(e)
        if e == "context_length_exceeded":
            return "context_length_exceeded"

        # "open ai 에러입니다. 잠시 후 다시 사용해주세요."
        return 400

content = 'Q: 오늘은 어떤 일이 있었나요?\nA: 산책을 했어\nQ: 오늘은 무슨 계획이 있어?\n A: 육개장 먹을 거 같아\nQ: 컵라면 어떤 거 먹을 거야?\nA: 사리곰탕 먹을 거야'
GPT_MODEL = 'gpt-4'
print(getGPTAPI(content, 2, alignment="차가운 외면 속에 뜨거운 열정을 품고 있는 유형", polite="존댓말"))
