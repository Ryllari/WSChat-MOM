import CosNaming
import os
import sys
import threading
import Tkinter as tk

from client import ClientServer
from datetime import datetime
from omniORB import CORBA, PortableServer
from utils import *

from tkSimpleDialog import *

chat_ui = tk.Tk()
chat_ui.geometry("5x5")

def run_orb():
    global orb
    orb.run()

# Initialize the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of CentralServer and an CentralServer object reference
ei = ClientServer()
eo = ei._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

name_ok = False
while(not name_ok):
    username = askstring("BEM-VINDO AO CHAT", "Como iremos te chamar?", parent=chat_ui)
    if username:
        name_server = username
        name_ok = True

# Bind context to the root context
try:
    name = [CosNaming.NameComponent(name_server, "context")]
    context = rootContext.bind_new_context(name)
    print "Ola, {}!".format(name_server)

except CosNaming.NamingContext.AlreadyBound, ex:
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    
    if context is None:
        print "Algo deu errado na conexao"
        sys.exit(1)
    
# Bind the object to the context
try:
    name = [CosNaming.NameComponent(name_server, "Object")]
    context.bind(name, eo)

except CosNaming.NamingContext.AlreadyBound:
    context.rebind(name, eo)

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

t1 = threading.Thread(target=run_orb)
t1.daemon = True
t1.start()

server = connect_to_server('Server')
status = server.connect_user(username)
diff_status = STATUS_OFF if status == STATUS_ON else STATUS_ON

running = True
while running:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n####################################")
    print("#############   CHAT   #############")
    print("####################################")
    print("@{} ({})".format(username, LIST_STATUS[status]))
    print("\n# DIGITE O NUMERO REFERENTE AO QUE DESEJA NO MENU")
    print("1 - Meus amigos")
    print("2 - Minhas Mensagens")
    print("3 - Ficar {}".format(LIST_STATUS[diff_status]))
    print("0 - Sair")
    option = raw_input("\nDigite uma opcao: ")
    if option == '1':
        print("Online:")
        print(server.list_users_by_status(STATUS_ON))
        print("---")
        print("Offline:")
        print(server.list_users_by_status(STATUS_OFF))
    elif option == "2":
        print("*****  Meus amigos *****")
        print("Online:")
        for user in server.list_users_by_status(STATUS_ON):
            print("{} - {} mensagens".format(user, eo.get_msg_count(user)))
        
        print("---\nOffline:")
        for user in server.list_users_by_status(STATUS_OFF):
            print("{} - {} mensagens".format(user, eo.get_msg_count(user)))
        
        print("\n\n- Para CONVERSAR COM ALGUM AMIGO, digite + e pressione Enter")
        print("- Para voltar ao MENU pressione Enter")
        chat_option = raw_input("\nO que deseja? ")
        if chat_option == "+":
            if status == STATUS_ON:
                friend = askstring("CHAT", "Com quem quer conversar?", parent=chat_ui)
                if friend in server.get_username_list():
                    in_chat = True
                    while(in_chat):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\n\n- Para ENVIAR MENSAGEM, digite + e pressione Enter")
                        print("- Para voltar ao MENU PRINCIPAL pressione Enter")

                        print("\n****** {} *******\n".format(friend))
                        
                        eo.show_chat(friend)              
                        msg_option = raw_input("\nDigite sua mensagem para {}".format(friend))
                        if msg_option != "":
                            send_msg = msg_option
                            # send_msg = askstring("CHAT", "Digite sua mensagem para {}".format(friend), parent=chat_ui)
                            timestamp = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
                            if server.get_user_status(friend) == STATUS_ON:
                                friend_server = connect_to_client(friend)
                                friend_server.receive_msg(username, timestamp, send_msg, '')
                                eo.receive_msg(friend, timestamp, send_msg, username)
                            else:
                                # FAZER INTEGRACAO COM RABBITMQ
                                pass
                        else:
                            in_chat = False
                else:
                    print("OPS! Tem certeza que este amigo existe?")
            else:
                print("Fique Online para poder conversar...")
            
    elif option == "3":
        server.change_user_status(username, diff_status)
        status, diff_status = diff_status, status
        print("Status atual: {}".format(LIST_STATUS[status]))

    elif option == "0":
        print("Tchau!")
        server.change_user_status(username, STATUS_OFF)
        running = False
        sys.exit(1)
    
    else:
        print("Opcao invalida!")
    
    raw_input("\nPressione qualquer tecla para voltar ao menu principal...")