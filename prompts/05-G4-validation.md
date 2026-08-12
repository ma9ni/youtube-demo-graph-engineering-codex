# G4 — valider et corriger

```text
G3 est terminé. Exécute make validate, puis teste manuellement le chemin principal via l'API ou TestClient. Corrige uniquement les erreurs directement liées à ISSUE.md. Ne masque aucun test et ne baisse aucune assertion.

Résultat attendu : lint et suite complète verts, avec le comportement visible dans Swagger.
Vérification : make validate et git diff --check.
Plan B : si une dépendance réseau bloque, utilise l'environnement déjà synchronisé et consigne le blocage sans fabriquer un résultat.
```

