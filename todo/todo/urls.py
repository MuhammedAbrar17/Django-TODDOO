
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('login/',views.Login),
    path('todopage/',views.todo),
    path('edit_todo/<int:srno>',views.edit_todo, name="edit_todo"),
]
