from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from anvil import Button, Image

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.count_click = 0
  
    self.map_1.center = GoogleMap.LatLng(30.285257089684773, -97.73679600611173)
    self.map_1.zoom = 18
    self.map_1.clickable_icons=False
    self.map_1.fullscreen_control=False
  
    pins = tables.app_tables.locations.search()
    self.markerList = []
    ind = 0
    for pin in pins:
      self.markerList.append(GoogleMap.Marker(animation=GoogleMap.Animation.DROP,position=GoogleMap.LatLng(pin['Lat'],pin['Lon'])))
      self.markerList[ind].tag = pin
      self.markerList[ind].add_event_handler('click',self.marker_click)
      self.map_1.add_component(self.markerList[ind])
      ind += 1
  

  def marker_click(self, sender, **properties):
    self.infoAbtPin.visible=True
    self.count_click += 1
    self.infoAbtPin.text= 'You have clicked a pin ' + str(self.count_click) + ' time'
  
    self.label_b.text = sender.tag['Name']  
    self.label_b.visible = False
    self.repeating_panel_1.visible = False
    self.label_b.visible = True
    self.repeating_panel_1.visible = False
    if self.count_click > 1:
      self.infoAbtPin.text += 's'
      self.pictures = tables.app_tables.images.search(Location=sender.tag)
      self.location = sender.tag

    self.infoAbtPin.text += '\nThis pin\'s location is '+str(sender.tag['Lat'])+' North, '+str(sender.tag['Lon']) + ' West'
    self.infoAbtPin.text += '\nIt is called ' + sender.tag['Name']
    
    self.image_1.visible=True
    self.pictures = tables.app_tables.images.search(Location=sender.tag)
    self.location = sender.tag
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['ID']
  

  def signBtn_click(self, **event_args):
    if len(self.text_box_1.text.strip())>0:
      self.wallLbl.visible=True
      self.repeating_panel_1.visible=True
      now = datetime.datetime.now()
      tables.app_tables.wall.add_row(Signer=self.text_box_1.text.strip(),When=now, Location = self.location, Message = self.text_box_2.text.strip())
      self.load_wall()
    else:
      alert('You cannot sign without a name!')

  def load_wall(self):
    wall = tables.app_tables.wall.search(Location = self.location)
    if len(wall) == 0:
      self.wallLbl.visible=False
      self.repeating_panel_1.visible=False
    else:
      self.wallLbl.visible=True
      self.repeating_panel_1.visible=True
      self.repeating_panel_1.items=[w for w in wall]

  def right_btn_click(self, **event_args):
    self.count_click += 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']

  def left_btn_click(self, **event_args):
    self.count_click -= 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']


  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.outlined_button_1.background = 'lightblue'
    self.outlined_button_1.text = "Baby Bevo wasn't a regular Bevo. He was a little squishmallow Bevo."

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("This Squishmallow Bevo had dreams. He wanted to go to the top of UT Tower! But Baby Bevo wasn't allowed in the tower, so Baby Bevo decided to go up all the buildings on Campus!")

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Baby Bevo wasn't a regular Bevo. He was a little squishmallow Bevo.")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_4.source = image_source_1
    self.image_4.visible = True

  def button_4_click(self, **event_args):
     self.image_4.source = image_source_2
     self.image_4.visible = True
     self.image_1.visible = False
  def form_show(self, **event_args):
    self.slider_1.min = 0
    self.slider_1.max = 100
    self.slider_1.start = [10]
    self.slider_1.step = 10
    
    self.slider_1.format = "{:.0f}"

  def slider_1_change(self, **event_args):
    slider_value = self.slider_1.value
    
    self.image_4.visible = False
    self.image_a.visible = False
    self.image_6.visible = False
    self.label_4_im.text = ""
    self.label_a_im.text = ""
    self.label_6_im.text = ""
    
    if slider_value > 30:
        self.image_4.source = '_/theme/hen.gif'
        self.image_4.visible = True
        self.label_4_im.text = "Thanks"
      
        
    if slider_value > 90:  
        self.image_6.source = '_/theme/hen4.gif'
        self.image_6.visible = True
        self.label_6_im.text = "Coming"

   
def change_image(self):
    """This method is called when the button is clicked"""
    self.image_4.source = '_/theme/hen.gif'
    self.image_4.visible = True
image_source_1 = "_/theme/giphy.gif"
image_source_2 = "_/theme/tenor.gif" 
image_source_3 = "_/theme/hen.gif" 

# Event handler for when an image is selected
def on_image_selected(self, **event_args):
    # Assuming 'selected_image_id' is the ID of the selected image
    selected_image_id = self.images_table.selected_row['id'] # Retrieve this from your app logic

    # Search for the image in the 'images' table by its ID
    selected_image = app_tables.images.get(id=image_id)

    # Check if the image was found
    if selected_image:
        # Update the label's text with the caption from the 'captions' column
        self.label_r.text = selected_image['caption']
    else:
        # If the image is not found, display a default message or handle the error
        self.label_r.text = "Caption not found."
