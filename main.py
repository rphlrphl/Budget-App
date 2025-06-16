from abc import ABC, ABCMeta, abstractmethod
from datetime import datetime
import matplotlib.pyplot as plt
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemSupportingText
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.dialog import (MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogContentContainer, MDDialogButtonContainer)
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from database import Database, BudgetDatabase, ExpenseDatabase, ClearDatabase

# Instantiate Database
db = Database()
budget_db = BudgetDatabase()
expense_db = ExpenseDatabase()
clear_db = ClearDatabase()

# Set window size
# Window.size = (720, 1280)

""" KV STRINGS HERE: """
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

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        # Header section
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(80)
            spacing: dp(15)
            
            FitImage:
                source: 'assets/img/icon.png'
                halign: "center"
                pos_hint: {'center_x': 14, 'center_y': .5}                
                padding: '15dp'
                size_hint: None, None
                size: dp(150), dp(100)
                
            Widget:  # Spacer to push content to the right
            Widget:
            Widget:  # Spacer to push content to the right
            Widget:
            Widget:  # Spacer to push content to the right
            Widget:
            Widget:  # Spacer to push content to the right

            
            MDBoxLayout:
                orientation: 'vertical'
                pos_hint: {'center_y': 0.5}
                size_hint_x: None
                width: dp(200)
                
                MDLabel:
                    text: "Welcome!"
                    role: 'small'
                    font_style: "Title"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_font_name: 'Custom'
                    font_name: 'assets/font/OpenSans-Medium.ttf'
                    halign: 'right'
                    text_size: self.size
                    
                MDLabel:
                    text: "Dashboard"
                    role: 'small'
                    font_style: "Headline"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_font_name: 'Custom'
                    font_name: 'assets/font/OpenSans-Medium.ttf'
                    halign: 'right'
                    text_size: self.size
            
            Widget:  # Spacer
        
        # Main content area
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(20)
                
                # Main card container
                MDCard:
                    style: 'elevated'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)
                    spacing: dp(15)
                    elevation: 2
                    radius: [15, 15, 15, 15]
                    theme_bg_color: "Custom"
                    md_bg_color: [195/255, 177/255, 225/255]   
                    
                    MDBoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(15)
                        
                        # Grid layout for cards
                        MDGridLayout:
                            cols: 1
                            spacing: dp(15)
                            size_hint_y: None
                            height: self.minimum_height
                            adaptive_height: True
                            
                            # Budget Card
                            MDCard:
                                style: 'elevated'
                                size_hint_y: None
                                height: dp(200)
                                padding: dp(15)
                                elevation: 1
                                radius: [12, 12, 12, 12]
                                theme_bg_color: "Custom"
                                md_bg_color: [1, 1, 1, 1]
                                ripple_behavior: True
                                on_release: root.switch_screen('budget')
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        size_hint_y: None
                                        height: dp(30)
                                        
                                        MDLabel:
                                            text: "Budget"
                                            role: 'medium'
                                            font_style: "Title"
                                            theme_text_color: "Primary"
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            theme_font_name: 'Custom'
                                            font_name: 'assets/font/OpenSans-SemiBold.ttf'
                                            
                                        Widget:  # Spacer
                                        
                                        MDIconButton:
                                            icon: "dots-vertical"
                                            theme_icon_color: "Custom"
                                            icon_color: [0.6, 0.6, 0.6, 1]
                                            size_hint: None, None
                                            size: dp(30), dp(30)
                                    
                                    Widget:  # Spacer
                                    
                                    FitImage:
                                        source: 'assets/img/budget-icon.png'
                                        size_hint: None, None
                                        size: dp(80), dp(80)
                                        pos_hint: {'center_x': 0.5}
                                        
                                    Widget:  # Spacer
                            
                            # Expenses Card
                            MDCard:
                                style: 'elevated'
                                size_hint_y: None
                                height: dp(200)
                                padding: dp(15)
                                elevation: 1
                                radius: [12, 12, 12, 12]
                                theme_bg_color: "Custom"
                                md_bg_color: [1, 1, 1, 1]
                                ripple_behavior: True
                                on_release: root.switch_screen('expense')
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        size_hint_y: None
                                        height: dp(30)
                                        
                                        MDLabel:
                                            text: "Expenses"
                                            role: 'medium'
                                            font_style: "Title"
                                            theme_text_color: "Primary"
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            theme_font_name: 'Custom'
                                            font_name: 'assets/font/OpenSans-SemiBold.ttf'
                                            
                                        Widget:  # Spacer
                                        
                                        MDIconButton:
                                            icon: "dots-vertical"
                                            theme_icon_color: "Custom"
                                            icon_color: [0.6, 0.6, 0.6, 1]
                                            size_hint: None, None
                                            size: dp(30), dp(30)
                                    
                                    Widget:  # Spacer
                                    
                                    FitImage:
                                        source: 'assets/img/expense-icon.png'
                                        size_hint: None, None
                                        size: dp(80), dp(80)
                                        pos_hint: {'center_x': 0.5}
                                        
                                    Widget:  # Spacer
                            
                            # Details Card
                            MDCard:
                                style: 'elevated'
                                size_hint_y: None
                                height: dp(200)
                                padding: dp(15)
                                elevation: 1
                                radius: [12, 12, 12, 12]
                                theme_bg_color: "Custom"
                                md_bg_color: [1, 1, 1, 1]
                                ripple_behavior: True
                                on_release: root.switch_screen('details')
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        size_hint_y: None
                                        height: dp(30)
                                        
                                        MDLabel:
                                            text: "Details"
                                            role: 'medium'
                                            font_style: "Title"
                                            theme_text_color: "Primary"
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            theme_font_name: 'Custom'
                                            font_name: 'assets/font/OpenSans-SemiBold.ttf'
                                            
                                        Widget:  # Spacer
                                        
                                        MDIconButton:
                                            icon: "dots-vertical"
                                            theme_icon_color: "Custom"
                                            icon_color: [0.6, 0.6, 0.6, 1]
                                            size_hint: None, None
                                            size: dp(30), dp(30)
                                    
                                    Widget:  # Spacer
                                    
                                    FitImage:
                                        source: 'assets/img/detail-icon.png'
                                        size_hint: None, None
                                        size: dp(80), dp(80)
                                        pos_hint: {'center_x': 0.5}
                                        
                                    Widget:  # Spacer
                            
                            # Visualization Card
                            MDCard:
                                style: 'elevated'
                                size_hint_y: None
                                height: dp(200)
                                padding: dp(15)
                                elevation: 1
                                radius: [12, 12, 12, 12]
                                theme_bg_color: "Custom"
                                md_bg_color: [1, 1, 1, 1]
                                ripple_behavior: True
                                on_release: root.switch_screen('visualization')
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        size_hint_y: None
                                        height: dp(30)
                                        
                                        MDLabel:
                                            text: "Visualization"
                                            role: 'medium'
                                            font_style: "Title"
                                            theme_text_color: "Primary"
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            theme_font_name: 'Custom'
                                            font_name: 'assets/font/OpenSans-SemiBold.ttf'
                                            
                                        Widget:  # Spacer
                                        
                                        MDIconButton:
                                            icon: "dots-vertical"
                                            theme_icon_color: "Custom"
                                            icon_color: [0.6, 0.6, 0.6, 1]
                                            size_hint: None, None
                                            size: dp(30), dp(30)
                                    
                                    Widget:  # Spacer
                                    
                                    FitImage:
                                        source: 'assets/img/graph-icon.png'
                                        size_hint: None, None
                                        size: dp(80), dp(80)
                                        pos_hint: {'center_x': 0.5}
                                        
                                    Widget:  # Spacer
                                                                

                    
