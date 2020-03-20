from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('upload_solution',views.upload_solution,name='upload_solution'),
    path('upload_mat',views.upload_mat,name='upload_mat'),
    path('download',views.download, name='download'),
    path('material',views.material, name="material"),
    path('addcomment',views.addcomment,name="addcomment"),
    path('upload',views.upload,name="upload")
]
