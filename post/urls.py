from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("category/<slug:slug>/<int:pk>/", views.CategoryListView.as_view(), name="category_list"),
    path("article/<slug:slug>/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"), # post detail
    path('search/', views.SearchView.as_view(), name="search"), # Search
    path('comment/<slug:slug>/<int:pk>/', views.comment_add, name="comment"), # comment
    path('aboutus/', views.aboutus, name="aboutus"), # comment


    # path("article/add_post", views.post_add, name="add_post"),
    # path("article/edit/<int:id>", views.post_update, name="update_post"),
    # path('article/delete/<int:id>',views.post_delete, name='delete_post'),
    # # Category
    # path("category/all_categories", views.all_category, name="all_categories"),    
    # path("category/add_category", views.add_category, name="add_category"),    
    # path("category/list/<slug:slug>", views.category_post_list, name="category_post_list"),
    # # Like
    # path('article/like/<int:id>', views.post_like, name='like_post'),
    # # Comment
    # path('article/comment/<int:id>', views.post_comment, name='post_comment'),
    # path('article/comment/answer/<int:id>/<int:post_id>', views.comment_answer, name='comment_answer' )

]