""")
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

    BoxLayout:
        orientation: 'vertical'
        spacing: '15dp'
        padding: '20dp'
        size_hint_y: None
        pos_hint: {'center_x' : .5 , 'top' : .8}
        height: self.minimum_height

        MDCard:
            style: 'filled'
            size_hint: None, None
            size: '400dp', '100dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.budget_expense_tab()
            
            MDLabel:
                text: "Your Current Budget vs. Expenses:"
                role: 'large'
                font_style: 'Title'
                halign: 'left'
                padding: '30dp'
                theme_font_name: 'Custom'
                font_name: 'assets/font/OpenSans-Medium.ttf'
                color: 'black'

        MDCard:
            style: 'filled'
            size_hint: None, None
            size: '400dp', '100dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.most_budgeted_and_spent()
            
            MDLabel:
                text: "Most Budgeted and Spent Category:"
                role: 'large'
                font_style: 'Title'
                halign: 'left'
                padding: '30dp'
                theme_font_name: 'Custom'
                font_name: 'assets/font/OpenSans-Medium.ttf'
                color: 'black'

        MDCard:
            style: 'filled'
            size_hint: None, None
            size: '400dp', '100dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.tips()
            
            MDLabel:
                text: "Tips:"
                role: 'large'
                font_style: 'Title'
                halign: 'left'
                padding: '30dp'
                theme_font_name: 'Custom'
                font_name: 'assets/font/OpenSans-Medium.ttf'
                color: 'black'
                    
        MDCard:
            style: 'filled'
            size_hint: None, None
            size: '400dp', '100dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.clear_all_data()
            
            MDLabel:
                text: "Clear Data"
                role: 'large'
                font_style: 'Title'
                halign: 'left'
                padding: '30dp'
                theme_font_name: 'Custom'
                font_name: 'assets/font/OpenSans-Medium.ttf'
                color: 'black'
                    
        # MDLabel:
        #     text: "comparison here"
        #     role: 'medium'
        #     font_style: 'Title'
        #     halign: 'left'
        #     # valign: 'top'
        #     pos_hint: {'top': .2}
        #     padding: '30dp'
        #     theme_font_name: 'Custom'
        #     font_name: 'assets/font/OpenSans-Medium.ttf'
        #     color: 'black'
                    
# <CardDialog>:
#     MDLabel:
        
""")
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
            text: "P0.00" # Placeholder only
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
                # on_press: root.test()

    MDFabButton:
        icon: 'plus'
        pos_hint: {'right': 0.95, 'y': 0.05}
        theme_bg_color: "Custom"
        md_bg_color: [195/255, 177/255, 225/255]       
        on_press: root.add_dialog()   
