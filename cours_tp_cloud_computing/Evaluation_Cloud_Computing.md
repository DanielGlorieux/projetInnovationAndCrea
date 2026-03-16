# ÉVALUATION – FONDAMENTAUX DU CLOUD COMPUTING

**Durée : 2 heures**
**Documents autorisés : Aucun**
**Barème total : 60 points**

> **Consignes générales :**
> - Répondez de manière claire et concise.
> - Justifiez systématiquement vos réponses.
> - Soignez la présentation et l'orthographe.

---

## PARTIE 1 – Questions à Choix Multiple (QCM) — 15 points

*Cochez la ou les bonne(s) réponse(s). Chaque question vaut 1,5 point. Attention, certaines questions peuvent avoir plusieurs bonnes réponses.*

**Question 1 :** Quelle définition correspond le mieux au Cloud Computing ?

- [ ] a) L'installation de serveurs physiques dans les locaux de l'entreprise
- [ ] b) La mise à disposition de ressources informatiques (calcul, stockage, réseau) à la demande via Internet
- [ ] c) Un logiciel de virtualisation installé sur un PC personnel
- [ ] d) Un réseau local privé d'entreprise

**Question 2 :** Parmi les modèles de services suivants, lequel correspond à la fourniture d'une infrastructure virtuelle (serveurs, stockage, réseau) sans gestion du matériel physique ?

- [ ] a) SaaS
- [ ] b) PaaS
- [ ] c) IaaS
- [ ] d) FaaS

**Question 3 :** Google Docs, Microsoft 365, Gmail sont des exemples de quel modèle de service cloud ?

- [ ] a) IaaS
- [ ] b) PaaS
- [ ] c) SaaS
- [ ] d) DaaS

**Question 4 :** Quel modèle de déploiement cloud combine l'utilisation de ressources privées et publiques ?

- [ ] a) Cloud public
- [ ] b) Cloud privé
- [ ] c) Cloud hybride
- [ ] d) Multi-cloud

**Question 5 :** Quelle est la principale différence entre un cloud hybride et un multi-cloud ?

- [ ] a) Le multi-cloud utilise plusieurs fournisseurs cloud, tandis que le cloud hybride combine cloud public et infrastructure privée
- [ ] b) Le cloud hybride est toujours plus cher que le multi-cloud
- [ ] c) Le multi-cloud est réservé aux grandes entreprises
- [ ] d) Il n'y a aucune différence

**Question 6 :** Quel service AWS permet d'exécuter du code sans gérer de serveur (serverless) ?

- [ ] a) Amazon EC2
- [ ] b) Amazon S3
- [ ] c) AWS Lambda
- [ ] d) Amazon RDS

**Question 7 :** Quelle commande Docker permet de lancer un conteneur nginx en arrière-plan et de mapper le port 8080 vers le port 80 ?

- [ ] a) `docker start nginx -p 8080:80`
- [ ] b) `docker run -d -p 8080:80 nginx`
- [ ] c) `docker pull nginx -p 8080:80`
- [ ] d) `docker create -p 80:8080 nginx`

**Question 8 :** Quel outil est utilisé pour l'Infrastructure as Code (IaC) ?

- [ ] a) Docker
- [ ] b) Terraform
- [ ] c) Kubernetes
- [ ] d) Git

**Question 9 :** Dans le modèle de responsabilité partagée du cloud, qui est responsable de la sécurité physique des datacenters ?

- [ ] a) Le client
- [ ] b) Le fournisseur cloud
- [ ] c) Les deux conjointement
- [ ] d) Aucun des deux

**Question 10 :** Quel type d'instance de facturation permet d'obtenir des réductions pouvant aller jusqu'à 90 % par rapport au tarif à la demande ?

- [ ] a) Instances réservées
- [ ] b) Instances Spot
- [ ] c) Instances On-Demand
- [ ] d) Instances dédiées

---

