import matplotlib.pyplot as plt
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

# Sample data - replace with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
budget = [2000, 2200, 2100, 2300, 2400, 2500, 
          2600, 2700, 2800, 2900, 3000, 3100]
expenses = [1800, 2300, 1950, 2400, 2200, 2600, 
            2700, 2550, 2900, 2800, 3100, 3200]

Builder.load_string("""
<BudgetTracker>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    
    # MDToolbar:
    #     title: "Budget vs Expenses"
    #     elevation: 10
    
    BoxLayout:
        id: chart_container
        size_hint_y: 0.9
    
    MDFloatLayout:
        size_hint_y: 0.1
        MDLabel:
            text: "Budget (Green) vs Expenses (Red)"
            halign: 'center'
            font_style: 'Headline'
""")

class BudgetTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_chart()

    def create_chart(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Plot both lines
        ax.plot(months, budget, 'g-', label='Budget', linewidth=2, marker='o')
        ax.plot(months, expenses, 'r-', label='Expenses', linewidth=2, marker='s')
        
        # Customize the chart
        ax.set_title('Monthly Budget vs Expenses', pad=20)
        ax.set_xlabel('Months')
        ax.set_ylabel('Amount ($)')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        # Add to Kivy layout
        self.ids.chart_container.add_widget(FigureCanvasKivyAgg(fig))

class BudgetApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return BudgetTracker()

if __name__ == '__main__':
    BudgetApp().run()
