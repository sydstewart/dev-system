from ._anvil_designer import Form7Template
from anvil import *
from anvil.js.window import mapboxgl, MapboxGeocoder
import anvil.js
import anvil.http

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.token = "pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbG5vajJ1b3kwMG9xMnRscWcxa3p4YXBtIn0.mnKGtTfkOCDAGkdxA-cZnw"
    # Any code you write here will run before the form opens.
    self.dom = anvil.js.get_dom_node(self.spacer_1)
  
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    mapboxgl.accessToken = self.token
    self.mapbox = mapboxgl.Map({
    'container': self.dom,
    # // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    'style': 'mapbox://styles/mapbox/streets-v12',
    'center': [-2.834603077700183, 54.1973265832562],
    'zoom': 15})
    
    self.marker = mapboxgl.Marker({'red': '#944840', 'draggable': True})
    self.marker.setLngLat([-2.834603077700183, 54.1973265832562]).addTo(self.mapbox)
    popup = mapboxgl.Popup({ 'offset': 25 }).setText(
         'Construction on the Washington Monument began in 1848.')
    self.marker.setPopup(popup)
    self.geocoder = MapboxGeocoder({'accessToken': mapboxgl.accessToken,
                                    'marker': False})
    self.mapbox.addControl(self.geocoder)
  
    self.geocoder.on('result', self.move_marker)
    # self.marker.on('drag', self.marker_dragged)

    popup = mapboxgl.Popup({ 'offset': 25 }).setText(
         'Construction on the Washington Monument began in 1848.')
    self.marker.on('dragend', sel.onDragEnd)  
  
  def move_marker(self, result):
    lnglat = result['result']['geometry']['coordinates']
    self.marker.setLngLat(lnglat)
    popup = mapboxgl.Popup({ 'offset': 25 }).setText(
         lnglat)
    self.marker.setPopup(popup)
    alert(lnglat)
    
  def onDragEnd(self, result):
      lngLat = marker.getLngLat();
      popup = mapboxgl.Popup({ 'offset': 25 }).setText(lnglat)
      self.marker.setPopup(popup)

 
  



