#! python3
import telebot
import subprocess
import time

CHAVE = "5799235373:AAEw3CWYbgitPm5oZ739IUjGU91x4lfgQsM"

bot = telebot.TeleBot(CHAVE)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    inic = time.time()
    #subprocess.run(["./ps_recursivo.sh"], shell=True)
    bot.send_message(mensagem.chat.id, '''Ele dorme. Embora a sorte lhe tenha sido adversa.\n Ele viveu. Morreu quando perdeu seu anjo.\n P artiu com a mesma simplicidade\n Como a chegada da noite após o dia.''' )
    fim = time.time()
    #print(fim - inic)
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    inic = time.time()
    #subprocess.run(["./ps_recursivo.sh"], shell=True)
    bot.send_message(mensagem.chat.id, "Instrumentos Mortais")
    fim = time.time()
    #print(fim - inic)


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    inic = time.time() 
    #subprocess.run(["./ps_recursivo.sh"], shell=True)
    bot.send_message(mensagem.chat.id, "Não se preocupe com as derrotas de hoje, amanhã terão mais!")
    fim = time.time()
    #print(fim - inic)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    #subprocess.run(["./ps_recursivo.sh"], shell=True)
    inic = time.time()
    texto = '''
            Escolha uma opção:
/opcao1 Poema de morte pra Jean valjean
/opcao2 Melhor série de fantasia adolescente
/opcao3 Mensagem motivadora
Se não for nenhuma das três não ira funcionar?'''
    bot.reply_to(mensagem, texto)
    fim = time.time()
    #print(fim - inic)

bot.polling()

