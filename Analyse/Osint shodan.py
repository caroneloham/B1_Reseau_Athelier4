import shodan

# Remplacez 'VOTRE_CLÉ_API' par votre clé API Shodan gratuite
api_key = "dVMk8k9gZURsjBCfEPVyYkOwnnPUMpOX"

# Créez une instance de l'API Shodan avec votre clé
api = shodan.Shodan(api_key)

# Spécifiez le site que vous souhaitez analyser
site = "icann.org"

try:
    # Utilisez la méthode search pour obtenir des informations sur le site
    results = api.search(f"hostname:{site}")

    # Affichez les résultats limités (par exemple, les 5 premiers résultats)
    for result in results['matches'][:5]:
        print(result)

except shodan.APIError as e:
    print(f"Erreur Shodan: {e}")
