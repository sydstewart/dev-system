from ._anvil_designer import Form7Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import mapboxgl, MapboxGeocoder, document , jQuery
from anvil.js import get_dom_node
import anvil.http


class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #token for mapbox
    self.token = "pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbG5vajJ1b3kwMG9xMnRscWcxa3p4YXBtIn0.mnKGtTfkOCDAGkdxA-cZnw"
    # Any code you write here will run before the form opens.
    #set up dom for javascript for self.map_1
    self.dom = anvil.js.get_dom_node(self.map_1)
    # self.repeating_panel_1.items = app_tables.trees.search()

  #show form with maps
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    
    # get tree list into dropdowns
    treelist =  applications =list({(r['Name']) for r in app_tables.trees.search(tables.order_by('Name'))})
    self.drop_down_1.items =treelist
    self.drop_down_2.items = treelist
    
    #declare  mapbox token
    mapboxgl.accessToken = self.token

    # layout map using self.maxbox
    self.mapbox = mapboxgl.Map({
    'container': self.dom,
     # // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    'style': 'mapbox://styles/mapbox/streets-v12',
    'center': [-2.834603077700183, 54.1973265832562],
    'zoom': 15})
   
    # get location of trees using the tree type dropdown selection
    locations = app_tables.location.search(TreeType = self.drop_down_1.selected_value) #anvil.server.call('get_all_locations' )
    # self.hits_textbox.text = len(locations) 
    print(self.drop_down_1.selected_value)

    # populate map with markers for tree4s for dropdown treetype  selection
    for location in locations:
       self.marker = mapboxgl.Marker({'color': 'brown', 'scale': '0.75', 'draggable': False})
       lat = location['Latitude']
       lng = location['Longitude']
       loc = location['Location']
       notes = location['Desc']
       treetype = location['TreeType']
       print('lng',lng, ' ' ,'lat',lat)
       #create a marker popup text
       popuptext = ('Name:' + loc + '<br>' +
                    'Notes:' + notes + '<br>' +
                    'lat:' + str(lat) + '<br>' +   
                    'lng:' + str(lng) + '<br>' +
                    'treetype ' + treetype + '<br>' +
                   '<button  id="myBtn">Hello </button>')
                   # '<button (click)="logger">View Full</button>')
       self.marker.on('click', self.text_change)
       # print(self.dom.getElementById('button'))
       self.marker.setLngLat([lng,lat]).addTo(self.mapbox)
       popup = mapboxgl.Popup({ 'offset': 25, 'max-width': 1000}).setHTML(popuptext)
    
       self.marker.setPopup(popup)
       
   # create a dragable blue marker for positioning a new tree
 
    self.marker = mapboxgl.Marker({'blue': '#0000FF', 'draggable': True})
    self.marker.setLngLat([-2.834603077700183, 54.1973265832562]).addTo(self.mapbox)
    popup = mapboxgl.Popup({ 'offset': 20 }).setText(
         '-2.834603077700183, 54.1973265832562')
    self.marker.on('dragend', self.onDragEnd)
    
         
    
  # not ussed yet???
  def move_marker(self, result):
    # lnglat = result['result']['geometry']['coordinates']
    lnglat = self.marker.getLngLat();
    popup = mapboxgl.Popup({ 'offset': 25 }).setText(
         lnglat)
    self.marker.setPopup(popup)
    alert(lnglat)
 
   # get lng lat of blue marker on dragging blue marker 
  def onDragEnd(self, dragend):
      xy = self.marker.getLngLat()
      alert(str(xy['lat']) + ' ' + str(xy['lng']))
      self.latitude_text_box.text = xy['lat']
      self.longitude_text_box.text = xy['lng']
      popup = mapboxgl.Popup({ 'offset': 25 }).setText(str(xy['lat']) + ' ' + str(xy['lng']))
      self.marker.setPopup(popup)


   # add a new tree to database
  def add_location_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    lnglat = self.marker.getLngLat();
    
    self.latitude_text_box.text = lnglat['lat']
    self.longitude_text_box.text = lnglat['lng']

    name = self.location_text_box.text
    desc = self.location_description_text_area.text
    lat =  self.latitude_text_box.text
    lng = self.longitude_text_box.text
    treetype =self.drop_down_2.selected_value
    
    anvil.server.call('add_location', name, desc, lat, lng,treetype)
    Notification("We have recorded your location, and sent an email to the owner of this map.", title="Thanks!", timeout = 10).show()
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.location_text_box.text  =""
    self.location_description_text_area.text =""
    self.latitude_text_box.text = ""
    self.longitude_text_box.text  = ""
   
    pass

   # repopulate map when treetype dropdown changed
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    # reset map to blank
    self.mapbox = mapboxgl.Map({
    'container': self.dom,
        # // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    'style': 'mapbox://styles/mapbox/streets-v12',
    'center': [-2.834603077700183, 54.1973265832562],
    'zoom': 15})
    
    self.marker = mapboxgl.Marker({'blue': '#0000FF', 'draggable': True})
    self.marker.setLngLat([-2.834603077700183, 54.1973265832562]).addTo(self.mapbox)
    popup = mapboxgl.Popup({ 'offset': 20 }).setText(
         '-2.834603077700183, 54.1973265832562')
    self.marker.setPopup(popup)
    self.marker.on('dragend', self.onDragEnd)  
    
    # get markers for tree type
    locations = app_tables.location.search(TreeType = self.drop_down_1.selected_value) #anvil.server.call('get_all_locations' )
    # self.hits_textbox.text = len(locations) 
    print(self.drop_down_1.selected_value)
    for location in locations:
       self.marker = mapboxgl.Marker({'color': 'brown', 'scale': '0.75', 'draggable': False})
       lat = location['Latitude']
       lng = location['Longitude']
       loc = location['Location']
       notes = location['Desc']
       treetype = location['TreeType']
       print('lng',lng, ' ' ,'lat',lat)
      # get popup texts
       popuptext = ('Name:' + loc + '<br>' +
                    'Notes:' + notes + '<br>' +
                    'lat:' + str(lat) + '<br>' +   
                   'lng:' + str(lng) + '<br>' +
                    'treetype ' + treetype + '<br>' +
                  '<button  id="myBtn">Hello </button>')
                   # '<button (click)="logger">View Full</button>')
       
       # print(self.dom.getElementById('button'))
       self.marker.setLngLat([lng,lat]).addTo(self.mapbox)
       popup = mapboxgl.Popup({ 'offset': 25, 'max-width': 1000}).setHTML(popuptext)
     
       self.marker.setPopup(popup)
      
    # find Woodland trust webpage and doisplay in frame
    url = app_tables.trees.get(Name=self.drop_down_1.selected_value)
    self.column_panel_1.clear()
    # print('url',url['WoodlandTrust_link'],'dropdown',self.drop_down_1.selected_value )
    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src",url['WoodlandTrust_link'])
    self.column_panel_1.visible = True
    iframe.appendTo(get_dom_node(self.column_panel_1))
    pass







 
  



