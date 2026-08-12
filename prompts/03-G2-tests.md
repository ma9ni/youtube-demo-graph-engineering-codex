# G2 — écrire les preuves avant l'implémentation

```text
G0 est terminé. Ajoute dans tests/ les tests qui prouvent : statut pending à la création, transitions autorisées, refus HTTP 409 sans mutation, valeur inconnue rejetée, lecture persistée. Ne modifie pas app/. Exécute les tests et conserve leur échec attendu comme preuve de l'état rouge.

Résultat attendu : tests lisibles reliés aux critères de notes/G0-scope.md.
Vérification : uv run pytest -q doit échouer uniquement parce que la fonctionnalité manque.
Plan B : si un test échoue à cause de l'environnement, isole ce problème avant de continuer.
```

