from kivy.uix.gridlayout import GridLayout

from kivy.properties import StringProperty,DictProperty,ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from libsk.uix.ripple import RippleButton
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.event import EventDispatcher
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
from kivy.lang.builder import Builder
Builder.unload_file("menus.kv")
Builder.load_file("menus.kv")
class MenuItem(EventDispatcher):
    __events__=("on_event1","on_event2","on_event3","on_event4","on_press")
    data=DictProperty({
                "module": "apps.hdiag_pro",
                "class": "HDiagPro",
                "icon": "assets/icons/4.png",
                "path": "apps/hdiag_pro",
                "name": "HDiag Pro",
                "version": "2023.0808.2121",
                "url": "apps/hdiag_pro.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "hdiag_pro",
                "short_description": "Remap tool for honda",
                "long_description": "",
                "requirements": []
            })
    def on_press(self):
        pass
    def on_event1(self):
        pass
    def on_event2(self):
        pass
    def on_event3(self):
        pass
    def on_event4(self):
        pass
    
    
class MenuItemTextUnderIcon(FloatLayout,MenuItem):
    pass

class GridMenu(GridLayout):
    __events__=("on_menu_selected","on_event4_selected","on_event3_selected","on_event2_selected","on_event1_selected")
    menu_data=DictProperty({})
    menu_item=ObjectProperty(MenuItemTextUnderIcon)
    item=ObjectProperty()
    data=DictProperty({})
    def __init__(self, **kwargs):
        super(GridMenu,self).__init__(**kwargs)
        self.menu_data={
            "hdiag_pro": {
                "module": "apps.hdiag_pro",
                "class": "HDiagPro",
                "icon": "assets/icons/4.png",
                "path": "apps/hdiag_pro",
                "name": "HDiag Pro",
                "version": "2023.0808.2121",
                "url": "apps/hdiag_pro.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "hdiag_pro",
                "short_description": "Remap tool for honda",
                "long_description": "",
                "requirements": []
            },
            "afr_meter": {
                "module": "apps.afr_meter",
                "class": "AFRMeter",
                "icon": "assets/icons/1.png",
                "path": "apps/afr_meter",
                "name": "AFR Meter",
                "version": "2023.0608.1010",
                "url": "apps/afr_meter.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "afr_meter",
                "short_description": "Wide band o2",
                "long_description": "",
                "requirements": []
            },
            "engineSync": {
                "module": "apps.engineSync",
                "class": "EngineSync",
                "icon": "assets/icons/3.png",
                "path": "apps/engineSync",
                "name": "Engine Sync",
                "version": "2023.0606.1540",
                "url": "apps/engineSync.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "engineSync",
                "short_description": "multi sylinder balance",
                "long_description": "",
                "requirements": []
            },
            
            "pressureGauge": {
                "module": "apps.pressureGauge",
                "class": "PressureGauge",
                "icon": "assets/icons/6.png",
                "path": "apps/pressureGauge",
                "name": "Pressure Gauge",
                "version": "2023.0820.0203",
                "url": "apps/pressureGauge.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "pressureGauge",
                "short_description": "Fuel Pressure measurement",
                "long_description": "",
                "requirements": []
            },

            "hdiag": {
                "module": "apps.hdiag",
                "class": "HDiag",
                "icon": "assets/icons/5.png",
                "path": "apps/hdiag",
                "name": "HDiag",
                "version": "2023.0606.1638",
                "url": "apps/hdiag.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "hdiag",
                "short_description": "Honda injection diagnostic",
                "long_description": "",
                "requirements": []
            },
            "volt_meter": {
                "module": "apps.volt_meter",
                "class": "VoltMeter",
                "icon": "assets/icons/2.png",
                "path": "apps/volt_meter",
                "name": "Battery Monitor",
                "version": "2023.0831.0001",
                "url": "apps/volt_meter.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "volt_meter",
                "short_description": "Android Volt Meter",
                "long_description": "",
                "requirements": []
            }
        }
    def on_menu_data(self,a,b):
        Clock.unschedule(self.create_menu)
        Clock.schedule_once(self.create_menu,.1)
    def create_menu(self,dt):
        
        self.clear_widgets()
        for i in self.menu_data:
            self.add_widget(self.menu_item(on_event4=self.on_event4_pressed,on_event3=self.on_event3_pressed,on_event2=self.on_event2_pressed,on_event1=self.on_event1_pressed,on_press=self.on_menu_pressed,data=self.menu_data[i]))
    def on_menu_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_menu_selected")
    def on_menu_selected(self):
        print(self.data)
        # pass
    def on_event4_pressed(self,instance):
        self.item=instance
        self.data=instance.data
        self.dispatch("on_event4_selected")
    def on_event3_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event3_selected")
    def on_event2_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event2_selected")
    def on_event1_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event1_selected")
    
    def on_event4_selected(self):
        pass
    def on_event3_selected(self):
        pass
    def on_event2_selected(self):
        pass
    def on_event1_selected(self):
        pass
    