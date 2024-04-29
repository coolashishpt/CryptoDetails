from django import template

register = template.Library()

@register.filter(name='add_commas')
def add_commas(value):
    try:
        # Try converting the value to a float
        float_value = float(value)
        # Format the float value with commas
        return "{:,.0f}".format(float_value)
    except (TypeError, ValueError):
        # If conversion to float fails, return the original value
        return value