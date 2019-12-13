from django.conf.urls import url

from . import views


app_name = 'applications'

urlpatterns = [
    # urls for school requests - user side
    url(r"^$", views.requests_list, name="requests"),
    url(r"new", views.new_request, name="createRequest"),
    url(r"edit/(?P<id>[0-9]+)/", views.edit_request, name="edit"),


    # url(r"addedRequest", views.add_new_request, name="addRequest"),
    # url(r"school/new/success/$", views.ListSchoolRequests.as_view(), name="all"),
    # # urls for restaurant requests - user side
    # url(r"restaurant/$", views.ListRestaurantRequests.as_view(), name="all-restaurant"),
    # url(r"restaurant/new/$", views.CreateRestaurantApplication.as_view(), name="create-restaurant"),
    # url(r"restaurant/new/success/$", views.ListRestaurantRequests.as_view(), name="all-restaurant"),
]
