def mod_list():
	with open(f'./mod_list.txt', 'r', encoding='utf-8') as o_file:
		return o_file.readlines()
