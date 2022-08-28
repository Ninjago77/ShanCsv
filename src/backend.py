from ShanCsvExceptions import ShanCsvError,ShanCsvIndexError,ShanCsvNotImplemented
from io import UnsupportedOperation

def isPyInt(s):
	try: 
		int(s)
		return True
	except Exception as e:
		return False

def isPyFloat(s):
	try: 
		float(s)
		return True
	except Exception as e:
		return False

class Csv():
	def __init__(self,inputObj,inputTypeStr=True,itemSplitter=",",lineSplitter="\n",boolValue=True,noneValue=True,floatValue=True,intValue=True,customTrueValue=("true","yes","y"),customFalseValue=("false","no","n"),customNoneValue=("none","null","")):
		self.itemSplitter,self.lineSplitter = itemSplitter,lineSplitter
		if inputTypeStr:
			if (type(inputObj)==str):
				li_ = []
				for j in [i.split(self.itemSplitter) for i in inputObj.split(self.lineSplitter)]:
					li_.append([])
					if j != [""]:
						for k2 in j:
							k = k2.lower().strip()
							if (k in customTrueValue) and boolValue:
								li_[-1].append(True)
							elif (k in customFalseValue) and boolValue:
								li_[-1].append(False)
							elif (k in customNoneValue) and noneValue:
								li_[-1].append(None)
							elif isPyInt(k) and intValue:
								li_[-1].append(int(k))
							elif isPyFloat(k) and floatValue:
								li_[-1].append(float(k))
							else:
								li_[-1].append(str(k.strip()))
				if (li_ != [[]]) and (li_ != []):
					while li_[-1] == []: _ = li_.pop()
					while li_[0] == []: _ = li_.pop(0)
				self.__main = li_
			else:
				raise ShanCsvError(r"{inputObj} is not [str], triggered by {inputTypeStr=True}")
		else:
			try:
				self.__main = [[j for j in list(i)] for i in list(inputObj)]
			except:
				raise ShanCsvError(r"{inputObj} cannot convert to [list], triggered by {inputTypeStr=False}")
	def __str__(self):
		return self.lineSplitter.join([self.itemSplitter.join([str(j) for j in i]) for i in self.__main])
	def __len__(self):
		return len(self.__main)
	def __getitem__(self,key):
		try:
			return self.__main[key]
		except IndexError:
			raise ShanCsvIndexError("Invalid key")
	def __setitem__(self,key,value):
		try: 
			self.__main[key] = list(value)
		except TypeError:
				raise ShanCsvError(r"{value} cannot convert to [list]")
		except IndexError:
				raise ShanCsvIndexError(r"{key} cannot assign to {value}")
	def __delitem__(self,key):
		try:
			del self.__main[key]
		except IndexError:
				raise ShanCsvIndexError(r"{key} cannot be deleted")
	def __reversed__(self):
		raise ShanCsvNotImplemented(r"{reversed} not implemented")
	def __repr__(self):
		raise ShanCsvNotImplemented(r"{repr} not implemented")
	def getList(self):
		return list(self.__main)
	def getTuple(self):
		return tuple((tuple(i) for i in self.__main))

def loads(data,getType=list,**kwargs):
	if getType == list:
		return Csv(data,**kwargs).getList()
	elif getType == tuple:
		return Csv(data,**kwargs).getTuple()
	elif getType == str:
		return str(Csv(data,**kwargs))
	else:
		raise ShanCsvNotImplemented(r"{getType} not implemented")

def dumps(data,**kwargs):
	return str(Csv(data,inputTypeStr=False,**kwargs))

def load(file,**kwargs):
	try:
		return loads(file.read(),**kwargs)
	except UnsupportedOperation as e:
		raise ShanCsvError(r"{file} not readable")
def dump(data,file,**kwargs):
	try:
		return file.write(dumps(data,**kwargs))
	except UnsupportedOperation as e:
		raise ShanCsvError(r"{file} not writable")