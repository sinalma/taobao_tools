# path/ : 所有操作进行的根目录
# csvname : 淘宝数据包图片名一列数据的csv文件名
# tbi/ ： 将要转换的图片文件夹，将所有图片放入此文件夹
# resPicP/ : 最终存放tbi图片的文件夹，和最终导入淘宝助理的csv同名文件夹

import csv
import pandas as pd
import os
import shutil

path = "C:/Users/sinalma/Desktop/"
csvname = "pic.csv"
tbiPn = "tbi/"
resPicP = "new/"


def transTbi(tbiPath):
	files = os.listdir(tbiPath)
	idx = 0
	print("--------------transform all picture to tbi.------------")
	for filename in files:
		idx += 1
		portion = os.path.splitext(filename)
		# print(portion)
		# if portion[1] ==".jpg" or portion[1] ==".png":
		# newname = portion[0]+".tbi"
		newname = '%s.tbi' %idx
		print(newname)
		os.chdir(tbiPath)
		os.rename(filename,newname)

def impPic(rootPath,csvPath,tbiPath):
	print("--------------import all picture to new(result) dir.------------")
	with open(csvPath, 'r',errors='ignore') as csvfile:
		reader = csv.reader(csvfile)
		column1 = [row for row in reader]
		picidx = 0
		totalPicN = countPicNum(tbiPath)
		for item in column1:
			picidx += 1
			# print(item)
			# 去图片名后缀
			if (len(item)):
				comps = item[0].split(":")
				print(comps)
				col = comps[0]
				print(col)
				print(col)
				# 复制图片修改图片名
				# alllist=os.listdir(u"C:/Users/sinalma/Desktop/")
				alllist=os.listdir(u"%s" %rootPath)
				if picidx >= totalPicN:
					picidx = 1
				oldname= u"C:/Users/sinalma/Desktop/tbi/"+str(picidx)+".tbi"
				newname= u"C:/Users/sinalma/Desktop/new/"+col+".tbi"
				shutil.copyfile(oldname,newname)

def countPicNum(tbiPath):
	print("--------------counting all tbi picture number.------------")
	filenum = 0
	dirnum = 0
	for lists in os.listdir(tbiPath):
		sub_path = os.path.join(path, lists)
		filenum += 1
		print(sub_path)
	return filenum


def clearPic(path):
	print("--------------clearing all result picture.------------")
	for i in os.listdir(path):
		path_file = os.path.join(path,i) 
		if os.path.isfile(path_file):
			print(path_file)
			os.remove(path_file)

clearPic('C:/Users/sinalma/Desktop/new/')
transTbi(path+tbiPn)
impPic(path,path+csvname,path+tbiPn)