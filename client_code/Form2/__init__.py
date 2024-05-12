from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form

class Form2(Form2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Bind the click event of outlined_button_3 to the method
        self.outlined_button_3.set_event_handler('click', self.switch_to_form1)
        self.outlined_button_4.set_event_handler('click', self.switch_to_form3)
      
        
    def switch_to_form1(self, **event_args):
        # This method will be called when outlined_button_3 is clicked
        
        # Open Form1
        open_form('Form1')
    def switch_to_form3(self, **event_args):
        # This method will be called when outlined_button_3 is clicked
        
        # Open Form1
        open_form('Form3')

    def outlined_button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Nope")
    def outlined_button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Not quite, but here: https://youtube.com/playlist?list=PLjvmvKWdNwufE7DunZgHDTqdXY1-Yw___&si=LPxI73xxdX22MEVd")


