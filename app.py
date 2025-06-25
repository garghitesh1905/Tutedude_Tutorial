from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data_file = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(data_file, 'r') as f:
        return jsonify(json.load(f))
    
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    itemName = request.form.get('itemName')
    itemDescription = request.form.get('itemDescription')
    collection.insert_one({
        'itemName': itemName,
        'itemDescription': itemDescription
    })
    return "<h2>Data submitted successfully</h2>"
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    ...
    collection.insert_one({...})
    return "Success"



if __name__ == '__main__':
    app.run(debug=True)
