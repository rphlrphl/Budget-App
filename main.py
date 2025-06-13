from kivymd.uix.dropdownitem import MDDropDownItem, MDDropDownItemText
from kivymd.uix.menu import MDDropdownMenu

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen

from abc import ABC, ABCMeta, abstractmethod

from kivy.uix.textinput import Texture
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemSupportingText
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
    MDDialogButtonContainer
)
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivy.uix.widget import Widget

from datetime import datetime
from kivy.storage.jsonstore import JsonStore

from kivy.properties import ListProperty
from kivy.core.window import Window
 
Window.size = (480, 854)

""" ------------------------------------------------------------------------------------------------------- """

class WindowManager(ScreenManager):
    pass

class Dialog:
    dialog = None
    
    def __init__(self, id=None, on_accept=None, input_type='number', 
                 input_filter='float', hint_text=None, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.on_accept = on_accept
        self.input_type = input_type
        self.input_filter = input_filter
        self.hint_text = hint_text or id
        self.amount_text_field = None
        self.category_button = None  # Store reference to the category button
        self.selected_category = None  # Track selected category
        self.menu = None  # To store the menu instance

    def add_dialog(self):
        if not self.dialog:
            self.amount_text_field = MDTextField(
                MDTextFieldHintText(text=self.hint_text),
                required=True,
                input_type=self.input_type,
                input_filter=self.input_filter
            )
            
            # Create and store reference to the category button
            self.category_button = MDButton(
                MDButtonIcon(icon='chevron-down'),
                MDButtonText(text='Select Category'),
                on_release=self.menu_open
            )
            
            self.dialog = MDDialog(
                MDDialogHeadlineText(text=f"Add {self.id}:", halign='left'),
                MDDialogButtonContainer(
                    Widget(),
                    self.category_button,  # Use the stored reference
                ),
                MDDialogContentContainer(self.amount_text_field),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        on_release=self.close_dialog,
                        style="text",
                    ),
                    MDButton(
                        MDButtonText(text="Accept"),
                        on_release=lambda x: self.handle_accept(),
                        style="text",
                    ),
                    spacing="8dp",
                )
            )
            self.dialog.open()

    def menu_open(self, button_press_me):
        menu = [
            {
                "text": "Essentials",
                "on_release": lambda x="Essentials": self.menu_callback(x),
            },
            {
                "text": "Financial Obligations", 
                "on_release": lambda x="Financial Obligations": self.menu_callback(x),
            },
            {
                "text": "Others",
                "on_release": lambda x="Others": self.menu_callback(x),
            }
        ]
        
        # Close existing menu if open
        if self.menu:
            self.menu.dismiss()
            
        self.menu = MDDropdownMenu(caller=button_press_me, items=menu)
        self.menu.open()

    def menu_callback(self, text_item):
        """Handle category selection"""
        self.selected_category = text_item
        print(f"Selected category: {text_item}")
        
        # Update button text to show selected category
        if self.category_button:
            # Find the MDButtonText child and update its text
            for child in self.category_button.children:
                if isinstance(child, MDButtonText):
                    child.text = text_item
                    break
        
        # Close the menu
        if self.menu:
            self.menu.dismiss()

    def handle_accept(self):
        # Check if amount is entered
        if not self.amount_text_field or not self.amount_text_field.text.strip():
            print("Please enter an amount")
            return
        
        # Check if category is selected
        if not self.selected_category:
            print("Please select a category")
            return
        
        try:
            added_value = float(self.amount_text_field.text)
            if added_value <= 0:
                print("Error: Amount must be greater than 0")
                return
            
            value = self.amount_text_field.text
            category = self.selected_category
            
            if self.on_accept:
                # Pass both value and category to the callback
                if hasattr(self.on_accept, '__code__') and self.on_accept.__code__.co_argcount > 2:
                    self.on_accept(value, category)
                else:
                    self.on_accept(value)
            
            self.close_dialog()
            
        except ValueError:
            print("Error: Invalid input (not a number)")

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None
            self.selected_category = None
            self.category_button = None
        if self.menu:
            self.menu.dismiss()
            self.menu = None

