from easyocr.easyocr import *
import os

class ocr:
    def __init__(self):
        previous_dir = os.getcwd()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        self.reader = Reader(['ko'], gpu=True,
                model_storage_directory='ocr_model',
                user_network_directory='ocr_network',
                recog_network='custom')
        os.chdir(previous_dir)
        
    def __call__(self,filename):
        result = self.reader.readtext(filename)
        return result