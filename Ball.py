
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button


Window.clearcolor=(0,0,0,1)

class FloatLayout(FloatLayout):
    Window.size=(500,500)
    ball_x=NumericProperty(.01)
    ball_y=NumericProperty(.5)
    pressed=ObjectProperty(False)
    
    pluss_minus_x=.01
    pluss_minus_y=.01
   
   


    def __init__(self,**kwargs):
        super(FloatLayout,self).__init__(**kwargs)

        Clock.schedule_interval(self.ball_bounce,1/60)

        return

    def ball_bounce(self,dt):

        self.ball_x+=self.pluss_minus_x
        self.ball_y+=self.pluss_minus_y
        
        self.ball_y+=.001

        if self.ball_x<.01:
            self.pluss_minus_x=.01

        if self.ball_x>.99:
            self.pluss_minus_x=-.01

        if self.ball_y>.99:
            self.pluss_minus_y=-.01

        if self.ball_y<.01 or self.pressed==True:
            self.pluss_minus_y=.01
            self.pressed=False
        
        return

    

class MyApp(App):
    pass
    def build(self):
        
        sm=root=FloatLayout()
        return sm

MyApp().run() 