## PARTIE 2 – Questions de cours — 15 points

*Répondez aux questions suivantes en quelques lignes (5 à 10 lignes maximum par question).*

**Question 11 (3 points) :** Définissez et comparez les trois modèles de services cloud : **IaaS**, **PaaS** et **SaaS**. Pour chaque modèle, donnez un exemple concret de service proposé par un fournisseur cloud majeur (AWS, Azure ou GCP).

**Question 12 (3 points) :** Expliquez ce qu'est la **virtualisation** et en quoi elle est essentielle au fonctionnement du Cloud Computing. Quelle est la différence fondamentale entre une machine virtuelle (VM) et un conteneur Docker en termes d'isolation et de consommation de ressources ?

**Question 13 (3 points) :** Décrivez les **quatre méthodes de déploiement** d'une application vers le cloud : Lift & Shift, Conteneurisation, Serverless (FaaS), et Déploiement Zero Downtime. Précisez dans quel contexte chacune est la plus adaptée.

**Question 14 (3 points) :** Quels sont les **principaux risques de sécurité** dans le cloud ? Citez au moins quatre mesures essentielles pour sécuriser une infrastructure cloud et donnez un exemple d'outil ou de service pour chacune.

**Question 15 (3 points) :** Expliquez le concept de **services gérés** (managed services) dans le cloud. Quels avantages apportent-ils par rapport à une gestion manuelle de l'infrastructure ? Donnez deux exemples concrets de services gérés et précisez leur utilité.

---

## PARTIE 3 – Étude de cas — 20 points

### Contexte

La **Banque Nationale du Burkina Faso (BNBF)** souhaite moderniser son système d'information en migrant vers le cloud. Actuellement, la banque dispose de serveurs physiques hébergés dans ses propres locaux. Voici les besoins identifiés :

