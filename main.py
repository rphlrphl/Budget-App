from kivy.uix.textinput import Texture
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivy.properties import ListProperty


Builder.load_string("""
<WindowManager>:
    HomeScreen:
        name: "home"

<HomeScreen>:

    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
                    

                    
    MDBoxLayout:
        adaptive_height: True
        adaptive_width: True   
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center both horizontally and vertically

        MDGridLayout:
            cols: 2
            spacing: '5dp'
            adaptive_height: True
            adaptive_width: True
                    
            MDCard:
                style: 'filled'
                size_hint: None, None
                size: '240dp', '300dp' 
                padding: '12dp'
                theme_bg_color: "Custom"
                md_bg_color: [240/255,241/255,228/255,1]
                on_release: root.call_test_function()
                    
                MDRelativeLayout:             
                    FitImage:
                        source: 'assets/img/budget-icon.png'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint: (None, None)
                        size: ("150dp", "150dp")  # Control size directly
                        # allow_stretch: True
                        # keep_ratio: True
                        # font_size: '2000sp'

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}

                    MDLabel:
                        text: "Budget"
                        adaptive_size: True
                        color: "black"
                        pos: "12dp", "12dp"
                        theme_font_name: 'Custom'
                        font_name: 'assets/font/OpenSans-SemiBold.ttf'
                    


            MDCard:
                style: 'filled'
                size_hint: None, None
                size: '240dp', '300dp' 
                padding: '12dp'
                theme_bg_color: "Custom"
                md_bg_color: [240/255,241/255,228/255,1]
                on_release: root.call_test_function()
                    
                MDRelativeLayout:
                    FitImage:
                        source: 'assets/img/expense-icon.png'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint: (None, None)
                        size: ("150dp", "150dp")  # Control size directly
                        # allow_stretch: True
                        # keep_ratio: True
                        # font_size: '2000sp'


                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}
                        
                    MDLabel:
                        text: "Expenses"
                        adaptive_size: True
                        color: "black"
                        pos: "12dp", "12dp"
                        theme_font_name: 'Custom'
                        font_name: 'assets/font/OpenSans-SemiBold.ttf'

            MDCard:
                style: 'filled'
                size_hint: None, None
                size: '240dp', '300dp' 
                padding: '12dp'
                theme_bg_color: "Custom"
                md_bg_color: [240/255,241/255,228/255,1]
                on_release: root.call_test_function()

                MDRelativeLayout:
                    FitImage:
                        source: 'assets/img/detail-icon.png'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint: (None, None)
                        size: ("150dp", "150dp")  # Control size directly
                        # allow_stretch: True
                        # keep_ratio: True
                        # font_size: '2000sp'                    

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}                    

                    MDLabel:
                        text: "Details"
                        adaptive_size: True
                        color: "black"
                        pos: "12dp", "12dp"
                        theme_font_name: 'Custom'
                        font_name: 'assets/font/OpenSans-SemiBold.ttf'
                    
            MDCard:
                style: 'filled'
                size_hint: None, None
                size: '240dp', '300dp' 
                padding: '12dp'
                theme_bg_color: "Custom"
                md_bg_color: [240/255,241/255,228/255,1]
                on_release: root.call_test_function()

                MDRelativeLayout:
                    FitImage:
                        source: 'assets/img/graph-icon.png'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint: (None, None)
                        size: ("150dp", "150dp")  # Control size directly
                        # allow_stretch: True
                        # keep_ratio: True
                        # font_size: '2000sp'                    

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}                   

                    MDLabel:
                        text: "Visualization"
                        adaptive_size: True
                        color: "black"
                        pos: "12dp", "12dp"
                        theme_font_name: 'Custom'
                        font_name: 'assets/font/OpenSans-SemiBold.ttf'
    
    # MDButton:
    #     pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #     style: "filled"
    #     MDButtonText:
    #         text: "Hello World"
""")

class Test:
    def printtext(self):
        print("Working")

class WindowManager(ScreenManager):
    pass

class HomeScreen(Screen):
    # Define the property that's used in KV file
    bg_color = ListProperty([161/255,135/255,120/255, 1])  # Light gray color

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.test = Test() # this is for testing purposes

    def call_test_function(self):
        self.test.printtext()

class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            HomeScreen(name='home')
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        self.wm.current = 'home'
        return self.wm
    


if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()