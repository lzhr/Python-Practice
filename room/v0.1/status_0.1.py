import urllib.request, urllib.error, urllib.parse
import json
import threading
import time
import sys
import winsound

global room_id
global filename
global timer
global iel

def registerUrl():
	try:
		url ="http://open.douyucdn.cn/api/RoomApi/Room/"+room_id
		res220149 = urllib.request.urlopen(url).read()
		return res220149
	except Exception as e:
		print(e)
		
def jsonFile(fileData):
	file = open(filename,'w')
	file.write(fileData.decode('utf-8'))
	file.close()
	
def readFile():
	file = open(filename,encoding='utf-8')
	try:
		jsonf = file.read()
		return jsonf
	finally:
		file.close()
		
def praserJsonFile(jsonData,count):
	value = json.loads(jsonData)
	da = value['data']
	nickname = da['owner_name']
	status = da['room_status']
	start_time = da['start_time']
	online = da['online']
	print('查询次数:',count)
	if status == '1' :
		print(nickname,'正在直播ing')
		winsound.PlaySound("start.wav", winsound.SND_FILENAME)
		print('人气值：',online)
	else:
		print('主播 ',nickname,'不在直播')
		print('上次开播时间：',start_time)
	count += 1
	return count
	
def fun_timer(im):
	jsonFile(registerUrl())
	jsonf = readFile()
	i = praserJsonFile(jsonf,im)
	print('本地时间:',time.strftime("%Y-%m-%d %X"))
	timer = threading.Timer(iel,fun_timer,[i])
	timer.start()
	
if __name__ == "__main__":
	room_id = '220149'
	iel = 30
	print('输入的房间ID：')
	if len(sys.argv) == 2 :
		print(sys.argv[1])
		room_id = sys.argv[1]
	else :
		if len(sys.argv) == 3 :
			print(sys.argv[1])
			room_id = sys.argv[1]
			iel = int(sys.argv[2])
		else :
			print(room_id)
	filename ='Room'+room_id+'.json'
	i = 1
	timer = threading.Timer(1,fun_timer,[i])
	timer.start()
 