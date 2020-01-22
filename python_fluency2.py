import re
def halved(lst):
  return [i / 2 for i in lst]
  
def only_postivie(lst):
  return [i for i in lst if i > 0]

def add_all(lst):
  return [sum = 0 i for i in lst sum += i]
  
def stripped_strings(lst):
  return [string for string in arr string = re.sub('\W')]
  
def find_special(lst):
  for i in range(len(lst)):
    if lst[i] == 'special':
      return i
    return -1
  #return [i for i in range(len(lst)) if i == 'special']
  
def valid_contacts(lstObj):
  new_lst = []
  for contact in lstObj:
    if contact.phoneNumber == 10:
      new_lst.append(contact)
  return new_lst
  
