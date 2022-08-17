import color
import os
import re

def add_def_adj(list):
	tmp = []
	for i in list:
		if(":" in i):
			loc = i.split(":")
			definitive = loc[0] + "_DEF:" + loc[1]
			adjective = loc[0] + "_ADJ:" + loc[1]
			tmp.append(i + definitive + adjective + " \n")
	return tmp

def clear_def_adj(list):
	tmp = []
	for i in list:
		if "DEF" not in i:
			if "ADJ" not in i:
				tmp.append(i)
	return tmp

def add_loc(tag, ja_name, continent):
	with open(f'./hoi4/localisation/english/_map/geacps_countries_l_english.yml', 'r', encoding='utf-8-sig') as o_file:
		all_loc = o_file.readlines()

	vanilla_list = []
	mod_list = []
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

	for i in range(all_loc.index('##バニラ\n') + 1, all_loc.index('##GEACPS\n') - 1):
		vanilla_list.append(all_loc[i])
	for i in range(all_loc.index('##GEACPS\n') + 1, len(all_loc)):
		mod_list.append(all_loc[i])

	color.division_continent(vanilla_list, "#アジア\n", "#ヨーロッパ\n", vanilla_asia)
	color.division_continent(vanilla_list, "#ヨーロッパ\n", "#アフリカ\n", vanilla_europe)
	color.division_continent(vanilla_list, "#アフリカ\n", "#新大陸\n", vanilla_africa)
	color.division_continent(vanilla_list, "#新大陸\n", "#大洋州\n", vanilla_new_continent)
	for i in range(vanilla_list.index('#大洋州\n') + 1, len(vanilla_list)):
		vanilla_oceania.append(vanilla_list[i])

	color.division_continent(mod_list, "#アジア\n", "#ヨーロッパ\n", mod_asia)
	color.division_continent(mod_list, "#ヨーロッパ\n", "#アフリカ\n", mod_europe)
	color.division_continent(mod_list, "#アフリカ\n", "#新大陸\n", mod_africa)
	color.division_continent(mod_list, "#新大陸\n", "#大洋州\n", mod_new_continent)
	color.division_continent(mod_list, "#大洋州\n", "#アメリカ諸州\n", mod_oceania)
	for i in range(mod_list.index('#アメリカ諸州\n') + 1, len(mod_list)):
		mod_america.append(mod_list[i])

	vanilla_asia = clear_def_adj(vanilla_asia)
	vanilla_europe = clear_def_adj(vanilla_europe)
	vanilla_africa = clear_def_adj(vanilla_africa)
	vanilla_new_continent = clear_def_adj(vanilla_new_continent)
	vanilla_oceania = clear_def_adj(vanilla_oceania)
	mod_asia = clear_def_adj(mod_asia)
	mod_europe = clear_def_adj(mod_europe)
	mod_africa = clear_def_adj(mod_africa)
	mod_new_continent = clear_def_adj(mod_new_continent)
	mod_oceania = clear_def_adj(mod_oceania)
	mod_america = clear_def_adj(mod_america)

	add_loc =  ' {}:0 "{}"\n'.format(tag, ja_name)

	if(continent == "アジア"):
		mod_asia.append(add_loc)
	elif(continent == "ヨーロッパ"):
		mod_europe.append(add_loc)
	elif(continent == "アフリカ"):
		mod_africa.append(add_loc)
	elif(continent == "新大陸"):
		mod_new_continent.append(add_loc)
	elif(continent == "大洋州"):
		mod_oceania.append(add_loc)
	elif(continent == "アメリカ諸州"):
		mod_america.append(add_loc)

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

	with open(f'./hoi4/localisation/english/_map/geacps_countries_l_english.yml', 'w', encoding='utf-8-sig') as f:
		f.write('l_english:\n')
		f.write('##バニラ\n')
		f.write('#アジア\n')
		f.writelines(add_def_adj(vanilla_asia))
		f.write('#ヨーロッパ\n')
		f.writelines(add_def_adj(vanilla_europe))
		f.write('#アフリカ\n')
		f.writelines(add_def_adj(vanilla_africa))
		f.write('#新大陸\n')
		f.writelines(add_def_adj(vanilla_new_continent))
		f.write('#大洋州\n')
		f.writelines(add_def_adj(vanilla_oceania))
		f.write('##GEACPS\n')
		f.write('#アジア\n')
		f.writelines(add_def_adj(mod_asia))
		f.write('#ヨーロッパ\n')
		f.writelines(add_def_adj(mod_europe))
		f.write('#アフリカ\n')
		f.writelines(add_def_adj(mod_africa))
		f.write('#新大陸\n')
		f.writelines(add_def_adj(mod_new_continent))
		f.write('#大洋州\n')
		f.writelines(add_def_adj(mod_oceania))
		f.write('#アメリカ諸州\n')
		f.writelines(add_def_adj(mod_america))
