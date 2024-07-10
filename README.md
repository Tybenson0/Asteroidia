<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">ASTEROIDIA</h3>
    <img src="mysite/members/static/asteroid-2-svgrepo-com.svg" alt="Asteroid Image" width="75" height="75">

  <p align="center">
    Use machine learning to predict if an asteroid is hazardous or not!
    <br />
    <br />
    <br />
    <a href="https://github.com/Tybenson0/Asteroidia/issues">Report Bug</a>
    ·
    <a href="https://github.com/Tybenson0/Asteroidia/pulls">Request Feature</a>
  </p>
</div>





<br />
<br />



<!-- ABOUT THE PROJECT -->
## About ASTEROIDIA
<div align="center">

</div>
<p> ASTEROIDIA is an application that predicts if an asteroid is hazardous by utilizing machine learning along the NASA NEOWs API for training! </p>
<br />
<br />
<br />


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br />
<br />



### Built With
<br />
ASTEROIDIA is a Django application...
<br />
<br />

<div align="center">
<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" alt="Python">
   
<img src="https://img.shields.io/badge/TensorFlow-2.0%2B-orange?style=for-the-badge" alt="TensorFlow">
   
<img src="https://img.shields.io/badge/NumPy-1.18%2B-green?style=for-the-badge" alt="NumPy">
   
<img src="https://img.shields.io/badge/pandas-1.0%2B-yellow?style=for-the-badge" alt="pandas">
   
<img src="https://img.shields.io/badge/scikit--learn-0.22%2B-brightgreen?style=for-the-badge" alt="scikit-learn">
   
<img src="https://img.shields.io/badge/Keras-2.3%2B-red?style=for-the-badge" alt="Keras">
   
<img src="https://img.shields.io/badge/Matplotlib-3.2%2B-blueviolet?style=for-the-badge" alt="Matplotlib">
</div>
<br />
<br />
<br />
<br />


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Test out the code for yourself and leave any recomendations!

### Prerequisites


[![Node.js](https://img.shields.io/badge/Python-%3E%3D%203.8-brightgreen)](https://nodejs.org/)



<!-- USAGE EXAMPLES -->
## Usage
  1*.  open your IDE/code editor and open the terminal to location you wish to clone the project
  <br />
  <br />
  2*. Clone Repository to location of your choice
  ```sh
  git clone https://github.com/Tybenson0/Asteroidia.git
  ```
  3*.  Move into the directory Asteroidia/mysite
  ```sh
  cd Asteroidia/mysite
  ```
  4*.  Install Dependencies
  ```sh
   pip install -r requirements.txt
  ```
  5*.  Run the App
  ```sh
  python manage.py runserver
  ```
  6*. Paste in your browser: http://127.0.0.1:8000/
  <br />
  <br />
  7*. <p>You should now be on the main page. From the main page you can go to the predictions page which has fields for you to fill out to predict if an asteroid is hazardous or not. You may also go to the model testing &
     accuracy page which displays the visuals for the model and data along with the calculated accuracy metric. Lastly there is a link to the raw data allowing you to view the raw jason data from the NASA NEOWs yourself.
  </p>

<br />
<br />
optional*.  You can uninstall the dependencies after you're done using the project
  ```sh
  pip uninstall -r requirements.txt
  ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br />
<br />

## Machine Learning
Asteroidia utilizes the NASA Near Earth Objects Web Service and a supervised linear regression machine learning model to predict if an asteroid is hazardous based on features such as size and velocity. Asteroidia employs the scikit-learn linear regression library and other libraries to split the NEOWs data into training and testing groups. The training set provides features that the model uses for training and predicting, while targets are dynamically assigned values that serve as goals for the model's predictions and performance evaluation. The model trains on the training set and evaluates itself using the test set, providing an accuracy metric based on its correct hazard predictions against the test data. This training/testing approach ensures a reliable accuracy metric by using similar datasets for both training and testing.
<br />
<br />
## Validation  
The model is trained and tested on distinct, non-overlapping subsets of data from the NASA NEOWs. The test data maintains the exact split between features and targets as in the training data, ensuring similarity between datasets. The model is then evaluated against the test data to measure its accuracy in correctly predicting hazards, thus validating its performance.
<br />
<br />
## Solution Summary
In recent years, technological advancements have significantly progressed, giving rise to television, computers, and the internet, which necessitate near-orbit satellites to support these services. However, asteroids and other Near Earth Objects pose a significant threat to Earth and its space assets due to potential collisions that could disrupt global communications. ASTEROIDIA aims to address this challenge by leveraging the NASA NEOWs database to predict the potential hazard of NEOs using machine learning algorithms. These algorithms analyze traits such as size and velocity to determine if an NEO poses a hazard.
<br />
<br />
## Data Summary
ASTEROIDIA retrieves data from the NASA Near Earth Object Web Service (NASA NEOWs), which contains detailed information on identified NEOs and their associated characteristics. The data undergoes preprocessing to extract relevant details essential for the model. Selected traits from this dataset serve as features for predictions, while dynamically assigned targets enable the model to predict hazards accurately.
<br />
<br />
## Visualizations
The chosen visualizations include a histogram, scatter plot, and confusion matrix. The histogram illustrates the distribution of minimum and maximum diameters among NEOs in the dataset, highlighting their variability. The scatter plot displays correlations between the minimum and maximum diameters of NEOs and their velocities, aiming to uncover potential patterns. Lastly, the confusion matrix provides a clear depiction of the model's accuracy when tested against the validation data, offering insights into its performance.



