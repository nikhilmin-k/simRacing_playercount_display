import requests
import json
import time
import neopixel
import board
import os
import socket
import time

HOST = ''
PORT = 50007

pixels = neopixel.NeoPixel(board.D18, 30)
white = [25,25,25]
red = [25, 0, 0]
green = [0,25,0]
assetto = red
rfactor = [25,11,0]
beamng = [25,25,0]
automob = [12,25,0]
assettocomp = [16,0,25]
pcars = [0,0,25]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

for i in range(8):
    if i%2 == 0:
        pixels[i] = green
    if i%2 == 1:
        pixels[i] = red

while(True):
    sock.listen(1)
    conn, addr = sock.accept()
    print('Connected to Processing via ', addr)

    procc_data = conn.recv(1024)
    procc_data_dict = json.loads(procc_data)
    parametersA = {"appid": procc_data_dict['idA'], "key": "66A09E7D651F71360ED06354A57830AE"}
    parametersB = {"appid": procc_data_dict['idB'], "key": "66A09E7D651F71360ED06354A57830AE"}
    parametersC = {"appid": procc_data_dict['idC'], "key": "66A09E7D651F71360ED06354A57830AE"}
    parametersD = {"appid": procc_data_dict['idD'], "key": "66A09E7D651F71360ED06354A57830AE"}
    parametersE = {"appid": procc_data_dict['idE'], "key": "66A09E7D651F71360ED06354A57830AE"}
    parametersF = {"appid": procc_data_dict['idF'], "key": "66A09E7D651F71360ED06354A57830AE"}
    try:
        respA = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersA)
        respB = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersB)
        respC = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersC)
        respD = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersD)
        respE = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersE)
        respF = requests.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", params=parametersF)
    except Exception as excep:
        print("request exception");
        break;
    if respB.status_code != 200:
        print("something went wrong\n")
    dataA = respA.json()
    dataB = respB.json()
    dataC = respC.json()
    dataD = respD.json()
    dataE = respE.json()
    dataF = respF.json()

    print("Game A Player Count: {0}".format(dataA['response']['player_count']))
    print("Game B Player Count: {0}".format(dataB['response']['player_count']))
    print("Game C Player Count: {0}".format(dataC['response']['player_count']))
    print("Game D Player Count: {0}".format(dataD['response']['player_count']))
    print("Game E Player Count: {0}".format(dataE['response']['player_count']))
    print("Game F Player Count: {0}".format(dataF['response']['player_count']))

    data_dict = {
        "idA": dataA['response']['player_count'],
        "idB": dataB['response']['player_count'],
        "idC": dataC['response']['player_count'],
        "idD": dataD['response']['player_count'],
        "idE": dataE['response']['player_count'],
        "idF": dataF['response']['player_count'],
    }

    data = json.dumps(data_dict)
    data_encoded = data.encode()

    sendstatus = conn.send(data_encoded)
    print(sendstatus)
    if sendstatus<1:
        print("somthing went wrong")
        break;
    else:
        print("data successfully sent")

#LED control based on data
    for i in range(8):
        if pixels[i] == red:
            pixels[i] = green
        elif pixels[i] == green:
            pixels[i] = red

    a = dataA['response']['player_count']
    b = dataB['response']['player_count']
    c = dataC['response']['player_count']
    d = dataD['response']['player_count']
    e = dataE['response']['player_count']
    f = dataF['response']['player_count'] 
   
    tot = a+b+c+d+e+f
    
    if a==max(a,b,c,d,e,f):
        color = assetto
    elif b==max(a,b,c,d,e,f):
        color = rfactor
    elif c==max(a,b,c,d,e,f):
        color = beamng
    elif d==max(a,b,c,d,e,f):
        color = automob
    elif e==max(a,b,c,d,e,f):
        color = assettocomp
    elif f==max(a,b,c,d,e,f):
        color = pcars
    else:
        color = assetto
    
    ratio = float(max(a,b,c,d,e,f))/float(tot) 
    numleds = int(ratio/0.125) 
    print("NumLeds: {0}, Color: {0}".format(numleds, color))
    for i in range(8):
        if(numleds>0):
            pixels[i] = color
            numleds -= 1
        else:
            pixels[i] = white


    conn.close()
#data_dict = json.loads(data['response'])
#print(data)
#resp.json()
