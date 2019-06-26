from PIL import Image
import tesserocr, requests

if __name__ == '__main__':
	image_path='F:/Python/Code/QRCode/test1431049.jpg'#图片文件路径
	image = Image.open(image_path)
	result = tesserocr.image_to_text(image)
	print(result)
