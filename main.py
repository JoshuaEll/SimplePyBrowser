####################################################################################################
# Simple PyBrowser                                                                                 #
# Author: Joshua Ellis                                                                             #
# A simple browser made using PyQt 5                                                               #
####################################################################################################

import sys
from turtle import forward
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class browserCanvas(QMainWindow):
    def __init__(self) -> None:
        super(browserCanvas, self).__init__()
        self.canvas = QWebEngineView()
        self.canvas.setUrl(QUrl('https://www.google.com')) # homepage
        self.setCentralWidget(self.canvas)
        self.showMaximized()
        
        #initialization of the browser toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        #back button implementation
        backButton = QAction('Back', self)
        backButton.triggered.connect(self.canvas.back)
        backButton.setStatusTip("Go back to previous Page")
        navbar.addAction(backButton)
        
        # forward button implementation
        forwardButton = QAction('Forward', self)
        forwardButton.triggered.connect(self.canvas.forward)
        forwardButton.setStatusTip("Go to next page")
        navbar.addAction(forwardButton)

        # reload button implementation
        reloadButton = QAction('Reload', self)
        reloadButton.triggered.connect(self.canvas.reload)
        reloadButton.setStatusTip("Reload page")

        # Home button implementation
        homeButton = QAction('Home', self)
        homeButton.triggered.connect(self.homeNav)
        homeButton.setStatusTip("Go to Home page")
        navbar.addAction(homeButton)

        # set the url bar
        self.url = QLineEdit()
        self.url.returnPressed.connect(self.urlNav)
        navbar.addWidget(self.url)
        
        # calls function to change the text in the url bar if the url changes
        self.canvas.urlChanged.connect(self.newUrl)

        self.canvas.loadFinished.connect(self.changeTitle)

    # custom function to send the user back home if they push the home button
    def homeNav(self):
        self.canvas.setUrl(QUrl("https://google.com"))
    
    def urlNav(self):
        nUrl = QUrl(self.url.text())
        #if the user does not type https:// it will be prepended
        if nUrl.scheme() == "":
            nUrl.setScheme("https")

        self.canvas.setUrl(nUrl)

    #updates the url bar with the new url
    def newUrl(self, urlText):
        self.url.setText(urlText.toString())

    #gets the title of the page and changes the browser window's title
    def changeTitle(self):
        title = self.canvas.page().title()
        self.setWindowTitle('%s | PyBrowser' % title)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    runApp = browserCanvas()
    QApplication.setApplicationName('Python Web Browser')
    sys.exit(app.exec())