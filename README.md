# Lab_4_Assignment - Fish Classification Model

This project is part of a Lab assignment for Durham College.

## Project Intro/Objective
The aim of this project is to deploy an application via Heroku. The application consists of a machine learning model able to classify 
within 7 possible categories of fish, the values entered by the user.

The model has been coded in a Jupyter Notebook using a Random Forest Classifier algorithm and the dataset has been retrieved from [Kaggle](https://www.kaggle.com/aungpyaeap/fish-market).

Using Flask, HTML and CSS styles, we were able to provide a UI and an API for users to be able to make a classification based on 6 input
numeric values: Weight, 3 length measures, height and width. Once provided, the user will receive the fish species that was classified in the 
appropriate category.

## Prerequisites
Before installing the project, the user needs to ensure a proper Internet connection is provided. The user will also need some programming tools:
+ [Python](https://www.python.org/downloads/)
+ IDE or Notebook - Jupyter Notebook, Google Colab, Pycharm, VS
+ Git Bash

## Install Project
To install the project, please download or clone properly using [repository url](https://github.com/AlanLozV/Lab_4_Assignment.git).
All necessary tools and libraries are already provided within installation.
To clone the repository using Git Bash follow below steps:
1. Open GitHub and go to the GitHub repository that you want to clone.
2. Click “Code” and copy the given URL.
3. Open Git Bash and change to the location where you want the cloned directory.
4. Type 'git clone' in the terminal and paste the URL you copied, press “Enter” to create your local clone.

## Deployment
For project deployment on web [Heroku](https://dashboard.heroku.com/apps) was used. Using the existing configuration for Github repositories 
and building it, we were able to launch the app and it is visible in http://fish-predict-model.herokuapp.com/.

## Author
Oscar Alan Lozada Villa

