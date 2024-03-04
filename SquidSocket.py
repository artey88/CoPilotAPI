import socket

BUFFER_SIZE = 1024

#Connection function, sets socket globablly and trys to connect, passes if already connected
def connect(TCP_IP,TCP_PORT):
    #create a tcp/ip socket
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((TCP_IP, TCP_PORT))
        sock.recv(BUFFER_SIZE)
    except Exception:
        pass

#define product count function and return count as integer
def product_count(TCP_IP,TCP_PORT):
    #connect if not connected
    connect(TCP_IP,TCP_PORT)
    message = b'PRODUCTION_COUNTER=QUERY\n'
    sock.sendall(message)

    data = sock.recv(BUFFER_SIZE)
    res = data.decode('utf-8').strip().split('=',1)[1]
    res = int(res)
    
    sock.close()

    return res

#define set_batch function, builds message on designated machine, builds auto string, resets product count to 0, returns okay status if no errors
def set_batch(TCP_IP,TCP_PORT,BatchNum,ProdFam):
    connect(TCP_IP,TCP_PORT)
    #build squidink message
    message = b'BUILD_MESSAGE=Auto Barcode\n'
    sock.sendall(message)
    resp = sock.recv(BUFFER_SIZE)
    if 'ACK-ERROR' in resp.decode('utf-8').upper():
        return 'Error Building Message'
    
    #build auto data message
    AutoString = 'D'+str(BatchNum)+'~'+str(BatchNum)+'~'+str(ProdFam)+'~^\n'
    message = AutoString.encode('utf-8')
    sock.sendall(message)
    sock.recv(BUFFER_SIZE)    

    #reset product count
    message = b'PRODUCTION_COUNTER=0\n'
    sock.sendall(message)
    resp = sock.recv(BUFFER_SIZE)
    if 'ERROR' in resp.decode('utf-8').upper():
        return 'Error Setting Counter'
    
    sock.close()

    resp = '200 OK'

    return resp
