import random
from flask import Flask

app = Flask(__name__)

orel = ["орел","решка"]
spisok = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс","Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.","Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.","Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.","Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."]
@app.route("/")
def gipersilka():
    return f'<p>Интересные факты. или поиграть в орел или решка<a href="/random_fact">Посмотреть случайный факт!></a>сыграть в орел или решка<a href="/game">></a><p>'

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(spisok)}</p>'
@app.route("/game")
def match():
    return f'<p>{random.choice(orel)}</p'

app.run(debug=True)
