import telebot

# Insira aqui o seu token do Telegram Bot
TOKEN = '5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA'
bot = telebot.TeleBot(TOKEN)

link = "<a href='https://arbety.com/home?ref=e13551a592ad4fcaa7d16a4c9f2bf9dd'>CADASTRE-SE AQUI</a>"

# Mensagem que será enviada
mensagem = f'🆘🆘 ATENÇÃO 🆘🆘\n\n⚠️ NOSSO SINAL SÓ FUNCIONA NA ARBETY ⚠️\n\nTEM MUITAS PESSOAS QUE ESTÃO TOMANDO RED PORQUE ESTÃO JOGANDO EM OUTRA CASA!\n\n🚨 NOSSOS SINAIS SÓ FUNCIONAM NA ARBETY🚨\n\n ✍️ {link}\n\n CADASTRE-SE E COMECE A PEGAR OS GREEEENS'

# Cria o botão
botao = telebot.types.InlineKeyboardButton(text='🎁 BÔNUS 100%', url='https://arbety.com/home?ref=e13551a592ad4fcaa7d16a4c9f2bf9dd')

# Cria o objeto de teclado inline e adiciona o botão
teclado_inline = telebot.types.InlineKeyboardMarkup()
teclado_inline.add(botao)

chat_id = '-1001943217493'
# Envia a mensagem com o botão
mensagem_enviada = bot.send_message(chat_id=chat_id, text=mensagem, reply_markup=teclado_inline, parse_mode='html')

# Fixa a mensagem no chat
bot.pin_chat_message(chat_id=chat_id, message_id=mensagem_enviada.message_id)
