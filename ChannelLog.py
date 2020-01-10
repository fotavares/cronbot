import amanobot


def log(bot,mensagem):
    me = bot.getMe()
    bot.sendMessage(-1001498194874,"#"+me["username"] + ": " + mensagem)