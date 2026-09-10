# 🌸 Iris Flower Prediction

A Machine Learning web application that predicts the species of an Iris flower based on its sepal and petal measurements.
The project uses a **Logistic Regression** model with **Min-Max Scaling** and **Label Encoding**, and provides predictions through a **Flask-based web application** with a simple HTML and CSS interface.

## 🌐 Live Demo

🚀 **[Open the Iris Flower Prediction Website](https://iris-flask-prediction-div.onrender.com/)**

## 📂 GitHub Repository

🔗 **[View Source Code on GitHub](https://github.com/Divya-kumari18/iris-flask-prediction)**

---

## 📌 Project Overview

The Iris Flower Classification problem is a classic Machine Learning classification task.

The application takes four measurements of an Iris flower as input:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Using these measurements, the trained Machine Learning model predicts the flower species.

The possible predictions are:

- 🌱 **Setosa**
- 🌿 **Versicolor**
- 🌸 **Virginica**

The trained model and preprocessing objects are saved using **Joblib** and loaded into the Flask application for making predictions.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand the Iris classification problem.
- Prepare and preprocess the dataset.
- Encode the target variable using Label Encoding.
- Scale numerical features using Min-Max Scaling.
- Train a Logistic Regression classification model.
- Save the trained Machine Learning components using Joblib.
- Build a Flask web application for prediction.
- Create a simple and user-friendly frontend using HTML and CSS.
- Deploy the application online using Render.

---

## 📊 Dataset

The project uses the **Iris dataset**.

The dataset contains measurements of Iris flowers belonging to three different species.

### Input Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal |
| Sepal Width | Width of the sepal |
| Petal Length | Length of the petal |
| Petal Width | Width of the petal |

### Target Variable

The target variable is:

```text
species
