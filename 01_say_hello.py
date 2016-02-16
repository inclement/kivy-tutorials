
from kivy.app import App
from kivy.uix.label import Label

class YourApp(App):

    def build(self):
        root_widget = Label(text='Hello world!')
        return root_widget

YourApp().run()
    
