# Parcours OBS — Graph Engineering

## Préparation hors écran

1. Utiliser une copie jetable pour chaque approche.
2. Synchroniser les dépendances et vérifier `make validate` sur `before-demo`.
3. Ouvrir uniquement : terminal, éditeur, `ISSUE.md`, `graph.yaml`, Swagger et `metrics-results.md`.
4. Couper notifications, masquer chemins personnels et fermer tout dépôt privé.

## Enregistrement

1. **État initial** — montrer `git rev-parse --short HEAD` sur `before-demo`, l'issue et les 2 tests verts.
2. **Approche A** — créer `experiment/prompt-libre`, démarrer le chrono, copier `prompts/00-prompt-libre.md`, capturer plan, interventions, diff et tests.
3. **Preuve A** — exécuter `make validate`, puis renseigner uniquement la colonne Prompt libre.
4. **Retour propre** — passer dans le second clone resté sur `before-demo`; ne pas réinitialiser le clone contenant A.
5. **Approche B** — créer `experiment/graphe`, afficher `graph.yaml`, puis lancer les prompts 01 à 07 dans l'ordre des dépendances.
6. **Preuve B** — capturer l'état rouge après G2, le passage au vert après G3/G4 et la revue G5.
7. **Comparaison** — remplir la colonne Graphe G0–G6 à l'écran, sans valeur préremplie.
8. **Limite** — montrer au moins un coût ou une friction du graphe, même si B gagne.
9. **Verdict** — enregistrer la conclusion seulement après les deux mesures.

## Checkpoints visuels

- Swagger : `/docs`, création d'un ticket, transition valide, transition refusée.
- Terminal : tag de départ, commande de validation, résumé du diff.
- Éditeur : ISSUE, graphe, tests, revue, tableau de mesures.

## Plan de secours

- `after-demo` est un résultat technique de référence, jamais une mesure de l'agent.
- Si une exécution échoue, capturer l'échec, conserver le clone et recommencer uniquement l'approche concernée depuis un nouveau clone de `before-demo`.
- Si Swagger tombe, utiliser les tests ciblés comme preuve visible.
- Si le temps manque, couper les animations et garder issue → exécution → tests → mesure → limite.
