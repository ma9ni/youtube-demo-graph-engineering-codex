# G3 — implémenter le changement minimal

```text
G1 et G2 sont terminés. Lis notes/G0-scope.md, notes/G1-impact-map.md et les tests rouges. Modifie seulement app/ pour ajouter le statut persistant et PATCH /tickets/{id}/status. Implémente uniquement pending → in_progress → done, avec HTTP 409 pour une transition interdite. Préserve les bases créées avant la nouvelle colonne.

Résultat attendu : les tests de G2 deviennent verts sans service externe ni refonte inutile.
Vérification : uv run pytest -q.
Plan B : si une migration SQLite échoue, conserve la donnée, documente le cas et privilégie une migration additive.
```

