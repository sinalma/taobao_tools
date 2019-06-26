# @by sinalma 2018.12.14
# 1.0.0
# function transTbi : Will make all picture transform to tbi on path.
# function impPic : Import picture to path , according to csv number.
# function countPicNum : Counting file(picture) number.
# function clearPic : Clear all file(picture).
 

import csv
import pandas as pd
import os
import shutil

path = "C:/Users/sinalma/Desktop/"
csvname = "pic.csv"
tbiPn = "tbi/"
resPicP = "20181215_all_01/"


def transTbi():
	files = os.listdir(path+tbiPn)
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
		os.chdir(path+tbiPn)
		os.rename(filename,newname)

def impPic():
	print("--------------import all picture to new(result) dir.------------")
	with open(path+csvname, "r",) as csvfile:
		reader = csv.reader(csvfile)
		column1 = [row for row in reader]
		picidx = 0
		totalPicN = countPicNum()
		for item in column1:
			picidx += 1
			# print(item)
			# 去图片名后缀
			if (len(item)):
				comps = item[0].split(":")
				col = comps[0]
				print(col)
				# 复制图片修改图片名
				# alllist=os.listdir(u"C:/Users/sinalma/Desktop/")
				alllist=os.listdir(u"%s" %path)
				if picidx >= totalPicN:
					picidx = 1
				oldname= u"C:/Users/sinalma/Desktop/tbi/"+str(picidx)+".tbi"
				newname=u"C:/Users/sinalma/Desktop/20181215_all_01/"+col+".tbi"
				shutil.copyfile(oldname,newname)

def countPicNum():
	print("--------------counting all tbi picture number.------------")
	filenum = 0
	dirnum = 0
	for lists in os.listdir(path+tbiPn):
		sub_path = os.path.join(path, lists)
		filenum += 1
		print(sub_path)
		# if os.path.isfile(sub_path):
		# 	filenum += 1
		# elif os.path.isdir(sub_path):
		# 	dirnum += 1
	return filenum


def clearPic():
	print("--------------clearing all result picture.------------")
	path = 'C:/Users/sinalma/Desktop/20181215_all_01/'
	for i in os.listdir(path):
		path_file = os.path.join(path,i) 
		if os.path.isfile(path_file):
			print(path_file)
			os.remove(path_file)

clearPic()
transTbi()
impPic()