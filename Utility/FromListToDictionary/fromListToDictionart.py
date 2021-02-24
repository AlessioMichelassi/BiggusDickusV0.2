class fromListToDictionary:
	menu = {}

	def __init__(self):
		pass

	'''
	From a list of Key like this:
	Transform = [Resize, Rotate, Translate, Perspective]
	create a dictionaty from create a menu like This
	menu = {"Resize": "Transform", "Rotate": "Transform"}
	'''

	def doDictionary(self, keyList: list, value: str):
		for eachName in keyList:
			self.menu[eachName] = value


###########################à
# Class test

Transform = ["Resize", "Rotate", "Translate", "Perspective"]
Erode = ["Simple", "Reflect", "Dilate", "Opening", "Closing"]
Threshold = ["Binary", "BinaryInverted", "Trunc", "ToZero", "ToZeroInverted", "AdaptiveMean", "AdaptiveGaussian",
             "Otzu"]
Denoise = ["Bilateral", "InPainting"]
Blur = ["2D", "Average", "Gaussian", "Median"]
MachineLearning = ["FaceDetection", "EyeDetection", "SmileDetection", "CornerDetection", "LineDetection",
                   "CircleDetection", "DocumentDetection"]

if __name__ == '__main__':
	a = fromListToDictionary()
	a.doDictionary(Transform, "Transform")
	a.doDictionary(Erode, "Erode")
	a.doDictionary(Threshold, "Threshold")
	a.doDictionary(Denoise, "Denoise")
	a.doDictionary(Blur, "Blur")
	a.doDictionary(MachineLearning, "MachineLearning")
	print(a.menu)

	'''
	Giving this:
	Transform = ["Resize", "Rotate", "Translate", "Perspective"]
	Erode = ["Simple", "Reflect", "Dilate", "Opening", "Closing"]
	Threshold = ["Binary", "BinaryInverted", "Trunc", "ToZero", "ToZeroInverted", "AdaptiveMean", "AdaptiveGaussian", "Otzu"]
	Denoise = ["Bilateral", "InPainting"]
	Blur = ["2D", "Average", "Gaussian", "Median"]
	MachineLearning = ["FaceDetection", "EyeDetection", "SmileDetection", "CornerDetection", "LineDetection", "CircleDetection", "DocumentDetection"]
	
	you can optain This: 
	{'Resize': 'Transform', 'Rotate': 'Transform', 'Translate': 'Transform', 'Perspective': 'Transform',
	'Simple': 'Erode', 'Reflect': 'Erode', 'Dilate': 'Erode', 'Opening': 'Erode', 'Closing': 'Erode', 
	'Binary': 'Threshold', 'BinaryInverted': 'Threshold', 'Trunc': 'Threshold', 'ToZero': 'Threshold', 
	'ToZeroInverted': 'Threshold', 'AdaptiveMean': 'Threshold', 'AdaptiveGaussian': 'Threshold', 'Otzu': 'Threshold', 
	'Bilateral': 'Denoise', 'InPainting': 'Denoise', '2D': 'Blur', 'Average': 'Blur', 'Gaussian': 'Blur', 
	'Median': 'Blur', 'FaceDetection': 'MachineLearning', 'EyeDetection': 'MachineLearning', 'SmileDetection': 
	'MachineLearning', 'CornerDetection': 'MachineLearning', 'LineDetection': 'MachineLearning', 'CircleDetection': 
	'MachineLearning', 'DocumentDetection': 'MachineLearning'} 
	
	'''
