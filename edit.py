import database

class CountryTags:	#国家タグ
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.country_data = database.csv_open(mod_name, "countries")
		self.culture_list = ["Asia", "Middle East", "Commonwealth", "Western Europe", "Eastern Europe", "Africa", "South America"]
	
	def select_file(self, type):
		if type == "バニラ":
			return open('./{0}/common/country_tags/zzz_defalt_countries.txt'.format(self.mod_name), 'w', encoding = 'UTF-8')
		elif type == "追加国家":
			return open('./{0}/common/country_tags/{0}_defalt_countries.txt'.format(self.mod_name), 'w', encoding='UTF-8')
		elif type == "動的国家":
			return open('./{0}/common/country_tags/zzz_dynamic_countries.txt'.format(self.mod_name), 'w', encoding='UTF-8')
	
	def add_tag(self, type):
		self.file = self.select_file(type)
		tmp = 0
		for self.culture in self.culture_list:
			if tmp == 0:	self.file.write("\n")
			self.list = database.csv_filter_sort(database.csv_filter(self.country_data, "type", type), "culture", self.culture, "tag")
			self.file.write('#{}\n'.format(self.culture))
			for t in self.list:
				self.file.write('{}	= "countries/{}.txt"	#{}\n'.format(t["tag"], self.culture, t["japanese"]))
			tmp += 1
	
	def main(self):
		self.add_tag("追加国家")

class CountryColors:	#国家カラー
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.country_data = database.csv_open(mod_name, "countries")
		self.type_list = ["バニラ", "追加国家"]
		self.continent_list = ["アジア", "ヨーロッパ", "アフリカ", "新大陸", "大洋州", "アメリカ諸州"]

	def set_country_color(self, list_name):
		for t in list_name:
			self.file.write('{} = '.format(t["tag"]))
			self.file.write('{')
			self.file.write('	#{}\n'.format(t["japanese"]))
			self.file.write('	color = rgb { ')
			self.file.write(t["color"])
			self.file.write(' }\n')
			self.file.write('	color_ui = rgb { ')
			self.file.write(t["color"])
			self.file.write(' }\n}\n')

	def add_country_color(self):
		self.file = open('./{0}/common/countries/colors.txt'.format(self.mod_name), 'w', encoding='UTF-8')
		for self.type in self.type_list:
			self.file.write('##{}\n'.format(self.type))
			for self.continent in self.continent_list:
				self.list = database.csv_filter_sort(database.csv_filter(
					self.country_data, "type", self.type), "continent", self.continent, "tag")
				self.file.write('#{}\n'.format(self.continent))
				self.set_country_color(self.list)
		self.file.write('##動的国家\n')
		self.dynamic_country = database.csv_filter_sort(
			self.country_data, "type", "動的国家", "tag")
		self.set_country_color(self.dynamic_country)

	def main(self):
		self.add_country_color()

class CountryNames:	#国名
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.country_data = database.csv_open(mod_name, "countries")
		self.type_list = ["バニラ", "追加国家"]
		self.continent_list = ["アジア", "ヨーロッパ", "アフリカ", "新大陸", "大洋州", "アメリカ諸州"]
	
	def add_country_name(self):
		self.file = open('./{0}/localisation/japanese/map/{0}_countries_l_japanese.yml'.format(self.mod_name), 'w', encoding = 'UTF-8-sig')
		self.file.write("l_japanese:\n")
		for self.type in self.type_list:
			self.file.write('##{}\n'.format(self.type))
			for self.continent in self.continent_list:
				self.list = database.csv_filter_sort(database.csv_filter(self.country_data, "type", self.type), "continent", self.continent, "tag")
				self.file.write('#{}\n'.format(self.continent))
				for t in self.list:
					self.file.write(' {}:0 "{}"\n'.format(t["tag"], t["japanese"]))
					self.file.write(' {}_DEF:0 "{}"\n'.format(t["tag"], t["japanese"]))
					self.file.write(' {}_ADJ:0 "{}"\n \n'.format(t["tag"], t["japanese"]))
	
	def main(self):
		self.add_country_name()


class CountryLongNames:  # 国名
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.country_data = database.csv_open(mod_name, "countries")
		self.cosmetic_data = database.csv_open(mod_name, "cosmetic")
		self.type_list = ["バニラ", "追加国家"]
		self.continent_list = ["アジア", "ヨーロッパ", "アフリカ", "新大陸", "大洋州", "アメリカ諸州"]

	def add_country_long_name(self):
		self.file = open('./{0}/localisation/japanese/map/{0}_countries_long_l_japanese.yml'.format(self.mod_name), 'w', encoding='UTF-8-sig')
		self.file.write("l_japanese:\n")
		for self.type in self.type_list:
			self.file.write('##{}\n'.format(self.type))
			for self.continent in self.continent_list:
				self.country_list = database.csv_filter_sort(database.csv_filter(self.country_data, "type", self.type), "continent", self.continent, "tag")
				self.file.write('#{}\n'.format(self.continent))
				i = 0
				for country in self.country_list:
					cosmetic_list = list(filter(lambda item: item["tag"] == country["tag"], self.cosmetic_data))
					for cosmetic in database.csv_sort(cosmetic_list, "form"):
						self.file.write(' {0}_{1}:0 "{2}{3}{4}"\n'.format(country["tag"], cosmetic["form"], cosmetic["prefix"], country["japanese"], cosmetic["suffix"]))
						self.file.write(' {0}_{1}_DEF:0 "{2}{3}{4}"\n'.format(country["tag"], cosmetic["form"], cosmetic["prefix"], country["japanese"], cosmetic["suffix"]))
					self.file.write(" \n")
	def main(self):
		self.add_country_long_name()

def add_history(mod, tag, en_name, capital):
	f = open('./{}/history/countries/{} - {}.txt'.format(mod, tag, en_name), 'w', encoding = 'UTF-8')
	f.write('capital = {}\nset_dictatorship = yes'.format(capital))
	f.close()

def add_country(mod_name):
	CountryTags(mod_name).main()
	CountryColors(mod_name).main()
	CountryNames(mod_name).main()
	CountryLongNames(mod_name).main()
