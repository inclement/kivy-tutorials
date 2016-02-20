
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line

from random import random

class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
            self.rect_colour = Color(1, 0, 0, 1)  # note that we must reset the colour
            Rectangle(size=(300, 100),
                      pos=(300, 200))
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)


    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        with self.canvas:
            Color(random(), random(), random())
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
            

class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
