import PySimpleGUI as sg
import re
import database
import edit

class ModSelectWindow:
	def __init__(self):
		self.layout = [
			[sg.Text("作成Mod")],
			[sg.Combo(database.mod_list(), key="mod_name", readonly=True)],
			[sg.Button("決定")],
			[sg.Button("新規作成")]
		]
		self.window = sg.Window("作成Mod", self.layout, finalize = True)
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				sg.Popup("終了")
				break
			if event == "新規作成":
				self.window.close()
				NewModWindow().main()
			if event == "決定":
				if (values["mod_name"] == ""):
					sg.Popup("実装するModを選択してください")
				else:
					self.window.close()
					self.mod_name = values["mod_name"].replace('\n', '')
					AddCountryWindow(self.mod_name).main()
					
		self.window.close()

class NewModWindow:
	def __init__(self):
		self.layout = [
			[sg.Text("略称", size=(15, 1)), sg.InputText()],
			[sg.Text("イデオロギーID", size=(15, 1)), sg.InputText()],
			[sg.Button("決定")]
		]
		self.window = sg.Window("新規MOD", self.layout, finalize=True)

	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				break
			if event == "決定":
				if (values["tag"] == ""):
					sg.Popup("MODの略称を入力してください")
				if (values["japanese"] == ""):
					sg.Popup("デフォルトとなるイデオロギーIDを入力してください")
				else:
					self.window.close()
					ModSelectWindow().main()

class AddCountryWindow:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.layout1 = [
			[sg.Text("和名", size=(7, 1)), sg.InputText(key="japanese")],
			[sg.Text("英名", size=(7, 1)), sg.InputText(key="english")],
			[sg.Text("文化", size = (7, 1)), sg.Combo(["Asia", "Middle East", "Western Europe", "Eastern Europe", "Africa", "South America"], key = "culture", readonly = True)],
			[sg.Text("大州", size = (7, 1)), sg.Combo(["アジア", "ヨーロッパ", "アフリカ", "新大陸", "大洋州", "アメリカ諸州"], key="continent", readonly = True)],
			[sg.Text("色", size = (7, 1)), sg.InputText(default_text='#', key="color")],
			[sg.Text("首都", size=(7, 1)), sg.InputText(key="capital")],
			# [sg.Text("政体英名", size=(7, 1)), sg.InputText(default_text='republic', key="form")],
			# [sg.Text("正式名称", size=(7, 1)), sg.InputText(size=(10, 1)), sg.InputText(default_text ='共和国', size=(10, 1))],
			[sg.Submit(button_text="タグ追加")],
		]
		self.layout2 = [
			[sg.Text("政体英名", size=(7, 1)), sg.InputText(default_text='republic', key="form")],
			[sg.Text("正式名称", size=(7, 1)), sg.InputText(size=(10, 1), key="prefix"), sg.InputText(default_text ='共和国', size=(10, 1), key="suffix")],
			[sg.Submit(button_text="政体名付き国名生成")]
		]
		self.layout0 = [
			[sg.Text(self.mod_name, size=(10, 1))],
			[sg.Text("タグ", size=(7, 1)), sg.InputText(size=(4, 1), key="tag")],
			[sg.TabGroup([[sg.Tab('国家タグ追加', self.layout1), sg.Tab('正式名称追加', self.layout2)]])]
		]
		self.window = sg.Window("国家タグ追加", self.layout0, finalize=True)
	
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				break
			if event == "タグ追加":
				i = 0
				if re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$").search(values["color"]):
					hex = values["color"].lstrip("#")
					self.rgb_color = [int(hex[i:i+2], 16) for i in (0, 2, 4)]
					self.add_color = ("{} {} {}".format(self.rgb_color[0], self.rgb_color[1], self.rgb_color[2]))
					if database.check_value(self.mod_name, "countries", "color", self.add_color) == True:
						sg.Popup("重複した色が存在している")
						i += 1
				else:
					i += 1
					sg.Popup("HEX以外の数値が入力されている")
				if (len(values["tag"]) != 3):
					i += 1
					sg.Popup("タグが三文字でない")
				if (values["japanese"] == "") or (values["english"] == "") or (values["culture"] == "") or (values["continent"] == "") or (values["color"] == ""):
					i += 1
					sg.Popup("空欄が存在する")
				if re.compile("\D+").search(values["capital"]):
					i += 1
					sg.Popup("数字以外入力されている")
				if database.check_value(self.mod_name, "countries", "tag", values["tag"]) == True:
					i += 1
					sg.Popup("重複したタグが存在している")
				if (i == 0):
					self.add_list = {"tag": values["tag"], "japanese": values["japanese"], "color": self.add_color, "culture": values["culture"], "continent": values["continent"], "type": "追加国家"}
					database.csv_edit(self.mod_name, "countries", self.add_list)
					edit.add_country(self.mod_name)
					edit.add_history(self.mod_name, values["tag"], values["english"], values["capital"])
					sg.Popup("国家タグ生成")
				print(i)
			if event == "政体名付き国名生成":
				i = 0
				if (len(values["tag"]) != 3):
					i += 1
					sg.Popup("タグが三文字でない")
				if (values["tag"] == ""):
					i += 1
					sg.Popup("タグが空欄である")
				else:
					if not database.check_value(self.mod_name, "countries", "tag", values["tag"]) == True:
						i += 1
						sg.Popup("タグが存在しない")
				if (values["form"] == "") or ((values["prefix"] == "") and (values["suffix"] == "")):
					i += 1
					sg.Popup("空欄が存在する")
				if (i == 0):
					self.add_list = {"tag": values["tag"], "form": values["form"], "prefix": values["prefix"], "suffix": values["suffix"]}
					database.csv_edit(self.mod_name, "cosmetic", self.add_list)
					edit.CountryLongNames(self.mod_name).main()
					sg.Popup("コズメティックタグ生成")
		self.window.close()

if __name__ == "__main__":
	ModSelectWindow().main()
