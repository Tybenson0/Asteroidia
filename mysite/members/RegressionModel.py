import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from matplotlib import pyplot as plt
import base64
import io


def regressionModel(): # function to create and train the logistic regression model
    asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'

    data = requests.get(asteroids_neows)  # request the NEO data
    data.raise_for_status()  # Raise an exception for HTTP errors
    near_earth_objects = data.json()  # Parse the JSON data
    features = []
    targets = []
    for neo in near_earth_objects['near_earth_objects']: # loops through each NEO and appends targets and features
        features.append([
            float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']),
            float(neo['estimated_diameter']['kilometers']['estimated_diameter_max']),
            float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
        ])


        # conditionally sets the target for hazardous asteroids
        if (float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                and float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 10
                or neo['is_potentially_hazardous_asteroid'] == True or (
                        float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                        and float(
                    neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 20)):
            targets.append('Hazardous')
        elif not neo['is_potentially_hazardous_asteroid']:
            targets.append('Non-Hazardous')

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.3, random_state=42)

    # Create and train the model with features and targets
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model

def model_performance(model): # for evaluating the model's performance and creating the confusion matric visual
    asteroids_neows = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kfoaNissh18rXuGll93dSPkfCfYoHxc1ibamSbci'

    data = requests.get(asteroids_neows)  # request the NEO data
    data.raise_for_status()  # Raise an exception for HTTP errors
    near_earth_objects = data.json()  # Parse the JSON data
    features = []
    targets = []
    for neo in near_earth_objects['near_earth_objects']: # same deal as above, appending features and targets
        features.append([
            float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']),
            float(neo['estimated_diameter']['kilometers']['estimated_diameter_max']),
            float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
        ])

        if (float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                and float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 10
                or neo['is_potentially_hazardous_asteroid'] == True or (
                        float(neo['estimated_diameter']['kilometers']['estimated_diameter_min']) > 2
                        and float(
                    neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) >= 20)):
            targets.append('Hazardous')
        elif not neo['is_potentially_hazardous_asteroid']:
            targets.append('Non-Hazardous')

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.3, random_state=42)


    # Make predictions on the test set
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    # report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    # Prepare evaluation results for display
    evaluation_results = {
        'Accuracy': f"{accuracy * 100:.2f}%",
        # 'Classification_Report': report,
        'Confusion_Matrix': matrix # Convert matrix to a nested list for JSON serialization
    }

    return evaluation_results
