#!flask/Scripts/python
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
Romanenko = [

	{
		# 'id': 1,
		'exam': 'Операционные системы',
		'result': "Удов",

	},


	{
		# 'id': 2,
		'exam': 'Вычислительная математика',
		'result': "Хорошо",

	},

	{
		# 'id': 3,
		'exam': 'Электротехника',
		'result': "Хорошо",

	},

	{
		# 'id': 4,
		'exam': 'ЭВМ и ПУ',
		'result': "Отлично",

	},
]
RM = []

def brut():
	for i in range(len(Romanenko)):
		a = Romanenko[i].get("result")
		if a == "Отлично" or a == "Хорошо":
			RM.append(Romanenko[i])
			# Romanenko[i].clear()
		else:
			continue
brut()
@app.route('/sber/api/Romanenko', methods=['GET'])

def get_Romanenko():
    return jsonify({'Romanenko Bogdan': RM})

if __name__ == '__main__':
    app.run(debug=True)