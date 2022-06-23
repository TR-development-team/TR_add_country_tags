def check_color(color):
	f = open('./hoi4/common/countries/colors.txt', 'r', encoding='UTF-8')
	all_color = f.readlines()
	f.close()
	for i in all_color:
		if(color in i):
			return True
	return False

def division_continent(l, x, y, r):
	for i in range(l.index(x) + 1, l.index(y) - 1):
		r.append(l[i])

def joint_country(l):
	t1 = []
	t2 = []
	i = 1
	for x in l:
		if(i % 4 == 1 ) or (i % 4 == 2) or (i % 4 == 3):
			t1.append(l[i - 1])
		elif(i % 4 == 0):
			t1.append(l[i - 1])
			t2.append("".join(t1))
			t1 = []
		i += 1
	return t2

def edit_color(tag, ja_name, continent, color):
	f = open('./hoi4/common/countries/colors.txt', 'r', encoding = 'UTF-8')
	all_color = f.readlines()
	f.close()

	vanilla_list = []
	mod_list = []
	dynamic_list = []
	vanilla_asia = []
	vanilla_europe = []
	vanilla_africa = []
	vanilla_new_continent = []
	vanilla_oceania = []
	mod_asia = []
	mod_europe = []
	mod_africa = []
	mod_new_continent = []
	mod_oceania = []
	mod_america = []

	for i in range(0, all_color.index('##GEACPS\n') - 1):
		vanilla_list.append(all_color[i])
	for i in range(all_color.index('##GEACPS\n') + 1, all_color.index('##動的国家\n') - 1):
		mod_list.append(all_color[i])
	for i in range(all_color.index('##動的国家\n') + 1, len(all_color)):
		dynamic_list.append(all_color[i])

	division_continent(vanilla_list, "#アジア\n", "#ヨーロッパ\n", vanilla_asia)
	division_continent(vanilla_list, "#ヨーロッパ\n", "#アフリカ\n", vanilla_europe)
	division_continent(vanilla_list, "#アフリカ\n", "#新大陸\n", vanilla_africa)
	division_continent(vanilla_list, "#新大陸\n", "#大洋州\n", vanilla_new_continent)
	for i in range(vanilla_list.index('#大洋州\n') + 1, len(vanilla_list)):
		vanilla_oceania.append(vanilla_list[i])

	division_continent(mod_list, "#アジア\n", "#ヨーロッパ\n", mod_asia)
	division_continent(mod_list, "#ヨーロッパ\n", "#アフリカ\n", mod_europe)
	division_continent(mod_list, "#アフリカ\n", "#新大陸\n", mod_africa)
	division_continent(mod_list, "#新大陸\n", "#大洋州\n", mod_new_continent)
	division_continent(mod_list, "#大洋州\n", "#アメリカ諸州\n", mod_oceania)
	for i in range(mod_list.index('#アメリカ諸州\n') + 1, len(mod_list)):
		mod_america.append(mod_list[i])

	vanilla_asia = joint_country(vanilla_asia)
	vanilla_europe = joint_country(vanilla_europe)
	vanilla_africa = joint_country(vanilla_africa)
	vanilla_new_continent = joint_country(vanilla_new_continent)
	vanilla_oceania = joint_country(vanilla_oceania)
	mod_asia = joint_country(mod_asia)
	mod_europe = joint_country(mod_europe)
	mod_africa = joint_country(mod_africa)
	mod_new_continent = joint_country(mod_new_continent)
	mod_oceania = joint_country(mod_oceania)
	mod_america = joint_country(mod_america)
	dynamic_list = joint_country(dynamic_list)

	add_color = tag + ' = {\t#' + ja_name + '\n\tcolor = rgb { ' + color +' }\n\tcolor_ui = rgb { ' + color +' }\n}\n'

	if(continent == "アジア"):
		mod_asia.append(add_color)
	elif(continent == "ヨーロッパ"):
		mod_europe.append(add_color)
	elif(continent == "アフリカ"):
		mod_africa.append(add_color)
	elif(continent == "新大陸"):
		mod_new_continent.append(add_color)
	elif(continent == "大洋州"):
		mod_oceania.append(add_color)
	elif(continent == "アメリカ諸州"):
		mod_america.append(add_color)

	vanilla_asia.sort()
	vanilla_europe.sort()
	vanilla_africa.sort()
	vanilla_new_continent.sort()
	vanilla_oceania.sort()
	mod_asia.sort()
	mod_europe.sort()
	mod_africa.sort()
	mod_new_continent.sort()
	mod_oceania.sort()
	mod_america.sort()
	dynamic_list.sort()

	f = open('./hoi4/common/countries/test.txt', 'w', encoding='UTF-8')
	f.write('##バニラ\n')
	f.write('#アジア\n')
	f.writelines(vanilla_asia)
	f.write('\n')
	f.write('#ヨーロッパ\n')
	f.writelines(vanilla_europe)
	f.write('\n')
	f.write('#アフリカ\n')
	f.writelines(vanilla_africa)
	f.write('\n')
	f.write('#新大陸\n')
	f.writelines(vanilla_new_continent)
	f.write('\n')
	f.write('#大洋州\n')
	f.writelines(vanilla_oceania)
	f.write('\n')
	f.write('##GEACPS\n')
	f.write('#アジア\n')
	f.writelines(mod_asia)
	f.write('\n')
	f.write('#ヨーロッパ\n')
	f.writelines(mod_europe)
	f.write('\n')
	f.write('#アフリカ\n')
	f.writelines(mod_africa)
	f.write('\n')
	f.write('#新大陸\n')
	f.writelines(mod_new_continent)
	f.write('\n')
	f.write('#大洋州\n')
	f.writelines(mod_oceania)
	f.write('\n')
	f.write('#アメリカ諸州\n')
	f.writelines(mod_america)
	f.write('\n')
	f.write('##動的国家\n')
	f.writelines(dynamic_list)
	f.close()