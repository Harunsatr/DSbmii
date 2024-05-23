from django.shortcuts import render
import pandas as pd
import os
from django.shortcuts import redirect
from django.conf import settings
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import joblib

from main.models import bmii
# Create your views here.
def save_model(request, dataset_id):
    context = {}
    dataset = bmii.objects.get(id=dataset_id)
    if request.method == 'POST':
        label = request.POST['label']
        dataset_path = os.path.join(settings.MEDIA_ROOT, dataset.file.name)
        df = pd.read_csv(dataset_path)

        atrribute = df.drop(label, axis=1)
        target = df[label]

        X_train, X_test, y_train, y_test = train_test_split(atrribute, target, test_size=0.2, random_state=42)
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)


        #classification report
        y_pred = clf.predict(X_test)
        report = classification_report(y_test, y_pred)

        #image tree 
        image_path = os.path.join(settings.MEDIA_ROOT, 'decision_tree.png')
        names = list(target.unique())
        class_names = [str(x) for x in names]  
        tree.plot_tree(clf, filled=True, feature_names=atrribute.columns, class_names=class_names)
        plt.savefig(image_path)
        plt.close()

        #save model
        model_path = os.path.join(settings.MEDIA_ROOT, 'decision_tree.joblib')
        joblib.dump(clf, model_path)

        context['dataset_id'] = dataset_id
        return render(request, 'pages/predict/index.html', context)
    else:
        context['dataset_id'] = dataset_id
        return redirect('uploads:prepocessing', dataset_id=dataset_id)   






