import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

def request(messages):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    assistant_message = res["choices"][0]["message"]
    return assistant_message

if __name__ == "__main__":
  messages = [
    {"role": "system", "content": "あなたはフランクに会話をするアシスタントです。"},
  ]
  while True:
      message = input("あなた:")
      message = {"role": "user", "content": message}
      messages.append(message)
      assistant_message = request(messages)
      print(f"{assistant_message['role']}: {assistant_message['content']}")
      messages.append(assistant_message)


