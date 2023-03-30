import random
import time
import telebot

key_api = "5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA"
bot = telebot.TeleBot(key_api)
link_cadastro = "<a href='https://www.example.com'>Cadastre-se</a>"
link_game = "<a href='https://www.example.com'>Ir para o Mines</a>"

def gerar_matriz():
    matriz = [[0]*5 for i in range(5)]  # cria uma matriz 5x5 preenchida com zeros
    posicoes = random.sample(range(25), 6)  # seleciona posições aleatórias
    for pos in posicoes:
        i, j = divmod(pos, 5)  # calcula as coordenadas da posição na matriz
        matriz[i][j] = 1  # preenche a posição com o número 1
    return matriz

mensagem_inicial = f"💰 Entrada Confirmada 💰\n\n💣 Minas: 3\n🕑 Válido até: 23:44\n🔁 Nº de tentativas: 2\n\n🔗{link_cadastro}\n🔗{link_game}\n\n"

while True:
    matriz = gerar_matriz()
    mensagem = mensagem_inicial + '\n'.join([''.join(['🟦' if valor == 0 else '⭐' for valor in linha]) for linha in matriz]).replace('0', '🟦').replace('1', '🟠')
    message = bot.send_message(chat_id="1978978248", text=mensagem, parse_mode='html')
    time.sleep(10)
    mensagem_aguarde = "🔹 Sinal Finalizado 🔹\n🕑 Finalizado às 23:59\n✅✅✅GREEN✅✅✅"
    bot.edit_message_text(chat_id="1978978248", message_id=message.message_id, text=mensagem_aguarde, parse_mode='html')  # edita a mensagem existente com "Grennn e espere mais 10 segundos antes de começar > > >" após 10 segundos. 
    time.sleep(10)
