import socket

def load_bulletins():
    bulletins = []
    with open("bulletins", "r") as bulletins_file:
        for line in bulletins_file:
            parts = line.strip().split(sep="\t")
            if len(parts) == 2:
                bulletins.append(parts)
    return bulletins

server = socket.socket()            # создаем объект сокета сервера
#hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 9090                        # устанавливаем порт сервера
server.bind(("localhost", port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
 
print("Server running")
#print("Load bulletins...")
#bulletins = load_bulletins()
message = "HTTP/1.1 200 OK\n\n<html><body>"
while True:
	print("Load bulletins...")
	bulletins = load_bulletins()
	
	con, addr = server.accept()     # принимаем клиента
	
	print("client address: ", addr)
    	
	for bulletin in bulletins:
        	message+=f"<p>From: {bulletin[1]}<br>{bulletin[0]}<br><br></p><hr>"
	
	message+="</body></html>"
        #con.send(f"From: {bulletin[1]}\n{bulletin[0]}\n{'-'*80}\n".encode())
        #message = "HTTP/1.1 200 OK\n\n<html><body><p>Hello Client!</p></body></html>"       # сообщение для отправки клиенту

	con.send(message.encode())      # отправляем сообщение клиенту
	
	message = "HTTP/1.1 200 OK\n\n<html><body>"
	
	con.close()                     # закрываем подключение
	
	
