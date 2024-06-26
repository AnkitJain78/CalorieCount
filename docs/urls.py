from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Calories API",
        default_version="v1",
        description="""
        The Calories API is a web service that provides functionality to manage and track calories consumed by users. 
        It allows users to retrieve information about their consumed calories, add new calorie entries, update existing 
        entries, and delete entries as needed.
      """,
        terms_of_service="https://github.com/AnkitJain78/CalorieCount"
        "/dev/LICENSE",
        contact=openapi.Contact(email="ankitjhanjhari0@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
