def edit_history(mod, tag, en_name, capital):
	f = open('./{}/history/countries/{} - {}.txt'.format(mod, tag, en_name), 'w', encoding = 'UTF-8')
	f.write('capital = {}\nset_dictatorship = yes'.format(capital))
	f.close()