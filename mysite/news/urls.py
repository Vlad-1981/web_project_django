from django.urls import path
from .views import *

urlpatterns = [
                # path('admin/', admin.site.urls),
                path('', index),                        #   http://127.0.0.1:8000/
                path('test/', test),                    #   http://127.0.0.1:8000/news/test
                                                        #   http://127.0.0.1:8000/test
                                                        #   http://127.0.0.1:8000/news
                                                        #   чтобы связать маршрутизатор ("urls") с представлением ("view")

]