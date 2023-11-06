import anvil.files
from anvil.files import data_files
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, time , date , timedelta
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

@anvil.server.callable
def add_location(name, desc, lat, lng, treetype):
  app_tables.location.add_row(
    Location =name, 
    Desc =desc, 
    Latitude = lat,
    Longitude = lng, 
    TreeType= treetype,
    created=datetime.now()
  )
  email ='sydney.w.stewart@gmail.com'
  anvil.email.send(to="noreply@anvil.works", # Messages go to the app owner 
                   subject="Location from {}".format(name),
                   text=f"""A new person has filled out the location form! Name: {name} Email address: {email} Description:{desc} """)



@anvil.server.callable
def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row 
      # We use Python's **kwargs syntax to pass the whole dict as 
      # keyword arguments 
      app_tables.your_table_name_here.add_row(**d)

@anvil.email.handle_message
def handle_incoming_emails(msg):
  
  msg.reply(text="Thank you for your message.")

  msg_row = app_tables.received_messages.add_row(
              from_addr=msg.envelope.from_address, 
              to=msg.envelope.recipient,
              subject =msg.subject,
              text=msg.text, 
              html=msg.html
            )
  for a in msg.attachments:
    app_tables.attachments.add_row(
      message=msg_row, 
      attachment=a
    )