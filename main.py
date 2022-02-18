from flask import Flask
import requests
app = Flask(__name__)
from datetime import datetime


@app.route('/')
def hello():
    return "Valorant Record/Leaderboard command for Nightbot. DM Vineyard__ on twitch or Vinayak9769#0861 on discord for a page!"

@app.route('/leon', methods=['POST', 'GET'])
def getrank():
    response = requests.get("https://api.henrikdev.xyz/valorant/v2/leaderboard/eu")
    json_data = response.json()
    for x in json_data["players"]:
        if x["gameName"] == "LJPH":
            return "LJPH is currently ranked #" + str(x["leaderboardRank"])+ " on the leaderboard with " + str(x["numberOfWins"]) + " wins and a ranked rating of " + str(x["rankedRating"]) 

# @app.route('/Josh', methods=['POST', 'GET'])
# def getrank2():
#     response = requests.get("https://api.henrikdev.xyz/valorant/v2/leaderboard/eu")
#     json_data = response.json()
#     for x in json_data["players"]:
#         if x["gameName"] == "JoshMun":
#             return "Josh is currently ranked #" + str(x["leaderboardRank"]) + " on the leaderboard with a ranked rating of " +str(x["rankedRating"] + " and " + str(x("numberOfWins")) + " wins")
@app.route('/Stout', methods=['POST', 'GET'])
def stoutrank():
    response = requests.get("https://api.henrikdev.xyz/valorant/v2/leaderboard/na")
    json_data = response.json()
    for x in json_data["players"]:
        if x["gameName"] == "SOL Stout":
            return "Stout is currently ranked #" + str(x["leaderboardRank"])+ " on the leaderboard with " + str(x["numberOfWins"]) + " wins and a ranked rating of " + str(x["rankedRating"])      
@app.route('/josh', methods=['POST', 'GET'])
def joshRank():
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr/eu/JoshMun/Mun")
    json_data = response.json()
    x = json_data["data"]
    return "Josh is currently " + x["currenttierpatched"] + " with a ranked rating of " +str(x["ranking_in_tier"])
@app.route('/josh/record', methods=['POST', 'GET'])
def mmrswede():
    y=[]
    a=[]
    wins = 0
    loss = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/JoshMun/Mun")
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        else:
            loss +=1
    return "Josh has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a)

@app.route('/swedish/record', methods=['POST', 'GET'])
def mmr():
    y=[]
    a=[]
    wins = 0
    loss = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/LittleSwede/IKEA")
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        else:
            loss +=1
    return "LittleSwedish has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a)
@app.route('/wasu/record', methods=['POST', 'GET'])
def wasummr():
    y=[]
    a=[]
    wins = 0
    loss = 0
    resultString = ""
    today = datetime.today()
    currentDate = today.strftime("%B %d, %Y")
    response= requests.get("https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/wasu/LFT")
    json_data = response.json()
    for x in json_data["data"]:
        splitString = x["date"].split()
        newDate = "" +splitString[1] + " "+ splitString[2] + " "+ splitString[3]
        if currentDate == newDate:
            y.append(x["mmr_change_to_last_game"])
    for n in y:
        if n>0:
            a.append("W")
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        else:
            loss +=1
    return "Wasu has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a)
@app.route('/leon/record', methods=['POST', 'GET'])
def mmrswede():
    y=[]
    a=[]
    wins = 0
    loss = 0
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
        else:
            a.append("L")
    for l in a:
        if l == "W":
            wins+=1
        else:
            loss +=1
    return "Leon has won " + str(wins) + " games and lost " + str(loss) + " games today. " + "Record- " + str(a)

if __name__ == "__main__":
    app.run(debug=True)
