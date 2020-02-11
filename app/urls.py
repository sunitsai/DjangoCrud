from django.urls import path,include
from . import views
urlpatterns = [
    
    path("",views.IndexPage,name="insert"),
    path("show/",views.ShowPage,name="show"),
    path("insert/",views.insertData,name="insert"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("update/<int:pk>",views.updateUser,name="update"),
    path("delete/<int:pk>",views.DeleteUser,name="delete"),
]
