
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,ColorProperty,ListProperty
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from ..ripple import RippleButton
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("topnav.kv")
Builder.load_file("topnav.kv")
class TopNav(BoxLayout):
    source=StringProperty("")
    background_color=ColorProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(TopNav,self).__init__(**kwargs)

class TopNavButton(RippleButton):
    icon_name=StringProperty("../libsk/assest/fonts/ico.ttf")
    icon=StringProperty("\ue5c4")

class TopNavIcon(Label):
    icon_name=StringProperty("../libsk/assest/fonts/ico.ttf")
    icon=StringProperty("\ue5c4")
    def __init__(self, **kwargs):
        super(TopNavIcon,self).__init__(**kwargs)

class TopNavBackButton(TopNavButton):
    icon=StringProperty("\ue5c4")

class TopNavMenuButton(TopNavButton):
    icon=StringProperty("\ue5d2")

class TopNavSettingButton(TopNavButton):
    icon=StringProperty("\ue8b8")

class TopNavQRButton(TopNavButton):
    icon=StringProperty("\uef6b")

class TopNavCameraButton(TopNavButton):
    icon=StringProperty("\ue3af")



class TopNavAppName(Label):
    pass





