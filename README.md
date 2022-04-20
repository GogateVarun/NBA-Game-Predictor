
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

Our group is attempting to create an algorithm that can be used to preidct your sleep-partner patterns. By prompting for user inputs of gender, age, household income, education level, and geopgraphic location, the algorithm will determine how often someone will sleep alone in their next relationship.

## Members
- Varun Gogate - Repo, Vis, 
- Kit Williams - Machine Learning
- Sakile Trowers - SQL, Database
- Sharon Zeilstra - Machine Learning, Vis
- Zach Mehlenbacher - SQL, Python, Database, Vis

## Communication Plan

Members have agreed to utilize all methods available. This includes our group's Slack channel, our email addresses, Zoom, Google Meet, and class time. In order to stay updated on the status of each of our parts of the project, we message each other regularly through Slack and zoom meetings.

## Overview

Project Question: Can demographic information be used to predict sleep-partner patterns?

## Resources

Our dataset was discovered through [data.world](https://data.world/fivethirtyeight/sleeping-alone-data/workspace/file?filename=sleeping-alone-data.csv). In it's original state, the data contains 1,094 rows with 31 fields. Using the "Sleep-Alone-Data", we will reduce fields significantly from 31 to 8, keeping the demographic data in the final fields, as well as, the field regarding how often partners sleep in separate beds. Using the demographic data, we will develop a Machine Learning algorithm that can hopefully predict how often someone will sleep alone in their next relationship.

## Storyboard/Next Steps

Currently have located a dataset and generated a question to attempt to answer.
Next Steps include:
- Cleaning the dataset using Python and Pandas to filter out empty rows and unnecessary columns
- Exploring PostgreSQL database structure for housing data and tracking log of user inputs
- Beginning to develop Machine Learning algorithm
- Continue to build dashboard framework as analysis and model take shape