""")
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
            text: "P0.00" # Placeholder only
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
        md_bg_color: [195/255, 177/255, 225/255]                      
        on_press: root.add_dialog()
""")
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

    # MDToolbar:
    #     title: "Budget vs Expenses"
    #     elevation: 10
    
    BoxLayout:
        id: chart_container
        size_hint_y: 0.9
    
    # MDFloatLayout:
    #     size_hint_y: 0.1
    #     MDLabel:
    #         text: "Budget (Green) vs Expenses (Red)"
    #         halign: 'center'
    #         font_style: 'Headline'
""")

class WindowManager(ScreenManager):
    pass

class DeleteListDialog:
    def __init__(self):
        self.dialog = None

    def delete_dialog(self, list_id, caller):

        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None
            
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Delete Item", halign='left'),
            MDDialogContentContainer(
                MDTextFieldHintText(text="Are you sure you want to delete this item?"),
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    on_release=lambda x: self.close_dialog(),
                    style="text",
                ),
                MDButton(
                    MDButtonText(text="Delete"),
                    on_release=lambda x: self._perform_delete(list_id, caller),
                    style="text",
                ),
                spacing="8dp",
            )
        )
        self.dialog.open()

    def _perform_delete(self, list_id, caller):
        """Handle the actual deletion logic"""
        class_name = caller.__class__.__name__
        
        try:
            if class_name == 'Budget':
                budget_db.delete_budget_by_id(list_id)
            elif class_name == 'Expense':
                expense_db.delete_expense_by_id(list_id)
                
            self.close_dialog()
            caller.on_enter()
        except Exception as e:
            print(f"Error during delete: {e}")
            self.close_dialog()

    def close_dialog(self):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

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
                ),
                auto_dismiss=False
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

class ListManager:
    @staticmethod
    def create_list_item(id, value, category, now, prefix='₱', suffix='', caller=None):
        """Creates a list item with proper ID binding"""
        # Convert ID to string to ensure consistency
        str_id = str(id) if id is not None else "N/A"
        # CHECKPOINT

        try:
            amount = float(value) if value is not None else 0.0
            return MDListItem(
                MDListItemHeadlineText(text=f'{prefix}{amount:,.2f}{suffix}'),
                MDListItemSupportingText(text=category or "No Category"),
                MDListItemSupportingText(text=now or "No Date"),
                # Fixed lambda to properly capture the ID
                on_press=lambda x, item_id=str_id: DeleteListDialog().delete_dialog(item_id, caller) #ListManager.handle_item_click(item_id),
            )
        except Exception as e:
            print(f"Error creating list item: {e}")
            return MDListItem(
                MDListItemHeadlineText(text="Invalid Item"),
                MDListItemSupportingText(text="Could not load this item"),
            )

    @staticmethod
    def handle_item_click(id):
        """Handle click events with proper ID conversion"""
        print(f"Clicked item with ID: {id} (type: {type(id)})")
        
        if id == "N/A":
            print("Invalid item ID")
            return
            
        try:
            # Convert ID back to integer for database lookup
            db_id = int(id)
            item = budget_db.get_budget_by_id(db_id)
            
            if item:
                print(f"Item details - ID: {item[0]}, Amount: {item[1]}, Category: {item[2]}, Date: {item[3]}")
                # Here you would typically show the details in your UI
            else:
                print(f"No details found for ID: {id}")
        except ValueError:
            print(f"Invalid ID format: {id}")
    
class HomeScreen(Screen): # Home Screen
    bg_color = ListProperty([255/255,255/255,255/255, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)       

    def switch_screen(self, name = 'home'):
        print(name)
        self.manager.current = name

class BaseClass(ABC):
    @abstractmethod
    def add_item(self):
        pass

    @abstractmethod
    def add_dialog(self):
        pass

    @abstractmethod
    def close_dialog(self):
        pass

    @abstractmethod
    def update_label(self):
        pass

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def return_to_home(self, name='home'):
        pass

class Budget(Screen, BaseClass, metaclass=ScreenABCMeta): # Budget Screen
    bg_color = ListProperty([1, 1, 1, 1])
    def __init__(self, **kwargs):
        # Initialize dialog with our callback
        self.budget_dialog = Dialog(
            id='Budget',
            on_accept=self.add_item,
            hint_text='Budget amount'
        )
        self.delete_dialog = DeleteListDialog()
        super().__init__(**kwargs)

    def add_item(self, value, category):
        try:
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Update UI
            new_id = budget_db.insert_budget(value, category, date_str)
            self.ids.total_budget_label.text = f"₱{budget_db.get_all_amounts():,.2f}"
            try:
            # Add list item
                list_item = ListManager.create_list_item(new_id, value, category, date_str, caller=self) #
                self.ids.container.add_widget(list_item)
            except Exception as e:
                print(f"ERROR: {e}")
        except ValueError:
            print("Error: Invalid input (not a number)")

    def add_dialog(self):
        self.budget_dialog.add_dialog()

    def close_dialog(self, *args):
        self.budget_dialog.close_dialog()

    def update_label(self):
        self.ids.total_budget_label.text = f"₱{budget_db.get_all_amounts():,.2f}"  # Update the label with the total budget amount

    def on_enter(self): # returns all budgets from database
        self.ids.container.clear_widgets()
        try:
            all_budget = budget_db.get_all_budgets()
            self.ids.total_budget_label.text = f"₱{budget_db.get_all_amounts():,.2f}"
            for budget in all_budget:
                saved_list_item = ListManager.create_list_item(budget[0], budget[1], budget[2], budget[3], caller=self)
                self.ids.container.add_widget(saved_list_item)
        except Exception as e:
            print(f"Error loading budgets from database: {e}")

    # def on_enter(self): # returns all budgets from database
    #     self.ids.container.clear_widgets()
    #     try:
    #         all_expense = expense_db.get_all_expense()
    #         self.ids.total_expense_label.text = f"₱{expense_db.get_all_amounts_expense():,.2f}"
    #         for expense in all_expense:
    #             saved_list_item = ListManager.create_list_item(expense[0], expense[1], expense[2], expense[3], caller=self)
    #             self.ids.container.add_widget(saved_list_item)
    #     except Exception as e:
    #         print(f"Error loading budgets from database: {e}")

    def return_to_home(self, name = 'budget'):
        self.manager.current = name

class Expense(Screen, BaseClass, metaclass=ScreenABCMeta): # Expense Screen
    bg_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize dialog with our callback
        self.expense_dialog = Dialog(
            id='Expense',
            on_accept=self.add_item,
            hint_text='Expense amount'
        )
        self.budget = Budget()

    def add_item(self, value, category):
        try:
            date_str = datetime.now().strftime("%Y-%m-%d")

            # Update UI
            
            new_id = expense_db.insert_expense(value, category, date_str)
            self.ids.total_expense_label.text = f"₱{expense_db.get_all_amounts_expense():,.2f}"

            try:
            # Add list item
                list_item = ListManager.create_list_item(new_id, value, category, date_str, caller=self) #
                self.ids.container.add_widget(list_item)
            except Exception as e:
                print(f"ERROR: {e}")
            
        except ValueError:
            print("Error: Invalid input (not a number)")

    def add_dialog(self):
        self.expense_dialog.add_dialog()

    def update_label(self):
        self.ids.total_expense_label.text = f"₱{expense_db.get_all_amounts_expense():,.2f}"  # Update the label with the total budget amount

    def close_dialog(self, *args):
        self.expense_dialog.close_dialog()

    def on_enter(self): # returns all budgets from database
        self.ids.container.clear_widgets()
        try:
            all_expense = expense_db.get_all_expense()
            self.ids.total_expense_label.text = f"₱{expense_db.get_all_amounts_expense():,.2f}"
            for expense in all_expense:
                saved_list_item = ListManager.create_list_item(expense[0], expense[1], expense[2], expense[3], caller=self)
                self.ids.container.add_widget(saved_list_item)
        except Exception as e:
            print(f"Error loading budgets from database: {e}")

    def return_to_home(self, name = 'expense'):
        self.manager.current = name

class CheckFinancialStatus:
    def __init__(self):
        self.total_budget = budget_db.get_all_amounts()
        self.total_expense = expense_db.get_all_amounts_expense()
        self.total_essential_budget = budget_db.get_all_essentials_budget()
        self.total_obligation_budget = budget_db.get_all_obligations_budget()
        self.total_other_budget = budget_db.get_all_others_budget()
        self.total_essential_expense = expense_db.get_all_essentials_expense()
        self.total_obligation_expense = expense_db.get_all_obligations_expense()
        self.total_other_expense = expense_db.get_all_others_expense()

    def financial_status(self):
        # Check for None first (missing data)
        if self.total_budget is None or self.total_expense is None:
            return None
        # Then check if both are 0 (no data)
        if self.total_budget == 0 and self.total_expense == 0:
            return None
        # If both budget and expenses are even
        if self.total_budget == self.total_expense:
            return 'breakeven'
        elif self.total_budget > self.total_expense:
            return 'saved'
        else:
            return 'overspent'
        
class BudgetExpenseDetail(CheckFinancialStatus):
    
    def title(self):
        status = self.financial_status()
        if not status: return "No data available"
        elif status == 'breakeven': return "Breakeven"         
        elif status == 'saved': return f"You've saved ₱{self.total_budget - self.total_expense}"
        elif status == 'overspent': return f"You've overspent ₱{abs(self.total_budget - self.total_expense)} so far"
            
    def description(self):
        return f"""
