#        Son Of a BiggusDickusV0_3 


import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class mainWindows(QMainWindow):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.mainMenu = self.menuBar()
        self.Init_MainMenu()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BiggusDickusV0_3")
        self.statusBar().showMessage("ready", 3000)
        self.show()

    def Init_MainMenu(self):
        self.Init_MenuFile()
        self.Init_MenuEdit()
        self.Init_MenuView()
        self.Init_MenuDraw()
        self.Init_MenuFilter()
        self.Init_MenuMachineLearning()

    def Init_MenuFile(self):
        #        FILE
        menuFile = self.mainMenu.addMenu("File")
        #                NEW
        new_Action = menuFile.addAction("New")
        new_Action.setIcon(QIcon.fromTheme("document-new"))
        new_Action.setShortcut(QKeySequence.New)
        new_Action.triggered.connect(self.doNew)
        menuFile.addAction(new_Action)
        #                OPEN
        open_Action = menuFile.addAction("Open")
        open_Action.setIcon(QIcon.fromTheme("document-open"))
        open_Action.setShortcut(QKeySequence.Open)
        open_Action.triggered.connect(self.doOpen)
        menuFile.addAction(open_Action)
        #                SAVE
        save_Action = menuFile.addAction("Save")
        save_Action.setIcon(QIcon.fromTheme("document-save"))
        save_Action.setShortcut(QKeySequence.Save)
        save_Action.triggered.connect(self.doSave)
        menuFile.addAction(save_Action)
        #                SAVE AS
        save_as_Action = menuFile.addAction("Save As")
        save_as_Action.setShortcut(QKeySequence.SaveAs)
        save_as_Action.triggered.connect(self.doSave_As)
        menuFile.addAction(save_as_Action)
        #####################################
        menuFile.addSeparator()
        #                EXPORT
        export_Action = menuFile.addAction("Export")
        export_Action.triggered.connect(self.doExport)
        menuFile.addAction(export_Action)
        #####################################
        menuFile.addSeparator()
        #                PRINT
        print_Action = menuFile.addAction("Print")
        print_Action.setIcon(QIcon.fromTheme("document-print"))
        print_Action.setShortcut(QKeySequence.Print)
        print_Action.triggered.connect(self.doPrint)
        menuFile.addAction(print_Action)
        #                PRINT PREVIEW
        print_preview_Action = menuFile.addAction("Print Preview")
        print_preview_Action.triggered.connect(self.doPrint_Preview)
        menuFile.addAction(print_preview_Action)
        #####################################
        menuFile.addSeparator()
        #                QUIT
        quit_Action = menuFile.addAction("Quit")
        quit_Action.setIcon(QIcon.fromTheme("application-exit"))
        quit_Action.setShortcut(QKeySequence.Quit)
        quit_Action.triggered.connect(self.doQuit)
        menuFile.addAction(quit_Action)

    def Init_MenuEdit(self):
        #        EDIT
        menuEdit = self.mainMenu.addMenu("Edit")
        #                UNDO
        undo_Action = menuEdit.addAction("Undo")
        undo_Action.setIcon(QIcon.fromTheme("edit-undo"))
        undo_Action.setShortcut(QKeySequence.Undo)
        undo_Action.triggered.connect(self.doUndo)
        menuEdit.addAction(undo_Action)
        #                REDO
        redo_Action = menuEdit.addAction("Redo")
        redo_Action.setIcon(QIcon.fromTheme("edit-redo"))
        redo_Action.setShortcut(QKeySequence.Redo)
        redo_Action.triggered.connect(self.doRedo)
        menuEdit.addAction(redo_Action)
        #####################################
        menuEdit.addSeparator()
        #                CUT
        cut_Action = menuEdit.addAction("cut")
        cut_Action.setIcon(QIcon.fromTheme("edit-cut"))
        cut_Action.setShortcut(QKeySequence.Cut)
        cut_Action.triggered.connect(self.docut)
        menuEdit.addAction(cut_Action)
        #                COPY
        copy_Action = menuEdit.addAction("copy")
        copy_Action.setIcon(QIcon.fromTheme("edit-copy"))
        copy_Action.setShortcut(QKeySequence.Copy)
        copy_Action.triggered.connect(self.docopy)
        menuEdit.addAction(copy_Action)
        #                PASTE
        paste_Action = menuEdit.addAction("paste")
        paste_Action.setIcon(QIcon.fromTheme("edit-paste"))
        paste_Action.setShortcut(QKeySequence.Paste)
        paste_Action.triggered.connect(self.dopaste)
        menuEdit.addAction(paste_Action)
        #                PASTEFROMHISTORY
        pastefromhistory_Action = menuEdit.addAction("PasteFromHistory")
        pastefromhistory_Action.triggered.connect(self.doPasteFromHistory)
        menuEdit.addAction(pastefromhistory_Action)
        #                DELETE
        delete_Action = menuEdit.addAction("Delete")
        delete_Action.setIcon(QIcon.fromTheme("edit-delete"))
        delete_Action.setShortcut(QKeySequence.Delete)
        delete_Action.triggered.connect(self.doDelete)
        menuEdit.addAction(delete_Action)
        #####################################
        menuEdit.addSeparator()
        #                SELECTALL
        selectall_Action = menuEdit.addAction("SelectAll")
        selectall_Action.setShortcut(QKeySequence.SelectAll)
        selectall_Action.triggered.connect(self.doSelectAll)
        menuEdit.addAction(selectall_Action)

    def Init_MenuView(self):
        #        VIEW
        menuView = self.mainMenu.addMenu("View")
        #                ZOOMIN
        zoomin_Action = menuView.addAction("zoomIn")
        zoomin_Action.setShortcut(QKeySequence.ZoomIn)
        zoomin_Action.triggered.connect(self.dozoomIn)
        menuView.addAction(zoomin_Action)
        #                ZOOMOUT
        zoomout_Action = menuView.addAction("zoomOut")
        zoomout_Action.setShortcut(QKeySequence.ZoomOut)
        zoomout_Action.triggered.connect(self.dozoomOut)
        menuView.addAction(zoomout_Action)
        #                SCALETOFIT
        scaletofit_Action = menuView.addAction("scaleToFit")
        scaletofit_Action.triggered.connect(self.doscaleToFit)
        menuView.addAction(scaletofit_Action)

    def Init_MenuDraw(self):
        #        DRAW
        menuDraw = self.mainMenu.addMenu("Draw")
        #                DRAWLINE
        drawline_Action = menuDraw.addAction("drawLine")
        drawline_Action.triggered.connect(self.dodrawLine)
        menuDraw.addAction(drawline_Action)
        #                DRAWCIRCLE
        drawcircle_Action = menuDraw.addAction("drawCircle")
        drawcircle_Action.triggered.connect(self.dodrawCircle)
        menuDraw.addAction(drawcircle_Action)
        #                DRAWRECTANGLE
        drawrectangle_Action = menuDraw.addAction("drawRectangle")
        drawrectangle_Action.triggered.connect(self.dodrawRectangle)
        menuDraw.addAction(drawrectangle_Action)
        #                DRAWTEXT
        drawtext_Action = menuDraw.addAction("drawText")
        drawtext_Action.triggered.connect(self.dodrawText)
        menuDraw.addAction(drawtext_Action)

    def Init_MenuFilter(self):
        #        FILTER
        menuFilter = self.mainMenu.addMenu("Filter")
        #                RESIZE
        resize_Action = menuFilter.addAction("Resize")
        resize_Action.triggered.connect(self.doResize)
        menuFilter.addAction(resize_Action)
        #####################################
        menuTransform = menuFilter.addMenu("Transform")
        #                ROTATE
        rotate_Action = menuTransform.addAction("Rotate")
        rotate_Action.triggered.connect(self.doRotate)
        menuTransform.addAction(rotate_Action)
        #####################################
        #                TRANSLATE
        translate_Action = menuTransform.addAction("Translate")
        translate_Action.triggered.connect(self.doTranslate)
        menuTransform.addAction(translate_Action)
        #####################################
        #                PERSPECTIVE
        perspective_Action = menuTransform.addAction("Perspective")
        perspective_Action.triggered.connect(self.doPerspective)
        menuTransform.addAction(perspective_Action)
        #####################################
        menuErode = menuFilter.addMenu("Erode")
        #                SIMPLE
        simple_Action = menuErode.addAction("Simple")
        simple_Action.triggered.connect(self.doSimple)
        menuErode.addAction(simple_Action)
        #####################################
        #                REFLECT
        reflect_Action = menuErode.addAction("Reflect")
        reflect_Action.triggered.connect(self.doReflect)
        menuErode.addAction(reflect_Action)
        #####################################
        #                DILATE
        dilate_Action = menuErode.addAction("Dilate")
        dilate_Action.triggered.connect(self.doDilate)
        menuErode.addAction(dilate_Action)
        #####################################
        #                OPENING
        opening_Action = menuErode.addAction("Opening")
        opening_Action.triggered.connect(self.doOpening)
        menuErode.addAction(opening_Action)
        #####################################
        #                CLOSING
        closing_Action = menuErode.addAction("Closing")
        closing_Action.triggered.connect(self.doClosing)
        menuErode.addAction(closing_Action)
        #####################################
        menuThreshold = menuFilter.addMenu("Threshold")
        #                BINARY
        binary_Action = menuThreshold.addAction("Binary")
        binary_Action.triggered.connect(self.doBinary)
        menuThreshold.addAction(binary_Action)
        #####################################
        #                BINARYINVERTED
        binaryinverted_Action = menuThreshold.addAction("BinaryInverted")
        binaryinverted_Action.triggered.connect(self.doBinaryInverted)
        menuThreshold.addAction(binaryinverted_Action)
        #####################################
        #                TRUNC
        trunc_Action = menuThreshold.addAction("Trunc")
        trunc_Action.triggered.connect(self.doTrunc)
        menuThreshold.addAction(trunc_Action)
        #####################################
        #                TOZERO
        tozero_Action = menuThreshold.addAction("ToZero")
        tozero_Action.triggered.connect(self.doToZero)
        menuThreshold.addAction(tozero_Action)
        #####################################
        #                TOZEROINVERTED
        tozeroinverted_Action = menuThreshold.addAction("ToZeroInverted")
        tozeroinverted_Action.triggered.connect(self.doToZeroInverted)
        menuThreshold.addAction(tozeroinverted_Action)
        #####################################
        #                ADAPTIVEMEAN
        adaptivemean_Action = menuThreshold.addAction("AdaptiveMean")
        adaptivemean_Action.triggered.connect(self.doAdaptiveMean)
        menuThreshold.addAction(adaptivemean_Action)
        #####################################
        #                ADAPTIVEGAUSSIAN
        adaptivegaussian_Action = menuThreshold.addAction("AdaptiveGaussian")
        adaptivegaussian_Action.triggered.connect(self.doAdaptiveGaussian)
        menuThreshold.addAction(adaptivegaussian_Action)
        #####################################
        #                OTZU
        otzu_Action = menuThreshold.addAction("Otzu")
        otzu_Action.triggered.connect(self.doOtzu)
        menuThreshold.addAction(otzu_Action)
        #####################################
        menuDenoise = menuFilter.addMenu("Denoise")
        #                BILATERAL
        bilateral_Action = menuDenoise.addAction("Bilateral")
        bilateral_Action.triggered.connect(self.doBilateral)
        menuDenoise.addAction(bilateral_Action)
        #####################################
        #                INPAINTING
        inpainting_Action = menuDenoise.addAction("InPainting")
        inpainting_Action.triggered.connect(self.doInPainting)
        menuDenoise.addAction(inpainting_Action)
        #####################################
        menuBlur = menuFilter.addMenu("Blur")
        #                BLUR2D
        blur2d_Action = menuBlur.addAction("blur2D")
        blur2d_Action.triggered.connect(self.doblur2D)
        menuBlur.addAction(blur2d_Action)
        #####################################
        #                AVERAGE
        average_Action = menuBlur.addAction("Average")
        average_Action.triggered.connect(self.doAverage)
        menuBlur.addAction(average_Action)
        #####################################
        #                GAUSSIAN
        gaussian_Action = menuBlur.addAction("Gaussian")
        gaussian_Action.triggered.connect(self.doGaussian)
        menuBlur.addAction(gaussian_Action)
        #####################################
        #                MEDIAN
        median_Action = menuBlur.addAction("Median")
        median_Action.triggered.connect(self.doMedian)
        menuBlur.addAction(median_Action)

    def Init_MenuMachineLearning(self):
        #        MACHINELEARNING
        menuMachineLearning = self.mainMenu.addMenu("MachineLearning")
        #                FACEDETECTION
        facedetection_Action = menuMachineLearning.addAction("FaceDetection")
        facedetection_Action.triggered.connect(self.doFaceDetection)
        menuMachineLearning.addAction(facedetection_Action)
        #                EYEDETECTION
        eyedetection_Action = menuMachineLearning.addAction("EyeDetection")
        eyedetection_Action.triggered.connect(self.doEyeDetection)
        menuMachineLearning.addAction(eyedetection_Action)
        #                SMILEDETECTION
        smiledetection_Action = menuMachineLearning.addAction("SmileDetection")
        smiledetection_Action.triggered.connect(self.doSmileDetection)
        menuMachineLearning.addAction(smiledetection_Action)
        #                CORNERDETECTION
        cornerdetection_Action = menuMachineLearning.addAction("CornerDetection")
        cornerdetection_Action.triggered.connect(self.doCornerDetection)
        menuMachineLearning.addAction(cornerdetection_Action)
        #                LINEDETECTION
        linedetection_Action = menuMachineLearning.addAction("LineDetection")
        linedetection_Action.triggered.connect(self.doLineDetection)
        menuMachineLearning.addAction(linedetection_Action)
        #                CIRCLEDETECTION
        circledetection_Action = menuMachineLearning.addAction("CircleDetection")
        circledetection_Action.triggered.connect(self.doCircleDetection)
        menuMachineLearning.addAction(circledetection_Action)
        #                DOCUMENTDETECTION
        documentdetection_Action = menuMachineLearning.addAction("DocumentDetection")
        documentdetection_Action.triggered.connect(self.doDocumentDetection)
        menuMachineLearning.addAction(documentdetection_Action)

