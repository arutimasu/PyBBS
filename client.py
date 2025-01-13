import socket
import time
import select

client = socket.socket()            # создаем сокет клиента
hostname = socket.gethostname()     # получаем хост локальной машины
port = 1237                    # устанавливаем порт сервера

    
#else:
#   print("Линия занята. Повторите попытку позже")
client.connect((hostname, port))    # подключаемся к серверу
client.settimeout(1)
#recon = False
while True:
    
    #client.send('hello'.encode())       # отправляем сообщение серверу
    #print("Отправляю сообщение hello для проверки связи. Ждём ответа...")
    
  
   
  
    try:
        message = input("Input a text: ")   # вводим сообщение
        if message=="q":
            client.close() 
            break
        client.send(message.encode())       # отправляем сообщение серверу
        data = client.recv(1024)            # получаем данные с сервера
        print("Server sent: ", data.decode()) 
        client.send('hello'.encode())       # отправляем сообщение серверу
        data = client.recv(1024)            # получаем данные с сервера
        if len(data)==0:
            print("Reconnecting...")
            client.close()
            #recon = True
            client = socket.socket()            # создаем сокет клиента
            hostname = socket.gethostname()     # получаем хост локальной машины
            port = 1237     
            client.connect((hostname, port))    # подключаемся к серверу
            #client.settimeout(1)
            #client.send(message.encode())       # отправляем сообщение серверу
        else:
            print("Server sent: ", data.decode()) 
    except Exception as e:
        print("Линия занята. Повторите попытку позже", repr(e))
        client.close() 
        exit()
    
   
  
                     # закрываем подключение
