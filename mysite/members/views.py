

# “ The past is past, now, but that’s… you know,

#    that’s okay! It’s never really gone completely.

#       The future is always built on the past, even if we won’t get to see it. ” - Riebeck from Outer Wilds

# https://www.youtube.com/watch?v=K1R9NA-cseY


import base64
import io
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from .RegressionModel import regressionModel, model_performance

asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'  # NASA NEOWs API
model = regressionModel()  # Creating and training the logistic regression model

def predictions(request):  # view for the predictions page
    if request.method == 'POST':

        try:  # captures the inputs from the user to pass to the model for testing
            estimated_diameter_min = float(request.POST['estimated_diameter_min'])
            estimated_diameter_max = float(request.POST['estimated_diameter_max'])
            closest_approach_velocity = float(request.POST['closest_approach_velocity'])
            # validation to ensure the maximum is not below the minimum
            if estimated_diameter_max <= estimated_diameter_min:
                error_message = "Estimated Diameter Max must be greater than Estimated Diameter Min."
                return render(request, 'prediction.html', {'error': error_message})
            # 2D array of features to pass into the model
            test_data_features = [
                [
                    estimated_diameter_min,
                    estimated_diameter_max,
                    closest_approach_velocity
                ]
            ]
            # make the prediction
            prediction = model.predict(test_data_features)
            # return the prediction to the front end
            return render(request, 'prediction.html', {'prediction': prediction})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'prediction.html')


plt.switch_backend('agg')


def model_testing(request):  # view for the visuals and the testing the model
    try:
        # Prepare evaluation results for display
        evaluation_results = model_performance(model)  # passes in the model and tests it against test data

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

        # pass both to the front end
        return render(request, 'model_test.html', {
            'evaluation_results': evaluation_results,
            'confusion_matrix_image': image_base64
        })

    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': str(e)})


def main(request):  # main page
    return render(request, 'main.html')


def raw_data(request):  # requests data from the API and returns it as JSON
    response = requests.get(asteroids_neows)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON data from the response
        return JsonResponse(data)  # Return the data as a JSON response
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)
