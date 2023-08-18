from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('',index,name="main-page"),
    path('top-sellers/',top_sellers,name="top_sellers"),
    path('advertisement-post/',top_sellers,name="advertisement-post"),
    path('login/',top_sellers,name="login"),
    path('profile/',top_sellers,name="profile"),
    path('register/',top_sellers,name="register"),
    # path('admin/', admin.site.urls)
]


