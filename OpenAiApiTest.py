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
# textChatSplit = textChat.split("\n")
textChatSplit = textChat.split("-"*100)
textChatSplit = list(filter(None, textChatSplit))
question = textChatSplit[-1]
question = question.replace("Query", "")

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
textChatw.write(textChat+"\nAnwser\n"+chat_completion.choices[0].message.content+ "\n\n" + "-"*100+"\nQuery\n"+"\n\n"+"-"*100)
