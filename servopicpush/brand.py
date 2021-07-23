

	# 所有型号包括的要素打乱重组
	# 品牌父类分为两大类 电机 和 驱动器
	# 孙类才是品牌

	# 所有电机型号四要素
	  # 1.系列
	  # 2.电压-编码器位数-转速-减速机？
	  # 3.功率
	  # 4.键槽刹车-定制款尾缀？



class brand:
	"""docstring for YASKAWA"""
	def __init__(self,model):
		super(brand, self).__init__()
		self.model = model

	
	yaskawa_I = ['SGM','SGMP','SGMCS','SGMM','SGME','SGML']
	yaskawa_II = ['SGMPH','SGM7J','SGM7A','SGM7G','SGM7P','SGMPS','SGMS','SGMG','SGMAH','SGMGH','SGMAV','SGMSV','SGMRV','SGMGV','SGMJV','SGMMV','SGMAJ','SGMRS','SGMSH']
	yaskawa_III = ['SGDS']
	yaskawa_IV = ['SGDM','SGDH','SGDA','SJDE','SGDB']
	yaskawa_V = ['SGDV','SGD7S']
	yaskawa_VI = ['SGDR','SRDA']
	def YASKAWA(self):
		 #安川 类型系列-功率/电压/编码器类型/转速/？是否带减速机--》
	 	   #1是否带键槽/是否带刹车和刹车类型
	       #2-定制型号后缀
		#拆分型号字母根据-分割
		#第一个结果将可以指定第一层文件夹
		#第二个结果将指定第二层文件夹
		    #分割第二个结果将获得功率 ，也将获得第三层文件夹
		    #如果没有第三个结果 。将获得第四层文件夹
		#第三个结果将直接拥有第四层文件夹
		models = self.model.split('-')
		# print(models)
		power = models[1][0:2]
		midF = ''
		if self.yaskawa_II.count(models[0]):
			#当前安川伺服型号是电机的型号
			#获取
			#1342当前型号的功率
			#判断当前型号有几个杠
			if len(models) > 2:
				#两个杠时 中间功率后可能存第四位为减速机标识
				if len(models[1])>=6:
					midF = models[1][2:6]
				else:
					midF = models[1][2:5]
			else :
				#一个杠	
				midF = models[1][2:5]
		elif self.yaskawa_I.count(models[0]):
			midF = models[1][2:4]
		elif self.yaskawa_III.count(models[0]):
			midF = models[1][2:5]
		elif self.yaskawa_IV.count(models[0]):
			if len(models[1]) > 2:
			    midF = models[1][2:5]
			else:
			    midF = models[1][2:4]
		elif self.yaskawa_V.count(models[0]):
			midF = models[1][3:6]
			# print(midF)
			power = models[1][0:3]
			# SGDR-SDA140A01A
			# SGDR - SDA A 
		elif self.yaskawa_VI.count(models[0]):
			res = self.strLine()
			# print(['YASKAWA',models[0],models[0]+'-'+res[0],models[0]+'-'+res[2]+'_',self.model])
			return ['YASKAWA',models[0],models[0]+'-'+res[0],models[0]+'-'+res[2],self.model]
		return ['YASKAWA',models[0],models[0]+'_'+midF,models[0]+'-'+power+midF,self.model]
		
	# yaskawa_VI 
	def strLine(self):
		models = self.model.split('-')
		power = ''
		midF = ''
		midPower = ''
		if models[1][5] == '0':
			power = models[1][4:6]
			midF = models[1][0:3]+'_'+models[1][6]
			midPower = models[1][0:7]
		else:
			power = models[1][4:5]
			midF = models[1][0:3]+'_'+models[1][5]
			midPower = models[1][0:6]
		return [midF,power,midPower]

	fuji_motor = ['GYS','GYC','GYB','GYH','GYG']
	fuji_servo = ['RYS','RYE','RYB','RYC','RYH','RYT']

	def FUJI(self):
		models = self.model.split('-')
		# print(models[0])
		leftM = models[0]
		tagM = leftM[0:3]
		if self.fuji_motor.count(tagM):
			midF = leftM[6:9]
			return ['FUJI',tagM,tagM+'_'+midF,leftM,self.model]
		elif self.fuji_servo.count(tagM):
			midF = leftM[6:8]
			return ['FUJI',tagM,tagM+'_'+midF,leftM,self.model]
		elif tagM == 'RYE':
			midF = leftM
			return ['FUJI',tagM,self.model]
		elif  tagM == 'RYG':
			midF = leftM
			pass


	ormon_motor_I = ['R7M','R88M']
	ormon_servo_I = ['R7D','R88D']
	def ORMON(self):
		models = self.model.split('-')
		tag = models[0]
		power = ''
		left = ''
		if self.ormon_motor_I.count(tag):
			#是电机
			power = models[1][1:6]
			left = models[1][0]
		elif self.ormon_servo_I.count(tag):
			power = models[1][2:4]
			left = models[1][0:2]

		return ['ormon',tag,tag+'-'+left+'_',tag+'-'+left+power+'_',self.model]
		

	passonic_motor_I = ['MDME','MHMF','MSMD','MSMF','MUDS','MUMS']
	passonic_servo_I = ['MADLN','MBDLN','MCDLN','MDDLN']
	passonic_servo_II = ['MADDT','MADHT','MADKT','MBDHT','MBDK','MBDKT','MCDHT','MCDKT','MDDHT','MFDKT']
	def PANASONIC(self):
		
		tagN = self.model[0:4]
		power = ''
		if self.passonic_motor_I.count(tagN):
			#passonic_motor_I
			power = self.model[4:7]
		else:
			tagN = self.model[0:5]

		if self.passonic_servo_I.count(tagN):
			power = self.model[5:7]
		elif self.passonic_servo_II.count(tagN):
			power = self.model[5:9]

		return ['passonic',tagN,tagN+power+'_',self.model]
		

			


if __name__ == '__main__':
	print('3333333')