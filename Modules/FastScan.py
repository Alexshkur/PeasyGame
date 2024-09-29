def Find(Search, In):
	if type(Search) == list:
		for find in Search:
			if In.find(find) != -1:
				return True
	elif type(Search) == str:
		if In.find(Search) != -1:
			return True
		else: return False
	else: raise IncorrectType(f"Incorrect type {type(Search)} in Find({type(Search)}, {In})")
def checkDir(dir):
	Dir = os.scandir(dir)
	for entry in Dir:
		#Cosmetics
		if entry.path.find(f"/home/{os.environ.get("USERNAME")}") != -1:
			path = entry.path.replace(f"/home/{os.environ.get("USERNAME")}", '~')
		else:
			path = entry.path.replace(Directory, '/')
		#Check if it's a direcrory
		if os.path.isdir(entry.path): #Code if it's a directory
			if Find(IgnoreDir, path) == False:
				if FindFile != "":
					if Find(FindFile, path): print(path)
				Scandir(entry.path)
		else: #Code if it's a file
			if FindFile != "":
				if Find(FindFile, entry.name):
					print(path)
			else: print(path)
def scan(Dir, find="", igndir=""):
	checkDir(Dir)
	if Directory[len(Directory) - 1:len(Directory)] != "/":
		Directory += "/"
	if FFile[:1] == "[":
		FindFile = eval(FFile)
	else: FindFile = FFile
	if IDir[:1] == "[":
		IgnoreDir = eval(IDir)
	else: IgnoreDir = IDir