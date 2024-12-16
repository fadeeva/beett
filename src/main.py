from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.text import LabelBase

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import StringProperty, ListProperty



kv = Builder.load_file('beett.kv')
class beettApp(App):
    def build(self):
        Window.clearcolor = (.06, .05, .1, 1)
        Window.size = (685, 710)
        
#        wm = WindowManager()
#           
#        return wm
    
    
if __name__ == '__main__':
    beettApp().run()