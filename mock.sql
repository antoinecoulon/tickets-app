-- Insertion de données dans la table core_ticket
INSERT INTO core_ticket (id, titre, description, statut, priorite, created_at, updated_at, agent_id, client_id)
VALUES
    (1, 'Problème de connexion', 'Impossible de se connecter au système.', 'Ouvert', 'Haute', '2023-10-01 08:00:00', '2023-10-01 08:00:00', 1, 1),
    (2, 'Demande de renseignement', 'Besoin d''informations sur les services.', 'Fermé', 'Basse', '2023-10-02 09:00:00', '2023-10-03 10:00:00', 2, 2),
    (3, 'Erreur sur la facture', 'La facture du mois dernier semble incorrecte.', 'En cours', 'Moyenne', '2023-10-03 10:00:00', '2023-10-04 11:00:00', 3, 3);

-- Insertion de données dans la table core_message
INSERT INTO core_message (id, contenu, created_at, auteur_id, ticket_id)
VALUES
    (1, 'Bonjour, je rencontre un problème de connexion.', '2023-10-01 08:05:00', 1, 1),
    (2, 'Merci pour votre message, nous allons vérifier cela.', '2023-10-01 08:10:00', 1, 1),
    (3, 'Je souhaite obtenir des renseignements sur vos services.', '2023-10-02 09:05:00', 2, 2),
    (4, 'Voici les informations demandées.', '2023-10-02 09:10:00', 2, 2),
    (5, 'Il semble y avoir une erreur sur ma facture.', '2023-10-03 10:05:00', 3, 3),
    (6, 'Nous allons examiner cela et revenir vers vous.', '2023-10-03 10:10:00', 3, 3);