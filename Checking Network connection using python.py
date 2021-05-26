import socket
def net():
    try:
        if socket.create_connection(('google.com',80)):
            print("You have internet access")
    except:
        print("you don't have internet access")
net()