1. **Application bancaire critique** : utilisée par 500 employés, elle gère les transactions des clients. Elle doit être disponible 24h/24 avec un niveau de sécurité maximal.
2. **Portail client en ligne** : une application web accessible au grand public, avec des pics de fréquentation en fin de mois (jours de paie).
3. **Stockage des documents** : archivage de millions de documents réglementaires (relevés, contrats, pièces d'identité).
4. **Plateforme d'analyse de données** : traitement de grandes quantités de données pour la détection de fraude et le reporting financier.

**Budget IT annuel estimé** : 50 000 000 FCFA (≈ 76 000 €)

---

**Question 16 (4 points) :** Quel **modèle de déploiement** (cloud public, privé, hybride ou multi-cloud) recommandez-vous pour la BNBF ? Justifiez votre choix en tenant compte des contraintes de sécurité, de réglementation (souveraineté des données), de disponibilité et de coût.

**Question 17 (4 points) :** Pour chacun des quatre besoins identifiés, proposez une **architecture cloud** en précisant :
- Le type de service cloud (IaaS, PaaS, SaaS)
- Le ou les services spécifiques d'un fournisseur (AWS, Azure ou GCP)
- La justification de votre choix

Présentez votre réponse sous forme de tableau en suivant le modèle ci-dessous :

| Besoin | Type de service (IaaS/PaaS/SaaS) | Service(s) proposé(s) | Justification |
|--------|----------------------------------|----------------------|---------------|
| Application bancaire | ... | ... | ... |
| Portail client | ... | ... | ... |
| Stockage documents | ... | ... | ... |
| Analyse de données | ... | ... | ... |

**Question 18 (4 points) :** Détaillez la **stratégie de sécurité** que vous mettriez en place pour cette banque. Votre réponse doit couvrir :
- La gestion des accès et des identités
- Le chiffrement des données (au repos et en transit)
- La conformité réglementaire (RGPD ou équivalent local)
- Le plan de sauvegarde et de reprise après sinistre

**Question 19 (4 points) :** Proposez une **stratégie de migration** pour le portail client en ligne. Quelle méthode de déploiement choisiriez-vous (Lift & Shift, Conteneurisation, Serverless) et pourquoi ? Décrivez les étapes principales de la migration et expliquez comment assurer la continuité de service pendant la transition (déploiement Zero Downtime).

**Question 20 (4 points) :** Réalisez une **estimation des coûts** mensuels pour l'hébergement cloud de la BNBF en vous basant sur les éléments suivants :
- 3 machines virtuelles pour l'application bancaire (haute disponibilité)
- Stockage objet pour les documents (estimé à 5 To)
- Service de base de données managé
- Service d'auto-scaling pour le portail client

Précisez le modèle de facturation recommandé (On-Demand, Instances Réservées, Spot) pour chaque composant et justifiez vos choix. Indiquez si le budget annuel de 76 000 € est réaliste.

---

## PARTIE 4 – Question de réflexion — 10 points

**Question 21 (5 points) :** « Le cloud computing est-il intrinsèquement moins sécurisé qu'une infrastructure hébergée en local (on-premise) ? »

Rédigez une argumentation structurée (introduction, développement avec arguments pour et contre, conclusion) en vous appuyant sur les concepts vus en cours : modèle de responsabilité partagée, chiffrement, gestion des accès, conformité, disponibilité et résilience.

**Question 22 (5 points) :** Une startup technologique basée à Ouagadougou développe une application mobile de livraison de repas. Elle hésite entre trois stratégies :
- **Option A** : Tout héberger sur des serveurs physiques locaux
- **Option B** : Utiliser uniquement des services serverless (FaaS) sur un cloud public
- **Option C** : Adopter une approche conteneurisée avec Kubernetes sur un cloud public

Pour chaque option, analysez les **avantages**, les **inconvénients** et les **coûts** associés. Concluez en recommandant l'option la plus adaptée en justifiant votre choix par rapport au contexte africain (connectivité, coûts, compétences locales disponibles).

---

## BARÈME RÉCAPITULATIF

| Partie | Thème | Points |
|--------|-------|--------|
| Partie 1 | QCM – Connaissances fondamentales | 15 |
| Partie 2 | Questions de cours | 15 |
| Partie 3 | Étude de cas – Architecture cloud | 20 |
| Partie 4 | Réflexion et analyse critique | 10 |
| **Total** | | **60** |

---

## CORRIGÉ INDICATIF

<details>
<summary><strong>Cliquez pour afficher le corrigé</strong></summary>

### Partie 1 – QCM

| Question | Réponse(s) | Explication |
|----------|-----------|-------------|
| Q1 | **b)** | Le cloud computing repose sur la mise à disposition de ressources à la demande via Internet |
| Q2 | **c) IaaS** | Infrastructure as a Service fournit des ressources virtualisées (VM, stockage, réseau) |
| Q3 | **c) SaaS** | Software as a Service – applications prêtes à l'emploi accessibles via un navigateur |
| Q4 | **c) Cloud hybride** | Combinaison d'infrastructure privée et de cloud public |
| Q5 | **a)** | Le multi-cloud = plusieurs fournisseurs ; le hybride = public + privé |
| Q6 | **c) AWS Lambda** | Service serverless (FaaS) d'AWS |
| Q7 | **b)** | `docker run -d -p 8080:80 nginx` : -d pour detached, -p pour le mapping de ports |
| Q8 | **b) Terraform** | Outil IaC permettant de définir l'infrastructure en code déclaratif |
| Q9 | **b) Le fournisseur cloud** | Dans le modèle de responsabilité partagée, le fournisseur gère la sécurité physique |
| Q10 | **b) Instances Spot** | Jusqu'à -90% mais avec risque d'interruption |

### Partie 2 – Éléments de réponse

