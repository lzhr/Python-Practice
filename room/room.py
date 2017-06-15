import types
import urllib.request, urllib.error, urllib.parse
import json
import threading
import time
import sys
import getopt
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def registerUrl(room_id):
	try:
		url ="http://open.douyucdn.cn/api/RoomApi/Room/"+room_id
		res220149 = urllib.request.urlopen(url).read()
		#print(type(res220149))
		return res220149
	except Exception as e:
		print(e)
		
def jsonFile(fileData):
	file = open("Room.json","w")
	file.write(fileData.decode('utf-8'))
	file.close()

def readFile():
	file = open("Room.json",encoding='utf-8')
	try:
		jsonf = file.read()
		return jsonf
	finally:
		file.close()

def praserJsonFile(jsonData,count):
	value = json.loads(jsonData)
	#print(type(value))
	#print(type(value['data']['room_status']))
	da = value['data']
	nickname = da['owner_name']
	status = da['room_status']
	start_time = da['start_time']
	online = da['online']
	#room_name = da['room_name']
	print('查询次数：',count)
	
	if status == '1' :
		print(nickname,'正在直播ing')
		#print('房间名称：',room_name)
		print('人气值：',online)
	else:
		print('主播 ',nickname,'不在直播')
		#print('房间名称：',room_name)
		print('上次开播时间：',start_time)
	count += 1
	return count
		
#def alert(message):
	#json.loads(res)

def fun_timer(im,room_id):
	jsonFile(registerUrl(room_id))
	jsonf = readFile()
	i = praserJsonFile(jsonf,im)
	print('本地时间:',time.strftime("%Y-%m-%d %X"))
	global timer
	timer = threading.Timer(10,fun_timer,[i,room_id])
	timer.start()

	
if __name__ == "__main__":
	room_id = '220149'
	print('输入的房间ID：')
	if len(sys.argv) == 2 :
		print(sys.argv[1])
		room_id = sys.argv[1]
	else :
		print(room_id)
	# inputid = ''
	# try:
		# opts,args = getopt.getopt(argv,"")
	i = 1
	timer = threading.Timer(1,fun_timer,[i,room_id])
	timer.start()
 