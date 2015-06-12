from actstream.models import Follow
from django.template import Library

register = Library()

def is_following(user, actor):
    """
    retorna True si el usuario esta siguiendo al actor

    ::

        {% if request.user|is_following:another_user %}
            You are already following {{ another_user }}
        {% endif %}
    """
    return Follow.objects.is_following(user, actor)

register.filter(is_following)