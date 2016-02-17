

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class YourApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        b1 = Button(text='button 1')
        b2 = Button(text='button 2')

        layout.add_widget(b1)
        layout.add_widget(b2)

        return layout


YourApp().run()
