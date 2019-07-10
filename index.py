Romanenko = [

	{
		'id': 1,
		'exam': 'Операционные системы',
		'result': "Отлично",

	},


	{
		'id': 2,
		'exam': 'Вычислительная математика',
		'result': "Удовлетворительно",

	},

	{
		'id': 3,
		'exam': 'Электротехника',
		'result': "Хорошо",

	},

	{
		'id': 4,
		'exam': 'ЭВМ и ПУ',
		'result': "Удовлетворительно",

	},
]
RM = []
def brut():
	for i in range(len(Romanenko)):
		a = Romanenko[i].get("result")
		print(a)
		if a == "Отлично" or a == "Хорошо":
			RM.append(Romanenko[i])
			# Romanenko[i].clear()
		else:
			continue
	print(Romanenko)
	print(RM)
brut()

