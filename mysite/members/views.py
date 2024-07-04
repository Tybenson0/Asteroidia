from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests


# Create your views here.
def members(request):
    # AsteroidsNEOWs api
    asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'

    try:
        # parsing the NEO data
        data = requests.get(asteroids_neows) # request the NEO data
        data.raise_for_status()  # Raise an exception for HTTP errors
        near_earth_objects = data.json()  # Parse the JSON data
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

    # Pass the data to the template
    return JsonResponse(near_earth_objects)
