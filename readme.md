# Kafka + Kafka Streams + Streamlit – Projet de Visites Utilisateurs

## Objectif

Ce projet simule deux utilisateurs visitant un site web. Chaque visite est envoyée à Kafka et traitée par un **Kafka Streams Processor** (Faust).  
Les visites dont la **durée est supérieure à 30 secondes** sont affichées en temps réel sur un **dashboard Streamlit**.

---

##  Architecture
```less
[Simulateur Users] ---> [Kafka Topic: visits] ---> [Kafka Streams Filter]
                                                             |
                                                             v
                                             [Kafka Topic: long_visits]
                                                             |
                                                             v
                                               [Streamlit Dashboard]
```

---

**Composants :**
- **Simulator** : Génère des visites aléatoires d’utilisateurs.
- **Kafka & Zookeeper** : Broker et coordination.
- **Stream Processor (Faust)** : Filtre les visites > 30 sec.
- **Dashboard (Streamlit)** : Affiche les visites filtrées en temps réel.

---

##  Arborescence du projet

```bash
kafka-streamlit-project/
│── docker-compose.yml
│── simulator/
│   └── producer.py
│── stream-processor/
│   └── stream_app.py
│── dashboard/
│   └── app.py
```

---

##  Installation et lancement

1. Cloner le projet

```bash
git clone https://github.com/kenkleven/kafka-streamlit-project.git
cd kafka-streamlit-project
```

2. Lancer tous les services avec Docker Compose

```bash
docker-compose up --build
```

3. Accéder au dashboard Streamlit

```bash
http://localhost:8501
```