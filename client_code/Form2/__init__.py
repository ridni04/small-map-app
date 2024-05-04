from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# Assuming 'database' is a list of dictionaries representing your images database
# Each dictionary has keys: 'location', 'image', and 'caption'

# Function to find the caption for the current image
def find_caption_for_image(current_image):
    for entry in database:
        if entry['image'] == current_image:
            return entry['caption']
    return "Caption not found."

# Function to update the caption label
def update_caption_label(image_1, label_r):
    # Find the caption for the image being shown in image_1
    caption = find_caption_for_image(image_1)
    # Update the text of label_r with the new caption
    label_r.config(text=caption)

# Example usage:
# update_caption_label(current_image_displayed_in_image_1, label_r)
