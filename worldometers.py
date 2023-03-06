from mainwindow import Ui_MainWindow
from PyQt6 import QtWidgets, QtGui, QtCore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class MainWindow_controller(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.worldometers = worldometers()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_active = None
        self.TB01 = self.ui.Ttile_Browser01
        self.NB01 = self.ui.Number_Browser01
        self.TB02 = self.ui.Ttile_Browser02
        self.NB02 = self.ui.Number_Browser02
        self.TB03 = self.ui.Ttile_Browser03
        self.NB03 = self.ui.Number_Browser03
        self.TB04 = self.ui.Ttile_Browser04
        self.NB04 = self.ui.Number_Browser04
        self.TB05 = self.ui.Ttile_Browser05
        self.NB05 = self.ui.Number_Browser05
        self.TB06 = self.ui.Ttile_Browser06
        self.NB06 = self.ui.Number_Browser06
        self.TB07 = self.ui.Ttile_Browser07
        self.NB07 = self.ui.Number_Browser07
        self.TB08 = self.ui.Ttile_Browser08
        self.NB08 = self.ui.Number_Browser08
        self.TB09 = self.ui.Ttile_Browser09
        self.NB09 = self.ui.Number_Browser09
        self.ui.world_population_Button.clicked.connect(self.world_population_refresh)
        self.ui.government_econmy_Button.clicked.connect(self.government_econmy_refresh)
        self.ui.society_media_Button.clicked.connect(self.society_media_refresh)
        self.ui.energy_Button.clicked.connect(self.energy_refresh)
        self.ui.health_Button.clicked.connect(self.health_refresh)
        
    def current_active_button(self):
        if self.current_active == True:
            self.timer.stop()
            
        self.current_active = True
        
    def world_population_refresh(self):
        self.current_active_button()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.world_population_click)
        self.timer.start(100)
        
    def government_econmy_refresh(self):
        self.current_active_button()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.government_econmy_click)
        self.timer.start(100)
        
    def society_media_refresh(self):
        self.current_active_button()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.society_media_click)
        self.timer.start(100)

    def energy_refresh(self):
        self.current_active_button()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.energy_click)
        self.timer.start(100)
        
    def health_refresh(self):
        self.current_active_button()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.health_click)
        self.timer.start(100)

    def world_population_click(self):
        self.TB01.clear()
        self.NB01.clear()
        self.TB02.clear()
        self.NB02.clear()
        self.TB03.clear()
        self.NB03.clear()
        self.TB04.clear()
        self.NB04.clear()
        self.TB05.clear()
        self.NB05.clear()
        self.TB06.clear()
        self.NB06.clear()
        self.TB07.clear()
        self.NB07.clear()
        self.TB08.clear()
        self.NB08.clear()
        self.TB09.clear()
        self.NB09.clear()
        items = self.worldometers.world_population()       
        self.TB01.setText("<html><center>"+items[0]+"</center></html>")
        self.NB01.setText("<html><center>"+items[1]+"</center></html>")
        self.TB02.setText("<html><center>"+items[2]+"</center></html>")
        self.NB02.setText("<html><center>"+items[3]+"</center></html>")
        self.TB03.setText("<html><center>"+items[4]+"</center></html>")
        self.NB03.setText("<html><center>"+items[5]+"</center></html>")
        self.TB04.setText("<html><center>"+items[6]+"</center></html>")
        self.NB04.setText("<html><center>"+items[7]+"</center></html>")
        self.TB05.setText("<html><center>"+items[8]+"</center></html>")
        self.NB05.setText("<html><center>"+items[9]+"</center></html>")
        self.TB06.setText("<html><center>"+items[10]+"</center></html>")
        self.NB06.setText("<html><center>"+items[11]+"</center></html>")
        self.TB07.setText("<html><center>無資料</center></html>")
        self.NB07.setText("<html><center>\ \ \ \ \ \</center></html>")
        self.TB08.setText("<html><center>無資料</center></html>")
        self.NB08.setText("<html><center>\ \ \ \ \ \</center></html>")
        self.TB09.setText("<html><center>無資料</center></html>")
        self.NB09.setText("<html><center>\ \ \ \ \ \</center></html>")

    def government_econmy_click(self):
        self.TB01.clear()
        self.NB01.clear()
        self.TB02.clear()
        self.NB02.clear()
        self.TB03.clear()
        self.NB03.clear()
        self.TB04.clear()
        self.NB04.clear()
        self.TB05.clear()
        self.NB05.clear()
        self.TB06.clear()
        self.NB06.clear()
        self.TB07.clear()
        self.NB07.clear()
        self.TB08.clear()
        self.NB08.clear()
        self.TB09.clear()
        self.NB09.clear()
        items = self.worldometers.government_econmy()       
        self.TB01.setText("<html><center><font size='2'>"+items[0]+"</font></center></html>")#
        self.NB01.setText("<html><center>"+items[1]+"</center></html>")
        self.TB02.setText("<html><center><font size='2'>"+items[2]+"</font></center></html>")#
        self.NB02.setText("<html><center>"+items[3]+"</center></html>")
        self.TB03.setText("<html><center><font size='2'>"+items[4]+"</font></center></html>")
        self.NB03.setText("<html><center>"+items[5]+"</center></html>")
        self.TB04.setText("<html><center>"+items[6]+"</center></html>")
        self.NB04.setText("<html><center>"+items[7]+"</center></html>")
        self.TB05.setText("<html><center>"+items[8]+"</center></html>")
        self.NB05.setText("<html><center>"+items[9]+"</center></html>")
        self.TB06.setText("<html><center>"+items[10]+"</center></html>")
        self.NB06.setText("<html><center>"+items[11]+"</center></html>")
        self.TB07.setText("<html><center>無資料</center></html>")
        self.NB07.setText("<html><center>\ \ \ \ \ \</center></html>")
        self.TB08.setText("<html><center>無資料</center></html>")
        self.NB08.setText("<html><center>\ \ \ \ \ \</center></html>")
        self.TB09.setText("<html><center>無資料</center></html>")
        self.NB09.setText("<html><center>\ \ \ \ \ \</center></html>")

    def society_media_click(self):
        self.TB01.clear()
        self.NB01.clear()
        self.TB02.clear()
        self.NB02.clear()
        self.TB03.clear()
        self.NB03.clear()
        self.TB04.clear()
        self.NB04.clear()
        self.TB05.clear()
        self.NB05.clear()
        self.TB06.clear()
        self.NB06.clear()
        self.TB07.clear()
        self.NB07.clear()
        self.TB08.clear()
        self.NB08.clear()
        self.TB09.clear()
        self.NB09.clear()
        items = self.worldometers.society_media()       
        self.TB01.setText("<html><center>"+items[0]+"</center></html>")
        self.NB01.setText("<html><center>"+items[1]+"</center></html>")
        self.TB02.setText("<html><center>"+items[2]+"</center></html>")
        self.NB02.setText("<html><center>"+items[3]+"</center></html>")
        self.TB03.setText("<html><center>"+items[4]+"</center></html>")
        self.NB03.setText("<html><center>"+items[5]+"</center></html>")
        self.TB04.setText("<html><center>"+items[6]+"</center></html>")
        self.NB04.setText("<html><center>"+items[7]+"</center></html>")
        self.TB05.setText("<html><center>"+items[8]+"</center></html>")
        self.NB05.setText("<html><center>"+items[9]+"</center></html>")
        self.TB06.setText("<html><center>"+items[10]+"</center></html>")
        self.NB06.setText("<html><center>"+items[11]+"</center></html>")
        self.TB07.setText("<html><center>"+items[12]+"</center></html>")
        self.NB07.setText("<html><center>"+items[13]+"</center></html>")
        self.TB08.setText("<html><center>"+items[14]+"</center></html>")
        self.NB08.setText("<html><center>"+items[15]+"</center></html>")
        self.TB09.setText("<html><center>"+items[16]+"</center></html>")
        self.NB09.setText("<html><center>"+items[17]+"</center></html>")
    
    def energy_click(self):
        self.TB01.clear()
        self.NB01.clear()
        self.TB02.clear()
        self.NB02.clear()
        self.TB03.clear()
        self.NB03.clear()
        self.TB04.clear()
        self.NB04.clear()
        self.TB05.clear()
        self.NB05.clear()
        self.TB06.clear()
        self.NB06.clear()
        self.TB07.clear()
        self.NB07.clear()
        self.TB08.clear()
        self.NB08.clear()
        self.TB09.clear()
        self.NB09.clear()
        items = self.worldometers.energy()       
        self.TB01.setText("<html><center><font size='3'>"+items[0]+"</font></center></html>")
        self.NB01.setText("<html><center>"+items[1]+"</center></html>")
        self.TB02.setText("<html><center>"+items[2]+"</center></html>")
        self.NB02.setText("<html><center>"+items[3]+"</center></html>")
        self.TB03.setText("<html><center>"+items[4]+"</center></html>")
        self.NB03.setText("<html><center>"+items[5]+"</center></html>")
        self.TB04.setText("<html><center><font size='3'>"+items[6]+"</font></center></html>")
        self.NB04.setText("<html><center>"+items[7]+"</center></html>")
        self.TB05.setText("<html><center>"+items[8]+"</center></html>")
        self.NB05.setText("<html><center>"+items[9]+"</center></html>")
        self.TB06.setText("<html><center>"+items[10]+"</center></html>")
        self.NB06.setText("<html><center>"+items[11]+"</center></html>")
        self.TB07.setText("<html><center>"+items[12]+"</center></html>")
        self.NB07.setText("<html><center>"+items[13]+"</center></html>")
        self.TB08.setText("<html><center>"+items[14]+"</center></html>")
        self.NB08.setText("<html><center>"+items[15]+"</center></html>")
        self.TB09.setText("<html><center>"+items[16]+"</center></html>")
        self.NB09.setText("<html><center>"+items[17]+"</center></html>")
     
    def health_click(self):
        self.TB01.clear()
        self.NB01.clear()
        self.TB02.clear()
        self.NB02.clear()
        self.TB03.clear()
        self.NB03.clear()
        self.TB04.clear()
        self.NB04.clear()
        self.TB05.clear()
        self.NB05.clear()
        self.TB06.clear()
        self.NB06.clear()
        self.TB07.clear()
        self.NB07.clear()
        self.TB08.clear()
        self.NB08.clear()
        self.TB09.clear()
        self.NB09.clear()
        items = self.worldometers.health()       
        self.TB01.setText("<html><center><font size='2'>"+items[0]+"</font></center></html>")#
        self.NB01.setText("<html><center>"+items[1]+"</center></html>")
        self.TB02.setText("<html><center>"+items[2]+"</center></html>")
        self.NB02.setText("<html><center>"+items[3]+"</center></html>")
        self.TB03.setText("<html><center>"+items[4]+"</center></html>")
        self.NB03.setText("<html><center>"+items[5]+"</center></html>")
        self.TB04.setText("<html><center>"+items[6]+"</center></html>")
        self.NB04.setText("<html><center>"+items[7]+"</center></html>")
        self.TB05.setText("<html><center>"+items[8]+"</center></html>")
        self.NB05.setText("<html><center>"+items[9]+"</center></html>")
        self.TB06.setText("<html><center>"+items[10]+"</center></html>")
        self.NB06.setText("<html><center>"+items[11]+"</center></html>")
        self.TB07.setText("<html><center>"+items[12]+"</center></html>")
        self.NB07.setText("<html><center>"+items[13]+"</center></html>")
        self.TB08.setText("<html><center><font size='2'>"+items[14]+"</font></center></html>")
        self.NB08.setText("<html><center>"+items[15]+"</center></html>")
        self.TB09.setText("<html><center>"+items[16]+"</center></html>")
        self.NB09.setText("<html><center>"+items[17]+"</center></html>")

