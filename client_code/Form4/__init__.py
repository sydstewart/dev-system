from ._anvil_designer import Form4Template
from anvil import *
from ..Form1 import Form1
from ..Form2 import Form2
from ..Form3 import Form3

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == 'Form1':
       open_form('Form1')
    elif self.drop_down_1.selected_value == 'Form2':
      open_form('Form2')
    elif self.drop_down_1.selected_value == 'Form3':
      open_form('Form3')

