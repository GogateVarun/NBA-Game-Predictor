
# Team-3-Project

## Members
- Varun Gogate - Repo, Vis, 
- Kit Williams - Machine Learning
- Sakile Trowers - SQL, Database
- Sharon Zeilstra - Machine Learning, Vis
- Zach Mehlenbacher - SQL, Database, Vis

## Overview

Currently researching data sources and available data to narrow down project topic. Will return by Thursday with suggestions for the group and final decisions.

Update from 4/19/22 class (Kit's comments in Slack):

With the advice of Felipe, the dataset we were working with was going to be more trouble than what it is worth. The demographic information would not be a good predictor due to limited to no correlation with what we were trying to predict. The rest of the questions/columns could maybe be used but it would require a lot of cleaning and even after that the data is very unbalanced. This would lead to other problems down the road when trying to make a good model. Anyways, we have been spending most of class trying to find another dataset. We haven't been able to find another good sleep one so since we are back at square one we were thinking it may be a good idea to try and pivot to a different topic. We were thinking we would meet tomorrow at some point so we can decide on a new dataset that way we can have all of class Thursday to catch back up.

To summarize (Sharon's interpretation):  the data has too much disimilarity between the sleep alone/sleep together groups (est to be 20%/80%) for meaningful analysis beyond supervised learning cluster analysis, that the demographics correlation was doubtful without initial analysis, and that the predictability of the sleep apart reason variables would be with extremely messy data and small sample sizes.

Before 4/21 class, we need to find a different database to work with and make some decisions about our project plan.

# Team-3-Project

Update for 4/21: A new NBA Odds dataset has been selected and we are reviewing if this dataset will be adequate for the focus of our analysis.  
Dataset has been downloaded in multiple formats and cleaned thus far.  The focus for this analysis will be to use inputs to detemine the accuracy of NBA sportsbetting odds and scores. 

## Members
- Varun Gogate - Repo, Vis, 
- Kit Williams - Machine Learning
- Sakile Trowers - SQL, Database
- Sharon Zeilstra - Machine Learning, Vis
- Zach Mehlenbacher - SQL, Python, Database, Vis

## Communication Plan

Members have agreed to utilize all methods available. This includes our group's Slack channel, our email addresses, Zoom, Google Meet, and class time. In order to stay updated on the status of each of our parts of the project, we message each other regularly through Slack and zoom meetings.

## Overview

Project Question: Can Vegas odds and historical scores amongst all NBA teams be used to detemine the accuracy of sports betting webistes, such as their money line or game score spreads?

## Resources

Our dataset was discovered through Kaggle, https://www.kaggle.com/datasets/erichqiu/nba-odds-and-scores.

The data has been cleaned and prepped for database analysis and machine learning.

## Storyboard/Next Steps

Currently have located a dataset and generated a question to attempt to answer.
Next Steps include:
- Cleaning the dataset using Python and Pandas to filter out empty rows and unnecessary columns
- Exploring PostgreSQL database structure for housing data and tracking log of user inputs
- Beginning to develop Machine Learning algorithm
- Continue to build dashboard framework as analysis and model take shape

# Final Project - Segment 2 

## Part 1 GitHub
•	All deliverable requirements for this section have been met in the current README from the previous submission

## Part 2 - Machine Learning
Our goal is to predict 3 metrics from sports betting:
•	MoneyLine
•	Spread
•	Over/Under

There are 3 different models being used to predict each of the metrics outlined above.

Description of Preliminary Preprocessing

General data cleaning was needed to reduce the complexity and dimensions of the data set. Unnecessary columns were removed, and it was ensured that every column was the correct data type. As we planned on using a binary classifier, one target column for each prediction was calculated, resulting in a total of three columns. The value was either 1 (indicating correct) or 0 (indicating incorrect). These columns for the target variables were added to the end of our DataFrame. 

Once the data was cleaned, we completed a process of feature selection. This method was used to determine which variables contributed to an accurate prediction of our target variable. With the features selected, some final preprocessing occurred before fitting our model. Categorical variables were then converted to numeric. 

## Part 3 - Database

Key points and Features:
•	Database connection to ML model --> PyMongo will be utilized to connect our DB to our Python ML Model.
•	User Input and DB connectivity --> An input table was created to store selections and connected through an app.py file.
•	Advantages of using MongoD: Ease of connectivity through PyMongo and set up | Data accessibility through web-based Atlas application

## Part 4 - Presentation

Google Slides and general outline for Presentation can be found here:

https://docs.google.com/presentation/d/1pg1xgsjBsOmQrMdxlT2wFP6VxVbv49QSj2FkXTKnR-k/edit?usp=sharing

## Part 5 - Dashboard

Blueprint:
•	Storyboard on Google Slide(s)
o	Please see the “Dashboard section of the Google Slides presentation outline.
•	Description of the tool(s) that will be used to create final dashboard (ReadMe)
o	Using Plotly to create gauges
o	Using index.html with associated javascript and static resources
o	Using app.py to create function interactivity for user inputs
•	Description of interactive elements
o	User inputs (7), text boxes
o	Resources/Links
o	Contact information links
o	Help button
o	Page refresh button

