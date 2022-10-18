class Folder:
	def __init__ (self, name, path, parent = None):
		self.name = name
		self.path = path + name + "/"
		self.contents = []
		self.folders = []
		self.files = []
		self.parent = parent

	def __str__(self):
		return self.name + "/"

	def __lt__ (self, other):
		return self.name < other.name

class File:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name + ".file"

	def __lt__ (self, other):
		return self.name < other.name

def ls(folder):
	for f in folder.folders:
		print (f)
	for f in folder.files:
		print (f)

def mkdir (name, folder):
	for archive in folder.contents:
		if archive == name:
			print ("Selection already exists")
			return

	folder.contents.append(name)
	folder.folders.append(Folder(name, folder.path, folder))
	folder.folders.sort()


def touch (name, folder):
	for archive in folder.contents:
		if archive == name:
			print ("Selection already exists")
			return

	folder.contents.append(name)
	folder.files.append(File(name))
	folder.files.sort()

def cd (root, source, path):
	if path == "/":
		return root

	current = source
	if path[0] == "/":
		current = root
		path = path[1:]

	splitPath = path.split("/")

	for i in range(len(splitPath)):
		has_parent = False

		if splitPath[i] == ".." and current.parent != None:
			current = current.parent
			has_parent = True
		elif splitPath[i] == ".." and current.parent == None:
			current = root
			has_parent = True

		else:
			for x in current.folders:
				if splitPath[i] == x.name and isinstance(x, Folder):
					current = x
					has_parent = True
					break
 
		if has_parent == False:
			print ("No such file or directory")
			return source 

	return current