# Create a compatible metaclass that combines ABCMeta and Screen class' metaclass
class ScreenABCMeta(type(Screen), ABCMeta):
    pass

class ReturnToHome(ABC):
    @abstractmethod
    def return_to_home(self, name='home'):
        pass

class ListManager:
    @staticmethod
    def create_list_item(value, prefix='$', suffix='', date_format="Date Added: %Y-%m-%d"):
        """Creates a reusable list item with value and date"""
        now = datetime.now().strftime(date_format)
        return MDListItem(
            MDListItemHeadlineText(text=f'{prefix}{float(value):,.2f}{suffix}'),
            MDListItemSupportingText(text=now)
        )
    
class TotalBudget:
    def __init__(self):
        self.__budget = 0.00
        
    def add_budget(self, value):
        self.__budget += value
        
    def get_budget(self):
        return self.__budget
        
class TotalExpense:
    def __init__(self):
        self.__expense = 0.00
        
    def add_budget(self, value):
        self.__expense += value
        
    def get_budget(self):
        return self.__expense  

class DataManager:
    def __init__(self):
        self.total_budget = TotalBudget()
        self.total_expense = TotalExpense()

""" ------------------------------------------------------------------------------------------------------- """
""" ------------------------------------------------------------------------------------------------------- """

""" ----- MAIN SCREEN ----- """
Builder.load_string("""
# <WindowManager>:
#     HomeScreen:
#         name: "home"
#     Budget:
#         name: 'budget'


<HomeScreen>:

    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
                    
    MDLabel:
        text: "Welcome!"
        role: 'Headline'
        role: 'medium'
        halign: "left"
        pos_hint: {'center_x': .507, 'center_y': .965}
        # size_hint: None, None
        padding: '15dp'
        theme_font_name: 'Custom'
        font_name: 'assets/font/OpenSans-Medium.ttf'
        color: 'gray'
        
    MDLabel:
        text: "Name"
        font_style: 'Headline'
        role: 'large'
        halign: "left"
        pos_hint: {'center_y': .93}
        # size_hint: None, None
        padding: '15dp'
        theme_font_name: 'Custom'
        font_name: 'assets/font/OpenSans-Medium.ttf'
        color: 'black'
                    
    ScrollView:
        FloatLayout:
            MDCard:
                style: 'filled'
                # adaptive_height: True
                # adaptive_width: True  
                # size_hint: None, None
                pos: 0, 0
                padding: '5dp'
                size: 50, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                radius: [30,30,30,30]
                theme_bg_color: "Custom"
                md_bg_color: [64/255, 123/255, 123/255, 255/255]     
                        
                MDBoxLayout:
                    adaptive_height: True
                    adaptive_width: True   
                    pos_hint: {'center_x': 0.5, 'center_y': 0.58}  # Center both horizontally and vertically
                    padding: '20dp'
                    spacing: '10dp'
               
                    MDGridLayout:
                        cols: 2 if root.width > dp(400) else 1
                        spacing: '10dp'
                        adaptive_height: True
                        adaptive_width: True
                        size_hint_y: None
                        height: self.minimum_height # This ensures that the grid layout grows with its content
                                
                        MDCard:
                            style: 'filled'
                            size_hint: None, None
                            width: dp(280) if root.width > dp(600) else (root.width - dp(60)) / 2 ###
                            height: '300dp' ###
                            padding: '12dp'
                            theme_bg_color: "Custom"
                            md_bg_color: [246/255,248/255,250/255,1]
                            on_release: root.switch_screen('budget')

                            MDRelativeLayout:             
                                FitImage:
                                    source: 'assets/img/budget-icon.png'
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                    size_hint: (None, None)
                                    size: dp(100), dp(100) ###
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
                            width: dp(280) if root.width > dp(600) else (root.width - dp(60)) / 2 ###
                            height: '300dp' ###
                            padding: '12dp'
                            theme_bg_color: "Custom"
                            md_bg_color: [246/255,248/255,250/255,1]
                            on_release: root.switch_screen('expense')
                                
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
                            width: dp(280) if root.width > dp(600) else (root.width - dp(60)) / 2 ###
                            height: '300dp' ###
                            padding: '12dp'
                            theme_bg_color: "Custom"
                            md_bg_color: [246/255,248/255,250/255,1]
                            on_release: root.switch_screen('details')

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
                            width: dp(280) if root.width > dp(600) else (root.width - dp(60)) / 2 ###
                            height: '300dp' ###
                            padding: '12dp'
                            theme_bg_color: "Custom"
                            md_bg_color: [246/255,248/255,250/255,1]
                            on_release: root.switch_screen('visualization')

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
                                                                

                    
""")

