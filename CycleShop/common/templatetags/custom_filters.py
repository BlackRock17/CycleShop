from django import template

register = template.Library()


@register.filter
def get_class_name(value):
    return value.__name__


@register.filter
def getattr(obj, attr):
    return obj.__getattribute__(attr)

