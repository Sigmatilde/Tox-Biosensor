#!/usr/bin/kivy
__version__ = "1.0"

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Canvas, Translate, Fbo, ClearColor, ClearBuffers
from kivy.properties import ObjectProperty 
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.checkbox import CheckBox
from kivy.logger import Logger
from kivy.clock import Clock
from kivy.graphics import Color, Line
from math import cos, sin, pi
from kivy.lang import Builder
from plyer import camera
from PIL import Image as pixel
from PIL import ImageStat
import os
import time
import datetime



class LoadDialog(BoxLayout):
    """Instance is a controller for a LoadDialog, a pop-up dialog to load a file.

    The View for this controller is defined in biosensor.kv."""
    filechooser = ObjectProperty(None)
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(BoxLayout):
    """Instance is a controller for a SaveDialog, a pop-up dialog to load a file.

    The View for this controller is defined in biosensor.kv."""
    text_input = ObjectProperty(None)
    savefile = ObjectProperty(None)
    cancel = ObjectProperty(None)
    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self._dismiss_popup()

    def show_save(self, *largs):
        content = SaveDialog(save=self.save, cancel=self._dismiss_popup)
        self._popup = Popup(title="Save file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()
    
    def _dismiss_popup(self):
        """Used to dismiss the currently active pop-up"""
        self.popup.dismiss()



class AddLocationForm(FloatLayout):
    icon = 'logo.png'
    hidden_text = ObjectProperty(None)
    text_input = ObjectProperty(None)
    progress_bar = ObjectProperty()
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    minutes = StringProperty()
    seconds = StringProperty()
    running = BooleanProperty(False)

    _operand = None # current executing option
    _op_args = None # arguments for the executing option
     
    def start(self, *latgs):
        self.clear_widgets()
        page= BoxLayout(orientation='vertical')
        self.add_widget(page)
        pict=Image(source='./logo.png',size_hint=(1, .3),pos_hint={'center_x': .5, 'center_y': .8})
        button1=Button(text='Test sample', bold=True, background_normal='bottone3.png', font_size='18sp', size_hint=(0.22,0.12), pos_hint={'center_x':.5,'center_y':.40})
        button1.bind(on_press=self.camerabutton)
        button2=Button(text='Select image', bold=True, background_normal='bottone3.png',font_size='18sp',size_hint=(0.22,0.12),pos_hint={'center_x':.5, 'center_y':.25})
        button2.bind(on_press=self.choosebutton)
        button3=Button(text='Procedure', bold=True, background_normal='bottone3.png',font_size='18sp',size_hint=(0.22,0.12),pos_hint={'center_x': .5, 'center_y': .55})
        button3.bind(on_press=self.howitworksbutton)
        button4=Button(text='info', bold=True,background_normal='trasp.png',font_size='18sp',size_hint=(0.22,0.12),pos_hint={'center_x': .5, 'center_y': .08})
        button4.bind(on_press=self.infobutton)
        self.add_widget(pict)
        self.add_widget(button2)
        self.add_widget(button3)
        self.add_widget(button4)
        self.add_widget(button1)

    def done(self, e): #receive e as the image location
        self.lblCam.text = e; #update the label to the image location
        img=Image(source=(e), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(img)
    
    def camerabutton(self, e):
        camera.take_picture('/storage/sdcard/screenshot%(counter)04d.jpg', self.done)
        
    
    def show_save(self, *largs):
        content = SaveDialog(save=self.save, cancel=self._dismiss_popup)
        self._popup = Popup(title="Save file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self._dismiss_popup()


    def howitworksbutton(self, *latgs):
        page= Widget()
        self.clear_widgets()
        self.add_widget(page)
        button1=Button(text='Home',background_normal='bottone3.png', size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
        button1.bind(on_press=self.start)
        self.add_widget(button1)
        label1=Label(text='1) Assemble the smartphone adaptor \n\n2) Add sample to T1-T2 wells \n\n3) Incubate 30 min \n\n4) Add BL substrate \n\n5) Insert cartridge into the adaptor \n\n6) Acquire BL image & Read result', color=(1, 1, 1, .9), font_size='15sp', pos_hint={'center_x': .24, 'center_y': .56})
        self.add_widget(label1)
        button2=Image(source='./app1-2.png',size_hint=(0.15,0.21), pos_hint={'center_x': .7, 'center_y': .75})
        self.add_widget(button2)
        button3=Image(source='./app2-1.png',size_hint=(0.20,0.26),pos_hint={'center_x': .85, 'center_y': .77})
        self.add_widget(button3)
        button4=Image(source='./app3-2.png',size_hint=(0.15,0.21), pos_hint={'center_x': .7, 'center_y': .52})
        self.add_widget(button4)
        button5=Image(source='./app4-2.png',size_hint=(0.20,0.26), pos_hint={'center_x': .85, 'center_y': .50})
        self.add_widget(button5)
        button6=Image(source='./app8-2.png',size_hint=(0.25,0.31), pos_hint={'center_x': .78, 'center_y': .2})
        self.add_widget(button6)
        button4=Button(text='Begin',background_normal='bottone3.png',size_hint=(0.21,0.11),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
        button4.bind(on_press=self.analysis)
        self.add_widget(button4)
        label=Button(text='Procedure',background_normal='bottone3.png', size_hint=(0.31,0.12), bold=True, font_size='20sp', color=(1, 1, 1, .9), valign='top', pos_hint={'center_x': .5, 'center_y': .92})
        pict=Image(source='./logo.png',size_hint=(1, .16),pos_hint={'center_x': .68, 'center_y': .92})
        self.add_widget(label)
        self.add_widget(pict)
    
    def analysis(self, *latgs):
        self.clear_widgets()
        label=Button(text=' Checklist ',background_normal='bottone3.png', size_hint=(0.31,0.14), bold=True, font_size='20sp', color=(1, 1, 1, .9), valign='top', pos_hint={'center_x': .5, 'center_y': .92})
        pict=Image(source='./logo.png',size_hint=(1, .16),pos_hint={'center_x': .68, 'center_y': .92})
        self.add_widget(label)
        self.add_widget(pict)
        label1=Label(text='Assembled Device \n\nSample Added \n\nBL Substrate Added \n\nCartridge inserted', color=(1, 1, 1, .9), font_size='15sp', pos_hint={'center_x': .24, 'center_y': .56})
        checkbox = CheckBox(pos_hint={'center_x': .10, 'center_y': .61})
        checkbox1 = CheckBox(pos_hint={'center_x': .10, 'center_y': .51})
        checkbox.bind(active=self.on_checkbox_active)
        button4=Button(text='Acquire',background_normal='bottone3.png',size_hint=(0.21,0.11),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
        self.add_widget(button4)
        button4.bind(on_press=self.camerabutton)
        self.add_widget(label1)
        self.add_widget(checkbox1)
        self.add_widget(checkbox)
        button1=Button(text='Home',background_normal='bottone3.png', size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
        button1.bind(on_press=self.start)
        self.add_widget(button1)
        


    def on_checkbox_active(self, checkbox, value):
        #delta = datetime.datetime.now()+datetime.timedelta(1, 60*30)
        delta = "30:00"
        hour_string = str(delta)
        self.minutes = hour_string.split(':')[0]
        self.seconds = hour_string.split(':')[1]
        if value:
            label3=Label(text="TIMER", font_size= 20, color=(0, 0, 0, .9), bold=True, pos_hint={'center_x': .703, 'center_y': .62}) #verdecolor=(0, 1, 0, .9)
            label2=Label(text= "%s:%s" % (self.minutes, self.seconds), font_size= 32, pos_hint={'center_x': .7, 'center_y': .545})
            label4=Label(text= "Minutes   Seconds", font_size= 12,color=(0, 0, 0, .9), pos_hint={'center_x': .7, 'center_y': .59})
            rec=Button(size_hint=(0.28,0.20),pos_hint={'center_x': .66, 'center_y': .57},background_normal='bottone3.png')
            pict=Image(source='./hourglass_blue_T.png',size_hint=(1, .16),pos_hint={'center_x': .58, 'center_y': .575})
            self.add_widget(rec)
            self.add_widget(label2)
            self.add_widget(label3)
            self.add_widget(label4)
            self.add_widget(pict)

            self.seconds=str(60)
            while int(self.minutes)<=30:
                os.system
                print self.minutes, " minutes", self.seconds," seconds"
                time.sleep(1)
                if (int(self.minutes)!=0 or int(self.seconds)!=0):
                    self.seconds=str(int(self.seconds)-1)
                    if int(self.seconds)==00:
                        if int(self.minutes)>0:
                            self.minutes=str(int(self.minutes)-1)
                            self.seconds=str(60)
                        if int(self.minutes)==0:
                            self.minutes=str(0)
                else:
                    break
            
            
        else:
            self.clear_widgets()
            label=Button(text=' Checklist ',background_normal='bottone3.png', size_hint=(0.31,0.14), bold=True, font_size='20sp', color=(1, 1, 1, .9), valign='top', pos_hint={'center_x': .5, 'center_y': .92})
            pict=Image(source='./logo.png',size_hint=(1, .16),pos_hint={'center_x': .68, 'center_y': .92})
            self.add_widget(label)
            self.add_widget(pict)
            label1=Label(text='Assembled Device \n\nSample Added \n\nBL Substrate Added \n\nCartridge inserted', color=(1, 1, 1, .9), font_size='15sp', pos_hint={'center_x': .24, 'center_y': .56})
            checkbox = CheckBox(pos_hint={'center_x': .10, 'center_y': .61})
            checkbox.bind(active=self.on_checkbox_active)
            self.add_widget(label1)
            self.add_widget(checkbox)
            checkbox1 = CheckBox(pos_hint={'center_x': .10, 'center_y': .51})
            checkbox1.bind(active=self.on_checkbox_active1)
            self.add_widget(checkbox1)
            button4=Button(text='Acquire',background_normal='bottone3.png',size_hint=(0.21,0.11),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
            self.add_widget(button4)
            button4.bind(on_press=self.camerabutton)
            button1=Button(text='Home',background_normal='bottone3.png', size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
            button1.bind(on_press=self.start)
            self.add_widget(button1)

    def on_checkbox_active1(self, checkbox1, value):
        delta= "00:30"
        hour_string = str(delta)
        self.minutes = hour_string.split(':')[0]
        self.seconds = hour_string.split(':')[1]
        if value:
            label5=Label(text="TIMER", font_size= 20, color=(0, 0, 0, .9), bold=True, pos_hint={'center_x': .703, 'center_y': .42})
            label6=Label(text= "%s:%s" % (self.minutes, self.seconds), font_size= 32, pos_hint={'center_x': .7, 'center_y': .345})
            label7=Label(text= "Minutes   Seconds", font_size= 12,color=(0, 0, 0, .9), pos_hint={'center_x': .7, 'center_y': .39})
            rec1=Button(size_hint=(0.28,0.20),pos_hint={'center_x': .66, 'center_y': .37},background_normal='bottone3.png')
            pict1=Image(source='./hourglass_blue_T.png',size_hint=(1, .16),pos_hint={'center_x': .58, 'center_y': .375})
            self.add_widget(rec1)
            self.add_widget(label5)
            self.add_widget(label6)
            self.add_widget(label7)
            self.add_widget(pict1)
            
        else:
            self.clear_widgets()
            label=Button(text=' Checklist ',background_normal='bottone3.png', size_hint=(0.31,0.14), bold=True, font_size='20sp', color=(1, 1, 1, .9), valign='top', pos_hint={'center_x': .5, 'center_y': .92})
            pict=Image(source='./logo.png',size_hint=(1, .16),pos_hint={'center_x': .68, 'center_y': .92})
            self.add_widget(label)
            self.add_widget(pict)
            label1=Label(text='Assembled Device \n\nSample Added \n\nBL Substrate Added \n\nCartridge inserted', color=(1, 1, 1, .9), font_size='15sp', pos_hint={'center_x': .24, 'center_y': .56})
            checkbox = CheckBox(pos_hint={'center_x': .10, 'center_y': .61})
            checkbox.bind(active=self.on_checkbox_active)
            self.add_widget(checkbox1)
            self.add_widget(label1)
            self.add_widget(checkbox)
            button4=Button(text='Acquire',background_normal='bottone3.png',size_hint=(0.21,0.11),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
            self.add_widget(button4)
            button4.bind(on_press=self.camerabutton)
            button1=Button(text='Home',background_normal='bottone3.png', size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
            button1.bind(on_press=self.start)
            self.add_widget(button1)

    def load(self, *latgs):
        """Open a dialog to load an image file."""
        content = LoadDialog(load=self._load_helper, cancel=self._dismiss_popup)
        self._popup = Popup(title="Load image", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def _load_helper(self, path, filename):
        """Callback function for load. Called when user selects a file.

        This method loads the image file and redisplays the ImagePanels."""
        print "filename:",filename[0]
        print "path:",path

        self._dismiss_popup()
	self.clear_widgets()
        global path_def
        path_def=path+"/"+filename[0]
        img=Image(source=(path_def), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(img)
        button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
        button1.bind(on_press=self.start)
        self.add_widget(button1)
        button2=Button(text='Analyze',background_normal='bottone3.png',size_hint=(0.22,0.12),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1}, state='down')
        button2.bind(on_press=self.calculatergb)
        self.add_widget(button2)
     
    def _dismiss_popup(self):
        """Used to dismiss the currently active pop-up"""
        self._popup.dismiss()

       
    def choosebutton(self, *latgs):
        self.clear_widgets()
        button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
        button1.bind(on_press=self.start)
        self.add_widget(button1) 
        button2=Button(text='Load',background_normal='background_normal.png',size_hint=(0.22,0.12),pos_hint={'center_x': .5, 'center_y': .1})
        button2.bind(on_submit=self.load(FileChooserIconView.path))
        #self.add_widget(button2)
        #self.add_widget(picture)

    def infobutton(self, *latgs):
        info = Widget()
        self.clear_widgets()
        self.add_widget(info)
        label=Label(text='This App was created by the group of Analytical & Bioanalytical Chemistry, \n                             Department of Chemistry "G.Ciamician", \n                                             University of Bologna', italic=True, color=(1, 1, 1, .9), font_size='17sp', pos_hint={'center_x': .5, 'center_y': .4})
        self.add_widget(label)
        button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
        button1.bind(on_press=self.start)
        self.add_widget(button1)
        dang2=Image(source="./logo.png", size_hint= (1, .3), pos_hint= {'center_x': .5, 'center_y': .8})
        self.add_widget(dang2) 

    def calculatergb(img, *largs):
        #img.clear_widgets
        #lab=Label(title=str(Logger.info('Progress: Wait.. work in progress')), size_hint=(0.9, 0.9))
        print Logger.info('Progress: Wait.. work in progress')
        #popup = MsgPopup(msg="Wait.. work in progress")
        #Clock.schedule_interval(img.calculatergb)
        imag=pixel.open(path_def)
        pix=imag.load()
        w=imag.size[0] 
        h=imag.size[1]
        L=[]
        A=[[[0,0,0]for i in range(700)]for i in range(550)] #700,550
        B=[[[0,0,0]for i in range(700)]for i in range(1500)] #700,1500
        C=[[[0,0,0]for i in range(1700)]for i in range(550)] #1700,550
        D=[[[0,0,0]for i in range(1700)]for i in range(1500)] #1700,1500
        a,b,c,n=0,0,0,0
        a1,b1,c1,n1=0,0,0,0
        a2,b2,c2,n2=0,0,0,0
        a3,b3,c3,n3=0,0,0,0
        mctrR,mctrG,mctrB=0,0,0
        mctrR1,mctrG1,mctrB1=0,0,0
        for i in range(350,550): #350,550
            for j in range(500,700): #500,700
                A[i][j] = imag.getpixel((i,j))
        for i in range(350,550): #350,550
            for j in range(500,700): #500,700
                n=n+1
                a=a+A[i][j][0]
                b=b+A[i][j][1]
                c=c+A[i][j][2]
        Ta,Tb,Tc=a/n,b/n,c/n
        for i in range(1300,1500): #1300,1500
            for j in range(500,700):#500,700
                B[i][j] = imag.getpixel((i,j))
        for i in range(1300,1500): #1300,1500
            for j in range(500,700):#500,700
                n1=n1+1
                a1=a1+B[i][j][0]
                b1=b1+B[i][j][1]
                c1=c1+B[i][j][2]
        Ta1,Tb1,Tc1=a1/n1,b1/n1,c1/n1
        mctrR,mctrG,mctrB= (Ta+Ta1)/2,(Tb+Tb1)/2,(Tc+Tc1)/2
        for i in range(350,550):    #350,550
            for j in range(1500,1700): #1500,1700
                C[i][j] = imag.getpixel((i,j))
        for i in range(350,550):    #350,550
            for j in range(1500,1700): #1500,1700
                n2=n2+1
                a2=a2+C[i][j][0]
                b2=b2+C[i][j][1]
                c2=c2+C[i][j][2]
        Ta2,Tb2,Tc2=a2/n2,b2/n2,c2/n2
        for i in range(1300,1500): #1300,1500
            for j in range(1500,1700):  #1500,1700
                D[i][j] = imag.getpixel((i,j))
        for i in range(1300,1500): #1300,1500
            for j in range(1500,1700):  #1500,1700
                n3=n3+1
                a3=a3+D[i][j][0]
                b3=b3+D[i][j][1]
                c3=c3+D[i][j][2]
        Ta3,Tb3,Tc3=a3/n3,b3/n3,c3/n3
        mctrR1,mctrG1,mctrB1= (Ta2+Ta3)/2,(Tb2+Tb3)/2,(Tc2+Tc3)/2
        L=[(mctrR-mctrR1),(mctrG-mctrG1),(mctrB-mctrB1)]
        sommasample= mctrR+mctrG
        sommactr= mctrR1+mctrG1
        res=(sommasample*100)/sommactr
        if res>80:
            if res>100:
                res=100
            img.clear_widgets()
            rec=Button(size_hint=(0.40,0.39),pos_hint={'center_x': .5, 'center_y': .6},background_normal='green.png')
            label0=Label(text='Result:', font_size='30sp', bold=True, valign='top', color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .7})
            label1=Label(text='Cell viability '+str(res)+"%", font_size='30sp', valign='top', color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .6})
            label2=Label(text='SAFE',italic=True, bold=True, font_size='30sp', valign='top',color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .5})
            button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
            button1.bind(on_press=img.start)
            button4=Button(text='Save Results',background_normal='bottone3.png',size_hint=(0.22,0.12),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
            button4.bind(on_press=img.show_save)
            dang2=Image(source="./logo.png", size_hint= (1, .15), pos_hint= {'center_x': .9, 'center_y': .1})
            img.add_widget(button4)
            img.add_widget(button1)
            img.add_widget(rec)
            img.add_widget(label0)
            img.add_widget(label1)
            img.add_widget(label2)
            img.add_widget(dang2)

        if res<80 and res>=40:
            img.clear_widgets()
            rec=Button(size_hint=(0.40,0.39),pos_hint={'center_x': .5, 'center_y': .6},background_normal='yellow.png')
            label0=Label(text='Result:', font_size='30sp', bold=True, valign='top', color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .7})
            label1=Label(text='Cell viability '+str(res)+"%", font_size='30sp', valign='top', color=(0, 0, 0, .9),pos_hint={'center_x': .5, 'center_y': .6})
            label2=Label(text="HARMFUL",italic=True, bold=True, font_size='30sp', valign='top', color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .5})
            button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
            button1.bind(on_press=img.start)
            button4=Button(text='Save Results',background_normal='bottone3.png',size_hint=(0.22,0.12),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
            button4.bind(on_press=img.show_save)
            dang2=Image(source="./logo.png", size_hint= (1, .15), pos_hint= {'center_x': .9, 'center_y': .1})
            img.add_widget(button4)
            img.add_widget(button1)
            img.add_widget(rec)
            img.add_widget(label0)
            img.add_widget(label1)
            img.add_widget(label2)
            img.add_widget(dang2)
        elif res<40:
            img.clear_widgets()
            rec=Button(size_hint=(0.40,0.39),pos_hint={'center_x': .5, 'center_y': .6}, background_normal='red.png')
            label0=Label(text='Result:', font_size='30sp', bold=True, valign='top', color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .7})
            label1=Label(text='Cell viability '+str(res)+"%", font_size='30sp', valign='top',color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .6})
            label2=Label(text='HIGHLY TOXIC', italic=True, bold=True, font_size='30sp', valign='top',color=(0, 0, 0, .9), pos_hint={'center_x': .5, 'center_y': .5})
            button1=Button(text='Home',background_normal='bottone3.png',size_hint=(0.11,0.10),pos_hint={'center_x': .1, 'center_y': .1})
            button1.bind(on_press=img.start)
            button4=Button(text='Save Results',background_normal='bottone3.png',size_hint=(0.22,0.12),bold=True, font_size='20sp', pos_hint={'center_x': .5, 'center_y': .1})
            button4.bind(on_press=img.show_save)
            dang2=Image(source="./logo.png", size_hint= (1, .15), pos_hint= {'center_x': .9, 'center_y': .1})
            img.add_widget(button4)
            img.add_widget(rec)
            img.add_widget(button1)
            img.add_widget(label0)
            img.add_widget(label1)
            img.add_widget(label2)
            img.add_widget(dang2)

class BiosensorRoot(FloatLayout):
    pass             

class BiosensorApp(App):
    pass

if __name__ == '__main__':
	BiosensorApp().run()
