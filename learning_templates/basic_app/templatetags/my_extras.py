from django import template

register = template.Library()

@register.filter(name='my_cut')
def cut(value, arg):
    """
        This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')


# register.filter('my_cut', cut)