#    ACTION DEFINITION
    def doNew(self):
        self.toBeImplemented()

    def doOpen(self):
        self.toBeImplemented()

    def doSave(self):
        self.toBeImplemented()

    def doSave_As(self):
        self.toBeImplemented()

    def doExport(self):
        self.toBeImplemented()

    def doPrint(self):
        self.toBeImplemented()

    def doPrint_Preview(self):
        self.toBeImplemented()

    def doQuit(self):
        self.toBeImplemented()

    def doUndo(self):
        self.toBeImplemented()

    def doRedo(self):
        self.toBeImplemented()

    def docut(self):
        self.toBeImplemented()

    def docopy(self):
        self.toBeImplemented()

    def dopaste(self):
        self.toBeImplemented()

    def doPasteFromHistory(self):
        self.toBeImplemented()

    def doDelete(self):
        self.toBeImplemented()

    def doSelectAll(self):
        self.toBeImplemented()

    def dozoomIn(self):
        self.toBeImplemented()

    def dozoomOut(self):
        self.toBeImplemented()

    def doscaleToFit(self):
        self.toBeImplemented()

    def dodrawLine(self):
        self.toBeImplemented()

    def dodrawCircle(self):
        self.toBeImplemented()

    def dodrawRectangle(self):
        self.toBeImplemented()

    def dodrawText(self):
        self.toBeImplemented()

    def doResize(self):
        self.toBeImplemented()

    def doRotate(self):
        self.toBeImplemented()

    def doTranslate(self):
        self.toBeImplemented()

    def doPerspective(self):
        self.toBeImplemented()

    def doSimple(self):
        self.toBeImplemented()

    def doReflect(self):
        self.toBeImplemented()

    def doDilate(self):
        self.toBeImplemented()

    def doOpening(self):
        self.toBeImplemented()

    def doClosing(self):
        self.toBeImplemented()

    def doBinary(self):
        self.toBeImplemented()

    def doBinaryInverted(self):
        self.toBeImplemented()

    def doTrunc(self):
        self.toBeImplemented()

    def doToZero(self):
        self.toBeImplemented()

    def doToZeroInverted(self):
        self.toBeImplemented()

    def doAdaptiveMean(self):
        self.toBeImplemented()

    def doAdaptiveGaussian(self):
        self.toBeImplemented()

    def doOtzu(self):
        self.toBeImplemented()

    def doBilateral(self):
        self.toBeImplemented()

    def doInPainting(self):
        self.toBeImplemented()

    def doblur2D(self):
        self.toBeImplemented()

    def doAverage(self):
        self.toBeImplemented()

    def doGaussian(self):
        self.toBeImplemented()

    def doMedian(self):
        self.toBeImplemented()

    def doFaceDetection(self):
        self.toBeImplemented()

    def doEyeDetection(self):
        self.toBeImplemented()

    def doSmileDetection(self):
        self.toBeImplemented()

    def doCornerDetection(self):
        self.toBeImplemented()

    def doLineDetection(self):
        self.toBeImplemented()

    def doCircleDetection(self):
        self.toBeImplemented()

    def doDocumentDetection(self):
        self.toBeImplemented()

    def toBeImplemented(self):
        self.statusBar().showMessage("To Be Implemented", 3000)

