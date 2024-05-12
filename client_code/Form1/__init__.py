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
        
        # Adjust the width of image_7
    
  

  def marker_click(self, sender, **properties):
    self.pictures = app_tables.images.search(Location=sender.tag)    
    for i, picture in enumerate(self.pictures):
        # Set the source of the image to the current picture
        self.image_1.source = picture['ID']
        
    if (len(self.pictures) + 1) % 3 == 0:  # Check if the number of images is a multiple of 3
        self.image_1.style = 'width: 150%; height: auto;'  # Enlarge the image
    else:
        self.image_1.style = 'width: 100%; height: auto;'  # Normal size for other images
    
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
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['ID']

  def left_btn_click(self, **event_args):
    self.count_click -= 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['ID']


  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.switch_to_form2(**event_args)
 
  def switch_to_form2(self, **event_args):
    # This method will be called when outlined_button_3 is clicked
    
    # Open Form2
    open_form('Form2')
    
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.switch_to_sorry(**event_args)
 
  def switch_to_sorry(self, **event_args):
    # This method will be called when outlined_button_3 is clicked
    
    # Open Sorry
    open_form('Sorry')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("https://photos.app.goo.gl/WtcpCUbHuJi2SJEi6")

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Wow!!!")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_3.source = image_source_1
    self.image_3.visible = True

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_3.source = image_source_2
    self.image_3.visible = True

  def form_show(self, **event_args):
    self.slider_1.min = 0
    self.slider_1.max = 100
    self.slider_1.start = [10]
    self.slider_1.step = 10
    
    self.slider_1.format = "{:.0f}"

  def slider_1_change(self, **event_args):
    slider_value = self.slider_1.value
    
    self.image_4.visible = False
    self.image_5.visible = False
    self.image_6.visible = False
    self.label_4a.text = ""
    self.label_5a.text = ""
    self.label_6a.text = ""
    
    if slider_value > 30:
        self.image_4.source = '_/theme/MOMG1.gif'
        self.image_4.visible = True
        self.label_4a.text = "Happy"
    if slider_value > 60:
        self.image_5.source = '_/theme/momg2.gif'
        self.image_5.visible = True
        self.label_5a.text = "Mothers"      
        
    if slider_value > 90:  
        self.image_6.source = '_/theme/momg3.gif'
        self.image_6.visible = True
        self.label_6a.text = "Day!"


image_source_1 = "_/theme/R.gif"
image_source_2 = "_/theme/giphy (1).gif" 




