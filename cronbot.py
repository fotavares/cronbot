# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import time
import amanobot
from amanobot.loop import MessageLoop
import ChannelLog
from datetime import datetime
from pytz import timezone
import os
import psutil
TOKEN = ''
bot = amanobot.Bot(TOKEN)
semana = ['Dom',"Seg",'Ter','Qua','Qui','Sex',"Sab"]

ChannelLog.log(bot,"CronBot rodando!")

while True:
    data = datetime.now(timezone('Brazil/East'))
    wday = int(data.strftime('%w'))
    hora = int(data.strftime('%H'))
    minuto = int(data.strftime('%M'))

    if semana[wday] == 'Qui':
        if hora == 9 and minuto == 0:
            os.system("pkill -f 'healthcheck.py'")
            ChannelLog.log(bot,"Desligando Healthcheck")
            time.sleep(10)
            os.system("python3 healthcheck.py Pergunta")
            ChannelLog.log(bot,"Healthcheck Pergunta enviado")
            time.sleep(10)
            os.system("python3 healthcheck.py &")
            ChannelLog.log(bot,"Aguardando respostas")
        if hora == 11 and minuto == 30:
            os.system("pkill -f 'healthcheck.py'")
            ChannelLog.log(bot,"Desligando Healthcheck")
            time.sleep(10)
            os.system("python3 healthcheck.py Resposta")
            ChannelLog.log(bot,"Healthcheck Resposta enviado")
            time.sleep(10)
            os.system("python3 healthcheck.py &")
            ChannelLog.log(bot,"Ligando Healthcheck")

    if semana[wday] == 'Sex' :
        if hora == 17 and minuto == 0:
            os.system("pkill -f 'k21saude.py'")
            ChannelLog.log(bot,"Desligando k21saude")
            time.sleep(10)
            os.system("python3 k21saude.py Pergunta")
            ChannelLog.log(bot,"k21saude Pergunta enviado")
            time.sleep(10)
            os.system("python3 k21saude.py &")
            ChannelLog.log(bot,"Aguardando respostas")
        if hora == 18 and minuto == 0:
            os.system("pkill -f 'k21saude.py'")
            ChannelLog.log(bot,"Desligando k21saude")
            time.sleep(10)
            os.system("python3 k21saude.py Resposta")
            ChannelLog.log(bot,"k21saude Resposta enviado") 
            time.sleep(10)
            os.system("python3 k21saude.py &")
            ChannelLog.log(bot,"Ligando k21saude")  

    time.sleep(60)


