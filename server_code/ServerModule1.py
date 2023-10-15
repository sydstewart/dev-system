import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime


@anvil.server.callable
def add_location(name, desc, lat, lng):
  app_tables.location.add_row(
    location =name, 
    desc =desc, 
    latitude = lat,
    longitude = lng, 
    created=datetime.now()
  )