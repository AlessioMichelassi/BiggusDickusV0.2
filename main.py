from Generator.mainGUIgenerator import mainGUIGenerator
from Generator.mainPageGenerator import mainGenerator
from Generator.menuGenerator import menuCreator

mainPath = F"/home/ted/Desktop/Pyqt6/BiggusDickusV0.2/"
#        key : value
menuFile = {'New': 'File', 'Open': 'File', 'Save': 'File', 'Save As': 'File', '-  ': 'File', 'Export': 'File',
            '- ': 'File', 'Print': 'File', 'Print Preview': 'File', '-': 'File', 'Quit': 'File', 'Undo': 'Edit',
            'Redo': 'Edit', '-    ': 'Edit', 'cut': 'Edit', 'copy': 'Edit', 'paste': 'Edit', 'PasteFromHistory': 'Edit',
            'Delete': 'Edit', '-   ': 'Edit', 'SelectAll': 'Edit', 'zoomIn': 'View', 'zoomOut': 'View',
            'scaleToFit': 'View', 'drawLine': 'Draw', 'drawCircle': 'Draw', 'drawRectangle': 'Draw', 'drawText': 'Draw',
            'Resize': 'Filter', 'Rotate': '*Transform', 'Translate': '*Transform', 'Perspective': '*Transform',
            'Simple': '*Erode', 'Reflect': '*Erode', 'Dilate': '*Erode', 'Opening': '*Erode', 'Closing': '*Erode',
            'Binary': '*Threshold', 'BinaryInverted': '*Threshold', 'Trunc': '*Threshold', 'ToZero': '*Threshold',
            'ToZeroInverted': '*Threshold', 'AdaptiveMean': '*Threshold', 'AdaptiveGaussian': '*Threshold',
            'Otzu': '*Threshold', 'Bilateral': '*Denoise', 'InPainting': '*Denoise', 'blur2D': '*Blur', 'Average': '*Blur',
            'Gaussian': '*Blur', 'Median': '*Blur', 'FaceDetection': 'MachineLearning', 'EyeDetection': 'MachineLearning',
            'SmileDetection': 'MachineLearning', 'CornerDetection': 'MachineLearning', 'LineDetection': 'MachineLearning',
            'CircleDetection': 'MachineLearning', 'DocumentDetection': 'MachineLearning'}


if __name__ == '__main__':
    menu = {**menuEdit, **menuFile}
    _mainGenerator = mainGenerator(mainPath, "BiggusDickusV0_3")
    _mainGui = mainGUIGenerator(mainPath, "BiggusDickusV0_3")
    _menuCreator = menuCreator(mainPath, "BiggusDickusV0_3", menuFile)
