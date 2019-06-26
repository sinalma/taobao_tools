from PIL import Image, ImageDraw, ImageFont
import os
# 图片添加水印
def add_num(img,name):
    # 创建绘画对象
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/simsun.ttc',size=50)
    fillcolor = '#ff0000'
    width,height = img.size
    x = 150
    y = height/2-50
    mark = '柒柒工控 17717458762'
    # 参数一：位置（x轴，y轴）；参数二：填写内容；参数三：字体；参数四：颜色
    draw.text((x, y),mark,font=myfont,fill=fillcolor)
    # myfont = ImageFont.truetype('C:/windows/fonts/simsun.ttc',size=20)
    # draw.text((50,50),'221907658912301992441',font=myfont,fill=fillcolor)
    img.save(name,'jpeg')
    return 0

def replaceName():
    path = "C:/Users/sinalma/Desktop/pic/"    # 目标路径
  
    """os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
    filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表
  
    a = 0
    for i in filename_list:
        used_name = path + filename_list[a]
        new_name = path + "img%d"%a+'.jpg'
        os.rename(used_name,new_name)
        print("文件%s重命名成功,新的文件名为%s" %(used_name,new_name))
        a += 1

def ThumbImg(infile):
    # 略缩图路径
    outfile = os.path.splitext(infile)[0] + "_ThumbNail" + ".jpeg"
    im = Image.open(infile)
    size = (300, 300)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile)
    return outfile

if __name__ == '__main__':
    replaceName()
    path = 'C:/Users/sinalma/Desktop/pic/'
    ls = os.listdir(path)
    count = 0
    for i in ls:
        if os.path.isfile(os.path.join(path,i)):
            count+=1
    idx = 1
    for idx in range(count):
        # if idx>=count:
        #     count
        idx += 1
        print(idx)
        # image = Image.open(('IMG (%d).jpg')%int(idx))
        # add_num(image,('IMG (%d).jpg')%int(idx))
        image = Image.open(path+('img%d.jpg')%int(idx))
        image.thumbnail((800,800),Image.ANTIALIAS)
        # image.transpose(Image.ROTATE_90)
        image.save(path+('img%d.jpg')%int(idx))
        add_num(image,(path+'img%d.jpg')%int(idx))
    	