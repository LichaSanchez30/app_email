import sqlite3


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
                                                                        razon_socia TEXT,
                                                                        siglas      TEXT,
                                                                        email       TEXT
                                                                        );
                                        
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
            resultado = self.cursor.execute(busqueda, (dato,)).fetchone()
            if resultado:
                return resultado
            else:
                return f'No hay datos para {param}: {dato}'
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


    def delete(self, tabla, param, valor):
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



dataBase = DataBase('facturacion.db')


dataBase.close_dataBase()