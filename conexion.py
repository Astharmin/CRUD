from loggerBase import log
from psycopg2 import pool
import sys


class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool (cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creacion de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexcion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexcion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexcion()
    conexion3 = Conexion.obtenerConexcion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexcion()
    conexion5 = Conexion.obtenerConexcion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexcion()
