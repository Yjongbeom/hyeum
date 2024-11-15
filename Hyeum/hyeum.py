import time
import openai
from openai import OpenAI
import os

API_KEY = os.environ.get('OPENAI_API_KEY')

def getGPTAPI(user_content, order, alignment="", cnt=0):
    try:
        if order == 1: # 닉네임 생성
            client = openai.OpenAI(api_key=API_KEY)
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
            client = openai.OpenAI(api_key=API_KEY)
            contents = user_content + "\n Q는 질문이고 A는 답변이야 내용을 읽는데 "+ "이 사람의 성향은 " + alignment + "야 이 성향도 고려해서 다음 질문을 대화를 이끌어갈 짧은 한문장으로 생성해줘 Q. 다음 질문 생성 형식으로 보내줘 답변에는 성향에 대한 말을 절대 넣지 마"
            chat_completion = client.chat.completions.create(
                model="gpt-4",
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
                temperature=0.5
            )

            get_message = chat_completion.choices[-1].message.content

            s = ''
            for i, ch in enumerate(get_message):
                if i-2 >= 0 and ch == ' ' and get_message[i-1] == '.' and get_message[i-2] == 'Q':
                    s = ''
                elif i-1 >= 0 and ch == '.' and get_message[i-1] == 'Q':
                    s = ''
                else:
                    s += ch


            return s

        #emotion, 위로의 말 생성
        elif order == 3:
            client = openai.OpenAI(api_key=API_KEY)
            contents = user_content + "\n Q는 질문이고 A는 답변이야 이 사람의 성향은" + alignment + "이고 다음 내용을 읽고 이 사람의 {'emotion': '감정[기쁨,화남,슬픔,즐거움]중 내용을 읽고 판단하여 택1', 'consolation': '위로의 말'} 이 형식으로 생성해줘, 답변에는 성향을 파악하는 얘기를 절대 하지마, 형식 꼭 맞춰줘"
            chat_completion = client.chat.completions.create(
                model="gpt-4",
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
                elif i + 1 < len(get_message) and get_message[i] == ' ' and get_message[i] == ':':
                    continue
                elif i + 1 < len(get_message) and get_message[i] == ',' and get_message[i + 1] == '\n':
                    continue
                elif i + 2 < len(get_message) and get_message[i] == ',' and get_message[i+1] == ' ':
                    continue
                elif ch == '{' or ch == '}' or ch == '\n' or ch == '"' or ch == "'":
                    continue
                elif i + 1 < len(get_message) and get_message[i] == 'e' and get_message[i + 1] == 'm':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "emotion":
                            break
                    s += ch
                elif i + 1 < len(get_message) and get_message[i] == 'c' and get_message[i + 1] == 'o':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in "consolation":
                            break
                    s += '\n'
                    s += ch
                else:
                    s += ch

            return s

        elif order == 4:
            client = openai.OpenAI(api_key=API_KEY)
            contents = user_content + "\n Q는 질문이고 A는 답변이야, 사용자의 감정 빈도가 이렇다고 했을 때, 내용과 연계하여 이번주는 어땟는지 코멘트 남겨줘 형식은 Comment : 할말 으로 해줘"
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
                max_tokens=400,
                temperature=0.5
            )
            get_message = chat_completion.choices[-1].message.content


            s = ''
            for i, ch in enumerate(get_message):
                if ch == ' ' and s == '':
                    continue
                elif i + 1 < len(get_message) and get_message[i] == ',' and get_message[i + 1] == '\n':
                    continue
                elif i + 1 < len(get_message) and get_message[i] == ' ' and get_message[i] == ':':
                    continue
                elif ch == '{' or ch == '}' or ch == '\n' or ch == '"' or ch == "'" or ch == "[" or ch == "]":
                    continue
                elif i + 1 < len(get_message) and (get_message[i] == 'C' or get_message[i] == 'c') and get_message[i + 1] == 'o':
                    for j in range(i, len(get_message)):
                        if get_message[j] not in ("Comment" or "comment"):
                            break
                    s += ch
                else:
                    s += ch

            return s




    except Exception as e:

        if e == "context_length_exceeded":
            return "context_length_exceeded"

        if cnt>5:
            # "open ai 에러입니다. 잠시 후 다시 사용해주세요."
            return 400

        time.sleep(5)

        return getGPTAPI(user_content, order, alignment, cnt+1)

def getDALLE(user_content, emotion="", cnt=0):
    try:
        content = user_content + " 기분은 " + emotion + "이고 " + "이 내용을 읽고 이 내용과 감정을 연관하여 그림으로 나타내줘 그림 안에 글자 넣지마"
        client = openai.OpenAI(api_key=API_KEY)


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


        if cnt > 5:
            # "open ai 에러입니다. 잠시 후 다시 사용해주세요."
            return 400

        return getDALLE(user_content, emotion, cnt+1)

con = "기쁨 4, 슬픔 4, 즐거움 1, 화남 1 Q. 오늘은 어떤 일이 있었나요? A. 나 오늘 되게 힘든 일이 있었어 Q. 오늘 대답해줘서 고마워요. 어떤 일이 그렇게 힘들었나요? 혹시 제가 도와줄 수 있는 게 있다면 말해주시겠어요? A. 일에서 큰 실수를 저질러서 많이 당황스럽고 힘들었어요. Q. 고민이 있는 것 같아요. 제가 어떻게 도울 수 있을지 말씀해주세요. 무엇이든지 공감하며 들어드릴게요. 함께 해결해봐요. A. 당장 어떻게 해야할 지 모르겠어서 도망갔어요. 저 어떻게 해야하나요? Q. 어쩔 수 없이 도망치는 상황이 왔다고 하셨군요. 그렇게 힘든 상황에서는 이해할 수 있어요. 하지만 그 상황을 직면하고 해결해야만 하는 게 중요할 거에요. 함께 해결책을 찾아보는 건 어떨까요? 함께 한번 고민해볼까요? A. 바로 상사에게 보고하는건 어때? Q. 상사에게 바로 보고하는 것도 좋은 방법일 수 있습니다. 하지만 이전에 비슷한 상황에 처해본 적이 있나요? 그렇다면 그 때 어떻게 해결했는지 공유해주실 수 있나요? 그 경험을 바탕으로 상황을 해결하는 데 도움이 될 수 있을 것 같아요. A. 이전에는 이런 상황에 처해본 적 없어"

print(getGPTAPI(con, 2))