-- UPDATES E DELETES
UPDATE patients SET name = 'Lucas Silva Alterado' WHERE user_id = 118;
UPDATE patients SET name = 'Mariana Santos Alterada' WHERE user_id = 119;
UPDATE patients SET name = 'Pedro Oliveira Alterado' WHERE user_id = 120;
UPDATE patients SET name = 'Ana Souza Alterada' WHERE user_id = 121;
UPDATE patients SET name = 'Carlos Pereira Alterado' WHERE user_id = 122;
UPDATE patients SET name = 'Julia Almeida Alterada' WHERE user_id = 123;
UPDATE patients SET name = 'Marcos Costa Alterado' WHERE user_id = 124;
UPDATE patients SET name = 'Beatriz Rodrigues Alterada' WHERE user_id = 125;
UPDATE patients SET name = 'Thiago Martins Alterado' WHERE user_id = 126;
UPDATE patients SET name = 'Fernanda Lima Alterada' WHERE user_id = 127;

DELETE FROM patients WHERE user_id = 118;
DELETE FROM patients WHERE user_id = 119;
DELETE FROM patients WHERE user_id = 120;
DELETE FROM patients WHERE user_id = 121;
DELETE FROM patients WHERE user_id = 122;
DELETE FROM patients WHERE user_id = 123;
DELETE FROM patients WHERE user_id = 124;
DELETE FROM patients WHERE user_id = 125;
DELETE FROM patients WHERE user_id = 126;
DELETE FROM patients WHERE user_id = 127;

DELETE FROM users WHERE id = 118;
DELETE FROM users WHERE id = 119;
DELETE FROM users WHERE id = 120;
DELETE FROM users WHERE id = 121;
DELETE FROM users WHERE id = 122;
DELETE FROM users WHERE id = 123;
DELETE FROM users WHERE id = 124;
DELETE FROM users WHERE id = 125;
DELETE FROM users WHERE id = 126;
DELETE FROM users WHERE id = 127;