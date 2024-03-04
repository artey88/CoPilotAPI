
from flask import Flask, jsonify
from waitress import serve
import SquidSocket
import socket

#get local IP for dynamic host generation in case API service needs switched on hosts will not need to hardcode
local_host = socket.gethostname()
local_ip = socket.gethostbyname(local_host)


app = Flask(__name__)

#create endpoint for getting count and returning in json
@app.route('/count/<ip>/<port>/')
def count(ip,port):

    count = SquidSocket.product_count(str(ip), int(port))

    return jsonify(count)

#create endpoint for setting batch number and prodfam for machine. Resets count to zero
@app.route('/setbatch/<ip>/<port>/<batch>/<prodfam>/', methods = ['POST'])
def setbatch(ip,port,batch,prodfam):
    
    setbatch = SquidSocket.set_batch(str(ip),int(port),str(batch),str(prodfam))

    return jsonify(setbatch)

#Waitress setup. Comment out for development work
serve(app, host=local_ip,port=5000,threads=4)
#uncomment for development servers on machine or within IDE
#app.run(host=local_ip)
#app.run()