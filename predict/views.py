from django.shortcuts import render, redirect
import pandas as pd
import os
from django.conf import settings
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import classification_report
import joblib
import numpy as np

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt

from main.models import bmii

def save_model(request, dataset_id):
    context = {}
    dataset = bmii.objects.get(id=dataset_id)
    if request.method == 'POST':
        label = request.POST['label']
        dataset_path = os.path.join(settings.MEDIA_ROOT, dataset.file.name)
        df = pd.read_csv(dataset_path)

        attribute = df.drop(label, axis=1)
        target = df[label]

        X_train, X_test, y_train, y_test = train_test_split(attribute, target, test_size=0.2, random_state=42)
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)

        # Classification report
        y_pred = clf.predict(X_test)
        report = classification_report(y_test, y_pred)

        # Image tree
        image_path = os.path.join(settings.MEDIA_ROOT, 'decision_tree.png')
        names = list(target.unique())
        class_names = [str(x) for x in names]  
        fig, ax = plt.subplots(figsize=(12, 8))
        tree.plot_tree(clf, filled=True, feature_names=attribute.columns, class_names=class_names, ax=ax)
        plt.savefig(image_path)
        plt.close()

        # Save model
        model_path = os.path.join(settings.MEDIA_ROOT, 'decision_tree_model.joblib')
        joblib.dump(clf, model_path)
        

        context['dataset_id'] = dataset_id
        context['image_url'] = settings.MEDIA_URL + 'decision_tree.png'

        return render(request, 'pages/predict/index.html', context)
    else:
        context['dataset_id'] = dataset_id
        return redirect('uploads:prepocessing', dataset_id=dataset_id)

def logic_predict(request, context={}):
    if request.method == 'POST':
        try:
            age = float(request.POST['age'])
            height = float(request.POST['height'])
            weight = float(request.POST['weight'])
            height_in_meters = height / 100
            bmi = weight / (height_in_meters ** 2)

            # Load model from file
            model_path = os.path.join(settings.MEDIA_ROOT, 'decision_tree_model.joblib')
            model = joblib.load(model_path)

            # Prediction
            X_new = np.array([[age, height, weight, bmi]])
            prediction = model.predict(X_new)[0]

            return render(request, 'pages/predict/hasil.html', {
                'age': age,
                'height': height,
                'weight': weight,
                'bmi': bmi,
                'hasil': prediction,
                'image_url': settings.MEDIA_URL + 'decision_tree.png'
            })
        except (ValueError, TypeError) as e:
            return render(request, 'pages/predict/hasil.html', {
                'error_message': f"Input harus berupa angka. Kesalahan: {e}",
                'image_url': settings.MEDIA_URL + 'decision_tree.png'
            })
    context['image_url'] = settings.MEDIA_URL + 'decision_tree.png'
    return render(request, 'pages/predict/hasil.html', context)

