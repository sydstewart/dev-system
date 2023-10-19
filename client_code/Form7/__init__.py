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
    self.token = "pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbG5vajJ1b3kwMG9xMnRscWcxa3p4YXBtIn0.mnKGtTfkOCDAGkdxA-cZnw"
    # Any code you write here will run before the form opens.
    self.dom = anvil.js.get_dom_node(self.map_1)
    self.repeating_panel_1.items = app_tables.trees.search()
    treelist =  applications =list({(r['Name']) for r in app_tables.trees.search(tables.order_by('Name'))})
    self.drop_down_1.items =treelist
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    mapboxgl.accessToken = self.token
    self.mapbox = mapboxgl.Map({
    'container': self.dom,
    
    # // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    'style': 'mapbox://styles/mapbox/streets-v12',
    'center': [-2.834603077700183, 54.1973265832562],
    'zoom': 15})
    locations = app_tables.location.search(TreeType = self.drop_down_1.selected_value) #anvil.server.call('get_all_locations' )
    # self.hits_textbox.text = len(locations) 
    
    for location in locations:
       self.marker = mapboxgl.Marker({'color': 'brown', 'scale': '0.75', 'draggable': False})
       lat = location['Latitude']
       lng = location['Longitude']
       loc = location['Location']
       notes = location['Desc']
       print('lng',lng, ' ' ,'lat',lat)

       popuptext = ('Name:' + loc + '<br>' +
                    'Notes:' + notes + '<br>' +
                    'lat:' + str(lat) + '<br>' +   
                   'lng:' + str(lng) + '<br>' +
                  '<button  id="myBtn">Hello </button>')
                   # '<button (click)="logger">View Full</button>')
       self.marker.on('click', self.text_change)
       # print(self.dom.getElementById('button'))
       self.marker.setLngLat([lng,lat]).addTo(self.mapbox)
       popup = mapboxgl.Popup({ 'offset': 25, 'max-width': 1000}).setHTML(popuptext)

      
       self.marker.setPopup(popup)
       
  # print('button', document.getElementById('View Full'))
  # document.getElementById("myBtn")  #.addEventListener("click",self.click)
  # # def click(self):
  #   # alert('Syd')

  # xdom.addEventListener('click',self.change_text)

  # def change_text(self):
  #  self.my_label.text='audio has finished playing'
     
    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src"," \
     https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/alder/") 
    iframe.appendTo(get_dom_node(self.column_panel_1))

  def text_change(self, popuptext):
    self.text_area_1.text = popuptext
    alert(popuptext)
 
   # document.getElementById('view-full').addEventListener('click', logger) 
    self.marker = mapboxgl.Marker({'blue': '#0000FF', 'draggable': True})
    self.marker.setLngLat([-2.834603077700183, 54.1973265832562]).addTo(self.mapbox)
    popup = mapboxgl.Popup({ 'offset': 20 }).setText(
         '-2.834603077700183, 54.1973265832562')

    self.marker.on('click', popuptext)
    xdom=document.getElementsById("myBtn")
    popupElem = popup.getElement(xdom)
    popupElem.style.fontSize = "25px"
    print(xdom[''])
    xdom.addEventListener('click',self.text_change)
    # self.marker.on('click', self.text_change)
  def text_change(self):

    
    self.marker.on('dragend', self.onDragEnd)  
    self.marker.on('help', self.logger) 
   
  
  def logger(self, **event_args):
     alert('syd')
  
  
  def move_marker(self, result):
    # lnglat = result['result']['geometry']['coordinates']
    lnglat = self.marker.getLngLat();
    popup = mapboxgl.Popup({ 'offset': 25 }).setText(
         lnglat)
    self.marker.setPopup(popup)
    alert(lnglat)
  def show_info(self,**event_args):
      alert('Syd')
  def onDragEnd(self, dragend):
      xy = self.marker.getLngLat()
      # alert(xy)
      popup = mapboxgl.Popup({ 'offset': 25 }).setText(xy)
      self.marker.setPopup(popup)



  def add_location_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    lnglat = self.marker.getLngLat();
    
    self.latitude_text_box.text = lnglat['lat']
    self.longitude_text_box.text = lnglat['lng']

    name = self.location_text_box.text
    desc = self.location_description_text_area.text
    lat =  self.latitude_text_box.text
    lng = self.longitude_text_box.text 
    
    anvil.server.call('add_location', name, desc, lat, lng)
    Notification("We have recorded your location, and sent an email to the owner of this map.", title="Thanks!", timeout = 10).show()
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.location_text_box.text  =""
    self.location_description_text_area.text =""
    self.latitude_text_box.text = ""
    self.longitude_text_box.text  = ""
   
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    
    pass




 
  



