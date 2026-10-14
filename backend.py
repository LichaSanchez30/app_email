import sqlite3
import pandas as pd 
import openpyxl as op



class DataBase:
    def __init__(self,nameDB):
        self.conexion = sqlite3.connect(nameDB)
        self.cursor = self.conexion.cursor()

    def crear_tabla(self):
        self.cursor.executescript('''
                                        CREATE TABLE IF NOT EXISTS socios(
                                                                            dni     TEXT PRIMARY KEY,
                                                                            nro_socio TEXT,
                                                                            nombYApe   TEXT,
                                                                            ooss       TEXT);
                                    
                                        CREATE TABLE IF NOT EXISTS prestadores(
                                                                                cuit TEXT PRIMARY KEY,
                                                                                nomYApe TEXT,
                                                                                email   TEXT,
                                                                                especialidad TEXT
                                                                                );
                                        CREATE TABLE IF NOT EXISTS ooss (
                                                                        cuit TEXT PRIMARY KEY,
                                                                        razon_social TEXT,
                                                                        siglas      TEXT,
                                                                        email       TEXT
                                                                        );

                                        CREATE TABLE IF NOT EXISTS facturas (
                                                                        cuit_prestador TEXT,
                                                                        cuit_ooss TEXT NOT NULL,
                                                                        dni_socio TEXT NOT NULL,
                                                                        fecha_fc  TEXT NOT NULL,
                                                                        tipo_comp TEXT CHECK (tipo_comp IN ('A', 'B', 'C')) NOT NULL,
                                                                        pto_vta   TEXT NOT NULL,
                                                                        nro_comp  TEXT NOT NULL,
                                                                        importe   DECIMAL(12,2) NOT NULL,
                                                                        cae       TEXT NOT NULL,
                                                                        periodo   TEXT NOT NULL,
                                                                        PRIMARY KEY (cuit_prestador, tipo_comp, pto_vta, nro_comp),
                                                                        FOREIGN KEY (dni_socio) REFERENCES socios (dni)
                                                                        FOREIGN KEY (cuit_prestador) REFERENCES prestadores (cuit)
                                                                        FOREIGN KEY (cuit_ooss) REFERENCES ooss (cuit)
                                        )
                                        
                                    ''')
    
    def cargar_datos(self,tabla, valores):
        try:
            campos = ','.join(f"{campo}" for campo in valores)
            param = ','.join("?" for _ in valores)
            query = f"INSERT INTO {tabla} ({campos}) VALUES ({param})"
            datos = list(valores.values())
            self.cursor.execute(query, datos)
            self.conexion.commit()
            print('Datos cargados Exitosamente')
        
        except sqlite3.IntegrityError as e:
            return f'Error de integridad: {e}'
        except sqlite3.OperationalError as e:
            return f'Hay un error en la Query: {e}'

    def todos_los(self, tabla):
        try:
            query = f'SELECT * FROM {tabla}'
            self.cursor.execute(query)
            columns = [description[0] for description in self.cursor.description]
            datos = self.cursor.fetchall()
            return datos, columns
        except sqlite3.OperationalError as e:
            return f'La tabla ingresada es incorrecta: {e}'


    def buscar_por_(self,tabla, param, dato):
        try:
            busqueda = f"SELECT * FROM {tabla} WHERE {param} = ?"
            self.cursor.execute(busqueda, (dato,))
            resultado = self.cursor.fetchone()
            columns = [description[0] for description in self.cursor.description]
            if resultado:
                return resultado, columns
            else:
                return None , f'No hay datos para {param}: {dato}'
        except sqlite3.OperationalError as e:
            return f'Error en la busqueda: {e}'

    def actualizarDatos(self, tabla, datoBusqueda, colBusqueda, valores):
        campos = ','.join(f'{columna} = ?' for columna in valores)
        query = f'UPDATE {tabla} SET {campos} WHERE {colBusqueda} = ?'
        parametros = list(valores.values())
        parametros.append(datoBusqueda)
        self.cursor.execute(query, parametros)
        self.conexion.commit()

        if self.cursor.rowcount == 1:
            return 'Dato actualizado correctamente'
        elif self.cursor.rowcount > 1:
            return f'Se actualizaron correctamente {self.cursor.rowcount} registros'
        else:
            return 'No se encontraron registros para actualizar'


    def borrar_dato(self, tabla, param, valor):
        delete = f'DELETE FROM {tabla} WHERE {param} = ?'
        self.cursor.execute(delete,(valor, ))
        self.conexion.commit()

        if self.cursor.rowcount == 1:
            return 'Dato borrado correctamente'
        elif self.cursor.rowcount > 1:
            return f'Se borraron correctamente {self.cursor.rowcount} registros'
        else:
            return 'No se encontraron registros para borrar'

    

    def close_dataBase(self):
        self.conexion.close()

    

db = DataBase('facturacion.db')
