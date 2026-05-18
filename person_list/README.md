# person_list

Script Python qui génère et affiche un tableau de 10 utilisateurs français fictifs.

## Dépendances

- [Faker](https://faker.readthedocs.io/) — génération de données aléatoires
- [tabulate](https://pypi.org/project/tabulate/) — affichage en tableau formaté

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Utilisation

```bash
python script.py
```

## Exemple de sortie

```
╭──────────────────────┬──────────────────────────────┬──────────────────╮
│ Nom                  │ Email                        │ Ville            │
├──────────────────────┼──────────────────────────────┼──────────────────┤
│ Marie Dupont         │ marie.dupont@example.fr      │ Lyon             │
│ Jean Martin          │ j.martin@orange.fr           │ Bordeaux         │
╰──────────────────────┴──────────────────────────────┴──────────────────╯
```
