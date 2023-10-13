from ._anvil_designer import Form4Template
from anvil import *
from ..Form1 import Form1
from ..Form2 import Form2
from ..Form3 import Form3
from ..Form5 import Form5

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.map_1.center=GoogleMap.LatLng(54.1973265832562, -2.834603077700183)
    self.map_1.zoom = 18
    green_icon = GoogleMap.Icon(
      url="http://maps.google.com/mapfiles/kml/paddle/grn-blank.png"
    )

    marker = GoogleMap.Marker(
    animation=GoogleMap.Animation.DROP,
    position=GoogleMap.LatLng(54.1973265832562, -2.834603077700183),
    icon = green_icon
    )
     

    self.map_1.add_component(marker)

    def marker_click(sender, **event_args):
       i =GoogleMap.InfoWindow(content=Label(text="This is Home!"))
       i.open(map, sender)

    marker.add_event_handler("click", marker_click)



  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == 'Form1':
       open_form('Form1')
    elif self.drop_down_1.selected_value == 'Form2':
      open_form('Form2')
    elif self.drop_down_1.selected_value == 'Form3':
      open_form('Form3')
    elif self.drop_down_1.selected_value == 'Form4':
      open_form('Form4')
    elif self.drop_down_1.selected_value == 'Form5':
      open_form('Form5')
    elif self.drop_down_1.selected_value == 'Form6':
      open_form('Form6')

  # def map_1_click(self, lat_lng, pixel, **event_args):
  #   """This method is called when the user clicks on the map."""
    
 
    # def marker_click(sender, **event_args):
    #       i =GoogleMap.InfoWindow(content=Label(text="This is Cambridge!"))
    #       i.open(map, sender)
    # marker.add_event_handler("click", marker_click)