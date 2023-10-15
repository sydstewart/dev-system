import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, time , date , timedelta


@anvil.server.callable
def add_location(name, desc, lat, lng):
  app_tables.location.add_row(
    Location =name, 
    Desc =desc, 
    Latitude = lat,
    Longitude = lng, 
    created=datetime.now()
  )
  email ='sydney.w.stewart@gmail.com'
  anvil.email.send(to="noreply@anvil.works", # Messages go to the app owner 
                   subject="Location from {}".format(name),
                   text=f"""A new person has filled out the location form! Name: {name} Email address: {email} Description:{desc} """)