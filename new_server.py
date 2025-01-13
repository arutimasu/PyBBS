import socket

def load_users():
    users = []
    with open("contacts", "r") as contacts:
        for line in contacts:
            parts = line.strip().split(sep="\t")
            if len(parts) == 2:
                users.append(parts)
    return users

def load_bulletins():
    bulletins = []
    with open("bulletins", "r") as bulletins_file:
        for line in bulletins_file:
            parts = line.strip().split(sep="\t")
            if len(parts) == 2:
                bulletins.append(parts)
    return bulletins

def handle_client(con, addr, users, bulletins):
  print("Client connected:", addr)
  current_user = None
  con.send("Enter your username: ".encode())
  username = con.recv(1024).decode("utf-8", "ignore")
  #Проверяем, есть ли пользователь в списке
  for usr in users:
  #if addr[0] in usr:
    if username.strip() in usr:
      current_user = usr[1]
      con.send(f"Welcome to our BBS, {usr[1]}\n\nThese are the latest bulletins:\n\n".encode())
      break
  if current_user is None:
    con.send("Unknown user. Disconnecting...\n".encode())
    con.send("Enter your name: ".encode())
    name = con.recv(1024).decode("utf-8", "ignore")
    con.send("Enter your surname: ".encode())
    surname = con.recv(1024).decode("utf-8", "ignore")
    current_user = name.strip()+" "+surname.strip()
        
        #con.send("Enter your screen name: ".encode())
        #username = con.recv(1024).decode()
    with open("contacts", "a") as contacts_file:
			#contacts_file.write(f"{addr[0]}\t{current_user}\n")
      contacts_file.write(f"\n{username.strip()}\t{current_user}")
        #return
  con.send(f"Welcome to our BBS, {current_user}\n\nThese are the latest bulletins:\n\n".encode())
  for bulletin in bulletins:
    con.send(f"From: {bulletin[1]}\n{bulletin[0]}\n{'-'*80}\n".encode())
  con.send("Type 's' to create a new bulletin, type 'b' to view latest bulletins\nType 'c' to chat with sysop of current BBS or 'q' to quit: ".encode())

  while True:
    	
    		#con.send("Type 's' to create a new bulletin or 'q' to quit: ".encode())
    
    	
    data = con.recv(1024).decode("utf-8", "ignore")  # Увеличиваем размер для больших сообщений
    	
    if not data:
      break
    cmd = data.strip()
    if cmd == "s":
      con.send("Enter a bulletin message: ".encode())
      msg = con.recv(1024).decode("utf-8", "ignore")
      msg = msg.strip()
      with open("bulletins", "a") as bulletins_file:
        bulletins_file.write(f"\n{msg}\t{current_user}")
            
        # Обновляем список bulletins
        bulletins.append([msg, current_user])
        con.send("Bulletin added!\n".encode())
    if cmd == "b":
      for bulletin in bulletins:
        con.send(f"From: {bulletin[1]}\n{bulletin[0]}\n{'-'*80}\n".encode())
    if cmd == "c":
      while True:
        con.send("\nEnter a instant message or 'e' for exit: ".encode())
        msg = con.recv(1024).decode("utf-8", "ignore")
        msg = msg.strip()
        if msg == 'e':
          con.send(f"[{username.strip()}] left from chat.\n".encode())
          print(f"[{username.strip()}] left from chat.")
          break
        print(f"[{username.strip()}] {msg}")
        msg = input("Enter a instant message: ")
        print(f"[SysOp] {msg}")
        con.send(f"\n[SysOp] {msg}".encode())
    elif cmd == "q":
      con.send("Goodbye!\n".encode())
      break
    else:
     con.send("Invalid command. Type 's' to create a new bulletin or 'q' to quit: ".encode())
    con.send("Type 's' to create a new bulletin, type 'b' to view latest bulletins\nType 'c' to chat with sysop of current BBS or 'q' to quit: ".encode())
  con.close()
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        hostname = socket.gethostname()
        port = 12345
        #server.bind((hostname, port))
        server.bind(("127.0.0.1", port))
        server.listen(5)
        
        print("Server running")
        users = load_users()
        bulletins = load_bulletins()

        while True:
            con, addr = server.accept()
            handle_client(con, addr, users, bulletins)

if __name__ == "__main__":
    main()

