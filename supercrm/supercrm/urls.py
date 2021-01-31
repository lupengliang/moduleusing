"""supercrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sales import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),    # 登录
    url(r'^register/', views.register, name='register'),    # 注册
    url(r'^home/', views.home, name='home'),    # 首页
    # 所有客户信息展示
    url(r'^customers', views.CutomerView.as_view(), name='customers'),
    # 我的客户
    url(r'^mycustomers', views.CutomerView.as_view(), name='mycustomers'),
    # 添加页面
    # url(r'^add_customer', views.add_customer, name='add_customer'),
    url(r'^add_customer', views.add_edit_customer, name='add_customer'),
    # 编辑客户
    # url(r'^edit_customer/(\d+)/', views.edit_customer, name='edit_customer'),
    url(r'^edit_customer/(\d+)/', views.add_edit_customer, name='edit_customer'),
]
