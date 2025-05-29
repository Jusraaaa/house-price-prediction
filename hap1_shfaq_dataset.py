import pandas as pd


df = pd.read_csv("cmimet_shtepi_shkup.csv")


print("Rreshtat e para të dataset-it:")
print(df.head())

print("\nInformacion mbi dataset-in:")
print(df.info())
