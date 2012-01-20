from webkit2png import *
from PyQt4.QtCore import QTimer
import csv
#import urllib2

    
class PhotoCreator:
    
    def __init__(self):
        self.listOfUrls = []
        
    def parse_csv(self):
        csvFilePath = raw_input("PleaseEnterCSVFilePath: ")
        #csvFilePath = urllib2.urlopen("#NEED CSVURL").read()
        theReader = csv.reader(open(csvFilePath, 'rb')) 
        for row in theReader:
            self.listOfUrls.append(row)
        self.run_method()
        
    def run_method(self):
        def renderer_func():   
            renderer = WebkitRenderer()
            renderer.width = 0
            renderer.height = 0
            renderer.timeout = 10
            renderer.wait = 1
            renderer.format = "png"
            renderer.grabWholeWindow = False
            for url in self.listOfUrls:
                url = url[0]
                fileName = url.split('://')
                if len(fileName) >1:
                    fileName = fileName[1].split('www.')
                else:
                    fileName = fileName[0].split('www.')
                if len(fileName) >1:
                    fileName = fileName[1].split('.')
                else:
                    fileName = fileName[0].split('.')
                fileName = fileName[0]
                
                outfile = open("%s.png" % fileName, "w") 
                renderer.render_to_file(url, outfile)
                outfile.close()
               
        app = init_qtgui()
        QTimer.singleShot(0, renderer_func)
        app.exec_()
        sys.exit(1)
        