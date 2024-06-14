from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

class MainScreen(Screen): # ui 1
    pass

class Register(Screen): 
    def check(self):
        id_card = self.ids.id_card.text
        phon_num = self.ids.phon_num.text

        if len(id_card) != 13 or len(phon_num) !=10:
            self. ids .btn_regis.text = "ไม่พร้อมบันทึกข้อมูล"
        
        else:
            self.ids .btn_regis.text = "พร้อมบันทึกข้อมูล"

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class dltApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    dltApp().run()