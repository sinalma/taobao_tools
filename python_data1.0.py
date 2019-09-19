import os 
from selenium import webdriver
driver = webdriver.Chrome("D:/Programming/python/chromedriver.exe") 
driver.maximize_window()
from os import path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time,unittest, re
from selenium.webdriver.common.keys import Keys



sleepTime = 0.1
product = {}
param = {}

def loadData():
    global product,param
    f = open(r"F:/Python/Code/tb_auto_publsh/product.txt",encoding='UTF-8')
    tmpProduct = f.readline()
    product = convertToDict(tmpProduct)
    f = open(r"F:/Python/Code/tb_auto_publsh/param.txt",encoding='UTF-8')
    tmpParam = f.readline()
    param = convertToDict(tmpParam)


# string convert to dictionary
def convertToDict(str):
    str = str.replace("{","").replace("}","")
    str = str.split(',')
    tmpDict = {}
    for idx1 in range(0,len(str)):
        keyValue = str[idx1].replace("'","").split(':')
        tmpDict[keyValue[0]] = keyValue[1]
    return tmpDict


def loginWithScan():
    driver.get("https://www.taobao.com/")
    time.sleep(2)
    driver.find_element_by_link_text(param['loginTrigger']).click()
    time.sleep(6)


def inputDelay(obj,value):
    for idx in xrange(0,len(value)):
        param.find_element_by_tag_name('input').send_keys(value[idx])
        time.sleep(0.1)

def choiceParam(id,value):
    excitation = driver.find_element_by_id(id)
    excitation.find_element_by_class_name('content').click()
    driver.find_element_by_xpath("//*[@title='"+value+"']").click()
    if excitation.find_element_by_link_text(value):
        return
    else:
        choiceParam(id,value)
    time.sleep(1)


# counting
maxCount = 5
def writeParam(id,value):
    global maxCount
    maxCount -= 1
    if maxCount < 0 :
        return
    param = driver.find_element_by_id(id)
    for idx in range(0,len(value)):
        param.find_element_by_tag_name('input').send_keys(value[idx])
        time.sleep(0.2)
    time.sleep(1)
    text = param.find_element_by_tag_name('input').get_attribute('value')
    if len(text) <= 0 or text != value:
        param.find_element_by_tag_name('input').clear()
        writeParam(id,value)
        time.sleep(1)
    else:
        maxCount = 5


def writeDoubleParam(id,value1,value2):
    size = driver.find_element_by_id(id)
    size_xy = size.find_elements_by_class_name('sell-o-measurement-operand')
    size_x_input = size_xy[0].find_element_by_tag_name('input')
    size_x_input.send_keys(value1)
    size_y_input = size_xy[1].find_element_by_tag_name('input')
    size_y_input.send_keys(value2)


def setCatogory():
    driver.get('https://upload.taobao.com/auction/sell.jhtml?spm=a313o.201708ban.category.d48.64f0197aLZBDbE&mytmenu=wym')
    time.sleep(1)
    # choice main category
    driver.find_element_by_id('J_SearchKeyWord').send_keys(param['createCategory'])
    time.sleep(1)
    driver.find_element_by_id('J_SearchButton').click()
    time.sleep(1)
    driver.find_element_by_id('J_CatePubBtn').click()
    time.sleep(1)

    

def publishProd():
    
    setCatogory()

    # set title
    driver.find_element_by_id('title').send_keys(product['title'])
    oriPlace = driver.find_element_by_id('struct-globalStock')
    oriPlace.find_element_by_xpath("//input[@aria-checked='true']").send_keys(Keys.SPACE)
    oriPlace.find_element_by_xpath("//input[@aria-checked='false']").click()
    # .find_element_by_tag_name('input').click()
    
    # mods = oriPlace.find_elements_by_class_name('tabNest-radio-info')
    # mods[1].find_element_by_class_name('next-radio').find_element_by_tag_name('input').click()

    # next-radio-inner press
    # radios = oriPlace.find_element_by_class_name('info-content').find_element_by_class_name('next-radio-inner').click()
    # oriPlaceRadios = oriPlace.find_elements_by_class_name('tabNest-radio-info')
    # oriPlaceRadios[1].find_element_by_tag_name('input').click()
    # oriPlaceRadios[1].find_element_by_link_text(product['originPlace']).send_keys(keys.space)
    # oriPlace.find_element_by_link_text(product['originPlace']).click()
    # oriPlaceRadios[1].find_element_by_link_text(product['originPlace']).click()


    # set left module param
    writeParam('struct-p-20000',product['brand'])
    writeDoubleParam('struct-p-148060595',product['sizeX'],product['sizeY'])
    writeParam('struct-p-10016',product['model'])
    writeParam('struct-p-29112',product['installMethod'])
    writeParam('struct-p-192254056',product['temperature'])
    writeParam('struct-p-186826808',product['lineLength'])
    writeParam('struct-p-191164129',product['encodeType'])
    writeParam('struct-p-195174015',product['rotation'])

    # set right module param
    # choiceParam('struct-p-195270003',product['axlehead'])
    writeParam('struct-p-122216515',product['scene'])
    writeParam('struct-p-147908493',product['weight'])
    writeParam('struct-p-159198215',product['power'])
    writeParam('struct-p-192190064',product['torque'])
    writeParam('struct-p-180944594',product['voltage'])
    writeParam('struct-p-195206008',product['electric'])
    writeParam('struct-p-195206009',product['speed'])
    writeParam('struct-p-191164130',product['gear'])
    choiceParam('struct-p-159662152',product['protectlevel'])

    choiceParam('struct-p-21299',product['place'])
    choiceParam('struct-p-192256056',product['excitation'])




def getPage():
    driver.get('https://shop70362492.taobao.com/category-1056421148.htm?spm=a1z10.1-c.0.0.19475140cHJ39v&search=y&catName=%B0%B2%B4%A8%CB%C5%B7%FE')
    productLines = driver.find_elements_by_class_name('item3line1')
    print(productLines)
    for idx in range(0,len(productLines)):
        products = productLines[idx]
        products = products.find_elements_by_class_name('item')
        for idx2 in range(0,len(products)):
            product = products[idx2]
            text = product.find_elements_by_class_name('item-name')
            print(text[0].text)



    

def publishProd_l():
    
    setCatogory()

    # set title
    driver.find_element_by_id('title').send_keys(product['title'])

    # set left module param
    choiceParam('struct-p-21299',product['place'])
    writeParam('struct-p-20000',product['brand'])
    writeDoubleParam('struct-p-148060595',product['sizeX'],product['sizeY'])
    choiceParam('struct-p-192256056',product['excitation'])
    writeParam('struct-p-10016',product['model'])
    writeParam('struct-p-29112',product['installMethod'])
    writeParam('struct-p-192254056',product['temperature'])
    writeParam('struct-p-186826808',product['lineLength'])
    writeParam('struct-p-191164129',product['encodeType'])
    writeParam('struct-p-195174015',product['rotation'])

    # set right module param
    # choiceParam('struct-p-195270003',product['axlehead'])
    writeParam('struct-p-147908493',product['weight'])
    choiceParam('struct-p-159662152',product['protectlevel'])
    writeParam('struct-p-159198215',product['power'])
    writeParam('struct-p-192190064',product['torque'])
    writeParam('struct-p-180944594',product['voltage'])
    writeParam('struct-p-195206008',product['electric'])
    writeParam('struct-p-195206009',product['speed'])
    writeParam('struct-p-191164130',product['gear'])


loadData()
loginWithScan()
time.sleep(2)
publishProd()

