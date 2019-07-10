#!flask/Scripts/python
from flask import Flask, jsonify

app = Flask(__name__)

Romanenko = [

	{
		'id': 1,
		'exam': 'Операционные системы',
		'result': "Fine",

	},


	{
		'id': 2,
		'exam': 'Вычислительная математика',
		'result': "Хорошо",

	},

	{
		'id': 3,
		'exam': 'Электротехника',
		'result': "Хорошо",

	},

	{
		'id': 4,
		'exam': 'ЭВМ и ПУ',
		'result': "Отлично",

	},
]

@app.route('/sber/api/Romanenko', methods=['GET'])
def get_Romanenko():
    return jsonify({'Romanenko Bogdan': Romanenko})

if __name__ == '__main__':
    app.run(debug=True)