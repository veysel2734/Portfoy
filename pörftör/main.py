# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)



# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    form="Veysel Gençten"
    forum = request.form.get('email')
    button_python = request.form.get('button_python')
    button_bot = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,button_bot=button_bot,button_html=button_html,button_db=button_db,form=forum)
    

if __name__ == "__main__":
    app.run(debug=True)
