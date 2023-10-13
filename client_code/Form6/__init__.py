from ._anvil_designer import Form6Template
from anvil import *
from anvil.js.window import mapboxgl
import anvil.js
import anvil.http

class Form6(Form6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.token = "<pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbG5vZXlqNm8wNGx3Mmpxb2FhM3RrZHB6In0.kvIg63WDg0fGaJjA2TR_3w"
    # Any code you write here will run before the form opens.



  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    #I defined my access token in the __init__ 
    mapboxgl.accessToken = self.token 

    #put the map in the spacer 
    self.mapbox = mapboxgl.Map({'container': anvil.js.get_dom_node(self.spacer_1), 
                                'style': 'mapbox://styles/mapbox/streets-v11', #use the standard Mapbox style 
                                'center': [0.1218, 52.2053], #center on Cambridge 
                                'zoom': 11})
    pass


