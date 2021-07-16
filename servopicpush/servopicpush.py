import os
import os.path
import shutil
from pathlib import Path
from enum import Enum, unique
from brand import brand


PATH = "C:\\Users\\sinalma\\Desktop\\dsvpps" # 需要转移存放的图片文件夹
SAVE_PATH = "C:\\Users\\sinalma\\Desktop\\svpps" # 图片最终存放的第一层级文件夹
# file_list = os.listdir(PATH)  # 打开对应的文件夹
name_list = os.listdir(PATH)#所有需要归类的图片的文件名数组
total_num = len(name_list)  #得到文件夹中需要归类的图像的个数
tmp_folder = os.getcwd() + "\\tmpSvp\\" # l临时存放进程中处理的图片和对应文件夹的总文件夹


#品牌枚举
class ServoBrand(Enum):
	S = 'YASKAWA'
	G = 'Fuji'
	RY = 'Fuji'
	M = 'PANASONIC'
	R = 'OMRON'
	MR = 'Mitsubishi'
	H = 'Mitsubishi'
	V = 'SIHMPO'


#处理当前图片所属型号，归类到文件夹
def deal_model_file_folder(pic_name):
	#获取型号
	model = pic_name.split("_")[0]	
	#临时文件夹中存放相同型号的图片
	model_path = Path(tmp_folder + model)
	#如果当前型号文件夹存在临时文件夹中
	if model_path.is_dir():
		#将图片剪切到临时文件夹中
		#判断将要移动的文件是否存在相同的文件名
		tmp_file_path = Path(str(model_path)+ "\\" + pic_name)
		if tmp_file_path.exists():
			print("当前图片（"+pic_name+"）已存在队列中,系统将删除当前重复的图片")
			os.remove(tmp_file_path)
		else:
			shutil.move(PATH+"\\"+pic_name, str(model_path)+"\\")
	else:
		print("bucunzai")
		#创建对应型号的文件夹保存到临时文件夹中
		os.makedirs(model_path)
		deal_model_file_folder(pic_name)


#分析图片名
def analyse_servo_brand(model):
	#读取文件名第一位字母
	first_n = model[0:1]
	#在品牌类枚举中没有特定值时 进入此判断
	if first_n == 'R':
		if model[0:2] == 'RY':
			first_n = model[0:2]
	brang = ServoBrand[first_n]
	return brang.value


#最终文件处理方法
def deal_file_down():

	floders = os.listdir(tmp_folder)
	nums = len(floders)
	#遍历临时文件夹中所有型号文件夹
	for i in range(nums):
		model = floders[i]
		#分析和移动文件夹
		#根据品牌将图片归类到最终文件夹
		dict = analyse_servo_model(model)
		createAndSavePicDir(dict)


#型号分析
def analyse_servo_model(model):
	#获得当前型号的品牌
	brand1 = analyse_servo_brand(model)
	# print(brand1)
	b = brand(model)
	dict = []
	if brand1 == 'YASKAWA':
		dict = b.YASKAWA()
	elif brand1 == 'Fuji':
		dict = b.FUJI()
	elif brand1 == 'OMRON':
		dict = b.ORMON()
	elif brand1 == 'PANASONIC':
		dict = b.PANASONIC()
	return dict
	

# 在已获得需要的文件夹名称后 则创建文件夹和归类相应的图片
def createAndSavePicDir(dict):
	topDir = SAVE_PATH + '\\'
	if dict:
		# 创建数组中相应的文件夹
		# 如果遇到已存在的文件夹 则将图片直接存放
		# 直到最终层级
		# 首先，检查第一个文件夹名称是否存在，以此类推
		num = 0
		totalNum = len(dict)
		for x in dict:
			print(x)
			num += 1
			topDir += x+'\\'
			topDirPath = Path(topDir)
			if topDirPath.exists():
				# print('指定文件夹已存在')
				pass
			else:
				os.makedirs(topDir)
				#如果当前创建的是最后一层型号文件夹 则将图片放入此文件夹

			#当前正在处理文件名数组中最后一个 型号 文件夹名
			#将要把临时文件夹相同型号目录名中的图片移动到最终文件夹中
			if totalNum == num:
				num = 0
				#遍历临时文件夹中所有当前型号的图片
				for y in os.listdir(tmp_folder+x):
					scrPicPath = os.path.join(tmp_folder+x,y)
					tmpF = topDir + '\\' + y
					#当前处理的相同图片名的同名图片存在 
					if os.path.exists(tmpF):
						#则删除临时文件夹中相同图片名的图片
						os.remove(tmp_folder+x+'\\'+y)
						continue
					else:
						#否则整合图片路径 准备移动到最终文件夹中
						destPicPath = os.path.join(topDir)
					#移动当前处理的图片
					shutil.move(scrPicPath,destPicPath)
				#当前型号文件夹下图片全部移动后 删除临时文件夹中临时型号文件夹
				os.rmdir(tmp_folder+x)
	else:
		print('文件列表为空')




if __name__ == '__main__':
	#遍历需要处理图片所在的文件夹
	for i in range(total_num):
		#读取当前图片文件名os.path.splitext
		pic_name = name_list[i]
		#创建当前图片所属型号
		deal_model_file_folder(pic_name)
	#在归类所有需要的图片至型号文件夹中
	#处理最后一步 将所有图片移动到最终文件夹中
	deal_file_down()



