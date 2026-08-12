# Approche A — prompt libre

## Prompt à copier

```text
Tu travailles dans ce dépôt public de démonstration. Lis entièrement ISSUE.md, puis implémente la fonctionnalité demandée.

Contraintes :
- tu peux modifier uniquement app/, tests/ et la documentation directement liée à l'issue ;
- conserve FastAPI, SQLite et pytest ;
- n'ajoute aucun service externe, secret, front-end ou donnée réelle ;
- pars du comportement existant et garde les routes actuelles compatibles ;
- exécute make validate avant de terminer.

Résultat attendu : tous les critères d'acceptation de ISSUE.md sont démontrés par le code et les tests. À la fin, résume les fichiers modifiés, les tests exécutés et les limites restantes.

Si tu bloques, n'invente pas un succès : décris le blocage, laisse le dépôt dans un état testable et indique la prochaine commande sûre.
```

## Vérification

```bash
make validate
git diff --stat before-demo
```

