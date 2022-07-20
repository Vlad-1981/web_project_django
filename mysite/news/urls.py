from django.urls import path
from .views import *

urlpatterns = [
                # path('admin/', admin.site.urls),
                path('', HomeNews.as_view(), name='home'),                                           #   http://127.0.0.1:8000/
                # path('', index, name='home'),                                           #   http://127.0.0.1:8000/

                path('category/<int:category_id>/', NewsFromCategory.as_view(), name='category'),     #   http://127.0.0.1:8000/category
                # В параметрах "as_view()" можно передать "title"
                # path('category/<int:category_id>/', NewsFromCategory.as_view(extra_context={'title': 'Категории!!!'}), name='category'),     #   http://127.0.0.1:8000/category
                # path('category/<int:category_id>/', get_category, name='category'),     #   http://127.0.0.1:8000/category

                path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
                # path('news/<int:news_id>/', view_news, name='view_news'),

                path('news/add_news/', CreateNews.as_view(), name='add_news'),
                # path('news/add_news/', add_news, name='add_news'),

                path('test/', test, name='test'),

                path('news/login/', login, name='login'),

]