**Q11 – IaaS, PaaS, SaaS :**
- **IaaS** : Infrastructure virtuelle à la demande (ex : AWS EC2, Azure Virtual Machines, GCP Compute Engine). Le client gère l'OS, les applications et les données.
- **PaaS** : Plateforme de développement et déploiement (ex : AWS Elastic Beanstalk, Azure App Service, Google App Engine). Le client gère uniquement son code applicatif.
- **SaaS** : Application complète accessible via le web (ex : Microsoft 365, Google Workspace, Salesforce). Le client utilise l'application sans se soucier de l'infrastructure.

**Q12 – Virtualisation et conteneurs :**
- La virtualisation permet de créer plusieurs machines virtuelles sur un seul serveur physique grâce à un hyperviseur. Chaque VM possède son propre OS complet.
- Un conteneur Docker partage le noyau de l'OS hôte, ce qui le rend plus léger (démarrage en secondes vs minutes pour une VM) et moins gourmand en ressources.
- La virtualisation est essentielle au cloud car elle permet le partage efficace des ressources matérielles entre de nombreux clients (multi-tenant).

**Q13 – Méthodes de déploiement :**
- **Lift & Shift** : Migration à l'identique vers une VM cloud. Rapide mais sans optimisation. Adapté pour une migration initiale urgente.
- **Conteneurisation** : Modernisation avec Docker/Kubernetes. Portabilité et scalabilité. Pour les applications à moderniser.
- **Serverless** : Exécution de fonctions à la demande (ex : AWS Lambda). Pas de serveur à gérer. Pour des traitements événementiels ou des API légères.
- **Zero Downtime** : Déploiement progressif (blue-green, canary) sans interruption de service. Pour les applications critiques en production.

**Q14 – Sécurité cloud :**
Risques : fuites de données, perte de contrôle de l'infrastructure, vulnérabilités applicatives, attaques réseau.
Mesures :
1. Gestion des accès (AWS IAM, Azure AD)
2. Chiffrement des données (AES-256, TLS)
3. Conformité et audit (RGPD, PCI-DSS)
4. Sauvegarde et reprise (snapshots, réplication multi-zones)

**Q15 – Services gérés :**
Un service géré est un service cloud où le fournisseur prend en charge l'installation, la maintenance, les mises à jour, la sauvegarde et la haute disponibilité. Le client se concentre sur l'utilisation du service.
- Exemples : Amazon RDS (base de données relationnelle managée), Amazon S3 (stockage objet), Azure SQL Database.
- Avantages : réduction de la charge opérationnelle, haute disponibilité intégrée, mises à jour automatiques, scalabilité simplifiée.

### Partie 3 – Étude de cas (éléments de réponse)

**Q16 – Modèle de déploiement :** Cloud **hybride** recommandé.
- L'application bancaire critique et les données sensibles restent sur un cloud privé ou on-premise pour respecter la souveraineté des données et les réglementations bancaires.
- Le portail client et l'analyse de données peuvent utiliser le cloud public pour bénéficier de la scalabilité et réduire les coûts.
- Le stockage des documents peut être réparti entre privé (documents sensibles) et public (archivage long terme).

**Q17 – Architecture proposée :**

| Besoin | Type de service | Service recommandé | Justification |
|--------|----------------|-------------------|---------------|
| Application bancaire | IaaS | AWS EC2 (instances réservées) + RDS | Contrôle total, haute disponibilité, base de données managée |
| Portail client | PaaS | Azure App Service + CDN | Auto-scaling pour les pics, déploiement simplifié |
| Stockage documents | SaaS/IaaS | Amazon S3 (classes de stockage) | Coût optimisé avec S3 Glacier pour l'archivage |
| Analyse de données | PaaS | Google BigQuery | Analyse massive de données, facturation à la requête |

**Q18 – Stratégie de sécurité :**
- **Gestion des accès** : IAM avec principe du moindre privilège, authentification multi-facteurs (MFA), rôles RBAC.
- **Chiffrement** : AES-256 au repos, TLS 1.3 en transit, gestion des clés via AWS KMS ou Azure Key Vault.
- **Conformité** : Audits réguliers, journalisation (CloudTrail/Azure Monitor), conformité RGPD et réglementations bancaires locales.
- **Sauvegarde/PRA** : Snapshots automatiques quotidiens, réplication multi-zones, RPO < 1h, RTO < 4h, tests de reprise trimestriels.

