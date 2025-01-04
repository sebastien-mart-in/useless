import os
import json
import shutil

# Configuration
json_file_path = "chemin/vers/votre/fichier.json"  # Chemin vers votre fichier JSON
source_folder = "chemin/vers/dossier/images"       # Chemin vers le dossier contenant toutes les images
destination_folder = "chemin/vers/nouveau/dossier" # Chemin vers le nouveau dossier pour les images sélectionnées

# Créer le dossier de destination s'il n'existe pas
os.makedirs(destination_folder, exist_ok=True)

# Charger le fichier JSON
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    try:
        data = json.load(json_file)
    except json.JSONDecodeError as e:
        print("Erreur lors du chargement du fichier JSON :", e)
        exit(1)

# Extraire tous les noms d'images du champ "members"
selected_images = set()  # Utiliser un ensemble pour éviter les doublons
for item in data:
    if "img_set" in item and "members" in item["img_set"]:
        selected_images.update(item["img_set"]["members"])

# Copier les images nécessaires dans le dossier de destination
for image_name in selected_images:
    source_path = os.path.join(source_folder, image_name)
    if os.path.exists(source_path):
        destination_path = os.path.join(destination_folder, image_name)
        shutil.copy(source_path, destination_path)
        print(f"Image copiée : {image_name}")
    else:
        print(f"Image non trouvée dans le dossier source : {image_name}")

print("Copie des images terminée.")
