
# Team-3-Project

## Members
- Varun Gogate - Repo, Vis, 
- Kit Williams - Machine Learning
- Sakile Trowers - SQL, Database
- Zach Mehlenbacher - SQL, Database, Vis


## Project Overview

Project Question: Can Vegas odds and historical scores amongst all NBA teams be used to detemine the accuracy of sports betting webistes, such as their money line or game score spreads?

## Resources

Our dataset was discovered through Kaggle, https://www.kaggle.com/datasets/erichqiu/nba-odds-and-scores.

The data has been cleaned and prepped for database analysis and machine learning.

## Project plan

- The dataset was cleaned using Python and Pandas to filter out empty rows and unnecessary columns
- Utilizing Mongodb Atlas database for housing data and tracking log of user inputs
- Machine Learning model developed for Money Line, Spread and Over/Under book lines
- The data connections were built using Javascript app routes
- Dashboard framework built using Bootstrap and Plotly where our visualizations will deploy for model output


Description of preliminary preprocessing:
General data cleaning was needed to reduce the complexity and dimensions of the data set. Redundant/Unneeded columns were deleted and we ensured every column was the correct data type. Since we planned on using a binary classifier, 3 target columns were calculated (one for each prediction) where the value was either a 1 for correct or 0 for incorrect. These columns for the target variables were added to the end of our dataframe. 
Once the data was cleaned we then went through a process of feature selection to determine which variables contributed to an accurate prediction of our target variable. 

With the features selected, some final preprocessing occurred before fitting our model. Categorical variables were converted to numeric and all the columns were scaled using the Standard Scaler. 
Description of preliminary feature engineering and preliminary feature selection, including their decision-making process.

The features for the model were selected by determining correlation metrics for all of the columns. A plot of 2 features were plotted against each other and colored by whether the outcome was 1 or 0. This was done for every combination of columns for the 3 different models. Graphs that showed a clear correlation were selected to train the model. 

Description of how data was split into training and testing sets:
The dataset contains 2452 rows. The data was split into training and testing sets using the SciKit learn train_test_split method.

Explanation of model choice, including limitations and benefits:
A neural network was selected to predict our target variables. We made 3 different neural networks, one for each target variable. Based on the feature selection process, the best correlated columns were used as inputs to the models (which varied)from 7 - 10 inputs). The benefits of using the neural network is that it is very customizable to try and optimize performance. Our topic is inherently difficult to predict so any prediction above 50% is better than guessing. We currently have an accuracy that ranges from 63% - 72% and we are looking to improve this number. Another benefit is that our data is scalable, we can include additional years of data as well as merge team data to the data frame. These options will be explored to try and increase the model’s accuracy. A limitation to the model is that optimizing the performance will require a lot of trial and error working with the number of hidden layers and neurons. In addition, there could be a possibility of overfitting the data so this must be considered when trying to improve the model.


## Database

Key points and Features:
•	Database connection to ML model --> PyMongo will be utilized to connect our DB to our Python ML Model.
•	User Input and DB connectivity --> An input table was created to store selections and connected through an app.py file.
•	Advantages of using MongoD: Ease of connectivity through PyMongo and set up | Data accessibility through web-based Atlas application

## Presentation

Google Slides and general outline for Presentation can be found here:

https://docs.google.com/presentation/d/1pg1xgsjBsOmQrMdxlT2wFP6VxVbv49QSj2FkXTKnR-k/edit?usp=sharing



