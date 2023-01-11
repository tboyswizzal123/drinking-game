from typing import Text
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.lang import Builder
from kivy.core.audio import Sound, SoundLoader
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from random import random
from random import randint 
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.switch import *

mega= SoundLoader.load('megalovania.mp3')
music= SoundLoader.load('music.mp3')
musicy= SoundLoader.load('Ram Ranch.mp3')
kek=[]
counter=0
pls=False
players={}
prev=0
class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    playas=ObjectProperty('Add Players!')
    def btn(self):
        global kek
        pls= True
        x=self.ids.names.text
        kek.append(x)
        self.playas=kek[0:]
        self.ids.names.text=''

    def dele(self):
        kek.pop()
        self.playas=kek[0:]

    def create(self):
            global players
            for i in kek:
                players[i]=0 

class WinScreen(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

    def change(self):
        sound= SoundLoader.load('treasure.wav')
        sound.play()

    def changee(self):
        sound= SoundLoader.load('treasuree.wav')
        sound.play()



class Screen2(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen3(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen4(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen5(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen6(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen7(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen8(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
class Screen9(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen10(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen11(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen12(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen13(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen14(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
class Screen15(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen31(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen16(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen17(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen18(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen19(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen20(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen21(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen22(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen23(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen24(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen25(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen26(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen27(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen28(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen29(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen30(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen31(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen32(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen33(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen34(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen35(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen36(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        
class Screen37(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen38(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen39(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen40(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen41(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen42(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen43(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen44(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen45(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen46(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen47(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen48(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen49(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen50(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
class Screen60(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen51(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen52(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen53(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen54(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen55(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen56(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen57(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen58(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen59(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen60(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen61(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen62(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen63(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen64(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen65(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen66(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen67(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen68(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen69(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen70(Screen): 
    special=ObjectProperty(0)
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        self.special=0
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]

    def sub(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,5)
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]-=value
                self.points=players[x]
        counter+=1

class Screen71(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen72(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen73(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen74(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen75(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen76(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen77(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen78(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen79(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen80(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen81(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen82(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen83(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen84(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen85(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen86(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen87(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen88(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen89(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen90(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen91(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen92(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen93(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen94(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen95(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen96(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen97(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen98(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen99(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen100(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen101(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen102(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen103(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen104(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen105(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen106(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen107(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen108(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen109(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen110(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen111(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen112(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen113(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen114(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen115(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen116(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen117(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen118(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen119(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen120(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen121(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen122(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen123(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen124(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen125(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen126(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen127(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen128(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen129(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen130(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen131(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen132(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen133(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen134(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen135(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen136(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen137(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen138(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen139(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen140(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen141(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen142(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen143(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen144(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen145(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen146(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen147(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen148(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen149(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen150(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class Screen151(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen152(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen153(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen154(Screen):
    pass

class Screen155(Screen):
    passer=ObjectProperty('Push me :)')
    order=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        self.order=kek
    def death(self):
        self.passer='PASS'
        rando=randint(1,20)
        print(rando)
        if (rando==10):
            self.passer='DOWN YOUR DRINK'

        if (rando==5):
            self.passer='TAKE 20 SIPS'

        if (rando==1):
            self.passer='You got lucky :). take one sip'

        if (rando==15):
            self.passer='TAKE ONE SHOT'

class Screen156(Screen):
    namer=ObjectProperty(None)
    passer=ObjectProperty('PUSH AT YOUR OWN RISK')
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
    def death(self):
        self.passer='PASS'
        rando=randint(1,5)
        print(rando)
        if (rando==1):
            self.passer='TAKE A SHOT'

        if (rando==2):
            self.passer='TAKE POISON (5)'

        if (rando==3):
            self.passer='Reroll?'

        if (rando==4):
            self.passer='Gain shield'

        if (rando==5):
            self.passer='GAIN SUPER SHIELD'

class Screen157(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen158(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen159(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen160(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen161(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen162(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen163(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen164(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen165(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen166(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen167(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen168(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class Screen169(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class Screen170(Screen):

    namer=ObjectProperty(None)
    passer=ObjectProperty('SMITE THEE')
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        global music
        if music:
            music.play()
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

    def stop(self):
        global music
        if music:
            music.stop()
    def death(self):
        self.passer='PASS'
        rando=randint(1,5)
        print(rando)
        if (rando==1):
            self.passer='TAKE A SHOT'

        if (rando==2):
            self.passer='DOWN YOUR DRINK'

        if (rando==3):
            self.passer='CURSE MARK (take 3 extra sips EVERY round)'

        if (rando==4):
            self.passer='POISON (5)'

        if (rando==5):
            self.passer='TAKE OFF ALL YOUR CLOTHES (or take 2 shots).'

class Screen171(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen172(Screen):

    namer=ObjectProperty(None)
    passer=ObjectProperty('18 NAKED COW BOYS')
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        global musicy
        if musicy:
            musicy.play()
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

    def stop(self):
        global musicy
        if musicy:
            musicy.stop()
    def death(self):
        rando=randint(1,18)
        print(rando)
        if (rando==1):
            self.passer='DIRECT 6 SIPS TO 3 OTHER PLAYERS'

        if (rando==2):
            self.passer='TAKE OFF A PIECE OF CLOTHING FROM ANOTHER PLAYER'

        if (rando==3):
            self.passer='HAVE ANOTHER PLAYER TAKE OFF A PIECE OF CLOTHING FROM YOU'

        if (rando==4):
            self.passer='EACH PLAYER INCLUDING YOU SPLITS 18 SIPS EQUALLY. (18/PLAYERS)'

        if (rando==5):
            self.passer='TAKE 18 SIPS.'

        if (rando==6):
            self.passer='EACH PLAYER TAKES 18 SIPS'

        if (rando==7):
            self.passer='GAIN SHIELD'

        if (rando==8):
            self.passer='GAIN POISON (18/PLAYERS) (round down)'

        if (rando==9):
            self.passer='NOTHING AT ALL'

        if (rando==10):
            self.passer='PREFORM A LAP DANCE FOR ANOTHER PLAYER'
        
        if (rando==11):
            self.passer='DOWN YOUR DRINK'

        if (rando==12):
            self.passer='LET ANOTHER PLAYER GRAB YOUR ASS FOR 18 SECONDS'

        if (rando==13):
            self.passer='GRAB ANOTHER PLAYERS ASS FOR 18 SECONDS'

        if (rando==14):
            self.passer='DO 18 SQUATS'

        if (rando==15):
            self.passer='MAKE EVERYBODY BUT YOU SPLIT BETWEEN 18 SIPS'

        if (rando==16):
            self.passer='GIVE OUT 18 COMPLIMENTS (split evenly among other players)'

        if (rando==17):
            self.passer='TAKE 18 INSULTS (split evenly among other players)'

        if (rando==18):
            self.passer='Deliver 18 sips to anybody'

class Screen173(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen174(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen175(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen176(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen177(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen178(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class Screen179(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen180(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen181(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen182(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class Screen183(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen184(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen185(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen186(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen187(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen188(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen189(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen190(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

class Screen191(Screen):
    pass

class Screen192(Screen):
    passer=ObjectProperty('Push me :)')
    order=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        self.order=kek
    def death(self):
        self.passer='PASS'
        rando=randint(1,20)
        print(rando)
        if (rando==10):
            self.passer='DOWN YOUR DRINK'

        if (rando==5):
            self.passer='TAKE 20 SIPS'

        if (rando==1):
            self.passer='You got lucky :). take one sip'

        if (rando==15):
            self.passer='TAKE ONE SHOT'

class GreedScreen(Screen):
    namer=ObjectProperty(None)
    passer=ObjectProperty('Claim your reward! ;)')
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

    def death(self):
        self.passer='PASS'
        rando=randint(1,5)
        print(rando)
        if (rando==1):
            self.passer='Shield'

        if (rando==2):
            self.passer='SUPER SHIELD'

        if (rando==3):
            self.passer='IMMUNE FROM ALL REDIRECT SIPS FOR THE REST OF THE GAME'

        if (rando==4):
            self.passer='IMMUNE FROM ALL PUNISH SIPS FOR THE REST OF THE GAME (not including greed room)'

        if (rando==5):
            self.passer='EVERYBODY TAKES 5 SIPS EXCEPT YOU'


class Screen193(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter]

class Screen194(Screen):
    namer=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 


class SansRoom(Screen):

    namer=ObjectProperty(None)
    passer=ObjectProperty('')
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, order):
        global mega
        if mega:
            mega.play()
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 

    def stop(self):
        global mega
        if mega:
            mega.stop()
    def death(self):
        self.passer='PASS'
        rando=randint(1,5)
        print(rando)
        if (rando==1):
            self.passer='Sans opening attack: Take a shot, poison (3)'

        if (rando==2):
            self.passer='Poison Bones: Poison(6)'

        if (rando==3):
            self.passer='Gaster Blaster: Finish your drink'

        if (rando==4):
            self.passer='Sans break: You get to rest. Continue to next prompt.'

        if (rando==5):
            self.passer='Sans ending attack: Down your drink, Take 7 sips.'




class BonusScreen(Screen): 
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    special=ObjectProperty(0)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        self.special=0
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
    def show(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        value=value+3
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1
    def showw(self):
        global prev
        global players
        global kek
        global counter
        value=1
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1
    def showww(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        value=value*2
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1

class ChampionScreen(Screen): 
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    special=ObjectProperty(0)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        self.special=0
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
    def show(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        value=value+5
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1
    def showw(self):
        global prev
        global players
        global kek
        global counter
        value=1
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1
    def showww(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1

class DeathScreen(Screen): 
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    special=ObjectProperty(None)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        self.special='???'
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
    def show(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        value=15
        self.special= '- 15 points'
        for x in players:
            if(x == kek[counter]):
                players[x]-=value
                self.points=players[x]
        counter+=1
    def showw(self):
        global prev
        global players
        global kek
        global counter
        self.special='Lose a shield. If none TAKE SHOT'
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
        counter+=1
    def showww(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,12)
        self.special='Take poison (3)'
        for x in players:
            if(x == kek[counter]):
                players[x]-=value
                self.points=players[x]
        counter+=1

class PassScreen(Screen): 
    special=ObjectProperty(0)
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter] 
        self.special=0
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
        self.ids.swtich=True
    def show(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]+=value
                self.points=players[x]
        if(self.points<50):
            counter+=1





class LoseScreen(Screen):
    special=ObjectProperty(None)
    namer=ObjectProperty(None)
    points=NumericProperty(0)
    def on_enter(self):
        Clock.schedule_once(self.update)
    def update(self, namer):
        global counter
        if (counter>len(kek)-1):
            counter=0
        self.namer=kek[counter]
        self.special=0
 
        for x in players:
            if(x == kek[counter]):
                self.points=players[x]
    
    def sub(self):
        global prev
        global players
        global kek
        global counter
        value=randint(1,10)
        self.special=value
        for x in players:
            if(x == kek[counter]):
                players[x]=players[x]-value
                self.points=players[x]
        counter+=1


kv = Builder.load_file("tboy.kv")


class TboyApp(App):
    def star(self):
        PassScreen.update(self)

    def build(self):
        return kv

if __name__ == '__main__':
    TboyApp().run()