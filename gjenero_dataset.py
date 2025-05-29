import pandas as pd
import random


def generate_skopje_data(num_records):
    data = {
        "Çmimi (EUR/m2)": [random.randint(1000, 2500) for _ in range(num_records)],  
        "Sipërfaqja (m2)": [random.randint(50, 200) for _ in range(num_records)], 
        "Dhoma Gjumi": [random.randint(1, 5) for _ in range(num_records)], 
        "Banjo": [random.randint(1, 3) for _ in range(num_records)],  
        "Kate": [random.randint(1, 5) for _ in range(num_records)], 
        "Rruga Kryesore": [random.choice(["Po", "Jo"]) for _ in range(num_records)],  
        "Parkim": [random.randint(0, 2) for _ in range(num_records)],  #
        "Statusi i Mobilimit": [random.choice(["E Mobiluar", "Gjysmë e Mobiluar", "E Pamobiluar"]) for _ in range(num_records)]
    }
    return pd.DataFrame(data)


num_records = 400
df = generate_skopje_data(num_records)


df.to_csv("cmimet_shtepi_shkup.csv", index=False)

print(f"Dataset-i me {num_records} rreshta për Shkup është ruajtur si 'cmimet_shtepi_shkup.csv'.")
