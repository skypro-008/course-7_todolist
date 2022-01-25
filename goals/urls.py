from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from goals import views

urlpatterns = [
    path("goal_category.list", views.GoalCategoryListView.as_view()),
    path("goal_category.create", views.GoalCategoryCreateView.as_view()),
    path("goal.list", views.GoalListView.as_view()),
]
