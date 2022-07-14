from django.urls import path
from . import views
urlpatterns = [
    path('view', views.list_blog, name="view"),
    path('create/', views.add_blog, name ="create"),
    #path('save/',views.save,name="save-blog"),
    path('update/<int:id>', views.update_blog, name='update'),
    path('delete/<int:id>', views.delete_blog, name='delete'),
]
