from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_string("""
<AboutScreen>
    name: 'about'
    BoxLayout:
        orientation: 'vertical'
        Image:
            width: dp(200)
            source: '/Users/btluu/Downloads/Project-Hermes-master/Screens_leo2/data/assets/static_img.jpg'
        Button:
            text:"Call the police"
            width: dp(20)
            on_release:
                print('fuck the police')
                app.root.ids.scr_mngr.current = 'dashboard'
                root.manager.transition.direction = "left"

""")


class AboutScreen(Screen):
    pass
