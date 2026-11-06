from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("districts/", views.districts, name="districts"),
    path("district/<slug:slug>/", views.district_detail, name="district"),
    path("assistant/", views.assistant, name="assistant"),
    path("report/", views.report, name="report"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("about/", views.about, name="about"),
    path("history/", views.history, name="history"),
    path("api/history/<slug:slug>/", views.api_history, name="api_history"),
    path("download/", views.download, name="download"),
    path("api/risk/", views.api_risk, name="api_risk"),
    path("api/district/<slug:slug>/", views.api_district, name="api_district"),
    path("api/advice/", views.api_advice, name="api_advice"),
    path("api/chat/", views.api_chat, name="api_chat"),
    path("api/health/", views.api_health, name="api_health"),
]
