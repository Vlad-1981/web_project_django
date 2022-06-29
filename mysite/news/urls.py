from django.urls import path
from .views import *

urlpatterns = [
                # path('admin/', admin.site.urls),
                path('', index, name='home'),                                           #   http://127.0.0.1:8000/
                path('category/<int:category_id>/', get_category, name='category'),     #   http://127.0.0.1:8000/category
                path('news/<int:news_id>/', view_news, name='view_news'),
                path('news/add_news/', add_news, name='add_news'),
                path('news/login/', login, name='login'),

]