from conexion import Conexion
from Persona import Persona
from loggerBase import log
from CursoPool import CursorPool


class PersonaDAO:

    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar (cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona Actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto Eliminado: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    #Insertar un registro
    # persona1 = Persona(nombre='Gerhad', apellido='D Rivia', email='GdRivia@mail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas Insertadas: {personas_insertadas}')

    # Actualizar un registro
    # persona1 = Persona(16, 'Gerhad', 'D Rivia', 'GDrivia@mail.com')
    # personasActualizados = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas Actualizadas : {personasActualizados}')

    # eliminar un registro
    # persona1 = Persona(id_persona=17)
    # personaseliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'personas eliminadas: {personaseliminadas}')

    #Seleccionar Objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)