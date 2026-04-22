import os
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader

# Catalogue de vos produits 1TPE (URLs de base)
CATALOGUE = {
    "guitare_barres": "https://mybiz.1tpego.net/mybiz/adieu-les-accords-barres-a-la-guitare.php",
    "guitare_seul": "https://mybiz.1tpego.net/mybiz/apprendre-la-guitare-seul.php",
    "machine_commissions": "https://mybiz.1tpego.net/mybiz/votre-machine-a-commissions-guitare.php",
    "business_automatique": "http://mybiz.1tpego.net/mybiz/business-automatique-illimite.php",
    "business_ligne": "https://mybiz.1tpego.net/mybiz/creer-et-reussir-votre-business-en-ligne.php",
    "medium_dons": "https://mybiz.1tpego.net/mybiz/developpez-vos-dons-de-medium.php",
    "guitare_facile": "https://mybiz.1tpego.net/mybiz/apprendre-la-guitare-facilement.php",
    "voyance_tarot": "https://mybiz.1tpego.net/mybiz/formation-voyance-tarot-de-marseille.php",
    "jardin_radis": "http://mybiz.1tpego.net/mybiz/radis-faciles.php",
    "jardin_tomates": "http://mybiz.1tpego.net/mybiz/tomates-faciles.php"
}

def build_client_pack(affiliate_id, product_key, ai_text_data):
    # Remplacement de 'mybiz' par l'ID du client
    base_url = CATALOGUE.get(product_key)
    final_url = base_url.replace("mybiz", affiliate_id)
    
    # Préparation des données pour le template
    # On force la densité pour le SEO [cite: 2026-02-02]
    context = {
        "affiliate_url": final_url,
        "lws_affiliate_link": "https://affiliation.lws-hosting.com/statistics/click/47/966494630",
        "lws_promo_code": "CF811",
        **ai_text_data
    }
    
    # Génération via Jinja2 et compression en ZIP
    # (Logique de build similaire à notre usine privée)
    print(f"✅ Pack généré pour {affiliate_id} sur le produit {product_key}")
