import json
import requests
import sys
import pandas as pd


def main():
    #Save data to the disk from Euroleague API
    #for i in range (329, 330):
        #saveGameData(str(i), "E2023")

    # get palyer statistic of the season by player Id
    playerStatisticOfTheGames = getPlayerStatsticOfGames("P011218", "ZAL")
    printStatisticToConsole (playerStatisticOfTheGames,"")

    #get gameData dictionary from Euroleague API
    #gameData = getGameDataFromEuroleagueAPI("16", "E2023")

    #get teams of the game
    #teams = getTeams(gameData)


    #get players names from gameData
    #players = getPlayersNames(gameData)
    #printStatisticToConsole(players, "")

    #get players statistics by team
    #playersStatisticTeamA = getPlayersStatistic(gameData, players, teams["CodeTeamA"] )
    #playersStatisticTeamB = getPlayersStatistic(gameData, players, teams["CodeTeamB"] )

    #print Team statistic to console
    #printStatisticToConsole(playersStatisticTeamA, teams["TeamA"])
    #printStatisticToConsole(playersStatisticTeamB, teams["TeamB"])


def getPlayerStatsticOfGames(playerId, teamCode):


    #329 games in the E2023 season
    stats = []
    for i in range (1, 330):
        try:
            file = "gameData/game"+str(i)+".json"
            with open(file, 'r') as myfile:
                data=myfile.read()
            gameData = json.loads(data)
        except ValueError:
            print("Game data "+ str(i) + " is empty")
            pass

        playerStatisticofTheGame = getPlayerStatisticInTheGame(gameData, playerId)
        if "PLAYER" in playerStatisticofTheGame:
            if teamCode == gameData["CodeTeamA"].strip():
                playerStatisticofTheGame["TEAM"] = gameData["TeamB"]
            else:
                playerStatisticofTheGame["TEAM"] = gameData["TeamA"]
            stats.append(playerStatisticofTheGame)

    return stats


def getGameDataFromEuroleagueAPI(gameCode, seasonCode):

    response = requests.get("https://live.euroleague.net/api/PlaybyPlay?gamecode="+gameCode+"&seasoncode="+seasonCode)
    return response.json()

def saveGameData(gameCode, seasonCode):

    response = requests.get("https://live.euroleague.net/api/PlaybyPlay?gamecode="+gameCode+"&seasoncode="+seasonCode)

    fileName = "gameData/game"+gameCode+".json"
    save_file = open(fileName, "w")
    json.dump(response.json(), save_file, indent = 6)
    save_file.close()

    return response.json()


def getTeams(o):

    teams ={}
    teams["TeamA"] = o["TeamA"]
    teams["CodeTeamA"] = o["CodeTeamA"].strip()
    teams["TeamB"] = o["TeamB"]
    teams["CodeTeamB"] = o["CodeTeamB"].strip()

    return teams



def getPlayersNames(o):
    quarters = ['FirstQuarter', 'SecondQuarter', 'ThirdQuarter', 'ForthQuarter', 'ExtraTime']
    players=[]
    for q in quarters:
        for event in o[q]:
            Player={}
            Player["Player_ID"] = event["PLAYER_ID"].strip()
            Player["Name"] = event["PLAYER"]
            Player["Team"] = event["TEAM"]
            Player["CODETEAM"] = event["CODETEAM"].strip()
            if Player not in players and Player["Name"] != None:
                players.append(Player)

    return players

def getPlayersStatistic(o, players, teamCode):

    statistic=[]
    for player in players:
        if player["CODETEAM"] == teamCode:
            statistic.append(getPlayerStatisticInTheGame(o,player["Player_ID"]))

    return statistic

def getPlayerStatisticInTheGame(o, id):
    quarters = ['FirstQuarter', 'SecondQuarter', 'ThirdQuarter', 'ForthQuarter', 'ExtraTime']
    statistic={}
    FTM = 0 # free throaws made
    FTA = 0 # free throaws missed
    P3FGM = 0 # 3 points throaws made
    P3FGA = 0 # 3 points throaws missed
    P2FGM = 0 # 2 points throaws made
    P2FGA = 0 # 2 points throaws missed
    TO = 0 # turnovers
    ST = 0 # steals
    AS = 0 # assists
    DR = 0 # defensive rebounds
    OR = 0 # offensive rebounds
    FC = 0 # fouls commited
    FR = 0 # fouls comited againts
    BR = 0 # Blocks made
    BA = 0 # Blocks getpython


    for q in quarters:
        for event in o[q]:
            if id == event["PLAYER_ID"].strip():

                #statistic["TEAM"] = event["TEAM"]
                statistic["PLAYER"] = event["PLAYER"]

                match event["PLAYTYPE"]:
                    case "FTM":
                        FTM = FTM+1
                    case "FTA":
                        FTA = FTA+1
                    case "2FGM":
                        P2FGM = P2FGM+1
                    case "2FGA":
                        P2FGA = P2FGA+1
                    case "3FGM":
                        P3FGM = P3FGM+1
                    case "3FGA":
                        P3FGA = P3FGA+1
                    case "TO":
                        TO = TO+1
                    case "ST":
                        ST = ST+1
                    case "AS":
                        AS = AS+1
                    case "D":
                        DR = DR+1
                    case "O":
                        OR = OR+1
                    case "CM":
                        FC = FC+1
                    case "RV":
                        FR = FR+1
                    case "AG":
                        BR = BR+1
                    case "FV":
                        BA = BA+1


    statistic["PTS"] = FTM + P2FGM*2 + P3FGM*3
    #statistic["FTM"] = FTM
    #statistic["FTA"] = FTA+FTM
    statistic["FT"] = str(FTM)+"/"+str(FTA + FTM)
    #statistic["2FGM"] = P2FGM
    #statistic["2FGA"] = P2FGA + P2FGM
    statistic["2FG"] = str(P2FGM)+"/"+str(P2FGA + P2FGM)
    #statistic["3FGM"] = P3FGM
    #statistic["3FGA"] = P3FGA + P3FGM
    statistic["3FG"] = str(P3FGM)+"/"+str(P3FGA + P3FGM)
    statistic["AS"] = AS
    statistic["ST"] = ST
    statistic["TO"] = TO
    statistic["DR"] = DR
    statistic["OR"] = OR
    statistic["REB"] = OR + DR
    statistic["FC"] = FC
    statistic["FR"] = FR
    statistic["BR"] = BR
    statistic["BA"] = BA
    statistic["PIR"] = FTM + P2FGM*2 + P3FGM*3+OR + DR+AS+ST+FR+BA-TO-FTA-P2FGA-P3FGA-FC-BR




    return statistic

def  printStatisticToConsole(playersStatisticList, team):

        df = pd.DataFrame(playersStatisticList)
        print(team)
        print(df)

if __name__ == "__main__":
    main()
