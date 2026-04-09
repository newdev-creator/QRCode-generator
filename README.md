# Générateur de QR Code avec Logo

Une application Python simple et intuitive pour générer des codes QR avec la possibilité d'ajouter un logo au centre.

## 📋 Fonctionnalités

✅ **Génération de QR Code** - Créez des codes QR à partir d'une URL ou d'un texte  
✅ **Logo personnalisé** - Ajoutez votre logo au centre du QR Code  
✅ **Couleur personnalisée** - Choisissez la couleur du QR Code en hexadécimal  
✅ **Sauvegarde simple** - Exportez votre QR Code en PNG, JPG ou autres formats  
✅ **Interface intuitive** - Interface utilisateur clean avec Tkinter  
✅ **Validation intelligente** - Vérification automatique des fichiers logo  

## 🚀 Installation

### Prérequis

- Python 3.12 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**

```bash
cd chemin/vers/QR_code
```

1. **Créer un environnement virtuel** (optionnel mais recommandé)

```bash
python -m venv .venv
```

1. **Activer l'environnement virtuel**
   - **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

   - **Mac/Linux:**

   ```bash
   source .venv/bin/activate
   ```

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

Ou directement:

```bash
pip install pillow>=11.0 qrcode>=8.0
```

## 📖 Utilisation

### Lancer l'application

```bash
python main.py
```

### Étapes d'utilisation

1. **Entrez l'URL ou le texte** - Modifiez le champ de texte avec votre URL ou message
2. **Optionnel : choisir une couleur hex** - Saisissez un code couleur comme `#FF0000` ou `#00FF00`
3. **Charger un logo (optionnel)** - Cliquez sur le bouton bleu pour sélectionner une image
4. **Générer le QR Code** - Cliquez sur "Générer QR Code"
5. **Sauvegarder** - Cliquez sur "Sauvegarder" pour choisir l'emplacement et le format

## 🎨 Spécifications des Logos

### Recommandations

- **Taille optimale:** 200-500 pixels de largeur/hauteur
- **Taille minimale:** 100x100 pixels (sinon avertissement)
- **Taille maximale:** 5 MB de fichier
- **Formats acceptés:** PNG, JPG, JPEG, GIF
- **Format recommandé:** PNG avec transparence

### Points importants

- Le logo occupera **20% de la taille du QR Code**
- Un fond blanc sera automatiquement ajouté autour du logo
- Le QR Code utilise une **correction d'erreur haute** pour rester lisible avec le logo

## 🔧 Configuration

### Paramètres du QR Code

```python
qrcode.QRCode(
    version=1,                                    # Taille du QR
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Correction haute
    box_size=10,                                  # Taille des boîtes
    border=4,                                     # Bordure
)
```

### Formats d'export supportés

- PNG (recommandé)
- JPG/JPEG
- GIF
- BMP
- TIFF
- Et tous les formats supportés par Pillow

## 🎨 Couleur du QR Code

- Entrez un code hexadécimal dans le format `#RRGGBB` ou `#RGB`
- Exemple : `#000000` pour noir, `#FF0000` pour rouge, `#00FF00` pour vert
- Si la couleur est invalide, le QR Code utilisera `#000000` par défaut
- La couleur s'applique uniquement à la zone du QR Code; le fond reste blanc

## ⚠️ Points importants

1. **Logo requis?** Non, le logo est **complètement optionnel**
2. **Scannabilité** - Le QR Code reste scannable même avec un logo grâce à la correction d'erreur haute
3. **Qualité** - Pour une meilleure qualité, utilisez des logos carrés avec contraste élevé
4. **Transparence** - Si votre logo a une transparence, elle sera remplacée par un fond blanc

## 📦 Structure du projet

```
QR_code/
├── main.py              # Application principale
├── README.md            # Ce fichier
├── pyproject.toml       # Configuration du projet
└── .venv/              # Environnement virtuel (créé après installation)
```

## 🐛 Dépannage

### Le script ne démarre pas

- Vérifiez que Python 3.12+ est installé: `python --version`
- Réinstallez les dépendances: `pip install --force-reinstall pillow qrcode`

### Le logo ne s'affiche pas

- Vérifiez que le chemin du fichier est correct
- Vérifiez que le fichier image est valide
- Consultez le message d'erreur affiché

### Le QR Code n'est pas lisible avec le logo

- Utilisez un logo plus petit
- Assurez-vous que le logo a du contraste avec le fond blanc
- Vérifiez que le texte/URL n'est pas trop long

## 📝 Dépendances

- **Pillow** (PIL) - Traitement d'images
- **qrcode** - Génération de codes QR
- **tkinter** - Interface graphique (incluse avec Python)

## 📄 Licence

Projet libre d'utilisation.
