from ._anvil_designer import SorryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Sorry(SorryTemplate):
    # Define image sources as a dictionary for better management
    image_sources = {
        'button_1': "_/theme/3.1.gif",
        'button_2': "_/theme/3.2.gif",
        'button_3': "_/theme/3.3.gif",
        'button_4': "_/theme/3.4.gif",
        'button_5': "_/theme/3.5.gif"
    }

    image_source_1 = "_/theme/3.1.gif"
    image_source_2 = "_/theme/3.2.gif"
    image_source_3 = "_/theme/3.3.gif"
    image_source_4 = "_/theme/3.4.gif"
    image_source_5 = "_/theme/3.5.gif"

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.button_6.set_event_handler('click', self.switch_to_form1)
    def switch_to_form1(self, **event_args):
        # This method will be called when outlined_button_3 is clicked
        
        # Open Form1
        open_form('Form1')


        # Any code you write here will run before the form opens.

    def button_click(self, button_name, **event_args):
        """Generic method called when any button is clicked"""
        # Set the image source based on the button clicked
        self.image_1.source = self.image_sources[button_name]
        self.image_1.visible = True

    def button_1_click(self, **event_args):
        self.button_click('button_1')

    def button_2_click(self, **event_args):
        self.button_click('button_2')

    def button_3_click(self, **event_args):
        self.button_click('button_3')

    def button_4_click(self, **event_args):
        self.button_click('button_4')

    def button_5_click(self, **event_args):
        self.button_click('button_5')


