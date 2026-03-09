/**
 * QCM très corsé — Cours "Challenge Innovation"
 * 30 questions couvrant les 3 modules du cours
 * Chaque question a 4 options avec une seule bonne réponse
 */

const quizData = [
  // ===== MODULE I : INTRODUCTION AU CHALLENGE INNOVATION (Q1-Q10) =====
  {
    id: 1,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Selon le cours, quelle est la définition correcte de l'innovation ?",
    options: [
      "Une invention technologique spectaculaire qui impressionne la communauté scientifique",
      "Une solution nouvelle ou améliorée qui répond efficacement à un besoin réel, dans un contexte donné, et qui est adoptée par ses utilisateurs",
      "Toute création d'un nouvel algorithme ou logiciel, indépendamment de son utilisation",
      "Un produit commercialisé avec succès sur le marché international",
    ],
    correct: 1,
    explanation:
      "Le cours définit l'innovation comme « une solution nouvelle ou améliorée qui répond efficacement à un besoin réel, dans un contexte donné, et qui est adoptée par ses utilisateurs ». L'adoption et l'utilité sont essentielles.",
  },
  {
    id: 2,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Pourquoi une solution techniquement avancée mais inutilisée n'est-elle PAS considérée comme une innovation selon le cours ?",
    options: [
      "Parce qu'elle n'est pas brevetée",
      "Parce qu'elle est trop complexe pour être comprise",
      "Parce que l'innovation exige l'adoption par les utilisateurs et un impact réel",
      "Parce qu'elle ne génère pas de profit",
    ],
    correct: 2,
    explanation:
      "Le cours insiste : « Une solution techniquement avancée mais inutilisée n'est pas une innovation. » L'adoption par les utilisateurs et la réponse à un besoin réel sont les critères fondamentaux.",
  },
  {
    id: 3,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Qu'est-ce qui distingue fondamentalement un challenge innovation d'un projet académique classique ?",
    options: [
      "Le challenge exige un code source plus complexe et mieux documenté",
      "Le challenge demande de partir d'un besoin réel, de justifier ses choix par leur valeur ajoutée et de prendre en compte les contraintes du terrain",
      "Le challenge se fait individuellement sans évaluation devant un jury",
      "Le challenge n'impose aucune contrainte de temps",
    ],
    correct: 1,
    explanation:
      "Le challenge innovation exige de : partir d'un besoin réel plutôt que d'une technologie imposée ; justifier les choix techniques par leur valeur ajoutée ; prendre en compte les contraintes du terrain ; produire une solution crédible.",
  },
  {
    id: 4,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Parmi les projets primés au Hackathon 226-Plus au Burkina Faso, lequel est un dispositif de détection et d'alerte d'incendies ?",
    options: ["Blood Alert", "SAFE", "Fire Off", "AquaIA"],
    correct: 2,
    explanation:
      "Fire Off est le dispositif de détection et d'alerte d'incendies primé lors du Hackathon 226-Plus. Blood Alert est une plateforme de mise en relation de donneurs de sang. SAFE est une solution d'innovation libre.",
  },
  {
    id: 5,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Selon le cours, quelle est la posture attendue d'un futur ingénieur dans le cadre de ce cours ?",
    options: [
      "Un expert technique spécialisé dans un seul domaine",
      "Un ingénieur-innovateur, apte à créer des solutions utiles et impactantes",
      "Un chercheur académique publiant des articles scientifiques",
      "Un entrepreneur créant sa propre startup",
    ],
    correct: 1,
    explanation:
      "Le cours précise qu'il aide à « dépasser l'approche technique pour adopter une posture d'ingénieur-innovateur, apte à créer des solutions utiles et impactantes ».",
  },
  {
    id: 6,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "L'équilibre que le cours enseigne à rechercher se situe entre quels éléments ?",
    options: [
      "Rapidité, coût et complexité",
      "Utilité, faisabilité et impact",
      "Performance, esthétique et rentabilité",
      "Technologie, marketing et finance",
    ],
    correct: 1,
    explanation:
      "Le cours indique : « vous apprendrez donc à rechercher l'équilibre entre utilité, faisabilité et impact. »",
  },
  {
    id: 7,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Pourquoi le cours insiste-t-il sur le travail en équipe dans l'innovation ?",
    options: [
      "Parce que c'est une exigence administrative de l'institut",
      "Parce que l'innovation est un processus collectif et qu'aucun projet d'innovation ne peut aboutir sans une collaboration efficace",
      "Parce que le travail individuel est interdit dans les challenges",
      "Parce que les entreprises recrutent uniquement des profils extravertis",
    ],
    correct: 1,
    explanation:
      "Le cours affirme : « L'innovation est un processus collectif. Aucun projet d'innovation ne peut aboutir sans une collaboration efficace entre les membres de l'équipe. »",
  },
  {
    id: 8,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Selon le cours, quel est l'objectif final attendu des étudiants à la fin du cours ?",
    options: [
      "Maîtriser un langage de programmation avancé",
      "Transformer une problématique réelle en une solution technologique innovante, faisable et à impact",
      "Rédiger un mémoire de recherche académique",
      "Créer une entreprise technologique rentable",
    ],
    correct: 1,
    explanation:
      "L'objectif global est de « rendre capables de transformer une problématique réelle en une solution technologique innovante, faisable et à impact ».",
  },
  {
    id: 9,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Quels sont les secteurs mentionnés comme terrains d'application privilégiés pour l'innovation au Burkina Faso ?",
    options: [
      "Finance, immobilier, tourisme de luxe",
      "Agriculture, eau, énergie, santé, éducation et services urbains",
      "Aérospatiale, nucléaire et biotechnologie de pointe",
      "Cryptomonnaie, métavers et réalité virtuelle",
    ],
    correct: 1,
    explanation:
      "Le cours cite : « Les problématiques locales liées à l'agriculture, à l'eau, à l'énergie, à la santé, à l'éducation ou aux services urbains constituent des terrains d'application privilégiés. »",
  },
  {
    id: 10,
    module: "Module I — Introduction au Challenge Innovation",
    question:
      "Selon le cours, quelle affirmation résume le mieux le rôle de la technologie pour un ingénieur innovateur ?",
    options: [
      "La technologie est la finalité principale de tout projet d'innovation",
      "La technologie est un moyen, pas une fin ; un bon ingénieur pose les bonnes questions avant de coder",
      "La technologie la plus avancée est toujours la meilleure solution",
      "La technologie doit être complexe pour être crédible",
    ],
    correct: 1,
    explanation:
      "Le cours enseigne que « La technologie est un moyen, pas une fin ; Un bon ingénieur pose les bonnes questions avant de coder. »",
  },

  // ===== MODULE II : MÉTHODOLOGIES D'INNOVATION (Q11-Q22) =====
  {
    id: 11,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Pourquoi de nombreux projets innovants échouent-ils, selon le cours ?",
    options: [
      "Par manque de financement exclusivement",
      "Non pas par manque de compétences techniques, mais parce que le problème n'est pas bien compris",
      "Par excès de créativité dans la phase de conception",
      "Par un usage excessif du Design Thinking",
    ],
    correct: 1,
    explanation:
      "Le cours explique que « De nombreux projets innovants échouent non pas par manque de compétences techniques, mais parce que le problème n'est pas bien compris. »",
  },
  {
    id: 12,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Le Design Thinking a été développé dans quelle institution et à quelle période ?",
    options: [
      "MIT dans les années 2000",
      "Stanford dans les années 80",
      "Harvard dans les années 90",
      "Oxford dans les années 70",
    ],
    correct: 1,
    explanation:
      "Le cours précise : « Cette approche développée à Stanford dans les années 80 a pour but d'appliquer la démarche d'un designer pour répondre à un problème. »",
  },
  {
    id: 13,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Quels sont les quatre principes fondamentaux du Design Thinking selon le cours ?",
    options: [
      "Analyse, planification, exécution, évaluation",
      "Empathie, créativité, itération et centrage sur l'utilisateur",
      "Spécification, codage, test, déploiement",
      "Rentabilité, rapidité, scalabilité, automatisation",
    ],
    correct: 1,
    explanation:
      "Le cours résume : « Le Design Thinking allie empathie, créativité et itération pour résoudre les problèmes de manière humaine et innovante » avec un processus centré sur l'utilisateur.",
  },
  {
    id: 14,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Dans le Double Diamant du Design Thinking, que représente la phase 'DÉCOUVRIR' ?",
    options: [
      "Convergence : réduire les idées à une seule solution",
      "Divergence : explorer largement la situation pour comprendre les utilisateurs, le contexte et les causes possibles",
      "Prototyper et tester la solution finale",
      "Définir les spécifications techniques du logiciel",
    ],
    correct: 1,
    explanation:
      "La phase Découvrir est une phase de divergence dont l'objectif est « explorer largement la situation pour comprendre les utilisateurs, le contexte et les causes possibles du problème ».",
  },
  {
    id: 15,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Quel outil est utilisé dans la phase DÉFINIR pour reformuler le problème sous forme de question ?",
    options: [
      "SCAMPER",
      "Customer Journey Map",
      "How Might We (HMW) — « Comment pourrions-nous… ? »",
      "Mind Mapping",
    ],
    correct: 2,
    explanation:
      "Le How Might We (HMW) est l'outil de la phase Définir qui permet de formuler le problème sous forme de question : « Comment pourrions-nous… ? »",
  },
  {
    id: 16,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Que signifie l'acronyme SCAMPER dans le contexte de l'idéation ?",
    options: [
      "Stratégie, Conception, Analyse, Mesure, Plan, Évaluation, Résultat",
      "Substituer, Combiner, Adapter, Modifier, Produire, Éliminer, Réorganiser",
      "Simplifier, Coder, Automatiser, Modéliser, Programmer, Exécuter, Réparer",
      "Sélectionner, Classifier, Annoter, Modéliser, Prédire, Entraîner, Raffiner",
    ],
    correct: 1,
    explanation:
      "SCAMPER signifie : Substituer, Combiner, Adapter, Modifier, Produire, Éliminer et Réorganiser. C'est un outil de la phase d'Idéation.",
  },
  {
    id: 17,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Quel est le principe clé de la phase 'Prototyper & Tester' selon le cours ?",
    options: [
      "On teste pour confirmer que notre idée est la meilleure",
      "On ne teste pas pour valider son idée, on teste pour apprendre",
      "Le prototype doit être parfait avant de le montrer aux utilisateurs",
      "Les tests utilisateurs ne sont pas nécessaires si la technologie fonctionne",
    ],
    correct: 1,
    explanation:
      "Le cours insiste sur le principe clé : « On ne teste pas pour valider son idée, on teste pour apprendre. »",
  },
  {
    id: 18,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Quel outil permet de regrouper les observations par thèmes dans la phase DÉFINIR ?",
    options: [
      "Brainstorming structuré",
      "Affinity Mapping",
      "SCAMPER",
      "Elevator Pitch",
    ],
    correct: 1,
    explanation:
      "L'Affinity Mapping est l'outil de la phase Définir qui permet de « regrouper les idées / observations par thèmes ».",
  },
  {
    id: 19,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "L'approche Problem-Driven / Outcome-Driven Innovation vous amène à passer de quelle logique à quelle autre ?",
    options: [
      "D'une logique de coût à une logique de profit",
      "D'une logique de moyens à une logique de résultats ; d'une logique technologique à une logique de valeur",
      "D'une logique académique à une logique entrepreneuriale",
      "D'une logique individuelle à une logique collective",
    ],
    correct: 1,
    explanation:
      "Le cours explique qu'on passe « d'une logique de moyens à une logique de résultats ; d'une logique technologique à une logique de valeur ; d'un raisonnement centré sur l'outil à un raisonnement centré sur l'impact ».",
  },
  {
    id: 20,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Comment le cours reformule-t-il l'exemple « Créer une application basée sur l'IA pour l'agriculture » de manière Problem-Driven ?",
    options: [
      "Développer un algorithme de deep learning pour l'agriculture de précision",
      "Réduire les pertes agricoles liées au manque d'information climatique",
      "Construire une plateforme big data pour les agriculteurs",
      "Automatiser complètement la chaîne de production agricole",
    ],
    correct: 1,
    explanation:
      "La reformulation Problem-Driven est : « Réduire les pertes agricoles liées au manque d'information climatique ». Cela élargit les options techniques et autorise des solutions plus simples.",
  },
  {
    id: 21,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Quels sont les avantages de la reformulation Problem-Driven mentionnés dans le cours ?",
    options: [
      "Elle rend le code plus performant et le déploiement plus rapide",
      "Elle élargit les options techniques possibles, autorise des solutions plus simples et facilite l'adaptation aux contraintes locales",
      "Elle garantit un financement plus important des investisseurs",
      "Elle élimine le besoin de prototypage et de tests utilisateurs",
    ],
    correct: 1,
    explanation:
      "La reformulation « élargit les options techniques possibles ; autorise des solutions plus simples et plus robustes ; facilite l'adaptation aux contraintes locales (coût, connectivité, énergie) ».",
  },
  {
    id: 22,
    module: "Module II — Méthodologies d'Innovation",
    question:
      "Comment le Design Thinking et l'approche Problem-Driven s'articulent-ils dans le Challenge Innovation ?",
    options: [
      "Ils sont utilisés séparément pour des projets différents",
      "Le Design Thinking remplace l'approche Problem-Driven",
      "Le Design Thinking permet de comprendre le terrain et formuler le problème ; l'approche Problem-Driven clarifie la valeur recherchée et oriente les choix techniques",
      "L'approche Problem-Driven est utilisée en premier, puis le Design Thinking pour le prototypage",
    ],
    correct: 2,
    explanation:
      "Le cours explique : « Le Design Thinking permet de comprendre le terrain, les utilisateurs et de formuler correctement le problème ; l'approche Problem-Driven permet de clarifier la valeur recherchée et d'orienter les choix techniques. »",
  },

  // ===== MODULE III : PRÉPARATION ET PITCH DU PROJET (Q23-Q30) =====
  {
    id: 23,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Selon le cours, la présentation d'un projet innovant n'est pas un simple exercice académique, mais plutôt :",
    options: [
      "Une démonstration technique approfondie",
      "Un outil de décision",
      "Un argumentaire de vente",
      "Un résumé de la documentation technique",
    ],
    correct: 1,
    explanation:
      "Le cours précise : « La présentation d'un projet n'est donc pas un simple exercice académique, mais un outil de décision. »",
  },
  {
    id: 24,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Quels sont les quatre éléments qu'un décideur doit comprendre clairement après votre présentation ?",
    options: [
      "L'algorithme, le langage de programmation, l'architecture et la base de données",
      "Le problème adressé, la solution proposée, la valeur créée et la crédibilité technique et opérationnelle",
      "Le budget, le calendrier, l'équipe et les partenaires",
      "Le marché cible, les concurrents, le business model et la stratégie marketing",
    ],
    correct: 1,
    explanation:
      "Le décideur doit comprendre : « le problème que vous adressez ; la solution que vous proposez ; la valeur créée ; la crédibilité technique et opérationnelle du projet ».",
  },
  {
    id: 25,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Pourquoi le storytelling professionnel commence-t-il par une situation réelle ?",
    options: [
      "Pour rendre la présentation plus longue et impressionnante",
      "Pour capter l'attention, montrer la compréhension du terrain et donner du sens à la solution",
      "Pour remplacer les données techniques par des anecdotes",
      "Pour éviter de parler de la technologie utilisée",
    ],
    correct: 1,
    explanation:
      "Le storytelling professionnel « permet de capter l'attention ; de montrer que vous comprenez le terrain ; de donner du sens à la solution ».",
  },
  {
    id: 26,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Selon le cours, quel est le signe de professionnalisme dans la présentation technique ?",
    options: [
      "Montrer le code source complet et détaillé",
      "Utiliser un maximum de termes techniques complexes",
      "La maîtrise de la complexité, et non son étalage",
      "Présenter toutes les alternatives techniques évaluées",
    ],
    correct: 2,
    explanation:
      "Le cours affirme : « La maîtrise de la complexité, et non son étalage, est un signe de professionnalisme. »",
  },
  {
    id: 27,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Qu'est-ce que l'elevator pitch et quels sont ses trois éléments essentiels ?",
    options: [
      "Une présentation de 30 minutes couvrant le problème, la solution et le business plan",
      "Un exercice rapide permettant de comprendre immédiatement le problème adressé, la solution proposée et la valeur créée",
      "Un document écrit résumant les spécifications techniques du projet",
      "Une démonstration du prototype devant un investisseur",
    ],
    correct: 1,
    explanation:
      "L'elevator pitch est un exercice rapide (30 secondes) qui « doit permettre de comprendre immédiatement : le problème que vous adressez ; la solution que vous proposez ; la valeur créée ».",
  },
  {
    id: 28,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Parmi les éléments suivants, lequel est à ÉVITER dans les supports visuels selon le cours ?",
    options: [
      "Schémas simples et diagrammes de fonctionnement",
      "Captures du prototype et quelques chiffres clés",
      "Longs textes et code source",
      "Visuels d'aide à la décision",
    ],
    correct: 2,
    explanation:
      "À éviter : « longs textes ; code source ; détails techniques inutiles ». À privilégier : schémas simples, diagrammes de fonctionnement, captures du prototype, quelques chiffres clés.",
  },
  {
    id: 29,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Après votre présentation, un décideur cherchera à comprendre plusieurs aspects. Lequel N'EN fait PAS partie selon le cours ?",
    options: [
      "La faisabilité réelle et les limites du prototype",
      "Les coûts et contraintes ainsi que le déploiement dans le contexte burkinabè",
      "Le détail complet du code source et de l'architecture logicielle",
      "L'adoption par les utilisateurs",
    ],
    correct: 2,
    explanation:
      "Le décideur cherche à comprendre : la faisabilité réelle, les limites, les coûts et contraintes, le déploiement dans le contexte burkinabè, et l'adoption par les utilisateurs. Le code source n'en fait pas partie.",
  },
  {
    id: 30,
    module: "Module III — Préparation et Pitch du Projet",
    question:
      "Selon le cours, comment renforce-t-on sa crédibilité face à un décideur ?",
    options: [
      "En affirmant que le projet n'a aucune limite",
      "En utilisant un jargon technique le plus complexe possible",
      "En reconnaissant une limite et en proposant une amélioration",
      "En évitant les questions difficiles du jury",
    ],
    correct: 2,
    explanation:
      "Le cours conseille : « Reconnaître une limite et proposer une amélioration renforce votre crédibilité. » Il faut préparer des « réponses honnêtes, structurées et réalistes ».",
  },
];

export default quizData;
