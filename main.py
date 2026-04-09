import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os


# Variable globale pour stocker le logo
logo_path = None


def select_logo():
    """Sélectionner un logo à intégrer au QR Code"""
    global logo_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif"), ("All files", "*.*")]
    )
    if file_path:
        # Vérifier la taille du fichier (max 5 MB)
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > 5:
            messagebox.showerror("Fichier trop volumineux", f"Le logo ne doit pas dépasser 5 MB.\nTaille actuelle: {file_size_mb:.2f} MB")
            return
        
        # Vérifier les dimensions de l'image
        try:
            img_check = Image.open(file_path)
            width, height = img_check.size
            if width < 100 or height < 100:
                messagebox.showwarning("Logo petit", f"Le logo est petit ({width}x{height}px).\nRecommandé: au moins 100x100 px pour une meilleure qualité.")
            logo_path = file_path
            btn_logo.config(text=f"Logo: {os.path.basename(file_path)} ({width}x{height}px)", fg="green")
            messagebox.showinfo("Logo sélectionné", f"Logo chargé: {os.path.basename(file_path)}\nDimensions: {width}x{height} pixels")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le logo: {str(e)}")


def is_valid_hex_color(value):
    value = value.strip()
    if not value:
        return False
    if value.startswith("#"):
        value = value[1:]
    return len(value) in (3, 6) and all(c in "0123456789abcdefABCDEF" for c in value)


def generate_qr_code():
    # Récupérer l'URL ou le texte depuis l'entrée
    data = entry_url.get()

    # Créer le QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Augmenté pour supporter le logo
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Valider la couleur de remplissage
    fill_color = entry_color.get().strip() or "#000000"
    if not is_valid_hex_color(fill_color):
        messagebox.showwarning("Couleur invalide", "La couleur hexadécimale n'est pas valide. Utilisation de #000000.")
        fill_color = "#000000"

    # Créer une image à partir du QR code
    img = qr.make_image(fill_color=fill_color, back_color="white").convert('RGB')

    # Ajouter le logo si un est sélectionné
    if logo_path:
        try:
            # Ouvrir et traiter le logo en mode RGBA pour préserver la transparence
            logo = Image.open(logo_path).convert('RGBA')

            # Calculer la taille du logo (20% de la taille du QR code)
            qr_width, qr_height = img.size
            logo_size = int(qr_width * 0.2)

            # Redimensionner le logo
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

            # Créer un fond blanc pour le logo avec une marge
            logo_bg_size = (logo_size + 20, logo_size + 20)
            logo_bg = Image.new('RGBA', logo_bg_size, (255, 255, 255, 255))
            logo_bg_pos = ((logo_bg_size[0] - logo_size) // 2, (logo_bg_size[1] - logo_size) // 2)
            logo_bg.paste(logo, logo_bg_pos, mask=logo)

            # Coller le logo au centre du QR code en conservant le blanc
            img = img.convert('RGBA')
            logo_pos = ((qr_width - logo_bg_size[0]) // 2, (qr_height - logo_bg_size[1]) // 2)
            img.paste(logo_bg, logo_pos, mask=logo_bg)
            img = img.convert('RGB')
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger le logo: {str(e)}")

    # Convertir l'image pour l'afficher dans Tkinter
    img_tk = ImageTk.PhotoImage(img)
    label_qr.config(image=img_tk)
    label_qr.image = img_tk  # Garder une référence

    # Activer le bouton de sauvegarde
    btn_save.config(state=tk.NORMAL)

    # Stocker l'image pour la sauvegarde
    global qr_image
    qr_image = img


def save_qr_code():
    # Ouvrir une boîte de dialogue pour choisir où sauvegarder
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])
    if file_path:
        qr_image.save(file_path)


# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur de QR Code")
root.geometry("400x800")

# Créer les widgets
frame_input = tk.Frame(root, pady=20)
frame_input.pack()

label_url = tk.Label(frame_input, text="URL ou texte:")
label_url.grid(row=0, column=0, padx=5)

entry_url = tk.Entry(frame_input, width=30)
entry_url.grid(row=0, column=1, padx=5)
entry_url.insert(0, "exemple.fr")

label_color = tk.Label(frame_input, text="Couleur du QR (hex):")
label_color.grid(row=1, column=0, padx=5, pady=10)
entry_color = tk.Entry(frame_input, width=30)
entry_color.grid(row=1, column=1, padx=5, pady=10)
entry_color.insert(0, "#000000")

btn_logo = tk.Button(root, text="Charger un logo (optionnel)", command=select_logo, bg="lightblue")
btn_logo.pack(pady=10)

btn_generate = tk.Button(root, text="Générer QR Code", command=generate_qr_code)
btn_generate.pack(pady=10)

# Espace pour afficher le QR code
label_qr = tk.Label(root)
label_qr.pack(pady=20)

# Bouton pour sauvegarder (désactivé par défaut)
btn_save = tk.Button(root, text="Sauvegarder", command=save_qr_code, state=tk.DISABLED)
btn_save.pack(pady=10)

# Lancer l'application
root.mainloop()