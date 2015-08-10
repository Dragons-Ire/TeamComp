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
    selection = {
        'champ1': request.form['champ1'],
        'champ2': request.form['champ2'],
        'champ3': request.form['champ3'],
        'champ4': request.form['champ4'],
        'champ5': request.form['champ5']
    }
    return render_template('team.html', champions=selection)

def get_win_rate(champId1, champId2, champId3, champId4, champId5):
    champIds = [champId1, champId2, champId3, champId4, champId5]
    selection = []
    for champ in champIds:
        if not int(champ) == 0:
            selection.append(int(champ))
    selection.sort()
    print(selection)
    wins, plays, first, second, third = getWinRate.get_win_rate_champs("5.7.0.275", selection)
    if not plays == 0:
        winRate = "{0:.2f}".format(wins/plays * 100)
    else:
        winRate = 0
    return [winRate, plays, first, second, third]

def get_champ_names(champId1, champId2, champId3, champId4, champId5):
    champNames = get_champion_ids()
    champIds = [champId1, champId2, champId3, champId4, champId5]
    output = []
    for champ in champIds:
        if not int(champ) == 0:
            output.append(champNames[int(champ)])
    output.sort()
    return output


def get_champion_ids():
    return {1: 'Annie', 2: 'Olaf', 3: 'Galio', 4: 'TwistedFate', 5: 'XinZhao', 6: 'Urgot', 7: 'LeBlanc',
    8: 'Vladimir', 9: 'Fiddlesticks', 266: 'Aatrox', 267: 'Nami', 268: 'Azir', 13: 'Ryze', 14: 'Sion',
    15: 'Sivir', 16: 'Soraka', 17: 'Teemo', 18: 'Tristana', 19: 'Warwick', 20: 'Nunu', 21: 'MissFortune',
    22: 'Ashe', 23: 'Tryndamere', 24: 'Jax', 25: 'Morgana', 26: 'Zilean', 27: 'Singed', 28: 'Evelynn',
    29: 'Twitch', 30: 'Karthus', 31: 'Chogath', 32: 'Amumu', 33: 'Rammus', 34: 'Anivia', 35: 'Shaco',
    36: 'DrMundo', 37: 'Sona', 38: 'Kassadin', 39: 'Irelia', 40: 'Janna', 41: 'Gangplank', 42: 'Corki',
    43: 'Karma', 44: 'Taric', 45: 'Veigar', 48: 'Trundle', 50: 'Swain', 51: 'Caitlyn', 53: 'Blitzcrank',
    54: 'Malphite', 55: 'Katarina', 56: 'Nocturne', 57: 'Maokai', 58: 'Renekton', 59: 'JarvanIV', 60:
    'Elise', 10: 'Kayle', 62: 'Wukong', 63: 'Brand', 64: 'LeeSin', 67: 'Vayne', 68: 'Rumble', 69:
    'Cassiopeia', 72: 'Skarnar', 12: 'Alistar', 74: 'Heimerdinger', 75: 'Nasus', 76: 'Nidalee', 77: 'Udyr',
    78: 'Poppy', 79: 'Gragas', 11: 'MasterYi', 81: 'Ezreal', 82: 'Mordekaiser', 83: 'Yorick', 84: 'Akali',
    85: 'Kennen', 86: 'Garen', 89: 'Leona', 90: 'Malzahar', 91: 'Talon', 92: 'Riven', 96: 'Kogmaw',
    98: 'Shen', 99: 'Lux', 101: 'Xerath', 102: 'Shyvana', 103: 'Ahri', 104: 'Graves', 105: 'Fizz',
    106: 'Volibear', 107: 'Rengar', 110: 'Varus', 61: 'Orianna', 112: 'Viktor', 113: 'Sejuani',
    114: 'Fiora', 115: 'Ziggs', 117: 'Lulu', 119: 'Draven', 120: 'Hecarim', 121: 'Khazix', 122: 'Darius',
    126: 'Jayce', 127: 'Lissandra', 131: 'Diana', 133: 'Quinn', 134: 'Syndra', 143: 'Zyra', 150: 'Gnar',
    154: 'Zac', 111: 'Nautilus', 412: 'Thresh', 157: 'Yasuo', 161: 'Velkoz', 421: 'Reksai', 429: 'Kalista',
    432: 'Bard', 201: 'Braum', 222: 'Jinx', 223: 'TahmKench', 80: 'Pantheon', 236: 'Lucian', 238: 'Zed',
    245: 'Ekko', 254: 'Vi'}

app.jinja_env.globals.update(get_win_rate=get_win_rate)
app.jinja_env.globals.update(get_champ_names=get_champ_names)
app.jinja_env.globals.update(get_champion_ids=get_champion_ids)

if __name__ == "__main__":
    app.debug = True
    app.run()
