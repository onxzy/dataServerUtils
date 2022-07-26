# Installation

Exectuer `pip3 install -r requirements.txt` pour installer les modules python nécessaires.

# Utilisation

Vous pouvez modifier les différents paramètres dans le fichier `config.json`.
> Attention l'adresse du serveur doit obligatoirement se terminer par un `/`

## Récupération des ECGs

`python3 getEcgs.py`

Les ECGs sont enregistrés dans un dossier `ecgs_YY-MM-DD_HH:MM:SS`. Il sont regroupés par _link_.
> Il n'est pas possible d'obtenir des informations sur l'utilisateur à qui appartient les données !

Chaque liste d'ECGs est sous la forme
```json
[
    {
        "value": [38,84,154,225,292],
        "date": "2022-01-23T21:24:40.000Z",
        "sampling_frequency":300
    }
]
```
