import os
import re
import sqlite3
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
psoupquan = suyaquan = moimoiquan = akaraquan = plantainquan = dodoquan = nkwobiquan = 1
isiquan = jollofquan = friedquan = ebaquan = pyamquan = amalaquan = ofadaquan = 1
beansquan = bannerquan = zoboquan = palmquan = capquan = fantaquan = kunuquan = 1
waterquan = guinessquan = maltquan = meatpiequan = rollsquan = puffquan = scotchquan = 1
bunsquan = yamquan = eggquan = sausagesquan = 1
totall = 0
activeuser = "None"
quantities = None
path = "../db/userdata.db"
conn = sqlite3.connect(path)
local = conn.cursor()
local.execute('''
                CREATE TABLE IF NOT EXISTS userdata(
                Username TEXT PRIMARY KEY,
                Password TEXT,
                Email TEXT,
                Date TEXT,
                FromCurrency TEXT,
                ToCurrency TEXT,
                Rate TEXT
                )
                                ''')
conn.close()

class SoMain(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = "../re/skins/skins.ui"
        uic.loadUi(ui_path, self)
        self.setFixedSize(881, 451)
        self.setWindowTitle('Ofido-Foods')
        self.loinscreen()
        self.cart_items = []

    def startup(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'Landing'):
            self.stackedWidget.setCurrentWidget(self.Landing)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.loadall()
        self.menubtn.clicked.connect(self.food_menu)
        self.pushButton_5.clicked.connect(self.printcart)

    def loadall(self):
        # <--------------pictures-------------->
        self.peperpic.setPixmap(
            QtGui.QPixmap("../re/icons/9e01e1d8-b222-4159-be9c-d76d807344a9 (1).jpg"))
        self.label_17.setPixmap(
            QtGui.QPixmap("../re/icons/5a367633-80c9-42ae-8495-19961467af58.jpg"))
        self.label_20.setPixmap(
            QtGui.QPixmap("../re/icons/ba57865f-6b56-4b38-b9fc-468819cd007b.jpg"))
        self.label_23.setPixmap(
            QtGui.QPixmap("../re/icons/8295ad43-746f-4712-8179-778dd2dd9169.jpg"))
        self.label_50.setPixmap(
            QtGui.QPixmap("../re/icons/898c7e3e-61df-422b-9e90-bd38e84e0aec.jpg"))
        self.label_47.setPixmap(
            QtGui.QPixmap("../re/icons/9693c129-af60-491d-8a62-6449a2b65e20.png"))
        self.label_44.setPixmap(
            QtGui.QPixmap("../re/icons/7db2090a-6450-498f-9689-926166b015b2.jpg"))
        self.label_41.setPixmap(
            QtGui.QPixmap("../re/icons/7c5ef53e-cd7c-4dbd-b50e-b345c2f0cfbc.jpg"))
        self.label_56.setPixmap(
            QtGui.QPixmap("../re/icons/bb5796b7-882c-4ff4-8c99-0287d9767e42.jpg"))
        self.label_59.setPixmap(
            QtGui.QPixmap("../re/icons/df43c5fd-ece3-4f4d-9fd4-de87828f1523.jpg"))
        self.label_62.setPixmap(
            QtGui.QPixmap("../re/icons/fa9ce99d-8243-49dc-8f99-cfd569782a8d.jpg"))
        self.label_65.setPixmap(
            QtGui.QPixmap("../re/icons/9261e4cf-4961-4a6f-9aa4-1b1167551a37.jpg"))
        self.label_68.setPixmap(
            QtGui.QPixmap("../re/icons/1086c733-3e72-4294-a150-a005a9ead753.jpg"))
        self.label_71.setPixmap(
            QtGui.QPixmap("../re/icons/e69fe91d-6ee6-49a9-a7de-1e037b7b29c2.jpg"))
        self.label_74.setPixmap(
            QtGui.QPixmap("../re/icons/f7c80f87-b358-4d47-8807-10dc1f03350a.jpg"))
        self.label_77.setPixmap(
            QtGui.QPixmap("../re/icons/29f9eba2-0afa-4904-bd40-7ddd45ec9d0c.jpg"))
        self.label_83.setPixmap(
            QtGui.QPixmap("../re/icons/c4307a85-08dd-49d2-8221-2ded5b0b4697.png"))
        self.label_86.setPixmap(
            QtGui.QPixmap("../re/icons/71323c86-199d-439f-b6d1-4d564162452a.jpg"))
        self.label_89.setPixmap(
            QtGui.QPixmap("../re/icons/521b7fb8-b3dd-4127-bb70-9647347a8d06.jpg"))
        self.label_92.setPixmap(
            QtGui.QPixmap("../re/icons/fd205ea0-0a1d-4dec-a716-54069ec091ab.jpg"))
        self.label_95.setPixmap(
            QtGui.QPixmap("../re/icons/5ec8b8b8-0778-4cf6-95ef-b978cb48c6fb.jpg"))
        self.label_98.setPixmap(
            QtGui.QPixmap("../re/icons/a24e4c5f-5fba-446a-a505-5cd364ad29be.jpg"))
        self.label_101.setPixmap(
            QtGui.QPixmap("../re/icons/918ba150-8363-4417-b2e2-6080a8233c15.jpg"))
        self.label_104.setPixmap(
            QtGui.QPixmap("../re/icons/0a0d3ce3-cf95-427e-9c1d-16ff6502fac2.jpg"))
        self.label_110.setPixmap(
            QtGui.QPixmap("../re/icons/1efe61d7-b8f1-4122-bd4b-611a366a7c85.jpg"))
        self.label_113.setPixmap(
            QtGui.QPixmap("../re/icons/94947354-9355-47f0-9861-1f13670c2dbd.jpg"))
        self.label_116.setPixmap(
            QtGui.QPixmap("../re/icons/d4f6665c-05f6-4312-9626-828d5f39cb99.jpg"))
        self.label_119.setPixmap(
            QtGui.QPixmap("../re/icons/c6ccd52c-56d6-4035-96c9-5349930116da.jpg"))
        self.label_122.setPixmap(
            QtGui.QPixmap("../re/icons/39cb00bc-a2b9-4f7d-b7a4-c7cb7fd8706f.jpg"))
        self.label_125.setPixmap(
            QtGui.QPixmap("../re/icons/498d9bac-e24e-498e-a6d6-aea58ca3c3e3.jpg"))
        self.label_128.setPixmap(
            QtGui.QPixmap("../re/icons/c3e2efe9-396c-4a5c-a4aa-0d28b3a5ecf2.jpg"))
        self.label_131.setPixmap(
            QtGui.QPixmap("../re/icons/a56714e4-3634-4e23-84b2-93048fa470c7.jpg"))
        self.label_9.setPixmap(
            QtGui.QPixmap("../re/icons/be06c705-eb16-4fde-86aa-962b039a379c.jpg"))

        # <------------ICONS-------------->
        icon = QIcon("../re/icons/smile-beam.png")
        self.userbtn.setIcon(icon)
        icon2 = QIcon("../re/icons/minus-hexagon.png")
        self.psoupminus.setIcon(icon2)
        icon3 = QIcon("../re/icons/plus-hexagon.png")
        self.psoupplus.setIcon(icon3)
        self.suyaminus.setIcon(icon2)
        self.suyaplus.setIcon(icon3)
        self.moimoiminus.setIcon(icon2)
        self.moiomoiplus.setIcon(icon3)
        self.akaraminus.setIcon(icon2)
        self.akaraplus.setIcon(icon3)
        self.plantainminus.setIcon(icon2)
        self.plantainplus.setIcon(icon3)
        self.dodominus.setIcon(icon2)
        self.dodplus.setIcon(icon3)
        self.nkowminus.setIcon(icon2)
        self.nkowplus.setIcon(icon3)
        self.isiminus.setIcon(icon2)
        self.isiplus.setIcon(icon3)
        self.jollofminus.setIcon(icon2)
        self.jollofplus.setIcon(icon3)
        self.friedminus.setIcon(icon2)
        self.friedplus.setIcon(icon3)
        self.ebaminus.setIcon(icon2)
        self.ebaplus.setIcon(icon3)
        self.pyamminus.setIcon(icon2)
        self.pyamplus.setIcon(icon3)
        self.amalaminus.setIcon(icon2)
        self.amalaplus.setIcon(icon3)
        self.ofadminus.setIcon(icon2)
        self.ofadaplus.setIcon(icon3)
        self.beanminus.setIcon(icon2)
        self.beanplus.setIcon(icon3)
        self.banerminus.setIcon(icon2)
        self.banerplus.setIcon(icon3)
        self.zobominus.setIcon(icon2)
        self.zoboplus.setIcon(icon3)
        self.palmminus.setIcon(icon2)
        self.plamplus.setIcon(icon3)
        self.capminus.setIcon(icon2)
        self.capplus.setIcon(icon3)
        self.fantaminus.setIcon(icon2)
        self.fantaplus.setIcon(icon3)
        self.kunuminus.setIcon(icon2)
        self.kunuplus.setIcon(icon3)
        self.waterminus.setIcon(icon2)
        self.waterplus.setIcon(icon3)
        self.guinessminus.setIcon(icon2)
        self.guinessplus.setIcon(icon3)
        self.maltminus.setIcon(icon2)
        self.maltplus.setIcon(icon3)
        self.meatpieminus.setIcon(icon2)
        self.meatpieplus.setIcon(icon3)
        self.rollsminus.setIcon(icon2)
        self.rollsplus.setIcon(icon3)
        self.puffminus.setIcon(icon2)
        self.puffplus.setIcon(icon3)
        self.scotcminus.setIcon(icon2)
        self.scotcplus.setIcon(icon3)
        self.bunsminus.setIcon(icon2)
        self.bunsplus.setIcon(icon3)
        self.yamminus.setIcon(icon2)
        self.yamplus.setIcon(icon3)
        self.eggminus.setIcon(icon2)
        self.eggplus.setIcon(icon3)
        self.sussminus.setIcon(icon2)
        self.sussplus.setIcon(icon3)

    def food_menu(self):
        try:
            if hasattr(self, 'stackedWidget') and hasattr(self, 'Starters'):
                self.stackedWidget.setCurrentWidget(self.Starters)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
            self.btnconnect()
        except Exception as e:
            print(e)

    def btnconnect(self):
        self.maindiss.clicked.connect(self.main_dish_menu)
        self.back1.clicked.connect(self.startup)
        self.drinksbtn.clicked.connect(self.drinks_menu)
        self.snacksbtn.clicked.connect(self.snacks_menu)
        self.psoupplus.clicked.connect(lambda: self.addtoquan('psoupquan'))
        self.psoupminus.clicked.connect(lambda: self.removequan('psoupquan'))
        self.suyaplus.clicked.connect(lambda: self.addtoquan('suyaquan'))
        self.suyaminus.clicked.connect(lambda: self.removequan('suyaquan'))
        self.moiomoiplus.clicked.connect(lambda: self.addtoquan('moimoiquan'))
        self.moimoiminus.clicked.connect(lambda: self.removequan('moimoiquan'))
        self.akaraplus.clicked.connect(lambda: self.addtoquan('akaraquan'))
        self.akaraminus.clicked.connect(lambda: self.removequan('akaraquan'))
        self.plantainplus.clicked.connect(lambda: self.addtoquan('plantainquan'))
        self.plantainminus.clicked.connect(lambda: self.removequan('plantainquan'))
        self.dodplus.clicked.connect(lambda: self.addtoquan('dodoquan'))
        self.dodominus.clicked.connect(lambda: self.removequan('dodoquan'))
        self.nkowplus.clicked.connect(lambda: self.addtoquan('nkwobiquan'))
        self.nkowminus.clicked.connect(lambda: self.removequan('nkwobiquan'))
        self.isiplus.clicked.connect(lambda: self.addtoquan('isiquan'))
        self.isiminus.clicked.connect(lambda: self.removequan('isiquan'))
        self.suyacart.clicked.connect(self.suya_cart)
        self.cartbtn.clicked.connect(self.printcart)
        self.nkowbicart.clicked.connect(self.nsoup_cart)
        self.moimoicart.clicked.connect(self.moimoi_cart)
        self.akaracart.clicked.connect(self.akara_cart)
        self.isicart.clicked.connect(self.isi_cart)
        self.dodocart.clicked.connect(self.dodo_cart)
        self.plantainaddtocart.clicked.connect(self.plantain_cart)
        self.psoupaddcart.clicked.connect(self.pepper_cart)

    def printcart(self):
        self.load_cart()

    def snacks_menu(self):
        try:
            if hasattr(self, 'stackedWidget') and hasattr(self, 'Snacks'):
                self.stackedWidget.setCurrentWidget(self.Snacks)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
            self.connectftn()
        except Exception as e:
            print(e)

    def connectftn(self):
        self.mainnnnss.clicked.connect(self.main_dish_menu)
        self.drinkssbtn.clicked.connect(self.drinks_menu)
        self.startersss.clicked.connect(self.food_menu)
        self.back3.clicked.connect(self.startup)
        self.snackcart.clicked.connect(self.printcart)
        self.meatpieplus.clicked.connect(lambda: self.addtoquan('meatpiequan'))
        self.meatpieminus.clicked.connect(lambda: self.removequan('meatpiequan'))
        self.rollsplus.clicked.connect(lambda: self.addtoquan('rollsquan'))
        self.rollsminus.clicked.connect(lambda: self.removequan('rollsquan'))
        self.puffplus.clicked.connect(lambda: self.addtoquan('puffquan'))
        self.puffminus.clicked.connect(lambda: self.removequan('puffquan'))
        self.scotcplus.clicked.connect(lambda: self.addtoquan('scotchquan'))
        self.scotcminus.clicked.connect(lambda: self.removequan('scotchquan'))
        self.bunsplus.clicked.connect(lambda: self.addtoquan('bunsquan'))
        self.bunsminus.clicked.connect(lambda: self.removequan('bunsquan'))
        self.yamplus.clicked.connect(lambda: self.addtoquan('yamquan'))
        self.yamminus.clicked.connect(lambda: self.removequan('yamquan'))
        self.eggplus.clicked.connect(lambda: self.addtoquan('eggquan'))
        self.eggminus.clicked.connect(lambda: self.removequan('eggquan'))
        self.sussplus.clicked.connect(lambda: self.addtoquan('sausagesquan'))
        self.sussminus.clicked.connect(lambda: self.removequan('sausagesquan'))
        self.meatpiecart.clicked.connect(self.meatpie_cart)
        self.rolls.clicked.connect(self.sam_osa)
        self.puffcart.clicked.connect(self.puff_cart)
        self.scrocart.clicked.connect(self.scotch_cart)
        self.bunscart.clicked.connect(self.buns_cart)
        self.yamcart.clicked.connect(self.yam_cart)
        self.eggcart.clicked.connect(self.egg_cart)
        self.susscart.clicked.connect(self.sausages_cart)

    def drinks_menu(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'Drinks'):
            self.stackedWidget.setCurrentWidget(self.Drinks)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.btns()

    def btns(self):
        try:
            self.back2.clicked.connect(self.startup)
            self.starterbtn.clicked.connect(self.food_menu)
            self.drinkcart.clicked.connect(self.printcart)
            self.mainnbtn.clicked.connect(self.main_dish_menu)
            self.snacksbtn_2.clicked.connect(self.snacks_menu)
            self.zoboplus.clicked.connect(lambda: self.addtoquan('zoboquan'))
            self.zobominus.clicked.connect(lambda: self.removequan('zoboquan'))
            self.plamplus.clicked.connect(lambda: self.addtoquan('palmquan'))
            self.palmminus.clicked.connect(lambda: self.removequan('palmquan'))
            self.capplus.clicked.connect(lambda: self.addtoquan('capquan'))
            self.capminus.clicked.connect(lambda: self.removequan('capquan'))
            self.fantaplus.clicked.connect(lambda: self.addtoquan('fantaquan'))
            self.fantaminus.clicked.connect(lambda: self.removequan('fantaquan'))
            self.kunuplus.clicked.connect(lambda: self.addtoquan('kunuquan'))
            self.kunuminus.clicked.connect(lambda: self.removequan('kunuquan'))
            self.waterplus.clicked.connect(lambda: self.addtoquan('waterquan'))
            self.waterminus.clicked.connect(lambda: self.removequan('waterquan'))
            self.guinessplus.clicked.connect(lambda: self.addtoquan('guinessquan'))
            self.guinessminus.clicked.connect(lambda: self.removequan('guinessquan'))
            self.maltplus.clicked.connect(lambda: self.addtoquan('maltquan'))
            self.maltminus.clicked.connect(lambda: self.removequan('maltquan'))
            self.zobocart.clicked.connect(self.zobo_cart)
            self.palmcart.clicked.connect(self.palm_cart)
            self.capmancart.clicked.connect(self.capman_cart)
            self.fantacart.clicked.connect(self.fanta_cart)
            self.kunucart.clicked.connect(self.kunu_cart)
            self.watercart.clicked.connect(self.water_cart)
            self.guinesscart.clicked.connect(self.guiness_cart)
            self.maltcart.clicked.connect(self.malt_cart)
        except Exception as e:
            print(e)

    def main_dish_menu(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'MainDishes'):
            self.stackedWidget.setCurrentWidget(self.MainDishes)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.bttn()

    def bttn(self):
        self.back.clicked.connect(self.startup)
        self.snaccckkssss.clicked.connect(self.snacks_menu)
        self.drrinks.clicked.connect(self.drinks_menu)
        self.pushButton_66.clicked.connect(self.printcart)
        self.startersssss.clicked.connect(self.food_menu)
        self.jollofplus.clicked.connect(lambda: self.addtoquan('jollofquan'))
        self.jollofminus.clicked.connect(lambda: self.removequan('jollofquan'))
        self.friedplus.clicked.connect(lambda: self.addtoquan('friedquan'))
        self.friedminus.clicked.connect(lambda: self.removequan('friedquan'))
        self.ebaplus.clicked.connect(lambda: self.addtoquan('ebaquan'))
        self.ebaminus.clicked.connect(lambda: self.removequan('ebaquan'))
        self.pyamplus.clicked.connect(lambda: self.addtoquan('pyamquan'))
        self.pyamminus.clicked.connect(lambda: self.removequan('pyamquan'))
        self.amalaplus.clicked.connect(lambda: self.addtoquan('amalaquan'))
        self.amalaminus.clicked.connect(lambda: self.removequan('amalaquan'))
        self.ofadaplus.clicked.connect(lambda: self.addtoquan('ofadaquan'))
        self.ofadminus.clicked.connect(lambda: self.removequan('ofadaquan'))
        self.beanplus.clicked.connect(lambda: self.addtoquan('beansquan'))
        self.beanminus.clicked.connect(lambda: self.removequan('beansquan'))
        self.banerplus.clicked.connect(lambda: self.addtoquan('bannerquan'))
        self.banerminus.clicked.connect(lambda: self.removequan('bannerquan'))
        self.jollofcart.clicked.connect(self.jollof_cart)
        self.fieldcart.clicked.connect(self.field_cart)
        self.ebacart.clicked.connect(self.eba_cart)
        self.pyamcart.clicked.connect(self.pyam_cart)
        self.amalacart.clicked.connect(self.amala_cart)
        self.ofadacart.clicked.connect(self.ofada_cart)
        self.beancart.clicked.connect(self.beans_cart)
        self.banercart.clicked.connect(self.banner_cart)

    def addtoquan(self, item):
        try:
            globals()[item] += 1
        except Exception as e:
            print(e)
        self.update_quantity_label(item)

    def removequan(self, item):
        if globals()[item] > 1:
            globals()[item] -= 1
        else:
            globals()[item] = 1
        self.update_quantity_label(item)

    def update_quantity_label(self, item):
        try:
            item_label_map = {
                'psoupquan': self.psoup_label,
                'suyaquan': self.suya_label,
                'moimoiquan': self.moimoi_label,
                'akaraquan': self.akara_label,
                'plantainquan': self.plantain_label,
                'dodoquan': self.dodo_label,
                'nkwobiquan': self.nkwobi_label,
                'isiquan': self.isi_label,
                'jollofquan': self.jollof_label,
                'friedquan': self.fried_label,
                'ebaquan': self.eba_label,
                'pyamquan': self.pyam_label,
                'amalaquan': self.amala_label,
                'ofadaquan': self.ofada_label,
                'beansquan': self.beans_label,
                'bannerquan': self.banner_label,
                'zoboquan': self.zobo_label,
                'palmquan': self.palm_label,
                'capquan': self.cap_label,
                'fantaquan': self.fanta_label,
                'kunuquan': self.kunu_label,
                'waterquan': self.water_label,
                'guinessquan': self.guiness_label,
                'maltquan': self.malt_label,
                'meatpiequan': self.meatpie_label,
                'rollsquan': self.rolls_label,
                'puffquan': self.puff_label,
                'scotchquan': self.scotch_label,
                'bunsquan': self.buns_label,
                'yamquan': self.yam_label,
                'eggquan': self.egg_label,
                'sausagesquan': self.sausages_label,
            }
            if item in item_label_map:
                item_label_map[item].setText(str(globals()[item]))
        except Exception as e:
            print(e)

    def pepper_cart(self):
        global psoupquan
        price = psoupquan * 2000
        itemname = "Suya"
        selected_type = self.comboBox.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, suyaquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Suya Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def suya_cart(self):
        global suyaquan
        price = suyaquan * 1000
        itemname = "Suya"
        selected_type = self.comboBox_2.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, suyaquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Suya Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def moimoi_cart(self):
        global moimoiquan
        price = moimoiquan * 1300
        itemname = "Moi Moi"
        selected_type = self.comboBox_3.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, moimoiquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Moi Moi Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def akara_cart(self):
        global akaraquan
        price = akaraquan * 50
        itemname = "Akara"
        self.cart_items.append((itemname, akaraquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Akara Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def isi_cart(self):
        global isiquan
        price = isiquan * 3000
        itemname = "Isi Ewu"
        selected_type = self.comboBox_9.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, isiquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Isi Ewu Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def dodo_cart(self):
        global dodoquan
        price = dodoquan * 2000
        itemname = "Dodo"
        selected_type = self.comboBox_11.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, dodoquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Dodo Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def plantain_cart(self):
        global plantainquan
        price = plantainquan * 300
        itemname = "Plantain"
        self.cart_items.append((itemname, plantainquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Plantain Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def nsoup_cart(self):
        global nkwobiquan
        price = nkwobiquan * 2500
        itemname = "Nkwobi Soup"
        selected_type = self.comboBox_10.currentText()
        if selected_type == "Select One":
            msgr = QMessageBox()
            msgr.setIcon(QMessageBox.Warning)
            msgr.setWindowTitle("Invalid Selection")
            msgr.setText("Please select a valid type.")
            msgr.setStandardButtons(QMessageBox.Ok)
            msgr.exec_()
        else:
            self.cart_items.append((itemname, nkwobiquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Nkwobi Soup Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def jollof_cart(self):
        global jollofquan
        price = jollofquan * 2500
        itemname = "Jollof Rice"
        selected_type = self.comboBox_4.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, jollofquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Jollof Rice Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def field_cart(self):
        global friedquan
        price = friedquan * 2500
        itemname = "Fried Rice"
        selected_type = self.comboBox_12.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, friedquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Fried Rice Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def eba_cart(self):
        global ebaquan
        price = ebaquan * 2500
        itemname = "Eba"
        self.cart_items.append((itemname, ebaquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Eba Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def pyam_cart(self):
        global pyamquan
        price = pyamquan * 5000
        itemname = "Pounded yam"
        self.cart_items.append((itemname, pyamquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Pounded yam Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def amala_cart(self):
        global amalaquan
        price = amalaquan * 3800
        itemname = "Amala"
        self.cart_items.append((itemname, amalaquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Amala Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def ofada_cart(self):
        global ofadaquan
        price = ofadaquan * 3000
        itemname = "Ofada Rice"
        self.cart_items.append((itemname, ofadaquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Ofada Rice Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def beans_cart(self):
        global beansquan
        price = beansquan * 2000
        itemname = "Beans"
        self.cart_items.append((itemname, beansquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Beans Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def banner_cart(self):
        global bannerquan
        price = bannerquan * 500
        itemname = "Banger Soup"
        selected_type = self.comboBox_16.currentText()
        if selected_type == "Select One":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, bannerquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Banger Soup Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def zobo_cart(self):
        global zoboquan
        price = zoboquan * 200
        itemname = "Zobo"
        self.cart_items.append((itemname, zoboquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Zobo Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def palm_cart(self):
        global palmquan
        price = palmquan * 500
        itemname = "Palm Wine"
        self.cart_items.append((itemname, palmquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Palm Wine Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def capman_cart(self):
        global capquan
        price = capquan * 300
        itemname = "Cap Man"
        self.cart_items.append((itemname, capquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Cap Man Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def fanta_cart(self):
        global fantaquan
        price = fantaquan * 350
        itemname = "Fanta"
        self.cart_items.append((itemname, fantaquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Fanta Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def kunu_cart(self):
        global kunuquan
        price = kunuquan * 400
        itemname = "Kunu"
        self.cart_items.append((itemname, kunuquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Kunu Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def water_cart(self):
        global waterquan
        price = waterquan * 200
        itemname = "Water"
        self.cart_items.append((itemname, waterquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Water Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def guiness_cart(self):
        global guinessquan
        price = guinessquan * 1500
        itemname = "Guinness"
        self.cart_items.append((itemname, guinessquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Guinness Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def malt_cart(self):
        global maltquan
        price = maltquan * 400
        itemname = "Malt"
        self.cart_items.append((itemname, maltquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Malt Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def meatpie_cart(self):
        global meatpiequan
        price = meatpiequan * 800
        itemname = "Meat Pie"
        selected_type = self.comboBox_23.currentText()
        if selected_type == "Select Type":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, meatpiequan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Meat Pie Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def puff_cart(self):
        global puffquan
        price = puffquan * 500
        itemname = "Puff Puff"
        self.cart_items.append((itemname, puffquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Puff Puff Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def sam_osa(self):
        global rollsquan
        price = rollsquan * 2500
        itemname = "Samosa"
        self.cart_items.append((itemname, rollsquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Samosa Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def scotch_cart(self):
        global scotchquan
        price = scotchquan * 500
        itemname = "Scotch"
        self.cart_items.append((itemname, scotchquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Scotch Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def buns_cart(self):
        global bunsquan
        price = bunsquan * 500
        itemname = "Buns"
        self.cart_items.append((itemname, bunsquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Buns Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def yam_cart(self):
        global yamquan
        price = yamquan * 700
        itemname = "Yam"
        selected_type = self.comboBox_26.currentText()
        if selected_type == "Select Side":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid type.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, yamquan, selected_type, price))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("Yam Added")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def egg_cart(self):
        global eggquan
        price = eggquan * 500
        itemname = "Egg Rolls"
        self.cart_items.append((itemname, eggquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Egg Rolls Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def sausages_cart(self):
        global sausagesquan
        price = sausagesquan * 500
        itemname = "Sausage Roll"
        self.cart_items.append((itemname, sausagesquan, None, price))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Done")
        msg.setText("Sausage Roll Added")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_cart(self):
        try:
            if hasattr(self, 'stackedWidget') and hasattr(self, 'cart'):
                self.stackedWidget.setCurrentWidget(self.cart)
            else:
                print("stackedWidget or cart not found in the UI file")
            self.menubtn_2.clicked.connect(self.food_menu)
            self.settable()
            self.cart_table.setColumnCount(4)
            self.cart_table.setHorizontalHeaderLabels(["Item Name", "Quantity", "Type/Side", "Price"])
            self.cart_table.setRowCount(0)
            print("Current Cart Items:", self.cart_items)
            row_height = 120
            for row_number, (item_name, quantity, type, price) in enumerate(self.cart_items):
                self.cart_table.insertRow(row_number)
                self.cart_table.setRowHeight(row_number, row_height)
                self.cart_table.setItem(row_number, 0, QTableWidgetItem(item_name))
                self.cart_table.setItem(row_number, 1, QTableWidgetItem(str(quantity)))
                self.cart_table.setItem(row_number, 2, QTableWidgetItem(type))
                self.cart_table.setItem(row_number, 3, QTableWidgetItem(str(price)))
                self.calculate_total()
        except Exception as e:
            print(e)

    def calculate_total(self):
        global totall
        total = 0.0
        for item in self.cart_items:
            price = item[3]
            total += price
        formatted_total = f"{total:,.2f}"
        totall = formatted_total
        self.label_4.setText(f"Total: ₦{formatted_total}")
        return total

    def settable(self):
        self.cart_table.setColumnWidth(0, 200)
        self.cart_table.setColumnWidth(1, 200)
        self.cart_table.setColumnWidth(2, 200)
        self.cart_table.setColumnWidth(3, 135)
        self.cart_table.setEditTriggers(QTableWidget.NoEditTriggers)

    def loinscreen(self):
        global activeuser
        activeuser = "None"
        try:
            if hasattr(self, 'stackedWidget') and hasattr(self, 'Login'):
                self.stackedWidget.setCurrentWidget(self.Login)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
            self.validate.clicked.connect(self.logvalid)
            self.new_2.clicked.connect(self.new__account)
        except Exception as e:
            print(e)

    def new__account(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'Signup'):
            self.stackedWidget.setCurrentWidget(self.Signup)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.newaccount.clicked.connect(self.accountcreate)
        self.cancel_2.clicked.connect(self.loinscreen)

    def logvalid(self):
        global userr
        user = self.user.text()
        passkey = self.password.text()
        try:
            path = "../db/userdata.db"
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM userdata WHERE Username = ? AND Password = ?", (user, passkey))
            result = cursor.fetchone()
            if result:
                self.yes()
                userr = user
            else:
                self.no()
            conn.close()
        except Exception as e:
            print(e)

    def no(self):
        self.label_28.setText("Incorrect username or password")

    def yes(self):
        global activeuser
        activeuser = "Yes"
        self.startup()

    def accountcreate(self):
        try:
            username = self.user_3.text()
            email = self.email.text()
            passkey = self.password_2.text()
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            reset_error = ("""background-color: transparent;
padding-bottom: -3;
border: 0;
font: 12pt "Agency FB";""")
            reset_style = """border-radius: 20px;
padding-left: 20px;
font: 75 12pt "Agency FB";
font-weight: bold;"""
            fields = """border-radius: 20px;
padding-left: 20px;
color: red;
font: 75 12pt "Agency FB";
font-weight: bold;"""
            error_style = """color: red; border: 0px; font: 75 12pt "Agency FB";"""

            if not username:
                self.user_3.setStyleSheet(fields)
                self.label_22.setText("Username must not be empty")
                self.label_22.setStyleSheet(error_style)
                QTimer.singleShot(2000, lambda: self.label_22.setText("Create a new account"))
                QTimer.singleShot(2000, lambda: self.user_3.setStyleSheet(reset_style))
                QTimer.singleShot(2000, lambda: self.label_22.setStyleSheet(reset_error))
                return False

            if not email:
                self.email.setStyleSheet(fields)
                self.label_22.setText("Email must not be empty")
                self.label_22.setStyleSheet(error_style)
                QTimer.singleShot(2000, lambda: self.label_22.setText("Create a new account"))
                QTimer.singleShot(2000, lambda: self.email.setStyleSheet(reset_style))
                QTimer.singleShot(2000, lambda: self.label_22.setStyleSheet(reset_error))
                return False

            if not re.match(email_regex, email):
                self.label_22.setText("Invalid email format")
                self.email.setStyleSheet(fields)
                self.label_22.setStyleSheet(error_style)
                QTimer.singleShot(2000, lambda: self.label_22.setText("Create a new account"))
                QTimer.singleShot(2000, lambda: self.email.setStyleSheet(reset_style))
                QTimer.singleShot(2000, lambda: self.label_22.setStyleSheet(reset_error))
                return False

            if not passkey or len(passkey) < 6:
                self.password_2.setStyleSheet(fields)
                self.label_22.setText("Password must be at least 6 characters long")
                self.label_22.setStyleSheet(error_style)
                QTimer.singleShot(2000, lambda: self.label_22.setText("Create a new account"))
                QTimer.singleShot(2000, lambda: self.password_2.setStyleSheet(reset_style))
                QTimer.singleShot(2000, lambda: self.label_22.setStyleSheet(reset_error))
                return False
        except Exception as e:
            print(e)
        self.createuser()
        print("Success")

    def createuser(self):
        username = self.user_3.text()
        email = self.email.text()
        passkey = self.password_2.text()
        try:
            path2 = "../db/userdata.db"
            conn = sqlite3.connect(path2)
            local = conn.cursor()
            local.execute('''
                    INSERT INTO userdata (Username, Password, Email)
                    VALUES (?, ?, ?);
                ''', (username, passkey, email))
            self.loinscreen()
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoMain()
    window.show()
    sys.exit(app.exec_())
