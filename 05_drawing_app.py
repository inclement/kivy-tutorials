
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
            Color(1, 0, 0, 1)  # note that we must reset the colour
            Rectangle(size=(300, 100),
                      pos=(300, 200))
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)


    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
            

class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
