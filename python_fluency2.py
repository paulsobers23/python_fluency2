import re
def halved(lst):
  return [i / 2 for i in lst]
  
def only_postivie(lst):
  return [i for i in lst if i > 0]

def add_all(lst):
  return sum(lst)
  
def stripped_strings(lst):
  return [re.sub('\W','',string) for string in lst]
  
def find_special(lst):
  for i in range(len(lst)):
    if lst[i] == 'special':
      return i
    return -1
  
def valid_contacts(lstObj):
  return [contact for contact in lstObj if len(contact['phoneNumber']) ==10\\\\\ ]
  
def names(lst):
  return [contact['name'] for contact in lst]