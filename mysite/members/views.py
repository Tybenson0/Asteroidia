import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, mean_squared_error, r2_score

asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'


# Create your views here.
def predictions(request):
    if request.method == 'POST':

        try:

            absolute_magnitude = float(request.POST['absolute_magnitude'])
            estimated_diameter_min = float(request.POST['estimated_diameter_min'])
            estimated_diameter_max = float(request.POST['estimated_diameter_max'])
            closest_approach_velocity = float(request.POST['closest_approach_velocity'])
            test_data_features = [
                [
                    absolute_magnitude,
                    estimated_diameter_min,
                    estimated_diameter_max,
                    closest_approach_velocity
                ]
            ]

            data = requests.get(asteroids_neows)  # request the NEO data
            data.raise_for_status()  # Raise an exception for HTTP errors
            near_earth_objects = data.json()  # Parse the JSON data
            features = []
            targets = []
            for neo in near_earth_objects['near_earth_objects']:
                features.append([
                    float(neo['absolute_magnitude_h']),
                    float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']),
                    float(neo['estimated_diameter']['kilometers']['estimated_diameter_max']),
                    float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
                ])

                # Define your own hazard metric based on asteroid size (estimated diameter)
                # For example, let's classify asteroids with estimated diameter > 0.5 km as hazardous
                if (float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                        and float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 10
                            or neo['is_potentially_hazardous_asteroid'] == True or (float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                                and float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 20)):
                    targets.append('Hazardous')
                elif not neo['is_potentially_hazardous_asteroid']:
                    targets.append('Non-Hazardous')

            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.4, random_state=42)

            # Initialize linear regression model
            model = LogisticRegression()
            model.fit(X_train, y_train)

            prediction = model.predict(test_data_features)
            # Return the prediction results to the template context
            return render(request, 'prediction.html', {'prediction': prediction})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'prediction.html')


def model_testing(request):
    asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'

    try:
        data = requests.get(asteroids_neows)  # request the NEO data
        data.raise_for_status()  # Raise an exception for HTTP errors
        near_earth_objects = data.json()  # Parse the JSON data
        features = []
        targets = []
        for neo in near_earth_objects['near_earth_objects']:
            features.append([
                float(neo['absolute_magnitude_h']),
                float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']),
                float(neo['estimated_diameter']['kilometers']['estimated_diameter_max']),
                float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
            ])

            # Define your own hazard metric based on asteroid size (estimated diameter)
            # For example, let's classify asteroids with estimated diameter > 0.5 km as hazardous
            if (float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                    and float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 18
                    or neo['is_potentially_hazardous_asteroid'] == True or (
                            float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                            and float(
                        neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 18)):
                targets.append('Hazardous')
            elif not neo['is_potentially_hazardous_asteroid']:
                targets.append('Non-Hazardous')

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.4, random_state=42)

        # Initialize linear regression model
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        # Prepare evaluation results for display
        evaluation_results = {
            'Accuracy': accuracy,
            'Classification_Report': report,
            'Confusion_Matrix': matrix.tolist()  # Convert matrix to a nested list for JSON serialization
        }

        print(X_train)
        return render(request, 'model_test.html', {'evaluation_results': evaluation_results})

    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': str(e)})
