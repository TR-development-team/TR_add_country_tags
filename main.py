import PySimpleGUI as sg
import re
import tag
import color
import history
import loc
import cosmetic

layout = [
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
	[sg.Submit(button_text="cosmetic")]
]

window = sg.Window("国家タグ追加", layout)

while True:
	event, values = window.read()
	if event is None:
		print("exit")
		break
	if event == "実行":
		i = 0
		if re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$").search(values[5]):
			hex = values[5].lstrip("#")
			rgb_color = [int(hex[i:i+2], 16) for i in (0, 2, 4)]
			add_color = ("{} {} {}".format(rgb_color[0], rgb_color[1], rgb_color[2]))
			if color.check_color(add_color):
				print("重複した色が存在している")
				i += 1
		else:
			i += 1
			print("HEX以外の数値が入力されている")
		if (len(values[0]) != 3):
			i += 1
			print("タグが三文字でない")
		if (values[1] == "") or (values[2] == "") or (values[3] == "") or (values[4] == "") or (values[5] == ""):
			i += 1
			print("空欄が存在する")
		if re.compile("\D+").search(values[6]):
			i += 1
			print("数字以外入力されている")
		if tag.check_tag(values[0]):
			i += 1
			print("重複したタグが存在している")
		if (i == 0):
			print("国家タグ生成")
			tag.edit_country_tags(values[0], values[1], values[3])
			color.edit_color(values[0], values[1], values[4], add_color)
			history.edit_history(values[0], values[2], values[6])
			loc.add_loc(values[0], values[1], values[4])
		print(i)
	if event == "政体名付き国名生成":
		i = 0
		if (len(values[0]) != 3):
			i += 1
			print("タグが三文字でない")
		if (values[4] == "") or (values[7] == "") or (values[8] == ""):
			i += 1
			print("空欄が存在する")
		if (i == 0):
			print("実行")
			cosmetic.add_long_name(values[0], values[8], values[4], values[7])
window.close()
