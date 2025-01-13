import socket
import time
#server = socket.socket()            # создаем объект сокета сервера
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        hostname = socket.gethostname()     # получаем имя хоста локальной машины
        print(hostname)
        port = 12345                      # устанавливаем порт сервера
        server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
        server.listen(5)                    # начинаем прослушиваение входящих подключений
#connection = True
        is_showed = False
        users = []
        current_user=""
        board = []
        print("Server running")
        contacts = open("contacts", "r")
        print("Reading contacts...")
        for line in contacts:
	        print(line.split(sep="\t"))
	        users.append([line.split(sep="\t")[0], line.split(sep="\t")[1]])
        print("Reading bulletins...")
        bulletins = open("bulletins", "r")
        for line in bulletins:
	        print(line.split(sep="\t"))
	        board.append([line.split(sep="\t")[0], line.split(sep="\t")[1]])
        while True:
        #global con
                con, addr = server.accept()     # принимаем клиента
                with con:
                        for usr in users:
                                if addr[0] in usr and not is_showed:
                                        print("Welcome to our BBS, ", usr[1])
                                        current_user=usr[1]
                                        
                                        con.send(f"Welcome to our BBS, {usr[1]}\n\nThere are last bulletins:\n".encode())
                                        is_showed = True
        #clients = []   
                        for bulletin in board:
                                print("-"*80)
                                print("From: ", bulletin[1])
                                print(bulletin[0])
                                print("-"*80)
                                con.send(f"{'-'*80}\nFrom: {bulletin[1]}\n{bulletin[0]}\n{'-'*80}".encode())
                        con.send(f"\nType 's' to create a new bulletin: ".encode())
                        while True:
                                data = con.recv(1)           # получаем данные от клиента
                                if not data: break
                                cmd = data.decode()         # преобразуем байты в строку   
                                if cmd == "s":
                                        con.send("\nEnter a bulletin message: ".encode())
                                        data = con.recv(5)           # получаем данные от клиента
                                        #if not data: break
                                        msg = data.decode()
                                        bulletins = open("bulletins", "a")
                                        bulletins.write(f"\n{msg}\t{current_user}")
                                        #con.send("\nA bulletin writed.".encode())
                                #else:
                                        #con.send("\nCommand not found.".encode())
        #time.sleep(1)
                                #print(f"Client sent: {message}")
                                #message = message[::-1]+"\n"         # инвертируем строку
        #if message.split()[0].lowewr() == "recv":
        #clients[message.split()[1]].send()
                                #con.send(message.encode())      # отправляем сообщение клиенту
                #con.setblocking(False)
        #server.sendall('Message: Line is busy.',.encode)
        #i+=1   
        #con.close()
              
    
              
