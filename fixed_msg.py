import telebot

# Insira aqui o seu token do Telegram Bot
TOKEN = '5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA'
bot = telebot.TeleBot(TOKEN)

link = "<a href='https://solcasino.life/cb2ab781a'>CADASTRE-SE AQUI</a>"

# Mensagem que será enviada
mensagem = f'🆘🆘 ATENÇÃO 🆘🆘\n\n⚠️ NOSSO SINAL SÓ FUNCIONA NA ARBETY ⚠️\n\nTEM MUITAS PESSOAS QUE ESTÃO TOMANDO RED PORQUE ESTÃO JOGANDO EM OUTRA CASA!\n\n🚨 NOSSOS SINAIS SÓ FUNCIONAM NA ARBETY🚨\n\n ✍️ {link}\n\n CADASTRE-SE E COMECE A PEGAR OS GREEEENS'

# Cria o botão
botao = telebot.types.InlineKeyboardButton(text='🎁 BÔNUS 100%', url='https://solcasino.life/cb2ab781a')

# Cria o objeto de teclado inline e adiciona o botão
teclado_inline = telebot.types.InlineKeyboardMarkup()
teclado_inline.add(botao)

chat_id = '-1002007689565'
# Envia a mensagem com o botão
mensagem_enviada = bot.send_message(chat_id=chat_id, text=mensagem, reply_markup=teclado_inline, parse_mode='html')

# Fixa a mensagem no chat
bot.pin_chat_message(chat_id=chat_id, message_id=mensagem_enviada.message_id)
