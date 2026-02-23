import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []
Y = []

with open(r"C:\Users\st025547\Downloads\kb4a_prog-main\Global_Homicide_Rate_1970_2025.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        years.append int(row["Year"])
        percentage.append = float(row["Global_Avg"])

        X.append([years i-2 years i-1])
        Y.append(percentage)

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

neural_network = MLPClassifier(
    hidden_layer_sizes=(10, 6, 4),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()