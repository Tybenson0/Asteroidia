import base64
import io
import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, \
    ConfusionMatrixDisplay

from .RegressionModel import regressionModel, model_performance

asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'
model = regressionModel()


# Create your views here.
def predictions(request):
    if request.method == 'POST':

        try:
            estimated_diameter_min = float(request.POST['estimated_diameter_min'])
            estimated_diameter_max = float(request.POST['estimated_diameter_max'])
            closest_approach_velocity = float(request.POST['closest_approach_velocity'])
            test_data_features = [
                [
                    estimated_diameter_min,
                    estimated_diameter_max,
                    closest_approach_velocity
                ]
            ]

            prediction = model.predict(test_data_features)
            # Return the prediction results to the template context
            return render(request, 'prediction.html', {'prediction': prediction})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'prediction.html')

plt.switch_backend('agg')
def model_testing(request):
    try:
        # Prepare evaluation results for display
        evaluation_results = model_performance()

        # Plot the confusion matrix
        fig, ax = plt.subplots()
        disp = ConfusionMatrixDisplay(confusion_matrix=evaluation_results['Confusion_Matrix'],
                                      display_labels=['Non-Hazardous', 'Hazardous'])
        disp.plot(cmap=plt.cm.Blues)

        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Encode the image to base64
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')

        # Update evaluation_results with the base64 encoded image
        evaluation_results['confusion_matrix_image'] = image_base64

        # Pass the image data to the template context
        context = {
            'confusion_matrix_image': image_base64,
        }

        return render(request, 'model_test.html', {
            'evaluation_results': evaluation_results,
            'confusion_matrix_image': image_base64
        })

    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': str(e)})
