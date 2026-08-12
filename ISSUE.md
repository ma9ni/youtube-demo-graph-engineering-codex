# Issue de démonstration : ajouter un statut persistant aux tickets

Le mini-SaaS sait créer et lire des tickets fictifs, mais il ne suit pas leur traitement.

## Critères d'acceptation

1. Chaque ticket possède un statut parmi `pending`, `in_progress` et `done`.
2. Un ticket créé démarre avec le statut `pending`.
3. `PATCH /tickets/{id}/status` modifie le statut d'un ticket existant.
4. Les seules transitions autorisées sont `pending → in_progress` et `in_progress → done`.
5. Une transition invalide retourne HTTP 409 et ne modifie pas la base.
6. Le statut survit au redémarrage de l'application grâce à SQLite.
7. Swagger expose le champ et le nouvel endpoint.
8. Des tests couvrent la création, les transitions valides, les refus et la persistance.

## Contraintes

- Conserver FastAPI, SQLite et pytest.
- Ne pas ajouter d'authentification, de front-end, de cloud ou de service payant.
- Ne jamais utiliser de donnée réelle ni de secret.
- Garder `make validate` vert.

