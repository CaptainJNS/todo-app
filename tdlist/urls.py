from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from todo_list.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', index),
	path('register/', registration),
	path('login/', login),
	path('logout/', logout),
	path('add_list/', add_list),
	path('change_status/', change_status),
	path('delete_task/', delete_task),
	path('delete_list/', delete_list),
	path('add_task/', add_task),
	path('add_list/', add_list),
	path('edit_list/', edit_list),
	path('edit_task/', edit_task),
	path('prup/', prup),
	path('prdown/', prdown),
	path('task_date/', task_date),
	path('project_date/', project_date),
    path('admin/', admin.site.urls),
] + staticfiles_urlpatterns()