class worldometers():
    def __init__(self):
        super().__init__() 
        url="https://www.worldometers.info/tw/"
        oP=webdriver.ChromeOptions()
        oP.add_argument("headless")
        self.web=webdriver.Chrome(options=oP)
        WebDriverWait(self.web, 5)
        self.web.get(url)
        
    def world_population(self):
        itemlist=[]
        titel01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[2]/td[2]').text
        number01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[2]/td[1]').text
        titel02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[3]/td[2]').text
        number02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[3]/td[1]').text
        titel03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[5]/td[2]').text
        number03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[5]/td[1]').text
        titel04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[7]/td[2]').text
        number04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[7]/td[1]').text
        titel05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[8]/td[2]').text
        number05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[8]/td[1]').text
        titel06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[9]/td[2]').text
        number06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[9]/td[1]').text
        itemlist.append(titel01)
        itemlist.append(number01)
        itemlist.append(titel02)
        itemlist.append(number02)
        itemlist.append(titel03)
        itemlist.append(number03)
        itemlist.append(titel04)
        itemlist.append(number04)
        itemlist.append(titel05)
        itemlist.append(number05)
        itemlist.append(titel06)
        itemlist.append(number06)
        return itemlist
    
    def government_econmy(self):
        itemlist=[]
        titel01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[12]/td[2]').text
        number01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[12]/td[1]').text
        titel02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[13]/td[2]').text
        number02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[13]/td[1]').text
        titel03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[14]/td[2]').text
        number03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[14]/td[1]').text
        titel04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[15]/td[2]').text
        number04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[15]/td[1]').text
        titel05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[16]/td[2]').text
        number05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[16]/td[1]').text
        titel06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[17]/td[2]').text
        number06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[17]/td[1]').text
        itemlist.append(titel01)
        itemlist.append(number01)
        itemlist.append(titel02)
        itemlist.append(number02)
        itemlist.append(titel03)
        itemlist.append(number03)
        itemlist.append(titel04)
        itemlist.append(number04)
        itemlist.append(titel05)
        itemlist.append(number05)
        itemlist.append(titel06)
        itemlist.append(number06)
        return itemlist
    
    def society_media(self):
        itemlist=[]
        titel01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[21]/td[2]').text
        number01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[21]/td[1]').text
        titel02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[22]/td[2]').text
        number02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[22]/td[1]').text
        titel03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[23]/td[2]').text
        number03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[23]/td[1]').text
        titel04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[24]/td[2]').text
        number04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[24]/td[1]').text
        titel05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[25]/td[2]').text
        number05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[25]/td[1]').text
        titel06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[26]/td[2]').text
        number06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[26]/td[1]').text
        titel07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[27]/td[2]').text
        number07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[27]/td[1]').text
        titel08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[28]/td[2]').text
        number08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[28]/td[1]').text
        titel09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[29]/td[2]').text
        number09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[29]/td[1]').text
        itemlist.append(titel01)
        itemlist.append(number01)
        itemlist.append(titel02)
        itemlist.append(number02)
        itemlist.append(titel03)
        itemlist.append(number03)
        itemlist.append(titel04)
        itemlist.append(number04)
        itemlist.append(titel05)
        itemlist.append(number05)
        itemlist.append(titel06)
        itemlist.append(number06)
        itemlist.append(titel07)
        itemlist.append(number07)
        itemlist.append(titel08)
        itemlist.append(number08)
        itemlist.append(titel09)
        itemlist.append(number09)
        return itemlist
    
    def energy(self):
        itemlist=[]
        titel01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[52]/td[2]').text[:-8]
        number01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[52]/td[1]').text
        titel02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[53]/td[2]').text[4:]
        number02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[53]/td[1]').text
        titel03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[54]/td[2]').text[4:]
        number03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[54]/td[1]').text
        titel04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[55]/td[2]').text[:-5]
        number04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[55]/td[1]').text
        titel05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[56]/td[2]').text
        number05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[56]/td[1]').text
        titel06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[57]/td[2]').text
        number06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[57]/td[1]').text
        titel07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[59]/td[2]').text
        number07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[59]/td[1]').text
        titel08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[60]/td[2]').text
        number08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[60]/td[1]').text
        titel09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[63]/td[2]').text
        number09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[63]/td[1]').text
        itemlist.append(titel01.split('，')[0])
        itemlist.append(number01)
        itemlist.append(titel02)
        itemlist.append(number02)
        itemlist.append(titel03)
        itemlist.append(number03)
        itemlist.append(titel04)
        itemlist.append(number04)
        itemlist.append(titel05)
        itemlist.append(number05)
        itemlist.append(titel06)
        itemlist.append(number06)
        itemlist.append(titel07)
        itemlist.append(number07)
        itemlist.append(titel08)
        itemlist.append(number08)
        itemlist.append(titel09)
        itemlist.append(number09)
        return itemlist
    
    def health(self):
        itemlist=[]
        titel01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[67]/td[2]').text
        number01=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[67]/td[1]').text
        titel02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[68]/td[2]').text
        number02=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[68]/td[1]').text
        titel03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[69]/td[2]').text
        number03=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[69]/td[1]').text
        titel04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[72]/td[2]').text
        number04=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[72]/td[1]').text
        titel05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[73]/td[2]').text
        number05=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[73]/td[1]').text
        titel06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[75]/td[2]').text
        number06=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[75]/td[1]').text
        titel07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[78]/td[2]').text
        number07=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[78]/td[1]').text
        titel08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[79]/td[2]').text
        number08=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[79]/td[1]').text
        titel09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[80]/td[2]').text
        number09=self.web.find_element(By.XPATH,'//*[@id="tablemore"]/tbody/tr[80]/td[1]').text
        itemlist.append(titel01)
        itemlist.append(number01)
        itemlist.append(titel02)
        itemlist.append(number02)
        itemlist.append(titel03)
        itemlist.append(number03)
        itemlist.append(titel04)
        itemlist.append(number04)
        itemlist.append(titel05)
        itemlist.append(number05)
        itemlist.append(titel06)
        itemlist.append(number06)
        itemlist.append(titel07)
        itemlist.append(number07)
        itemlist.append(titel08)
        itemlist.append(number08)
        itemlist.append(titel09)
        itemlist.append(number09)
        return itemlist

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec())    
