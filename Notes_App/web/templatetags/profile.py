from django import template
from Notes_App.web.models import Profile

register = template.Library()


@register.simple_tag
def has_profile():
    return Profile.objects.first()
