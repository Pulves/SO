import requests
import time as t
def send_message(token, mensagem):
    try:
        data = {"text": mensagem}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no SendMesssage: ", e)

#chat_id = 2068612697
#cont = 0
#while cont <= 10:
    #for n in range(1,4):
token = "5799235373:AAEw3CWYbgitPm5oZ739IUjGU91x4lfgQsM"
msg = '/opcao1'
print(msg)
send_message(token, msg)
        #t.sleep(3)
       # cont += 1
