from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager


class Scr_knowledge(Screen): 
    pass

class Scr_bmi(Screen): # ui 1
    def cal_bmi(self): #ค่า bmi =นน/สส*สส
        weight=float(self.ids.txt_weight.text)
        height=float(self.ids.txt_height.text)
        height=height/100

        bmi=weight/(height*height)
        self.ids.lbl_bmi.text=str(bmi)
        if bmi > 35:
            self.ids.lbl_bmi.color="red"
            self.ids.img_bmi.source="pic/5.PNG"
        elif bmi > 30:
            self.ids.lbl_bmi.color="orange"
            self.ids.img_bmi.source="pic/4.PNG"
        elif bmi > 25:
            self.ids.lbl_bmi.color="yellow"
            self.ids.img_bmi.source="pic/3.PNG"
        elif bmi > 18:
            self.ids.lbl_bmi.color="blue"
            self.ids.img_bmi.source="pic/2.PNG"           
        else:
            self.ids.lbl_bmi.color="green"
            self.ids.img_bmi.source="pic/1.PNG"    

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class bmiApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    bmiApp().run()