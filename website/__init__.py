from flask import Flask, render_template, request, redirect, url_for
import os
import glob
import getWinRate
app = Flask(__name__)

@app.route("/")
def index():
    os.chdir(r"C:/Users/Christopher/Desktop/TeamComp/website/static/images/icons")
    championIcons = glob.glob("*1.png")
    os.chdir(r"C:/Users/Christopher/Desktop/TeamComp/website")
    return render_template('index.html', champions=championIcons)

@app.route("/team", methods=['POST'])
def show_team():
    champs = {
        'champ1': request.form['champ1'],
        'champ2': request.form['champ2'],
        'champ3': request.form['champ3'],
        'champ4': request.form['champ4'],
        'champ5': request.form['champ5']
    }
    #for i in range(len(request.args)):
        #champs["champ{}".format(i+1)] = int(request.args.get('champ{}'.format(i+1)))
    return render_template('team.html', champions=champs)

def get_champ_names(champId1, champId2, champId3, champId4, champId5):
    champNames = {}
    champIds = [champId1, champId2, champId3, champId4, champId5]
    with open("champlist.txt") as f:
        for line in f:
            (key, val) = line.split(',')
            champNames[int(key)] = val
    output = []
    for champ in champIds:
        if not int(champ) == 0:
            output.append(champNames[int(champ)])
    output.sort()
    return output

def get_win_rate(champId1, champId2, champId3, champId4, champId5):
    champIds = [champId1, champId2, champId3, champId4, champId5]
    champions = []
    for champ in champIds:
        if not champ == 0:
            champions.append(int(champ))
    champions.sort()
    wins, plays = getWinRate.get_win_rate_champs("5.7.0.275", champions)
    if not plays == 0:
        winRate = "{0:.2f}".format(wins/plays * 100)
    else:
        winRate = 0
    return [winRate, plays]


app.jinja_env.globals.update(get_win_rate=get_win_rate)
app.jinja_env.globals.update(get_champ_names=get_champ_names)

if __name__ == "__main__":
    app.debug = True
    app.run()
