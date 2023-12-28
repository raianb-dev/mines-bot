import telebot, pytz, time, random
from datetime import datetime, timedelta


key_api = "5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA"
bot = telebot.TeleBot(key_api)
tz = pytz.timezone('America/Sao_Paulo')
link_cadastro = "<a href='https://solcasino.life/cb2ab781a'> Cadastre aqui</a>"
link_game = "<a href='https://sol.casino/pt/table/gamingcorps-coinminer2'> Jogar agora</a>"
def gerar_matriz():
    n_minas = random.choice([2, 3, 4, 5])
    if n_minas == 2:
        minas = random.sample(range(25), random.choice([4, 5]))
    elif n_minas == 3:
        minas = random.sample(range(25), random.choice([4]))
    elif n_minas == 4:
        minas = random.sample(range(25), random.choice([2, 3]))
    elif n_minas == 5:
        minas = random.sample(range(25), random.choice([2, 3]))
    matriz = [[0]*5 for i in range(5)]  # cria uma matriz 5x5 preenchida com zeros
    for pos in minas:
        i, j = divmod(pos, 5)  # calcula as coordenadas da posição na matriz
        matriz[i][j] = 1  # preenche a posição com o número 1
    return matriz, n_minas
def gerar_gale(n_minas):
    if n_minas <= 3:
        gale = 3
    else:  
        gale = 2
    return gale
mensagem_inicial = f"💰 Entrada Confirmada 💰\n\n"
while True:
    n_minas = None
    now = datetime.now(tz) # pega a hora atual
    valid_until = now + timedelta(minutes=3) # define a hora de validade com base na hora atual, adicionando 3 minutos
    valid_until_str = valid_until.strftime("%H:%M") # formata a hora de validade em uma string
    matriz, n_minas = gerar_matriz()
    mensagem = mensagem_inicial + f"💣 Minas: {n_minas}\n🔁 Nº de tentativas: {gerar_gale(n_minas)}\n🕑 Válido até: {valid_until_str}\n\n🔗{link_cadastro}\n🔗{link_game}\n\n" + '\n'.join([''.join(['🟩' if valor == 0 else '💎' for valor in linha]) for linha in matriz]).replace('0', '🟦').replace('1', '🟠')
    chat_id = '-1002007689565'
    mensagem = bot.send_message(chat_id=chat_id, text="🔎 Validando entrada. Aguarde 🔎")
    time.sleep(18)
    nova_mensagem = mensagem_inicial + f"💣 Minas: {n_minas}\n🔁 Nº de tentativas: {gerar_gale(n_minas)}\n🕑 Válido até: {valid_until_str}\n\n🔗{link_cadastro}\n🔗{link_game}\n\n" + '\n'.join([''.join(['🟩' if valor == 0 else '💎' for valor in linha]) for linha in matriz]).replace('0', '🟦').replace('1', '🟠')
    bot.edit_message_text(chat_id=chat_id, message_id=mensagem.message_id, text=nova_mensagem, parse_mode='html')
    time.sleep(180)
    bot.send_message(chat_id=chat_id, text=f"🔹 Sinal Finalizado 🔹\n🕑 Finalizado às {valid_until_str}\n✅✅✅GREEN✅✅✅")
    time.sleep(30)
