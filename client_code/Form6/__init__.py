from ._anvil_designer import Form6Template
from anvil import *
from anvil.js.window import mapboxgl
import anvil.js
import anvil.http

class Form6(Form6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def spacer_1_show(self, **event_args):
    """This method is called when the Spacer is shown on the screen"""
    pass

