import datetime

from django import template

register = template.Library()

#classes

#filters

#tags

def copyright_tag(year):
  try:
    now = datetime.datetime.now().year
    if year != str(now):
      return "Copyright " + year + " - " + str(now)
    else:
      return "Copyright " + year
  except UnicodeEncodeError:
    return ''

register.simple_tag(copyright_tag)

#inclusion tags

