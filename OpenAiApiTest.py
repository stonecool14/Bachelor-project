import os
from openai import OpenAI

apikey = open("apikey.txt", "r")

client = OpenAI(
    # This is the default and can be omitted
    api_key=apikey.read(),
)

textChat = open("Queries_and_responses.txt", "r")

textChat = textChat.read()
# question = 
textChatSplit = textChat.split("\n")
textChatSplit = list(filter(None, textChatSplit))
question = textChatSplit[-1]

print(question)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="gpt-3.5-turbo",
)

textChatw = open("Queries_and_responses.txt", "w")
textChatw.write(textChat+"\n"+chat_completion.choices[0].message.content+ "\n")