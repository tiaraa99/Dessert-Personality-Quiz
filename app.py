from flask import Flask, render_template, request, redirect, url_for
import json
from collections import Counter

app = Flask(__name__)

# Load mapping
with open('mapping.json') as f:
    answer_map = json.load(f)

# Deskripsi karakter
character_descriptions = {
    "Pudding Calm": (
        "🍮 Pudding Calm 🍮\n\n"
        "Kamu adalah tipe yang reflektif, tenang, kadang keliatan dingin padahal mikir terus. "
        "Kamu suka menyendiri di tengah keramaian dan lebih nyaman jadi observer. "
        "Tapi justru di situlah charm kamu.\n"
    ),

    "Strawberry Pop": (
        "🍓 Strawberry Pop 🍓\n\n"
        "Kamu adalah orang yang hangat, nyambung sama siapa pun, dan punya vibe yang positif. "
        "Suka ngobrol santai, kadang ngeledek, kadang jadi tempat curhat. "
        "Selalu bisa bikin suasana lebih chill.\n"
    ),

    "Dark Choco Deep": (
        "🍫 Dark Choco Deep\n"
        "Kamu itu overthinker, logis, kadang emosional tapi gak nunjukin. "
        "Suka mikir dalam dan gak suka ngobrol ngalor ngidul. Kalau udah nyaman, bisa intense banget.\n"
        "“Bikin lucu boleh, tapi deep talk is a must.”"
    ),

    "Cookie Crackle": (
        "🍪 Cookie Crackle\n"
        "Kamu orangnya spontan, rame, dan suka ngelucu di waktu gak terduga. "
        "Kamu gak suka suasana canggung, jadi selalu jadi penyelamat suasana.\n"
        "“Aku chaos, tapi chaos yang bisa dicintai.”"
    ),

    "Cheesecake Core": (
        "🍰 Cheesecake Core\n"
        "Kamu dewasa, stabil, dan keliatan \"wise\" di antara teman-teman. "
        "Gak banyak gaya tapi bisa diandalkan. Gak nyari spotlight, tapi dihargai karena vibe-nya kalem dan elegan.\n"
        "“Aku gak banyak ngomong, tapi sekali ngomong langsung nancep.”"
    ),

    "Coconut Chill": (
        "🥥 Coconut Chill\n"
        "Kamu itu cuek, santai, dan gak suka drama. "
        "Kamu jalan sesuai mood, gak maksa apa pun, tapi tetep punya kepekaan yang gak banyak orang sadari.\n"
        "“Lowkey bukan berarti lost, aku cuma gak ribut.”"
    )
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/result', methods=['POST'])
def result():
    answers = [request.form['q1'], request.form['q2'], request.form['q3']]
    points = []

    for i, ans in enumerate(answers, 1):
        key = f"{i}{ans.upper()}"
        points.extend(answer_map.get(key, []))

    counter = Counter(points)
    result = counter.most_common(1)[0][0]
    description = character_descriptions[result]

    return render_template('result.html', character=result, description=description)

if __name__ == '__main__':
    app.run(debug=True)
