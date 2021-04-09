import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
app.config["DEBUG"] = True
zero_shot_classifier = pipeline('zero-shot-classification')


@app.route('/')
def hello():
    return '<h1 style={text-align:\'center\';}>Hello, Welcome to Zero-Shot-Classification!<h1>'


@app.route('/zero-shot-classification/classify', methods=["POST"])
def add_input():
    sentence = request.json['sentence']
    categories = request.json['categories']

    if sentence and categories:
        result = zero_shot_classifier(
            sentence,
            categories
        )

        result_dic = {}
        for index, cat in enumerate(result["labels"]):
            result_dic[cat] = result['scores'][index]

        return jsonify(result_dic)
    return '''Invalid Request! Try setting header content-type='application/json'.
        The request must have sentence and categories parameter.
        Sample Request Data:
        {
            "sentence": "This computer is slow!",
            "categories": ["IT issue", "Price request", "Datetime query"]
        }                    
        '''


app.run()

