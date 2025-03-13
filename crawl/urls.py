from django.urls import path
from crawl.views import index, fetch_jobs, privacy_policy

urlpatterns = [
    path("fetch-jobs/", fetch_jobs, name="fetch_jobs"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path('', index, name='index'),  # A basic example
    # Add more URL patterns here for other views
]