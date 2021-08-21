from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot Bill')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english.conversations")

print("Bill: Hello, i'm Bill the Bot!")
while True:
    quest = input('You: ')
    response = bot.get_response(quest)
    print(f'Bill: {response}')