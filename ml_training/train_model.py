import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib



data = {

    "amount":[
        5000,
        10000,
        20000,
        80000,
        120000,
        150000
    ],

    "payment_delay":[
        2,
        5,
        10,
        40,
        60,
        90
    ],

    "vendor_rating":[
        5,
        4,
        4,
        2,
        1,
        1
    ],

    "risk":[
        0,
        0,
        0,
        1,
        1,
        1
    ]
}


df = pd.DataFrame(data)



X = df[
    [
        "amount",
        "payment_delay",
        "vendor_rating"
    ]
]


y = df["risk"]



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(
    X_train,
    y_train
)



prediction = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    prediction
)


print(
    "Model Accuracy:",
    accuracy
)

os.makedirs(
    "app/ml_models",
    exist_ok=True
)

joblib.dump(
    model,
    "app/ml_models/invoice_risk_model.pkl"
)


print(
    "Model saved successfully"
)