class HomeScreen(Screen): # Home Screen
    # Define the property that's used in KV file
    bg_color = ListProperty([255/255,255/255,255/255, 1])  # Light gray color

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        # self.call_budget = CallBudget()

    def switch_screen(self, name = 'home'):
        # self.test.printtext()
        print(name)
        self.manager.current = name
        # return name_ko_later


""" ----- BUDGET SCREEN ----- """
Builder.load_string("""
<Budget>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
     
    FloatLayout:
        size_hint_y: 0.1
        pos_hint: {'y': 0.93}
                    
        MDIconButton:
            icon: 'arrow-left'
            size_hint: None, None
            size: '72dp', '72dp'
            pos_hint: {'x': 0.02, 'top': .75}  # Changed from 'left' to 'x' and adjusted values   
            on_release: root.return_to_home('home')
                    
        MDLabel:
            text: "Budget"
            role: 'medium'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .8}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'gray'
                    
        MDLabel:
            id: total_budget_label
            text: "$0.00" # Placeholder only
            role: 'large'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .4}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'black'
                 
    GridLayout:
        cols: 1
        size_hint_y: 0.9
        MDScrollView:
            MDList:
                id: container

    MDFabButton:
        icon: 'plus'
        pos_hint: {'right': 0.95, 'y': 0.05}
        theme_bg_color: "Custom"
        md_bg_color: [64/255, 123/255, 123/255, 255/255]       
        on_press: root.add_budget_dialog()   
""")

class Budget(Screen, ReturnToHome, metaclass=ScreenABCMeta): # Budget Screen
    bg_color = ListProperty([1, 1, 1, 1])
    budget_dialog = Dialog('Budget') # fix this thing later (must be loosely coupled)
    # total_budget = 0.0

    def __init__(self, **kwargs):
        # Initialize dialog with our callback
        self.budget_dialog = Dialog(
            id='Budget',
            on_accept=self.add_budget_item,
            hint_text='Budget amount'
        )
        super().__init__(**kwargs)
        self.total_budget = TotalBudget() # new

    def add_budget_item(self, value):
        try:
            value_to_float = float(value)
            self.total_budget.add_budget(value_to_float)  # Reuse the same instance

            print(self.total_budget.get_budget()) # Debugging line to check the budget value
            
            # Update UI
            self.ids.total_budget_label.text = f"${self.total_budget.get_budget():,.2f}"
            
            # Add list item
            list_item = ListManager.create_list_item(value)
            self.ids.container.add_widget(list_item)
            
        except ValueError:
            print("Error: Invalid input (not a number)")

    def add_budget_dialog(self):
        self.budget_dialog.add_dialog()

    def close_budget_dialog(self, *args):
        self.budget_dialog.close_dialog()

    def update_budget_label(self):
        self.ids.total_budget_label.text = f"${self.total_budget.get_budget():,.2f}"

    def return_to_home(self, name = 'budget'):
        self.manager.current = name

""" ----- EXPENSE SCREEN ----- """
Builder.load_string("""
<Expense>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
     
    FloatLayout:
        size_hint_y: 0.1
        pos_hint: {'y': 0.93}
                    
        MDIconButton:
            icon: 'arrow-left'
            size_hint: None, None
            size: '72dp', '72dp'
            pos_hint: {'x': 0.05, 'top': .5}  # Changed from 'left' to 'x' and adjusted values   
            on_release: root.return_to_home('home')
                    
        MDLabel:
            text: "Expense"
            role: 'medium'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .8}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'gray'
                    
        MDLabel:
            id: total_expense_label
            text: "$0.00" # Placeholder only
            role: 'large'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .4}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'black'
                 
    GridLayout:
        cols: 1
        size_hint_y: 0.9
        MDScrollView:
            MDList:
                id: container

    MDFabButton:
        icon: 'plus'
        pos_hint: {'right': 0.95, 'y': 0.05}
        theme_bg_color: "Custom"
        md_bg_color: [64/255, 123/255, 123/255, 255/255]                      
        on_press: root.add_expense_dialog()
""")

