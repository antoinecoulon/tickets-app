-- 🧾 Création de 20 tickets pour les clients 2 à 4, certains assignés à agents 5 à 7
INSERT INTO core_ticket (
    titre, description, statut, priorite,
    created_at, updated_at, client_id, agent_id
)
VALUES
-- Tickets avec agent assigné
('Connexion impossible', 'Je ne peux plus me connecter à mon compte.', 'ouvert', 'haute', NOW(), NOW(), 2, 5),
('Erreur serveur', 'Erreur 500 lors de l’envoi du formulaire.', 'en_cours', 'moyenne', NOW(), NOW(), 3, 5),
('Mot de passe oublié', 'Le lien de réinitialisation ne fonctionne pas.', 'resolu', 'basse', NOW(), NOW(), 4, 6),
('Affichage cassé', 'Le tableau de bord est mal aligné.', 'ouvert', 'moyenne', NOW(), NOW(), 2, 6),
('Notifications inactives', 'Je ne reçois plus d’alertes.', 'ferme', 'haute', NOW(), NOW(), 3, 7),
('Problème de langue', 'La langue par défaut change seule.', 'ouvert', 'basse', NOW(), NOW(), 4, 7),
('Impossible de supprimer', 'Erreur lors de la suppression d’un élément.', 'resolu', 'haute', NOW(), NOW(), 2, 5),
('Déconnexions fréquentes', 'Je suis déconnecté automatiquement.', 'en_cours', 'moyenne', NOW(), NOW(), 3, 6),
('Champ non valide', 'Un champ obligatoire n’est pas reconnu.', 'ouvert', 'basse', NOW(), NOW(), 4, 7),
('Téléversement échoue', 'Upload de fichier bloque à 99%.', 'resolu', 'moyenne', NOW(), NOW(), 2, 6),

-- Tickets non assignés
('Erreur de profil', 'Impossible de modifier mes infos.', 'ouvert', 'basse', NOW(), NOW(), 3, NULL),
('Lien mort', 'Le lien de la FAQ ne fonctionne pas.', 'en_cours', 'moyenne', NOW(), NOW(), 4, NULL),
('Affichage vide', 'Une page apparaît blanche.', 'ouvert', 'haute', NOW(), NOW(), 2, NULL),
('Erreur aléatoire', 'Parfois l’app plante sans raison.', 'ouvert', 'moyenne', NOW(), NOW(), 3, NULL),
('Chargement infini', 'Le spinner tourne sans fin.', 'ferme', 'haute', NOW(), NOW(), 4, NULL),
('Impossible de filtrer', 'La recherche ne filtre rien.', 'ouvert', 'basse', NOW(), NOW(), 2, NULL),
('Aucune réponse', 'J’ai ouvert un ticket il y a 3 jours.', 'en_cours', 'moyenne', NOW(), NOW(), 3, NULL),
('Champ grisé', 'Je ne peux pas éditer un champ.', 'resolu', 'basse', NOW(), NOW(), 4, NULL),
('Erreur inconnue', 'Un message d’erreur s’affiche sans explication.', 'ouvert', 'haute', NOW(), NOW(), 2, NULL),
('Export échoue', 'Téléchargement du rapport impossible.', 'ouvert', 'moyenne', NOW(), NOW(), 3, NULL);

-- 💬 Messages sur quelques tickets
INSERT INTO core_message (
    contenu, created_at, auteur_id, ticket_id
)
VALUES
('Bonjour, je rencontre un problème avec la connexion.', NOW(), 2, 1),
('Merci, j’ai bien reçu une réponse.', NOW(), 5, 1),
('J’ai réessayé, mais ça bloque toujours.', NOW(), 2, 1),

('Pouvez-vous regarder l’erreur serveur ?', NOW(), 3, 2),
('Problème identifié, nous investiguons.', NOW(), 5, 2),

('Lien changé, le nouveau fonctionne.', NOW(), 4, 3),

('Toujours pas d’alertes reçues.', NOW(), 3, 5),
('Je vais vérifier les paramètres.', NOW(), 7, 5);

-- ✅ Mise à jour des séquences (PostgreSQL only)
SELECT setval('core_ticket_id_seq', (SELECT MAX(id) FROM core_ticket));
SELECT setval('core_message_id_seq', (SELECT MAX(id) FROM core_message));