Total Budget: {self.total_budget}
Total Expense: {self.total_expense}
"""

# class BudgetExpenseDetail inherits from CheckFinancialStatus class. Inheriting from the said class gives 
# BudgetExpenseDetail() access to numerous attributes and function

class MostBudgetedAndSpent(BudgetExpenseDetail):
    def title(self):
        budget_category = {
            'Essentials' : self.total_essential_budget,
            'Obligations' : self.total_obligation_budget,
            'Others' : self.total_other_budget
        }
        top_budgeted = max(budget_category, key=budget_category.get)
        budget_value = budget_category[top_budgeted]
        expense_category = {
            'Essentials' : self.total_essential_expense,
            'Obligations' : self.total_obligation_expense,
            'Others' : self.total_other_expense
        }
        most_spent = max(expense_category, key=expense_category.get)
        expense_value = expense_category[most_spent]

        if not budget_value and not expense_value: return f"None"
        else: return f"""
Most Budgeted: {top_budgeted} (₱{budget_value})
Most Spent On: {most_spent} (₱{expense_value})
"""

    def description(self):
        return f"""
Budget:
Essentials - {self.total_essential_budget}
Financial Obligations - {self.total_obligation_budget}
Others - {self.total_other_budget}

Expense:
Essentials - {self.total_essential_expense}
Financial Obligations - {self.total_obligation_expense}
Others - {self.total_other_expense}
"""

class Tips(BudgetExpenseDetail):
    def title(self):
        status = self.financial_status()
        if not status:
            return "No data available"
        elif status == 'breakeven':
            return f"Since you've managed to breakeven,"    
        elif status == 'saved':
            return f"Since you've been saving,"
        elif status == 'overspent':
            return f"Since you've overspent,"
    
    # This function has different functionalities. It is just folded.
    def description(self):
        from random import choice
        status = self.financial_status()
        if not status:
            return "None"

        if status == 'saved':
            tips = [
                "📈 Nice job! Consider putting the extra money into savings or investments.",
                "✅ Think about rewarding yourself with a small treat — you deserve it!",
                "💰 You might want to reduce your budget next time if you consistently underspend.",
                "🟢 Analyze which category you saved most in — can you repeat it?"
            ]
        elif status == 'overspent':
            tips = [
                "❌ Review your biggest expenses this month — cut back on non-essentials.",
                "💸 Try setting a daily spending limit to stay on track.",
                "📉 Look for subscriptions or habits that can be paused or reduced.",
                "🔴 Compare your budget vs actuals to adjust future budgets realistically."
            ]
        elif status == 'breakeven':
            tips = [
                "⚖️ You managed your budget well — but watch for surprise expenses.",
                "💡 Breakeven is a good goal, but can you find room to save a little next time?",
                "🧠 Consider adding an emergency buffer to your budget for more flexibility.",
                "📝 Next month, try setting a challenge: save 5% more."
            ]
        else:
            return "None"

        return choice(tips) 

# These two classes are an example of polymorphism. Tips class inherits from MostBudgetedAndSpent
# class, and each classes both have title and description function, overriding each method.
# Overriding methods allows developers to implement unique implementation while using the same method name

class ClearAllData:
    dialog = None

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(text = f"Are you sure you want to clear all your data? This can’t be undone.", halign = 'left'),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        style="text",
                        on_release=lambda x: self.close_dialog()
                    ),
                    MDButton(
                        MDButtonText(text="Yes"),
                        style="text",
                        on_release=lambda x: self.clear_data()
                    ),
                    spacing="8dp",
                ),
                auto_dismiss=False
            )
            self.dialog.open()
    
    def clear_data(self):
        clear_db.clear_data()
        self.close_dialog()
        self.dialog = None

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

class CardDialog:
    dialog = None

    def __init__(self, dialog_title, text_one):
        self.dialog_title = dialog_title
        self.text_one = text_one


    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(text = f"{self.dialog_title}", halign = 'left'),
                MDDialogSupportingText(text = f"{self.text_one}", halign = 'left'),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="OK"),
                        style="text",
                        on_release= lambda x: self.close_dialog(),
                    ),
                    spacing="8dp",
                ),
                auto_dismiss=False
            )
            self.dialog.open()
    
    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

class Details(Screen):
    
    bg_color = ListProperty([1, 1, 1, 1])

    def budget_expense_tab(self):
        budget_expense_detail = BudgetExpenseDetail()
        title = budget_expense_detail.title()
        message = budget_expense_detail.description()
        card_dialog = CardDialog(title,message)
        card_dialog.show_dialog()

    def most_budgeted_and_spent(self):
        budgeted_and_spent = MostBudgetedAndSpent()
        title = budgeted_and_spent.title()
        message = budgeted_and_spent.description()
        card_dialog = CardDialog(title, message)
        card_dialog.show_dialog()

    def tips(self):
        detail_tips = Tips()
        title = detail_tips.title()
        message = detail_tips.description()
        card_dialog = CardDialog(title, message)
        card_dialog.show_dialog()

    def clear_all_data(self):
        confirm_clear = ClearAllData()
        confirm_clear.show_dialog()

    def return_to_home(self, name = 'details'):
        self.manager.current = name

class Visualization(Screen):
    bg_color = ListProperty([1, 1, 1, 1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_chart()

    def create_chart(self):
        self.ids.chart_container.clear_widgets()  # Clear previous chart if any

        fig, ax = plt.subplots(figsize=(10, 5))

        # Get your actual data from the database
        budgets = [budget[0] for budget in budget_db.get_budget_from_each()]
        expenses = [expense[0] for expense in expense_db.get_expense_from_each()]

        # Plot the lines
        ax.plot(budgets, 'g-', label='Budget', linewidth=2, marker='o')
        ax.plot(expenses, 'r-', label='Expenses', linewidth=2, marker='s')

        # Add customizations
        ax.set_title('Budget vs Expenses', pad=20)
        ax.set_ylabel('Amount (₱)')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed the figure in Kivy
        self.ids.chart_container.add_widget(FigureCanvasKivyAgg(fig))

    def on_enter(self):
        self.create_chart()
        
    def return_to_home(self, name = 'visualization'):
        self.manager.current = name

class MainApp(MDApp):
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
        self.wm.current = 'home'
        return self.wm
    
# This class inherits directly from MDApp, a class from KivyMD library.
# Inheriting from MDApp allows access to Material Design features via KivyMD.
# This class mainly serves as a manager for multiple screens.





if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()