class Expense(Screen, ReturnToHome, metaclass=ScreenABCMeta):
    bg_color = ListProperty([1, 1, 1, 1])
    expense_dialog = Dialog('Expense')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize dialog with our callback
        self.expense_dialog = Dialog(
            id='Expense',
            on_accept=self.add_expense_item,
            hint_text='Expense amount'
        )
        self.total_expense = TotalExpense()
        self.total_budget = TotalBudget()
        self.budget = Budget()

    def add_expense_item(self, value):
        try:
            value_to_float = float(value)
            self.total_expense.add_budget(value_to_float)  # Reuse the same instance
            
            print(self.total_budget.get_budget()) 

            # Update UI
            self.ids.total_expense_label.text = f"${self.total_expense.get_budget():,.2f}"
            
            # Add list item
            list_item = ListManager.create_list_item(value)
            self.ids.container.add_widget(list_item)

        except ValueError:
            print("Error: Invalid input (not a number)")

    def add_expense_dialog(self):
        self.expense_dialog.add_dialog()

    def close_expense_dialog(self, *args):
        self.expense_dialog.close_dialog()

    def return_to_home(self, name = 'expense'):
        self.manager.current = name

""" ----- DETAILS SCREEN ----- """
Builder.load_string("""
<Details>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
                    
    FloatLayout:
        size_hint_y: 0.1
        pos_hint: {'y': 0.93}
                    
        MDIconButton:
            icon: 'arrow-left'
            size_hint: None, None
            size: '72dp', '72dp'
            pos_hint: {'x': 0.05, 'top': .5}  # Changed from 'left' to 'x' and adjusted values   
            on_release: root.return_to_home('home')
                    
        MDLabel:
            text: "Budget and Expenses"
            role: 'medium'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .8}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'gray'
                    
        MDLabel:
            text: "Details"
            role: 'large'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .4}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'black'
""")

class Details(Screen):
    bg_color = ListProperty([1, 1, 1, 1])

    def return_to_home(self, name = 'details'):
        self.manager.current = name

""" ----- VISUALIZATION SCREEN ----- """
Builder.load_string("""
<Visualization>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
                    
    FloatLayout:
        size_hint_y: 0.1
        pos_hint: {'y': 0.93}
                    
        MDIconButton:
            icon: 'arrow-left'
            size_hint: None, None
            size: '72dp', '72dp'
            pos_hint: {'x': 0.05, 'top': .5}  # Changed from 'left' to 'x' and adjusted values   
            on_release: root.return_to_home('home')
                                     
        MDLabel:
            text: "Visualization" # Placeholder only
            role: 'large'
            font_style: 'Title'
            halign: 'right'
            # valign: 'top'
            pos_hint: {'right': .9, 'top': .4}
            theme_font_name: 'Custom'
            font_name: 'assets/font/OpenSans-Medium.ttf'
            color: 'black'
""")

class Visualization(Screen):
    bg_color = ListProperty([1, 1, 1, 1])

    def return_to_home(self, name = 'visualization'):
        self.manager.current = name

""" ------------------------------------------------------------------------------------------------------- """


    


class MainScreen(MDApp):
    def build(self):
        # from budget_screen import Budget
        self.wm = WindowManager()
        self.wm.transition = NoTransition()
        screens = [
            HomeScreen(name='home'),
            Budget(name='budget'),
            Expense(name='expense'),
            Details(name='details'),
            Visualization(name='visualization')
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        self.wm.current = 'budget'
        return self.wm
    



if __name__ == "__main__":
    main_app = MainScreen()
    main_app.run()
