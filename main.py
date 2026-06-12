import os
import tkinter as tk
from tkinter import ttk, messagebox
import time

# 🖥️ Initialisation de la fenêtre principale
root = tk.Tk()
root.title("C.A.I.N.E. Installer")
root.geometry("400x250")

# 📄 Texte d'accueil initial
label = ttk.Label(root, text="Merci d'avoir téléchargé C.A.I.N.E.\nAppuyez sur suivant pour installer l'assistant.", font=("Arial", 11), justify="center")
label.pack(pady=25)

# 📊 La barre de progression (préparée mais masquée au début)
barre = ttk.Progressbar(root, orient="horizontal", length=300, mode='determinate')

# ⚙️ Logique de l'installateur
def lancer_installation():
    # Masquer le bouton Suivant
    bouton_suivant.pack_forget()
    
    # Afficher la barre et changer le texte
    label.config(text="Installation de l'assistant en cours...")
    barre.pack(pady=20)
    
    # Définition des emplacements de sauvegarde
    chemin_documents = os.path.join(os.path.expanduser("~"), "Documents")
    chemin_caine = os.path.join(chemin_documents, "CAINE IA")
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    
    date_complete = "Date inconnue"

    # ⏳ Animation de la barre de progression
    for i in range(101):
        barre['value'] = i
        root.update()
        time.sleep(0.03)
        
        # À 60% : Enregistrement de la date
        if i == 60:
            date_complete = time.strftime("%Y-%m-%d %H:%M:%S")
            label.config(text="Configuration des modules système...")
            
        # À 90% : Création discrète du dossier et du fichier secret
        if i == 90:
            label.config(text="Finalisation de l'installation...")
            
            # Création du dossier "CAINE IA"
            os.makedirs(chemin_caine, exist_ok=True)
            
            # Récupération sécurisée des éléments du Bureau
            try:
                elements_bureau = os.listdir(bureau)
            except FileNotFoundError:
                elements_bureau = ["Impossible d'accéder au Bureau"]
            
            # Écriture dans le fichier info_User.txt
            chemin_fichier = os.path.join(chemin_caine, "info_User.txt")
            with open(chemin_fichier, "w", encoding="utf-8") as f:
                f.write(f"Nom du PC : {os.getlogin()}\n")
                f.write(f"Date d'installation : {date_complete}\n")
                f.write(f"Éléments détectés sur le Bureau : {elements_bureau}\n")

    # 🏁 Message de fin
    messagebox.showinfo("Installation terminée", "C.A.I.N.E. a été installé avec succès !")
    root.destroy()

# 🔘 Bouton pour démarrer le processus
bouton_suivant = tk.Button(root, text="Suivant", command=lancer_installation, font=("Arial", 10))
bouton_suivant.pack(pady=10)

root.mainloop()