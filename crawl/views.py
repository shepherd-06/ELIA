import random
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from decouple import config

RAPIDAPI_KEY = config.get("RAPIDAPI_KEY", "")
RAPIDAPI_HOST = "jobs-api14.p.rapidapi.com"
BASE_URL = f"https://{RAPIDAPI_HOST}/v2/list"

def index(request):
    return HttpResponse("Hello, this is the crawl app index page.")

def fetch_jobs(request):
    # Get query parameters from Django request
    keyword = request.GET.get("keyword", "Web Developer")
    location = request.GET.get("location", "United States")
    remote_only = request.GET.get("remoteOnly", "false")  # Default: false
    employment_types = request.GET.get("employmentTypes", "fulltime;parttime;intern;contractor")  # Default values


    # Construct query parameters
    params = {
        "query": keyword,
        "location": location,
        "autoTranslateLocation": "true",
        "remoteOnly": remote_only,
        "employmentTypes": "fulltime;parttime;intern;contractor"
    }

    # Set request headers
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    try:
        # Make the API request
        response = requests.get(BASE_URL, headers=headers, params=params)

        # Handle response
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({"error": "Failed to fetch jobs", "status_code": response.status_code}, status=500)

    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

def privacy_policy(request):
    """hastily made privacy policy for chatgpt

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "privacy_policy.html")