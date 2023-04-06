from django.urls import path
from wxcloudrun.views import PetListCreateView
from wxcloudrun.views import UserLoginView

urlpatterns = [
    path('api/', PetListCreateView.as_view(), name='pet_list_create'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    # 其他 URL 路由
    url(r'(/)?$', views.index)
]
