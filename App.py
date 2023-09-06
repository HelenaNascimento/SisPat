from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.properties import DictProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

KV = '''
<MD3Card>
    padding: 4
    size_hint: None, None
    size: "300dp", "140dp"

    MDRelativeLayout:

        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "10dp", "5dp"
            bold: True

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

<MySwiper@MDSwiperItem>

    MDLabel:
        text: "guitar.png"
        radius: [20,]

MDScreenManager:

    MDScreen:
        md_bg_color:
        name: "screen A"

        MDBoxLayout:
            orientation: "vertical"
            id: box
            adaptive_size: True
            spacing: "20dp"
            pos_hint: {"center_x": .5, "center_y": .6}
        
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .1}
            md_bg_color: "green" 
            on_release:
                root.current = "screen B"


    MDScreen:
        name: "screen B"
        md_bg_color: "lightblue" 

        MDBoxLayout:
            id: box1
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .1}

            MDRaisedButton:
                text: "Login"
                md_bg_color: "green" 
                on_release:
                    root.current = "screen C"

            MDRaisedButton:
                text: "Cancelar"
                md_bg_color: "green" 
                on_release:
                    root.current = "screen A"

    MDScreen:
        name: "screen C"
        md_bg_color: "lightblue" 

        MDBoxLayout:
            id: box2
            orientation: "vertical"
            
            MDTopAppBar:
                pos_hint: {"center_y": .1}
                title: "SisPat"                
                left_action_items: [['menu', lambda x: app.navigation_draw()]]
                right_action_items: [['logout', lambda x: app.novigation_draw()]]


            MDRaisedButton:
                pos_hint: {"center_x": .5, "center_y": .3}
                text: "Consultar"
                md_bg_color: "green" 
                on_release:
                    root.current = "screen consulta"

            MDRaisedButton:
                pos_hint: {"center_x": .5, "center_y": .5}
                text: "Cadastro Itens"
                md_bg_color: "green" 
                on_release:
                    root.current = "screen A"
            
            MDRaisedButton:
                pos_hint: {"center_x": .5, "center_y": .5}
                text: "Cadastro Patrimônio"
                md_bg_color: "green" 
                on_release:
                    root.current = "screen A"

            Label:
                text: ""
                font_size:'1dp'
                pos_hint: {'center_x': .5}

    MDScreen:
        name: "screen consulta"
        md_bg_color: "lightblue" 


        MDTopAppBar:
            id: toolbar
            title: "Consultar"
            elevation: 4
            pos_hint: {"top": 1}
            use_overflow: True
            right_action_items:
                [
                ["message-question",lambda x:app.callback(x),"Help","Help"],
                ["logout",lambda x:app.callback(x),"Sair","Sair"],
                ]
            left_action_items: [["home", lambda x: app.callback(x), "Home", "Home"]]
        

        MDFloatLayout:
            orientacion: 'vertical'

            MDTextField:
                md_bg_color: 1, 1, 1, 1 
                icon_left: 'camera'
                hint_text: 'Empty field'
                pos_hint: {'center_y': .8}

            Label:
                text: "Consulta Itens"
                font_size:'10dp'
                pos_hint: {'center_x': .55, 'center_y': .75}

            Check:
                active: True
                pos_hint: {'center_x': .68, 'center_y': .75}

            Label:
                text: "Consulta Pat"
                font_size: '10dp'
                pos_hint: {'center_x': .8, 'center_y': .75}

            Check:
                pos_hint: {'center_x': .9, 'center_y': .75}

        MDSwiper:
            id: swiper
            size_hint_y: None
            height: root.height - toolbar.height - dp(40)
            y: root.height - self.height - toolbar.height - dp(20)
            on_swipe: self.get_current_item().ids.icon.shake()

            MySwiper:

            MySwiper:

            MySwiper:

            MySwiper:

            MySwiper:
        
        MDFloatingActionButtonSpeedDial:
            data: app.data
            root_button_anim: True        

    MDScreen:
        name: "screen consulta"
        md_bg_color: "lightblue"     
        
        
'''

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()

class MainApp(MDApp):
#    data = {
#        'Editar': 'pencil',
#        'Adicionar': 'plus',
#    }

    data = DictProperty()

    def build(self):
        Window.size = (380,680)
        self.theme_cls.material_style = "M3"
        self.data = {
            'Edita' : [
                'pencil',
                "on_press", lambda x: print("pressed pencil"),
                "on_release", self.callback],
            'Adicionar' : [
                'plus',
                "on_press", lambda x: print("pressed plus"),
                "on_release", self.callback]
        }

        return Builder.load_string(KV)
    
    def navigation_draw():
        print ("NavBar")

    def on_start(self):
        styles = {
            "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
        }
        for style in styles.keys():
            self.root.ids.box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=styles[style],
                    shadow_softness=2 if style == "elevated" else 12,
                    shadow_offset=(0, 1) if style == "elevated" else (0, 2),
                )
            )
    
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive','and', checkbox.state,'state')
            
    
MainApp().run()

