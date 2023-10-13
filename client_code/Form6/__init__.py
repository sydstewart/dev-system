from ._anvil_designer import Form6Template
from anvil import *
from anvil.js.window import mapboxgl, MapboxGeocoder
import anvil.js
import anvil.http

class Form6(Form6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.dom = anvil.js.get_dom_node(self.spacer_1)
    # self.time_dropdown.items = [("10 minutes", "10"), ("20 minutes", "20"), ("30 minutes", "30")]
    self.token = "pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbG5vajJ1b3kwMG9xMnRscWcxa3p4YXBtIn0.mnKGtTfkOCDAGkdxA-cZnw"
    self.geocoder = MapboxGeocoder({'accessToken': self.token,
                                    'marker': False}) #we've already added a marker 
    # self.mapbox.addControl(self.geocoder)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    mapboxgl.accessToken = self.token
    self.mapbox = mapboxgl.Map({'container': self.dom,
                                'style': 'mapbox://styles/mapbox/streets-v11',
                                # 'style': 'mapbox://styles/brookemyers/cklk04z7x1f5d17pedafupa3e',
                                'center': [-2.834603077700183, 54.1973265832562], #center on Cambridge
                                'zoom': 14})
    
    self.marker = mapboxgl.Marker({'red': '#944840', 'draggable': True})
    self.marker.setLngLat([-2.834603077700183, 54.1973265832562]).addTo(self.mapbox)
    
    # self.geocoder = MapboxGeocoder({'accessToken': mapboxgl.accessToken,
    #                                 'marker': False})
    # self.mapbox.addControl(self.geocoder)
  
  #   self.geocoder.on('result', self.move_marker)
  #   self.marker.on('drag', self.marker_dragged)

    
    
  # def move_marker(self, result):
  #   lnglat = result['result']['geometry']['coordinates']
  #   self.marker.setLngLat(lnglat)
  #   self.get_iso(self.profile_dropdown.selected_value.lower(), self.time_dropdown.selected_value)
    
  # def marker_dragged(self, drag):
  #   self.get_iso(self.profile_dropdown.selected_value.lower(), self.time_dropdown.selected_value)
    
  # def get_iso(self, profile, contours_minutes):
  #   if not self.mapbox.getSource('iso'):
  #     self.mapbox.addSource('iso', {'type': 'geojson',
  #                                   'data': {'type': 'FeatureCollection',
  #                                            'features': []}
  #                                  }
  #                          )
  #     self.mapbox.addLayer({'id': 'isoLayer',
  #                           'type': 'fill',
  #                           'source': 'iso',
  #                           'layout': {},
  #                           'paint': {
  #                           'fill-color': '#955547',
  #                           'fill-opacity': 0.3}
  #                          })
    
  #   lnglat = self.marker.getLngLat()
  #   response = anvil.http.request(f"https://api.mapbox.com/isochrone/v1/mapbox/{profile}/{lnglat.lng},{lnglat.lat}?contours_minutes={contours_minutes}&polygons=true&access_token={self.token}", json=True)
  #   self.mapbox.getSource('iso').setData(response)

      # map.on('click', (event) => {
      #   // If the user clicked on one of your markers, get its information.
      #   const features = map.queryRenderedFeatures(event.point, {
      #     layers: ['YOUR_LAYER_NAME'] // replace with your layer name
      #   });
      #   if (!features.length) {
      #     return;
      #   }
      #   const feature = features[0];



