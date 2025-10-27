

from django.urls import path
from.views import *

urlpatterns = [
    path("add-items/", create, name="add-items"),
    path("get_all/", get_all, name="get-all"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("delete/<int:id>/", delete, name="delete"),
    path("items/<int:id>/", get_data_by_id, name="get_data_by_id"),
    path("update/<int:id>/", update, name="update")
]