from typing import Dict

import requests
test_url = "https://reqres.in/api/users/2"
response = requests.get(test_url)
product_data = response.json()

def get_additional_data(style_number, sku_id):
    additional_data_temp = {'style_number': style_number, 'sku_id': sku_id, 'support': "test_support_data"}
    return additional_data_temp

additional_data: Dict = get_additional_data("CWS10", 10)

def pre_process_data():
   filteradditipnal_data ={a:v for a,v in additional_data.items()
                           if a != 'support'}
   product_data.update(filteradditipnal_data)
   return product_data
print(pre_process_data())

