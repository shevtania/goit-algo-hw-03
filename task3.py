import re

def normalize_phone(phone_number):
# change all no digit symbols, excluding '+', to '' and remove extra spaces
    new_number = re.sub(r'[^+|\d]+', '', phone_number.strip())
# replace numbers, that start with '0', '380', '+380' to '+380'    
    searching = re.sub(r'(\A380)|(\A0)|(\A\+380)', '+380', new_number)

    return searching
  
 
