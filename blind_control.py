import requests
import os

locations = {
  'bedroom': 'input_number.bedroom_blind',
  'office': 'input_number.office_blind'
}

class BlindController:
  def __init__(self,ha_host,ha_port,api_key):
    self.ha_host = ha_host
    self.ha_port = ha_port
    self.api_key = api_key
    self.root_url = f"http://{ha_host}:{ha_port}/api/services/input_number/set_value"

  def set_blind_state (self,location,state):
    location_key = locations.get(location)
    post_data = {
      'entity_id': location_key,
      'value': int(state)
    }
    headers = {'Authorization': f'Bearer {self.api_key}'}
    print(location_key)
    print(post_data)
    result = requests.post(self.root_url,json=post_data, headers=headers)
    print(result)
