import random
import time
import telebot
from datetime import datetime, timedelta

key_api = "5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA"
bot = telebot.TeleBot(key_api)

link_cadastro = "<a href='https://www.example.com'>Cadastre-se</a>"
link_game = "<a href='https://www.example.com'>Ir para o Mines</a>"

def gerar_matriz():
    matriz = [[0]*5 for i in range(5)]  # cria uma matriz 5x5 preenchida com zeros
    posicoes = random.sample(range(25), 4)  # seleciona posições aleatórias
    for pos in posicoes:
        i, j = divmod(pos, 5)  # calcula as coordenadas da posição na matriz
        matriz[i][j] = 1  # preenche a posição com o número 1
    return matriz

mensagem_inicial = f"💰 Entrada Confirmada 💰\n\n💣 Minas: 3\n🔁 Nº de tentativas: 3\n"

while True:
    now = datetime.now() # pega a hora atual
    valid_until = now + timedelta(minutes=1) # define a hora de validade com base na hora atual, adicionando 5 minutos
    valid_until_str = valid_until.strftime("%H:%M") # formata a hora de validade em uma string

    matriz = gerar_matriz()
    mensagem = mensagem_inicial + f"🕑 Válido até: {valid_until_str}\n\n🔗{link_cadastro}\n🔗{link_game}\n\n" + '\n'.join([''.join(['🟦' if valor == 0 else '💎' for valor in linha]) for linha in matriz]).replace('0', '🟦').replace('1', '🟠')

    bot.send_message(chat_id="1978978248", text=mensagem, parse_mode='html')
    time.sleep(60)
    bot.send_message(chat_id="1978978248", text="🔹 Sinal Finalizado 🔹\n🕑 Finalizado às 23:59\n✅✅✅GREEN✅✅✅")
    time.sleep(30)