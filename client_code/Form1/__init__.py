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
        self.outlined_button_1.background = 'lightblue'
        self.count_click = 0

        # Initialize map properties
        self.map_1.center = GoogleMap.LatLng(30.285257089684773, -97.73679600611173)
        self.map_1.zoom = 18
        self.map_1.clickable_icons = False
        self.map_1.fullscreen_control = False

        # Load pins from the database and create markers
        pins = tables.app_tables.locations.search()
        self.markerList = []
        self.pin_walls = {}  # Dictionary to store walls associated with each pin

        for pin in pins:
            marker = GoogleMap.Marker(animation=GoogleMap.Animation.DROP, position=GoogleMap.LatLng(pin['Lat'], pin['Lon']))
            marker.tag = pin
            marker.add_event_handler('click', self.marker_click)
            self.map_1.add_component(marker)
            self.markerList.append(marker)
            self.pin_walls[pin['Name']] = []  # Initialize an empty list for each pin

    def marker_click(self, sender, **properties):
        self.infoAbtPin.visible = True
        self.count_click += 1
        self.infoAbtPin.text = f'You have clicked pin {self.count_click} time'
        if self.count_click > 1:
            self.infoAbtPin.text += 's'

        pin_name = sender.tag['Name']
        self.infoAbtPin.text += f'\nThis pin\'s location is {sender.tag["Lat"]} North, {sender.tag["Lon"]} West'
        self.infoAbtPin.text += f'\nIt is called {pin_name}'

        self.image_1.visible = True
        self.pictures = tables.app_tables.images.search(Location=sender.tag)
        self.location = sender.tag
        self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image'] if len(self.pictures) > 0 else None

        # Load the wall associated with this pin
        self.load_wall(pin_name)

    def load_wall(self, pin_name):
        wall = tables.app_tables.wall.search(Location=self.location)
        self.pin_walls[pin_name] = wall  # Store the wall entries for this pin

        if len(wall) == 0:
            self.wallLbl.visible = False
            self.repeating_panel_1.visible = False
        else:
            self.wallLbl.visible = True
            self.repeating_panel_1.visible = True
            self.repeating_panel_1.items = wall

    def right_btn_click(self, **event_args):
        self.count_click += 1
        self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image'] if len(self.pictures) > 0 else None

    pass

    def left_btn_click(self, **event_args):
        self.count_click -= 1
        self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']

    def drop_down_1_change(self, **event_args):
      self.image_1.source = self.pictures[self.drop_down_1.selected_value % len(self.pictures)]['Image']
  
    def map_1_bounds_changed(self, **event_args):
      """This method is called when the viewport bounds have changed."""
      pass
  
    def outlined_button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.outlined_button_1.background = 'lightblue'
      self.outlined_button_1.text = "Baby Bevo wasn't a regular Bevo. He was a little squishmallow Bevo."
    def button_1_click(self, **event_args):
          """This method is called when the button is clicked"""
          alert("This Squishmallow Bevo had dreams. He wanted to go to the top of UT Tower! But Baby Bevo wasn't allowed in the tower, so Baby Bevo decided to go up all the buildings on Campus!")

    def signBtn_click(self, **event_args
        # Code to execute when signBtn is clicked or enter is pressed in text_box_1
        pass

    # Make sure to bind the event handler to the signBtn and text_box_1
    self.signBtn.set_event_handler('click', self.signBtn_click)
    self.text_box_1.set_event_handler('pressed_enter', self.signBtn_click)