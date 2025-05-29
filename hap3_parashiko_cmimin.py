import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


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


print("\n--- Parashikim i Çmimit të Shtëpisë ---")
sip = float(input("Jep sipërfaqen në m²: "))
dhoma = int(input("Jep numrin e dhomave të gjumit: "))
banjo = int(input("Jep numrin e banjove: "))
kate = int(input("Jep numrin e kateve: "))
rruga_kryesore = input("A është pranë rrugës kryesore (Po/Jo)? ").strip().capitalize()
parkim = int(input("Sa vende parkimi ka (0/1/2)? "))
mobilim = input("Statusi i mobilimit (E Mobiluar/Gjysmë e Mobiluar/E Pamobiluar): ").strip().capitalize()


user_input = pd.DataFrame({
    "Sipërfaqja (m2)": [sip],
    "Dhoma Gjumi": [dhoma],
    "Banjo": [banjo],
    "Kate": [kate],
    "Rruga Kryesore": [rruga_kryesore],
    "Parkim": [parkim],
    "Statusi i Mobilimit": [mobilim]
})


predicted_price = model.predict(user_input)
print(f"\nÇmimi i parashikuar për shtëpinë është: {predicted_price[0]:.2f} EUR/m²")
