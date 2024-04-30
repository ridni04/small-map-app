from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.youtube_video_1.youtube_id = 'FALlhXl6CmA'
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
  
      # wall stuff
      #self.load_wall()
      #self.drop_down_1.items = [('Hello',1),('There',2)]

  def marker_click(self, sender, **properties):
    self.infoAbtPin.visible=True
    self.count_click += 1
    self.infoAbtPin.text= 'You have clicked a pin ' + str(self.count_click) + ' time'
    if self.count_click > 1:
      self.infoAbtPin.text += 's'

    self.infoAbtPin.text += '\nThis pin\'s location is '+str(sender.tag['Lat'])+' North, '+str(sender.tag['Lon']) + ' West'
    self.infoAbtPin.text += '\nIt is called ' + sender.tag['Name']
    
    self.image_1.visible=True
    self.pictures = tables.app_tables.images.search(Location=sender.tag)
    self.location = sender.tag
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']

    

  def disappearBtn_click(self, **event_args):
    if self.map_1.visible == True:
      self.map_1.visible = False
      self.disappearBtn.text='Make the map appear!'
      open_form('Form2')
    else:
      self.map_1.visible=True
      self.disappearBtn.text='Make the map disappear!'

  def signBtn_click(self, **event_args):
    if len(self.text_box_1.text.strip())>0:
      self.wallLbl.visible=True
      self.repeating_panel_1.visible=True
      now = datetime.datetime.now()
      tables.app_tables.wall.add_row(Signer=self.text_box_1.text.strip(),When=now, Location = self.location, Comments = self.text_box_2.text.strip())
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
    # write some python code for what happens when this button is clicked
    # go to the next picture
    pass

  def left_btn_click(self, **event_args):
    self.count_click -= 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']

  def drop_down_1_change(self, **event_args):
    self.image_1.source = self.pictures[self.drop_down_1.selected_value % len(self.pictures)]['Image']

  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass


