from django import template

register = template.Library()


@register.filter
def get_class_name(value):
    return value.__name__


@register.filter
def getattr(obj, attr):
    return obj.__getattribute__(attr)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def camel_case_to_spaces(value):
    return ''.join(' ' + c if c.isupper() else c for c in value).strip()


