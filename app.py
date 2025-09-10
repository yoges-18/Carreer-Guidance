from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/main')
def main_page():
    return render_template('main.html')
@app.route('/btech')
def b_tech():
    return render_template('btech.html')
@app.route('/bcom')
def b_com():
    return render_template('bcom.html')
@app.route('/bsc')
def b_sc():
    return render_template('bsc.html')
@app.route('/ba')
def b_a():
    return render_template('ba.html')
@app.route('/profil')
def profil_page():
    return render_template('profil.html')
@app.route('/cs')
def cs_page():
    return render_template('cs.html')
@app.route('/mech')
def mech_page():
    return render_template('mechanical.html')
@app.route('/eee')
def ee_page():
    return render_template('electrical.html')
@app.route('/civil')
def civil_page():
    return render_template("civil.html")
@app.route('/ece')
def ece_page():
   return render_template("ece.html")
@app.route('/it')
def it_page():
   return render_template("it.html")
@app.route('/bc')
def bc_page():
   return render_template("bcm.html")
@app.route('/bba')
def bba_page():
   return render_template("bba.html")
@app.route('/ca_syllabus')
def ca_syllabus():
    return render_template('ca.html')
@app.route('/cs_professional')
def cs_professional():
    return render_template('cs_professional.html')
@app.route('/economics')
def economics():
    return render_template('economics.html')
@app.route('/cma')
def ema_page():
    return render_template('cma.html')
@app.route('/bachelorOfArts')
def bachelorOfArts_page():
    return render_template('bachelorOfArts.html')
@app.route('/Philosophy')
def Philosophy_page():
    return render_template('Philosophy.html')
@app.route('/Languages')
def Languages_page():
    return render_template('Languages.html')
@app.route('/Bsw')
def Bsw_page():
    return render_template('Bsw.html')
@app.route('/Journalism')
def Journalism_page():
    return render_template('Journalism.html')
@app.route('/Bfa')
def Bfa_page():
    return render_template('Bfa.html')
@app.route('/cutoff')
def cutoff_page():
    return render_template('cutoff.html')
@app.route('/bdes')
def bdes():
    return render_template('bdes.html')
@app.route('/bfa')
def bfa():
    return render_template('bfaa.html')
@app.route('/uxui')
def uxui():
    return render_template('uxui.html')
@app.route('/interior')
def interior():
    return render_template('interior.html')
@app.route('/fashion')
def fashion():
    return render_template('fashion.html')
@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = [
        {"question": "What subject do you enjoy the most?", "A": "Science", "B": "Commerce", "C": "Arts"},
        {"question": "Which activity do you prefer?", "A": "Coding", "B": "Marketing", "C": "Writing"},
        {"question": "Favorite type of project?", "A": "Building an app", "B": "Starting a business", "C": "Making a video"},
        {"question": "What excites you most?", "A": "Robots", "B": "Money", "C": "Design"},
        {"question": "Your best skill?", "A": "Problem Solving", "B": "Persuasion", "C": "Creativity"},
        {"question": "Preferred workplace?", "A": "Lab or tech company", "B": "Office or bank", "C": "Studio"},
        {"question": "Which is your dream job?", "A": "Engineer", "B": "Manager", "C": "Artist"},
        {"question": "Which tool do you enjoy using?", "A": "Python", "B": "Excel", "C": "Photoshop"},
        {"question": "Choose a favorite task", "A": "Programming", "B": "Selling ideas", "C": "Editing videos"},
        {"question": "Your personality?", "A": "Logical", "B": "Leader", "C": "Imaginative"},
    ]

    if request.method == 'POST':
        answers = [request.form.get(f'q{i}') for i in range(1, 11)]
        count_A = answers.count('A')
        count_B = answers.count('B')
        count_C = answers.count('C')

        if count_A >= max(count_B, count_C):
            result = "Suggested Courses: B.Tech Computer Science, B.Sc. Data Science"
        elif count_B >= max(count_A, count_C):
            result = "Suggested Courses: B.Com, BBA"
        else:
            result = "Suggested Courses: B.A English, B.Des (Design)"

        return render_template('quiz.html', questions=questions, result=result)

    return render_template('quiz.html', questions=questions)
@app.route('/cutoff', methods=['GET', 'POST'])
def cutoff_calculator():
    cutoff = None
    if request.method == 'POST':
        stream = request.form['stream']
        physics = int(request.form['physics'])
        chemistry = int(request.form['chemistry'])

        if stream == 'maths':
            maths = int(request.form['maths'])
            cutoff = (physics / 2) + (chemistry / 2) + maths
        elif stream == 'bio':
            biology = int(request.form['biology'])
            cutoff = (physics / 2) + (chemistry / 2) + (biology / 2)

        cutoff = round(cutoff, 2)

    return render_template('cutoff.html', cutoff=cutoff)

if __name__ == '__main__':
    app.run(debug=True)