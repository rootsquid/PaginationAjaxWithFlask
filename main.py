from flask import Flask, jsonify, render_template, request
from database import Database
from randomdata import GetRandomLine
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_get_data', methods=['POST'])
def _get_data():
    if request.method == 'POST':
        print("Getting data from database")
        page = request.form['page']
        print("Page: " + page)
        return jsonify(db.get_all_data())
        

@app.route('/_get_data_page', methods=['POST'])
def _get_data_page():
    print("Getting data from database")
    if request.method == 'POST':
        print("Getting data from database")
        page = request.form['page']
        print("Page: " + page)
        return jsonify(db.get_data(page))


@app.route('/_get_total_records', methods=['POST'])
def _get_total_records():
    if request.method == 'POST':
        print("Getting total rows from database")
        return jsonify(db.get_total_rows())



if __name__ == "__main__":
    print("Starting Flask Server")

    #Initialize Database
    db = Database()
    db.create_table()

    if db.isEmpty():
        #Fill Database with random dummy data
        for i in range(55):
            db.insert_data(name=GetRandomLine('names.txt'), color=GetRandomLine('colors.txt'), age=random.randint(18, 110))
        print("Database filled with dummy data")


    app.run(host='0.0.0.0', port=5000, debug=True)