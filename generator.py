import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Catalogue des 10 produits stratégiques
CATALOGUE = {
    "1": {"nom": "Adieu les accords barrés", "url": "https://mybiz.1tpego.net/mybiz/adieu-les-accords-barres-a-la-guitare.php", "niche": "musique"},
    "2": {"nom": "Apprendre la guitare seul", "url": "https://mybiz.1tpego.net/mybiz/apprendre-la-guitare-seul.php", "niche": "musique"},
    "3": {"nom": "Machine à Commissions", "url": "https://mybiz.1tpego.net/mybiz/votre-machine-a-commissions-guitare.php", "niche": "business"},
    "4": {"nom": "Business Automatique", "url": "http://mybiz.1tpego.net/mybiz/business-automatique-illimite.php", "niche": "business"},
    "5": {"nom": "Réussir son Business", "url": "https://mybiz.1tpego.net/mybiz/creer-et-reussir-votre-business-en-ligne.php", "niche": "business"},
    "6": {"nom": "Dons de Médium", "url": "https://mybiz.1tpego.net/mybiz/developpez-vos-dons-de-medium.php", "niche": "spiritualite"},
    "7": {"nom": "Guitare Facile", "url": "https://mybiz.1tpego.net/mybiz/apprendre-la-guitare-facilement.php", "niche": "musique"},
    "8": {"nom": "Tarot de Marseille", "url": "https://mybiz.1tpego.net/mybiz/formation-voyance-tarot-de-marseille.php", "niche": "spiritualite"},
    "9": {"nom": "Radis Faciles", "url": "http://mybiz.1tpego.net/mybiz/radis-faciles.php", "niche": "jardin"},
    "10": {"nom": "Tomates Faciles", "url": "http://mybiz.1tpego.net/mybiz/tomates-faciles.php", "niche": "jardin"}
}

def generate_pack():
    env = Environment(loader=FileSystemLoader('templates'))
    os.makedirs('dist', exist_ok=True)

    print("--- Générateur de Mini-Site d'Affiliation ---")
    affiliate_id = input("Entrez votre pseudo 1TPE (ex: pseudo123) : ")
    
    print("\nProduits disponibles :")
    for k, v in CATALOGUE.items():
        print(f"{k}. {v['nom']}")
    
    choice = input("\nChoisissez un numéro de produit : ")
    prod = CATALOGUE.get(choice)
    
    if not prod:
        print("Choix invalide.")
        return

    # Injection de l'ID utilisateur
    final_url = prod['url'].replace("mybiz", affiliate_id)

    # Simulation de saisie de texte IA (à remplacer par une lecture de fichier YAML si besoin)
    print("\n--- SEO & IA ---")
    print("Conseil : Utilisez un texte dense pour Bing & Google !")
    h1 = input("Votre Titre H1 : ")
    intro = input("Votre texte d'introduction : ")

    context = {
        "affiliate_url": final_url,
        "h1_title": h1,
        "seo_intro": intro,
        "lws_link": "https://affiliation.lws-hosting.com/statistics/click/47/966494630",
        "lws_code": "CF811",
        "niche": prod['niche']
    }

    template = env.get_template('index.php.jinja')
    with open('dist/index.php', 'w', encoding='utf-8') as f:
        f.write(template.render(context))
    
    print(f"\n✅ Succès ! Votre fichier 'index.php' est prêt dans le dossier /dist/")
    print(f"👉 N'oubliez pas d'utiliser le code {context['lws_code']} pour votre hébergement LWS.")

if __name__ == "__main__":
    generate_pack()
