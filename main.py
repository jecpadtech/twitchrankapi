from flask import Flask
import requests
from datetime import datetime
app = Flask(__name__)

def getRank(name,irlname,region):
    response = requests.get("https://api.henrikdev.xyz/valorant/v2/leaderboard/" + region)
    json_data = response.json()
    for x in json_data["players"]:
        if x["gameName"] == name:
            return irlname + " is currently ranked #" + str(x["leaderboardRank"])+ " on the leaderboard with " + str(x["numberOfWins"]) + " wins and a ranked rating of " + str(x["rankedRating"])
def getRecord(name,tag,irlname):
    y=[]
    a=[]
    wins = 0
    loss = 0
    draw = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/"+name+"/"+tag)
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        elif 0>=n>10:
            a.append("T")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        elif l == "L":
            loss +=1
        else:
            draw +=1
        
    return irlname + " has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a)
def maps(name,tag):
    mapList = []
    response = requests.get("https://api.henrikdev.xyz/valorant/v3/matches/eu/"+name+"/"+tag)
    json_data = response.json()
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    if json_data["status"] == 200:
        today = datetime.today()
        currentDate = today.strftime("%B %d, %Y")
        for x in range(0,5):
            if json_data["data"][x]["metadata"]["mode"] == "Competitive":
                splitString = json_data["data"][x]["metadata"]["game_start_patched"].split()
                newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
                if currentDate == newDate:
                    mapList.append(json_data["data"][x]["metadata"]["map"])
    return "Today's map history is "+ str(mapList)

@app.route('/')
def hello():
    return "Valorant Record/Leaderboard command for Nightbot. DM Vineyard__ on twitch or Vinayak9769#0861 on discord for a page!"
 

@app.route('/leon', methods=['POST', 'GET'])
def leonRank():
    return getRank("LJPH", "Leon","eu")
@app.route('/leon/record', methods=['POST', 'GET'])
def getLeonRec():
    y=[]
    a=[]
    wins = 0
    loss = 0
    draw = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/LJPH/018")
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        elif 0>n>10:
            a.append("T")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        elif l == "L":
            loss +=1
        else:
            draw +=1
        
    return "Leon has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a[::-1])
@app.route('/Stout', methods=['POST', 'GET'])
def stoutrank():
    return getRank("SOL Stout","Stout","na")
@app.route('/josh', methods=['POST', 'GET'])
def joshRank():
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr/eu/JoshMun/Mun")
    json_data = response.json()
    x = json_data["data"]
    return "Josh is currently " + x["currenttierpatched"] + " with a ranked rating of " +str(x["ranking_in_tier"])
@app.route('/josh/record', methods=['POST', 'GET'])
def joshrecord():
    return getRecord("JoshMun","Mun", "Josh")
@app.route('/swedish/record', methods=['POST', 'GET'])
def swedeRec():
    return getRecord("LittleSwede","IKEA", "LittleSwedish")
@app.route('/wasu/record', methods=['POST', 'GET'])
def wasummr():
    return getRecord("wasu","LFT","Wasu")
@app.route('/eggo', methods=['POST', 'GET'])
def eggoRank():
    return getRank("egnarO5","Eggo","eu")
@app.route('/kyle', methods=['POST', 'GET'])
def kyleRank():
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr/eu/KYCA/KYCA")
    json_data = response.json()
    x = json_data["data"]
    return "Kyle is currently " + x["currenttierpatched"] + " with a ranked rating of " +str(x["ranking_in_tier"])
@app.route('/eggo/record', methods=['POST', 'GET'])
def eggoRec():
    return getRecord("egnarO5","713", "Eggo")

@app.route('/kyle/record', methods=['POST', 'GET'])
def kyleRecord():    
    return getRecord("KYCA","KYCA","Kyle")
@app.route('/linka/record', methods=['POST', 'GET'])
def linkaRec():
    y=[]
    a=[]
    wins = 0
    loss = 0
    draw = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/Pancakes/1313")
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        elif 0>n>10:
            a.append("T")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        elif l == "L":
            loss +=1
        else:
            draw +=1
        
    return "Linka has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a[::-1])
@app.route('/linka', methods=['POST', 'GET'])
def linkaRank():
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr/eu/Pancakes/1313")
    json_data = response.json()
    x = json_data["data"]
    return "Linka is currently " + x["currenttierpatched"] + " with a ranked rating of " +str(x["ranking_in_tier"])
@app.route('/josh/maps', methods=['POST', 'GET'])
def joshMaps():
    return maps("JoshMun","Mun")
@app.route('/leon/maps', methods=['POST', 'GET'])
def leonMaps():
    return maps("LJPH","018")
@app.route('/linka/maps', methods=['POST', 'GET'])
def linkaMaps():
    return maps("Pancakes","1313")

if __name__ == "__main__":
    app.run(debug=True)
