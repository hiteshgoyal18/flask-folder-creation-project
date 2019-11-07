import flask
from flask import render_template
from flask import request
from flask import jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('make_folder.html',
                               Title='Make Folder')
    elif request.method == "POST":
        folder_name = request.form.get('make_folder')
        try:
            os.mkdir('/home/hitesh/Desktop/'+folder_name)
            return jsonify({"Message": 'Folder Created Successfully'})
        except Exception as exc:
            return jsonify({'Message': exc})

    else:
        return "Error"

app.run()