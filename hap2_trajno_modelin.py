import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("cmimet_shtepi_shkup.csv")


X = df[["Sipërfaqja (m2)", "Dhoma Gjumi", "Banjo", "Kate", "Rruga Kryesore", "Parkim", "Statusi i Mobilimit"]]
y = df["Çmimi (EUR/m2)"]


categorical_features = ["Rruga Kryesore", "Statusi i Mobilimit"]
categorical_transformer = OneHotEncoder()


preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_transformer, categorical_features)
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Gabimi mesatar absolut (MAE):", mean_absolute_error(y_test, y_pred))
