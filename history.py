def edit_history(tag, en_name, capital):
	f = open('./hoi4/history/countries/{} - {}.txt'.format(tag, en_name), 'w', encoding = 'UTF-8')
	f.write('capital = {}\nset_dictatorship = yes'.format(capital))
	f.close()