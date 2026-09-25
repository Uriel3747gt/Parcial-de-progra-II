
-- EJERCICIO 4: SQL e integridad referencial (HelpDesk EDU)

-- a) Tickets abiertos con el nombre del solicitante mediante JOIN
SELECT t.id, t.title, u.name AS requester_name 
FROM tickets t 
JOIN users u ON t.requester_id = u.id 
WHERE t.status = 'open';

-- b) Conteo de tickets por técnico asignado, agrupado por id y nombre,
-- con HAVING para excluir conteos cero y orden descendente
SELECT u.id AS technician_id, u.name AS technician_name, COUNT(t.id) AS total_tickets
FROM users u
JOIN tickets t ON u.id = t.assignee_id
GROUP BY u.id, u.name
HAVING COUNT(t.id) > 0
ORDER BY total_tickets DESC;

-- c) Tickets sin comentarios mediante LEFT JOIN
SELECT t.* 
FROM tickets t 
LEFT JOIN comments c ON t.id = c.ticket_id 
WHERE c.id IS NULL;

-- d) Demostración de ON DELETE CASCADE sobre el historial, dentro de BEGIN y ROLLBACK
BEGIN;
-- Mostrar conteo inicial mayor que cero para un ticket con historial (ejemplo: ID 3)
SELECT COUNT(*) AS initial_history_count FROM history WHERE ticket_id = 3;

-- Eliminar el ticket (debe activar el borrado en cascada del historial)
DELETE FROM tickets WHERE id = 3;

-- Mostrar conteo tras el DELETE (debe ser cero)
SELECT COUNT(*) AS count_after_delete FROM history WHERE ticket_id = 3;

-- Revertir los cambios para que la base de datos permanezca intacta
ROLLBACK;

-- Comprobar la recuperación del conteo original tras el ROLLBACK
SELECT COUNT(*) AS restored_history_count FROM history WHERE ticket_id = 3;