import asyncio
from aiogram import Bot, types

async def obter_membros(bot, grupo_id):
    membros = await bot.get_chat_members(grupo_id)
    return membros

# Substitua as informações abaixo com seu token e ID do grupo
token = '5328905392:AAG29HHnR1vZQpCs5wcAvtDMfhzqJXzfrMA'
grupo_id = -1001631556673  # Substitua pelo ID real do Grupo A

async def main():
    # Criar um objeto Bot assíncrono
    bot = Bot(token=token)

    try:
        # Obter informações sobre os membros do grupo
        membros = await obter_membros(bot, grupo_id)

        # Calcular o total de membros
        total_membros = len(membros)
        print(f"Total de membros no grupo: {total_membros}")

        # Imprimir informações sobre os 10 primeiros membros do grupo
        print("Os 10 primeiros membros do grupo:")
        for i, membro_info in enumerate(membros[:10], start=1):
            print(f"{i}. {membro_info.user.username}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # Certificar-se de encerrar o bot, independentemente de erros
        await bot.close()

# Executar o loop de eventos assíncrono com um pequeno atraso
asyncio.run(main())
