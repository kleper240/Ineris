from io import StringIO
import pandas as pd
import requests


# r = requests.get('https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port')
# j = r.json()


"""
curl -X POST -F data=@path/to/file.csv -F columns=voie -F columns=ville -F citycode=ma_colonne_code_insee https://api-adresse.data.gouv.fr/search/csv/
"""
url = "https://api-adresse.data.gouv.fr/search/csv/"
with open("/Users/souha_kassab/Downloads/search.csv", 'r') as f:
    r = requests.post(url, files={"data": f})
csv_str = r.text

# Convert String into StringIO
csvStringIO = StringIO(csv_str)
df = pd.read_csv(csvStringIO, sep=",", header=0)
