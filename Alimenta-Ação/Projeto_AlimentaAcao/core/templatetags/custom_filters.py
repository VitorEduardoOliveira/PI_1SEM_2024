from django import template

register = template.Library()

@register.filter
def getId(dicionario, key):
  return dicionario.get(key)