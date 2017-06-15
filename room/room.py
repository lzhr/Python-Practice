import types
import urllib.request, urllib.error, urllib.parse
import json
import gzip 
import struct

def registerUrl():
	try:
		url ="http://open.douyucdn.cn/api/RoomApi/Room/220149"
		res220149 = urllib.request.urlopen(url).read()
		print(type(res220149))
		#res = gzip.decompress(res220149)
		#return res
		return res220149
	except Exception as e:
		print(e)
		
def jsonFile(fileData):
	file = open("D:\WorkSpace\Python\json.txt","w")
	file.write(fileData)
	file.close()

def praserJsonFile(jsonData):
	value = json.loads(jsonData)
	rootlist = list(value.keys())
	print(rootlist)
	for rootkey in rootlist:
		print(rootkey)
	subvalue = value[rootkey]
	print(subvalue)
	for subkey in subvalue:
		print(subkey,subvalue[subkey])
		
def alert(message):
	json.loads(res)

if __name__ == "__main__":
	res = registerUrl()
	print(res)
	
	praserJsonFile(data)
	
	