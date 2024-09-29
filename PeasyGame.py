print("Hi from PeasyGame!")
import sys
path = sys.argv[1]
modules = eval(sys.argv[2])
EasyGUI = ""
AIMode = ""
FastScan = ""
PeasyGame = ""
if "FastScan" in modules:
	FastScan = open("/media/alexey/FORSHCOOL/PeasyGame/Modules/EasyGUI.py", 'r').read()
if "EasyGUI" in modules:
	EasyGUI = open("/media/alexey/FORSHCOOL/PeasyGame/Modules/EasyGUI.py", 'r').read()
if "AIMode" in modules:
	AIMode = open("/media/alexey/FORSHCOOL/PeasyGame/Modules/AIMode.py", 'r').read()
PeasyGame = open("/media/alexey/FORSHCOOL/PeasyGame/Modules/PeasyGame.py", 'r').read()
with open(path, 'r') as file:
	code = FastScan + "\n" + EasyGUI + "\n" + AIMode + "\n" + file.read() + "\n" + PeasyGame
	try:
		exec(code)
	except KeyboardInterrupt as e:
		sys.exit()
	except SystemExit as e:
		""""""
	except BaseException as e:
		print("Someting went wrong:")
		print(e)