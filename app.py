from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


app = Flask(__name__)


df = pd.read_csv("script/cmimet_shtepi_shkup.csv")


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


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
       
        sip = float(request.form["sip"])
        dhoma = int(request.form["dhoma"])
        banjo = int(request.form["banjo"])
        kate = int(request.form["kate"])
        rruga_kryesore = request.form["rruga_kryesore"]
        parkim = int(request.form["parkim"])
        mobilim = request.form["mobilim"]

        
        user_input = pd.DataFrame([{
            "Sipërfaqja (m2)": sip,
            "Dhoma Gjumi": dhoma,
            "Banjo": banjo,
            "Kate": kate,
            "Rruga Kryesore": rruga_kryesore,
            "Parkim": parkim,
            "Statusi i Mobilimit": mobilim
        }])

        
        predicted_price_per_m2 = model.predict(user_input)[0]

        
        total_price = round(predicted_price_per_m2 * sip, 2)

        return render_template("result.html",
    price_per_m2=round(predicted_price_per_m2, 2),  
    total_price=round(total_price, 2)  
)

    return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)
