# takes request as an argument and returns a dictionary as context
from .models import Category

def menu(request):
    links = Category.objects.all()
    return dict(links=links)

