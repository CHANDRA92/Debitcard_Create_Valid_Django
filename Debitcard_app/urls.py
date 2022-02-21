from django.urls import path,include
from .views import *

urlpatterns = [
    path('', check, name="check"),
    path('Generate/', Generate, name="Generate")
    # path('check/', check, name="check"),
]