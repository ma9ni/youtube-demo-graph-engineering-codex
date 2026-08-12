# Graph Engineering avec Codex — démo reproductible

Ce dépôt permet de tester une question simple : un graphe explicite de tâches réduit-il les oublis et les reprises face à un prompt libre, sur la même issue de code ? Il fournit un mini-SaaS neutre de tickets, deux états Git reproductibles et un protocole de mesure. Il ne contient aucune donnée ni dépendance issue d'un projet privé.

## Résultat visible

L'issue ajoute aux tickets un statut persistant `pending`, `in_progress` ou `done`, une validation stricte des transitions et `PATCH /tickets/{id}/status`. Le comportement est visible dans Swagger, SQLite, les tests et le diff Git.

## Stack

- Python 3.11+
- FastAPI + Swagger
- SQLite local
- pytest et Ruff
- `uv` pour une installation reproductible

## Installation et lancement

```bash
git clone https://github.com/ma9ni/youtube-demo-graph-engineering-codex.git
cd youtube-demo-graph-engineering-codex
make install
make validate
make run
```

Ouvrir ensuite <http://127.0.0.1:8000/docs>. Aucun fichier `.env` ni aucune clé API ne sont requis.

## Déroulé rapide de la fonctionnalité

1. Créer un ticket avec `POST /tickets` : son statut vaut `pending`.
2. Envoyer `{"status":"in_progress"}` à `PATCH /tickets/{id}/status`.
3. Passer ensuite à `done`.
4. Essayer `pending → done` sur un autre ticket : l'API répond 409 et conserve `pending`.
5. Redémarrer l'API et relire le ticket pour montrer la persistance.

## Préparer l'expérience A/B sans écraser son travail

Utiliser deux clones jetables démarrant du même repère Git :

```bash
git clone https://github.com/ma9ni/youtube-demo-graph-engineering-codex.git demo-prompt
git clone https://github.com/ma9ni/youtube-demo-graph-engineering-codex.git demo-graph

cd demo-prompt
git switch --detach before-demo
git switch -c experiment/prompt-libre
uv sync

cd ../demo-graph
git switch --detach before-demo
git switch -c experiment/graphe
uv sync
```

Dans `demo-prompt`, lancer le prompt `prompts/00-prompt-libre.md`. Dans `demo-graph`, lancer les prompts 01 à 07 dans l'ordre de `graph.yaml`. Utiliser une copie de `metrics-template.md` pour chaque exécution et ne saisir que des résultats observés.

Le repère Git `after-demo` contient une implémentation de référence et sert seulement de plan de secours. Il ne constitue pas le résultat mesuré d'une exécution Codex.

## Commandes utiles

```bash
make run       # démarre Swagger
make test      # tests rapides
make validate  # lint + tests
make reset     # supprime uniquement la base locale demo.db
git diff --stat before-demo
```

## Arborescence

```text
app/                  API, validation et SQLite
tests/                preuves rapides du comportement
data/                 tickets 100 % synthétiques
prompts/              prompt libre puis G0 à G6
docs/                 architecture et parcours OBS
ISSUE.md              besoin et critères communs
graph.yaml             nœuds, dépendances et preuves
metrics-template.md    mesures volontairement vides
```

## Dépannage

- `uv: command not found` : installer `uv`, rouvrir le terminal puis relancer `make install`.
- Port 8000 occupé : lancer `uv run uvicorn app.main:app --port 8001`.
- Base locale incohérente : sauvegarder ce qui compte, puis `make reset`; cette commande ne touche qu'à `demo.db`.
- Échec de l'agent : conserver sa branche comme preuve et repartir d'un nouveau clone sur `before-demo`.

## Limites méthodologiques

Une seule issue ne constitue pas un benchmark général. Le temps de cadrage, le comportement non déterministe du modèle et les interventions humaines peuvent influencer le résultat. Le tableau de mesures est donc directionnel. Aucun facteur « 10x » n'est supposé ni prérempli.

Voir aussi [le parcours OBS](docs/OBS-RECORDING.md) et [l'architecture](docs/ARCHITECTURE.md).

## Licence

MIT.
