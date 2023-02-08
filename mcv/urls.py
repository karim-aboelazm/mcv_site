from django.urls import path
from . import views
from . import api

app_name = "mcv"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("dashboard/", views.DashBoardPageView.as_view(), name="dashboard"),
    # cars Api url
    path("api/car-list/", api.CarListApi.as_view(), name="api_car_list"),
    path("api/car-detail/<int:pk>", api.CarDetailApi.as_view(), name="api_car_detail"),
    path("api/car-filter/<str:kw>", api.CarFilterApi.as_view(), name="api_car_filter"),
    # cardiagnostic Api url
    path(
        "api/cardiagnostic-list/",
        api.CarDiagnosticListApi.as_view(),
        name="api_cardiagnostic_list",
    ),
    path(
        "api/cardiagnostic-detail/<int:pk>",
        api.CarDiagnosticDetailApi.as_view(),
        name="api_cardiagnostic_detail",
    ),
    path(
        "api/cardiagnostic-filter/<str:kw>",
        api.CarDiagnosticFilterApi.as_view(),
        name="api_cardiagnostic_filter",
    ),
    # drivers Api url
    path("api/driver-list/", api.DriverListApi.as_view(), name="api_Drivers_list"),
    path(
        "api/driver-detail/<int:pk>",
        api.DriverDetailApi.as_view(),
        name="api_Drivers_list",
    ),
    path(
        "api/driver-filter/<str:kw>",
        api.DriverFilterApi.as_view(),
        name="api_Drivers_filter",
    ),
]
