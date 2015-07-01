class ConsoleCommandHandler:
    def __init__(self, bot, post_to_chat):
        self.bot = bot
        self.post_to_chat = post_to_chat

    def reply(self, text):
        if self.post_to_chat:
            self.bot.room.send_message(text)
        print(text)

    def send_message(self, text):
        self.reply(text)