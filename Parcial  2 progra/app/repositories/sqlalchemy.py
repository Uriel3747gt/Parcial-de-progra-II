def count_by_status(self) -> dict[str, int]:
        """Devuelve un diccionario con el conteo de tickets agrupados por su estado."""
        stmt = select(TicketORM.status, func.count()).group_by(TicketORM.status)
        rows = self._session.execute(stmt).all()
        return {status: count for status, count in rows}