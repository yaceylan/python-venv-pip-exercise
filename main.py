import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**3 for i in x]  # Quadratzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Kubik')

# Legende anzeigen
plt.legend()

# Diagramm anzeigen
# plt.show()

# Speichere das Diagramm als PNG-Datei
plt.savefig('mein_diagramm.png')

nums = pd.DataFrame(y)
nums.to_csv('zahlen.csv', sep='\t', encoding='UTF-8', index=False, header=True)
