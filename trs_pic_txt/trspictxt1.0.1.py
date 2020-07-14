from PIL import Image, ImageDraw, ImageFont
import os
import random
import re
# 20200715   pip install pyerclip
# 20200715   python -m pip install --upgrade pip
import pyperclip
import time

shopName = '阳明工控'
phone = '18124988815'
# 楷体
fontPathS1 = './1.ttf'
# 汇文筑地五号明朝体
fontPathS2 = './2.otf'
# load font and set font size
fontS1 = ImageFont.truetype('./1.ttf', 80)
fontS2 = ImageFont.truetype('./2.otf', 60)
# reset image size
imgW = 800
imgH = 800
# value 
RED = '#FF0000'
IsFanWM = True



def add_text_to_image(image, text):

    # ADD BACKGROUND
    new_img = Image.new('RGBA', (image.size[0] * 9, image.size[1] * 9), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # ADD WATER MARK
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    

    for i in range(0, rgba_image.size[0], font_len*40+250):
        for j in range(0, rgba_image.size[1], 200):
            image_draw.text((i, j), text, font=fontS1, fill=(0, 0, 0, 100))
            image_draw.text((i, j+105), phone, font=fontS2, fill=(0, 0, 0, 100))
    
    # text_overlay = text_overlay.transform((200, 200), Image.EXTENT, (0, 0, 300, 0))
    
    text_overlay = text_overlay.rotate(random.randint(4,70)*-5)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)
    
    # CROP IMAGE
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text


def add_text_to_image2(path):
    text_width,text_height = fontS1.getsize(shopName)
    phone_width,phone_height = fontS1.getsize(phone)
    canvas = Image.open(path)
    canvas = canvas.resize((imgW,imgH))
    draw = ImageDraw.Draw(canvas)
    textX = (imgW - text_width) / 2
    textY = (imgH - text_height) / 2 
    phoneX = (imgW - phone_width) / 2
    draw.text((textX,textY),shopName,font=fontS1,fill=RED)
    draw.text((phoneX,textY+20+text_height),phone,font=fontS1,fill=RED)
    return canvas

# counting files 
def counting_files(path):
    file_list = os.listdir(path)
    count = 0
    for i in file_list:
        if os.path.isfile(os.path.join(path,i)):
            count+=1
    print('all count is %d'%count)
    return count


allFiles = []
# get all files on add water path
def getALLFiles(path):
    for root,dirs,files in os.walk(picPath):
        return files

# change picture file name to (.png)
def rename(path):
    # scan file on path,take file name save to list
    filename_list = os.listdir(path)  
    a = 0 
    for i in filename_list:
        used_name = path + filename_list[a]
        strS = filename_list[a].split('.',1)
        new_name = path + strS[0] + '.png'
        os.rename(used_name,new_name)
        a = a + 1

# check phone 
def saftyCheck(phone):
    res = re.match(r"^1[35678]\d{9}$", phone)
    if res:
        print('-------checked is safty!!!!!!!---------')
    else :
        print('---------------checked is not ok!!!!!Plases check phone.------------------')
    return res


if __name__ == '__main__':
    
    if saftyCheck(phone):

        print(shopName+','+phone)

        picPath = 'C:/Users/sinalma/Desktop/test/'
        count = counting_files(picPath)
        print('all pic is %d'%count)
        curFileN = ''
        rename(picPath)
        allFiles = getALLFiles(picPath)
        firstServoModel = ''
        for x in range(0,count):
            if x==0:
                modelList = allFiles[x].split("_", 1)
                firstServoModel = modelList[0]
                print('first servo model is '+ firstServoModel)
            img = Image.open(u''+picPath + allFiles[x])
            print(allFiles[x])
            img = img.resize((imgW,imgH))
            # im_after = add_text_to_image(img, u'18124988815')
            # im_after.show()
            # curDelFileName = picPath + allFiles[x]
            # im_after = ''
            if IsFanWM:
                im_after = add_text_to_image(img, shopName)
                im_after.save(u''+picPath+'deal.png')
                im_after = add_text_to_image2(u''+picPath+'deal.png')
                im_after.save(picPath + allFiles[x])
                os.remove(u''+picPath+'deal.png')
            else:
                im_after = add_text_to_image2(u''+picPath + allFiles[x])
                im_after.save(picPath + allFiles[x])
        pyperclip.copy(firstServoModel)
    else:
        print('---------------checked is not ok!!!!!Plases check phone.------------------')
    
