from django.urls import path
from ss_blog.views import home_view,edit_my_model,add_article,contentpage_view,post_comment,loging,delete_post

app_name='ss_blog'

urlpatterns = [
    path('',home_view,name='home'),
    path('home',home_view),
    path('add',add_article,name='add-article'),
    path('<int:Topics_id>/comment',post_comment,name='post_comment'),
    path('log_reg',loging,name='log_reg_template'),

    path('article/<int:Topics_id>',contentpage_view,name='contentpage_view'),
    path('article/<int:Article_id>/edit',edit_my_model,name='edit'),
    path('article/<int:Article_id>/delete/', delete_post, name='delete_post'),
]
