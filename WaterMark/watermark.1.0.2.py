from PIL import Image, ImageDraw, ImageFont
import os
import sys


# describe (string , number,eg)
MARK = '柒柒工控 17717458762'
# all operation from this path , is root and nesscessary a directory
ROOT_PATH = 'C:/Users/sinalma/Desktop/pic/'
# want to rename string , wait make down
MODEL = ''
# thumbnail image size,(px,px)
THUMB_IMG_SIZE = (800,800)
# watermark model
# 'string,picture,sp_string'
WATERMARK_MODEL = "string"
MARK_STRING_SIZE = 50
MARK_COLOR = '#ff0000'


def cacl_str_len(value):
	length = len(value)
	utf8_length = len(value.encode('utf-8'))
	length = (utf8_length - length)/2 + length
	return length

# core method : add watermark
def add_watermark(path,mark):
	img = Image.open(path)
	draw = ImageDraw.Draw(img)
	myfont = ImageFont.truetype('C:/windows/fonts/simsun.ttc',size=MARK_STRING_SIZE)
	fillcolor = MARK_COLOR
	imgW,imgH = img.size
	strW,strH = myfont.getsize(MARK)
	x = (imgW-strW) / 2 
	y = (imgH-strH) / 2
	# paramer 1：position（x，y）；paramer：fill content；paramer 3：font；paramer：color
	draw.text((x, y),mark,font=myfont,fill=fillcolor)
	img.save(path)
	print('add_watermark->'+path+'---is success.')


# mark a watermark ,  according model
def make_watermark():
	pass


# fitter watermark to picture
def fitter_watermark():
	pass


# rename a file , according ___
def rename(path):
	filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表

	a = 0

	for i in filename_list:

		used_name = path + filename_list[a]
		a += 1

		# new_name = path + ('img%d'%i)+'.jpg'
		new_name = path + "img%d"%a+'.jpg'

		os.rename(used_name,new_name)

		print("rename->File %s rename success,new name is %s" %(used_name,new_name))




# thumbnail image , give a size(px,px)
# return a image 
def thumb_img(path,idx):
	image = Image.open(path)
	image.thumbnail((800,800),Image.ANTIALIAS)
	# image.transpose(Image.ROTATE_270)
	image.save(path)
	print('thumb_img->'+path+'---is success')
	# return image


# give a directory,counting this directory files number,return a number
# this method not container counting children directory
def counting_files(path):
	file_list = os.listdir(path)
	count = 0
	for i in file_list:
	    if os.path.isfile(os.path.join(path,i)):
	        count+=1
	print('all count is %d'%count)
	return count

def ll(path):
	
	img = Image.open(path)
	try:
		for orientation in ExifTags.TAGS.keys() : 
			if ExifTags.TAGS[orientation]=='Orientation' : break 
		exif=dict(img._getexif().items())
		if   exif[orientation] == 3 : 
			print('exif == 3')
			img=img.rotate(180, expand=True)
		elif exif[orientation] == 6 : 
			print('exif == 6')
			img=img.rotate(270, expand=True)
		elif exif[orientation] == 8 : 
			img=img.rotate(90, expand=True)
			print('exif == 8')
	except:
			print('exif == null')	


if __name__ == '__main__':
	# counting all pic number
	count = counting_files(ROOT_PATH)
	# cycle all pic 
	# rename
	rename(ROOT_PATH)
	# thumbnail iamge
	x = 1
	for i in range(x,count+1):
		print('Now is deal ( %d ) picture.'%i)
		img = thumb_img(ROOT_PATH+('img%d.jpg')%int(i),x)
		img = add_watermark(ROOT_PATH+('img%d.jpg')%int(i),MARK)
		x+=1
	