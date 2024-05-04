from django.urls import path

from books.views import books_list_view
from courses.views import login_view, courses_view

app_name = 'courses'

urlpatterns = [
    path('list/', courses_view, name='list'),
    path('', login_view, name='login'),

]