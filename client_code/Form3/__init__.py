from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_1.source = image_source_1
    self.image_1.visible = True

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_1.source = image_source_2
    self.image_1.visible = True
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_1.source = image_source_3
    self.image_1.visible = True

image_source_1 = "_/theme/s.gif"
image_source_2 = "_/theme/tenor (1).gif" 
image_source_3 = "_/theme/sorry.gif" 