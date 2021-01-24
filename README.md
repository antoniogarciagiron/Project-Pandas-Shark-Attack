![Portada](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/tiburon.jpg)

# **Shark Attacks**

## 01. Introduction

- The target of the current project was to take a dataset, clean it and analyse the data. This is one of the projects done during the [IronHack](https://www.ironhack.com/es) Data Analytics bootcamp.
- The selected dataset was created by Toby Jolly and can be downloaded from [Kaggle](https://www.kaggle.com/teajay/global-shark-attacks). In this case the original dataset was a csv file with shark attacks information.
- The following Python libraries were used to sort the data and perform the analysis: Pandas, Re (Regex), Numpy and Seaborn.

## 02. Hypothesis

- My first hypothesis was that shark attacks depend on the time during the year, as most sharks are migratory animals. In particular, I wanted to know if shark attacks are produced during the warm months.
- My second task was to take as much usefull information as I can from the dataset.

## 03. Cleaning data

- The raw dataset had 25.000 rows and 24 columns, however, most rows didn't contain any information, and some columns were either empty or containing useless information.
- Some columns contain usefull information but the data was not well registered. I used Redex to find the usefull data and clean the rest.
- Also some column names were not correctly written, I changed the names to avoid confusion.
- The columns with repeated data were removed.
- After cleaning the null information and empty columns, the final dataset dimension was 6.293 x 13.

## 04. Results

After sorting the dataset, the most straightforward information to study was the relation between the age of the shark victims and the attacks, as shown as follows:

[Fig1](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/01_victims.jpg)

In this figure it can be observed that most shark victims are males younger than 20 years. This is probably related with people practising water sports.
To confirm this hypothesis, the activities performed by the victims during the shark attacks were studied and plotted in the next graphic:

[Fig2](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/02_Activities.jpg)

As espected, the two major activities were surfing and swimming, and among the 10 most recurrent activities only fishing is not related with a extreme sport.

## 05. Conclusions