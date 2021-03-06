from . import views
from django.conf.urls import url, include



urlpatterns = [
    # 用户注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 判断用户名是否重复注册
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$',views.UsernameCountView.as_view()),
    # 判断用户名是否重复注册
    url(r'mobiles/(?P<mobile>1[3-9]\d{9})/count/$',views.MobileCountView.as_view()),
    # 用户登录
    url(r'^login/$',views.LoginView.as_view(),name='login'),
    #用户退出登录
    url(r'^logout/$',views.LogoutView.as_view(),name='logout'),
    #用户中心
    url(r'^info/$',views.UserInfoView.as_view(),name='info'),
#     添加邮箱
    url(r'^emails/$',views.EmailView.as_view()),
]