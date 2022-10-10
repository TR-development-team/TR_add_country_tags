import PySimpleGUI as sg
import re
import tag
import color
import history
import l_japanese
import cosmetic
import load_mod_list

class ModSelectWindow:
	def __init__(self):
		self.layout = [
			[sg.Text("作成Mod")],
			[sg.Combo(load_mod_list.mod_list(), default_value = "", readonly = True)],
			[sg.Button("決定")]
		]
		self.window = sg.Window("作成Mod", self.layout, finalize = True)
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				sg.Popup("終了")
				break
			if event == "決定":
				if (values[0] == ""):
					sg.Popup("実装するModを選択してください")
				else:
					self.window.close()
					self.mod_name = values[0].replace('\n', '')
					AddCountryWindow(self.mod_name).main()
		self.window.close()

class AddCountryWindow:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.layout = [
			[sg.Text(self.mod_name, size=(15, 1))],
			[sg.Text("タグ", size=(15, 1)), sg.InputText()],
			[sg.Text("和名", size = (15, 1)), sg.InputText()],
			[sg.Text("英名", size = (15, 1)), sg.InputText()],
			[sg.Text("文化", size = (15, 1))],
			[sg.Combo(["Asia", "Middle East", "Western Europe", "Eastern Europe", "Africa", "South America"], default_value = "", readonly = True)],
			[sg.Text("大州", size = (15, 1))],
			[sg.Combo(["アジア", "ヨーロッパ", "アフリカ", "新大陸", "大洋州", "アメリカ諸州"], default_value="", readonly = True)],
			[sg.Text("色", size = (15, 1)), sg.InputText()],
			[sg.Text("首都", size=(15, 1)), sg.InputText()],
			[sg.Text("政体英名", size=(15, 1)), sg.InputText()],
			[sg.Text("正式名称", size=(15, 1)), sg.InputText()],
			[sg.Submit(button_text="実行")],
			[sg.Submit(button_text="政体名付き国名生成")]
		]
		self.window = sg.Window("国家タグ追加", self.layout, finalize = True)
	
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				break
			if event == "実行":
				i = 0
				if re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$").search(values[5]):
					hex = values[5].lstrip("#")
					rgb_color = [int(hex[i:i+2], 16) for i in (0, 2, 4)]
					add_color = ("{} {} {}".format(rgb_color[0], rgb_color[1], rgb_color[2]))
					if color.check_color(self.mod_name, add_color):
						sg.Popup("重複した色が存在している")
						i += 1
				else:
					i += 1
					sg.Popup("HEX以外の数値が入力されている")
				if (len(values[0]) != 3):
					i += 1
					sg.Popup("タグが三文字でない")
				if (values[1] == "") or (values[2] == "") or (values[3] == "") or (values[4] == "") or (values[5] == ""):
					i += 1
					sg.Popup("空欄が存在する")
				if re.compile("\D+").search(values[6]):
					i += 1
					sg.Popup("数字以外入力されている")
				if tag.check_tag(self.mod_name, values[0]):
					i += 1
					sg.Popup("重複したタグが存在している")
				if (i == 0):
					tag.edit_country_tags(self.mod_name, values[0], values[1], values[3])
					color.edit_color(self.mod_name, values[0], values[1], values[4], add_color)
					history.edit_history(self.mod_name, values[0], values[2], values[6])
					l_japanese.add_loc(self.mod_name, values[0], values[1], values[4])
					sg.Popup("国家タグ生成")
				print(i)
			if event == "政体名付き国名生成":
				i = 0
				if (len(values[0]) != 3):
					i += 1
					sg.Popup("タグが三文字でない")
				if (values[4] == "") or (values[7] == "") or (values[8] == ""):
					i += 1
					sg.Popup("空欄が存在する")
				if (i == 0):
					sg.Popup("コズメティックタグ生成")
					cosmetic.add_long_name(self.mod_name, values[0], values[8], values[4], values[7])
		self.window.close()

if __name__ == "__main__":
	ModSelectWindow().main()
