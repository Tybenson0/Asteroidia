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
*1.  open your IDE/code editor and open the terminal to location you wish to clone the project
  <br />
  *2. Clone Repository to location of your choice
  ```sh
  git clone https://github.com/Tybenson0/Asteroidia.git
  ```
  *3.  Move into the directory/folder Asteroidia/mysite
  ```sh
  cd asteroida/mysite
  ```
  *4.  Install Dependencies
  ```sh
  pip install django numpy pandas scikit-learn tensorflow keras matplotlib
  ```
  *5.  Run the App
  ```sh
  python manage.py runserver
  ```
  *6. Paste in your browser: http://127.0.0.1:8000/



<br />
<br />



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br />
<br />

## Machine Learning
Asteroidia uses the Nasa Near Earth Objects Web Service and a supervised linear regression machine learning model in order to predict if an azteroid is hazardous based on features such as size and velocity.
Asteroidia uses the scikit linear regression library along with various other libararies to split the NEOWs data into two different groups, testing and training. The groups receive sets of features and targets that 
model will use to train test. The features are the components that the model uses to train and make predictions off of. Targets are dynamically assigned values that the model is using as the goal for its predictions
and performance. The model then trains with the training set and tests itself with the test set and provides an accuracy metric based on the model correct hazard predictions based on the test data. This method of 
training/testing allows us to train the model and test the model with similar data allowing for a reliable accuracy metric.
<br />
<br />
## Validation  
The model is trained and testes on the same data from the NASA NEOWs, but without duplication. The test data uses the exact same split between features and targets ensuring the datasets are very similar. The model 
is then tested agains the test data and we define the accuracy metric as the amount of correct hazard predictions from the model on the test data; ensuring the model is working as intended. 
<br />
<br />
## Solution Summary
Humanity in recent years has advanced rapidly with technology, enabling the birth of television, computers, and interent. This also led to the need for near orbit satellites in order to have these services. Asteroids and other
Near Earth Objects pose a great threat to Earth and her many space assets as colisions could disrupt communications across the world. ASTEROIDIA aims to remedy this by using a pre-existing database (NASA NEOWs) in order 
to predict the potential severity of NEOs using machine learning algorithms to determine if an NEO is hazardous or not by certain traits they exhibit like size or velocity.
<br />
<br />
## Data Summary
ASTEROIDIA is pulling from the NASA Near Earth Object Web Service(NASA NEOWs). The data consists of multiple already identifies NEO's and various traits associated with them. The data was pre-processed in order to extract
details that will be useful for the model. The model uses some of theses traits as features for predictions, along with dynamically assigned targets for the model to attempt to predict.
<br />
<br />
## Visualizations
The visualizations I chose to go with are a histogram, scatterplot, and confusion matric. The histogram is used to demonstrate the variance among the minimum and maximum diameters of NEO's provided in the dataset. The
Scatterplot is used to show correlation between the minimum and maximum diameters of the NEO's along with their velocity in order to potentially extract patterns. The confusion matrix is used to show the accuacy of the model
when it is run against the test data to describe the accuaracy of the model.



