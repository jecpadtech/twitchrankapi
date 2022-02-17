from flask import Flask
import requests
import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

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
            

if __name__ == "__main__":
    app.run(debug=True)