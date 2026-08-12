# G5 — revue indépendante

```text
Effectue une revue séparée du diff depuis before-demo. Cherche : critère oublié, transition contournable, mutation après erreur, migration destructive, donnée sensible, régression des routes existantes et complexité inutile. Écris les constats dans notes/G5-review.md, classés bloquant/importante/mineure. Corrige seulement les constats bloquants ou importants, puis relance make validate.

Résultat attendu : revue traçable, y compris si aucun défaut n'est trouvé.
Vérification : git diff before-demo et make validate.
Plan B : en cas de doute non testable, marque-le comme limite au lieu d'affirmer qu'il est résolu.
```