**Q19 – Stratégie de migration du portail client :**
Méthode recommandée : **Conteneurisation** avec déploiement Zero Downtime.
- Étape 1 : Conteneuriser l'application avec Docker
- Étape 2 : Tester en environnement de staging
- Étape 3 : Déploiement blue-green : l'ancienne version reste active (blue) pendant que la nouvelle (green) est déployée
- Étape 4 : Basculement progressif du trafic (canary deployment : 10% → 50% → 100%)
- Étape 5 : Monitoring et rollback automatique en cas de problème
- Continuité assurée par le load balancer qui redirige le trafic de manière transparente.

**Q20 – Estimation des coûts :**

> *Note : Les estimations ci-dessous sont indicatives et basées sur les tarifs publics approximatifs des fournisseurs cloud. Les coûts réels varient selon la région, la période et les négociations commerciales. Il est recommandé d'utiliser les calculateurs de coûts officiels (AWS Pricing Calculator, Azure Pricing Calculator, GCP Pricing Calculator) pour une estimation précise.*

| Composant | Service | Modèle de facturation | Coût estimé/mois |
|-----------|---------|----------------------|-----------------|
| 3 VM (application bancaire) | EC2 m5.large | Instances réservées (1 an) | ~350 € |
| Stockage 5 To | S3 Standard + Glacier | On-Demand | ~120 € |
| Base de données | RDS MySQL Multi-AZ | Instances réservées | ~250 € |
| Auto-scaling portail | EC2 + ALB | On-Demand + Spot (hors pics) | ~200 € |
| Réseau/transfert | Data Transfer | On-Demand | ~80 € |
| **Total mensuel** | | | **~1 000 €** |
| **Total annuel** | | | **~12 000 €** |

Le budget de 76 000 €/an est réaliste et laisse une marge confortable pour les imprévus, les licences logicielles, le support premium et l'évolution de l'infrastructure.

### Partie 4 – Réflexion (éléments attendus)

**Q21 – Sécurité cloud vs on-premise :**
- Arguments « moins sécurisé » : perte de contrôle physique, dépendance au fournisseur, risque de mauvaise configuration, partage de ressources (multi-tenant), questions de souveraineté.
- Arguments « plus sécurisé » : les fournisseurs cloud investissent massivement dans la sécurité (certifications ISO 27001, SOC 2), équipes dédiées 24/7, chiffrement natif, redondance géographique, mises à jour automatiques.
- Conclusion attendue : la sécurité dépend davantage de la bonne configuration et du respect du modèle de responsabilité partagée que du modèle d'hébergement lui-même.

**Q22 – Startup de livraison :**
- **Option A (serveurs locaux)** : ✅ Contrôle total, pas de dépendance Internet. ❌ Coût initial élevé, maintenance complexe, scalabilité limitée. Non adapté pour une startup.
- **Option B (Serverless)** : ✅ Aucun serveur à gérer, coût proportionnel à l'usage, idéal pour démarrer. ❌ Vendor lock-in, latence potentielle, complexité pour les traitements lourds.
- **Option C (Kubernetes)** : ✅ Portabilité, scalabilité, pas de vendor lock-in. ❌ Complexité de mise en œuvre, nécessite des compétences DevOps avancées.
- **Recommandation** : Option B (Serverless) pour démarrer, puis migration progressive vers Option C quand l'activité se développe. Dans le contexte africain : le serverless limite les coûts initiaux (facturation à l'usage), réduit le besoin en compétences infrastructure, et fonctionne malgré une connectivité variable grâce aux CDN et aux architectures edge.

</details>

---

*Bonne chance à tous !*
