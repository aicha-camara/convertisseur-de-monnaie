from forex_python.converter import CurrencyRates
from datetime import datetime

def convertir_montant(montant, devise_origine, devise_destination):
    convertisseur = CurrencyRates()

    try:
        taux_de_change = convertisseur.get_rate(devise_origine, devise_destination)
        convertion = montant * taux_de_change

        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entree_conversion = f"{horodatage}: {montant} {devise_origine} => {convertion:.2f} {devise_destination} )"
        with open("historique_conversion.txt", "a") as fichier:
            fichier.write(entree_conversion + "\n")

        print(f"\nLe resultat de la convertion de {devise_origine}  à {devise_destination} est de {convertion:.2f} ")
    except Exception as erreur:
        print(f"Erreur lors de la conversion : {erreur}")

# Saisie des informations de conversion par l'utilisateur
montant= float(input("Entrez le montant à convertir : "))
devise_origine = input("Entrez la devise d'origine ( exemple : EUR) : ").upper()
devise_destination = input("Entrez la devise de destination ( exemple : USD) : ").upper()

# Conversion et affichage des résultats
convertir_montant(montant, devise_origine, devise_destination)
