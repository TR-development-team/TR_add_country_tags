def check_tag(tag):
	f = open('./hoi4/common/country_tags/_geacps_defalt_countries.txt', 'r', encoding='UTF-8')
	all_tags = f.readlines()
	f.close()
	f = open('./hoi4/common/country_tags/zzz_default_countries.txt', 'r', encoding='UTF-8')
	all_tags.extend(f.readlines())
	f.close()
	f = open('./hoi4/common/country_tags/zzz_dynamic_countries.txt', 'r', encoding='UTF-8')
	all_tags.extend(f.readlines())
	f.close()
	for i in all_tags:
		if(tag in i):
			return True
	return False

def edit_country_tags(tag, ja_name, culture):
	f = open('./hoi4/common/country_tags/_geacps_defalt_countries.txt', 'r', encoding='UTF-8')

	all_tags = f.readlines()

	f.close()
	
	add_tags = '{}	= "countries/{}.txt"	#{}\n'.format(tag, culture, ja_name)
	all_tags.append(add_tags)

	asia_tags = [i for i in all_tags if 'Asia.txt' in i]
	middle_east_tags = [i for i in all_tags if 'Middle East.txt' in i]
	commonwealth_tags = [i for i in all_tags if 'Commonwealth.txt' in i]
	western_europe_tags = [i for i in all_tags if 'Western Europe.txt' in i]
	eastern_europe_tags = [i for i in all_tags if 'Eastern Europe.txt' in i]
	africa_tags = [i for i in all_tags if 'Africa.txt' in i]
	south_america_tags = [i for i in all_tags if 'South America.txt' in i]


	asia_tags.sort()
	middle_east_tags.sort()
	commonwealth_tags.sort()
	western_europe_tags.sort()
	eastern_europe_tags.sort()
	africa_tags.sort()
	south_america_tags.sort()

	f = open('./hoi4/common/country_tags/_geacps_defalt_countries.txt', 'w', encoding='UTF-8')
	f.write('#アジア\n')
	f.writelines(asia_tags)
	f.write('\n')
	f.write('#中東\n')
	f.writelines(middle_east_tags)
	f.write('\n')
	f.write('#英連邦\n')
	f.writelines(commonwealth_tags)
	f.write('\n')
	f.write('#西欧\n')
	f.writelines(western_europe_tags)
	f.write('\n')
	f.write('#東欧\n')
	f.writelines(eastern_europe_tags)
	f.write('\n')
	f.write('#アフリカ\n')
	f.writelines(africa_tags)
	f.write('\n')
	f.write('#南米\n')
	f.writelines(south_america_tags)

	f.close()