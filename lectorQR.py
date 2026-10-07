from pathlib import *
from urllib.parse import *
from base64 import *
from backend import *
import pymupdf
import cv2
import json
import numpy
import binascii

ruta = '/home/licha-sanchez-30/Escritorio/todasLasFC'

dataBase = DataBase('facturacion.db')

#--- GESTIONA TODOS LOS ARCHIVOS PDF CONTENIDOS EN LA CARPERTA PASADA EN URL
class Gestor_archivos:
    def __init__(self, url):
        self._url_carpeta = Path(url)

    def name_archivo(self):
        archivos = self._url_carpeta.iterdir()
        for archivo in archivos:
            print(archivo.stem.split("_"))

#--- GUARDA TODOS LA DIRECCION DE LOS ARCHIVOS PDF EN UN ARRAY Y LOS RETORNA
    def archivos_pdf(self):
        url_pdfs = []
        for pdf in self._url_carpeta.iterdir():
            if pdf.suffix.lower() == '.pdf':
                url_pdfs.append(pdf)
        return url_pdfs


#--- HACE LA LECTURA LOS PDF Y DEVUELVE LA PAGINA QUE CONTIENE EL PDF
class Lector_pdf:
#-- Abro PDF y me quedo con la primer pagina 
    def __init__(self,archivo):
        self.open_pdf = pymupdf.open(archivo)
        self.pagina_ver = self.open_pdf.load_page(0)

#--- DEVUELVE LA PRIMER PAGINA DEL ARCHIVO PDF
    @property
    def pagina_pdf(self):
        return self.pagina_ver

#--- CIERRA EL ARCHIVO PDF PARA QUE NO OCUPE ESPACIO EN LA MEMORIA
    def cerrar_pdf(self):
        self.open_pdf.close()


#--- CONVIERTE EL PDF A IMG
class Convertir_a_Img:
#--- CONVIERTE EL PDF EN UNA IMAGEN 
    def __init__(self, paginaPdf):
        self.render_pdf = paginaPdf.get_pixmap(dpi=300)

#--- RENDERIZA LA IMAGEN DEL PDF Y RETORNA LOS BYTS DE LA IMG
    @property
    def render_img(self):
        img_byte = self.render_pdf.tobytes()
        return img_byte

#--- RENDERIZA LOS BYTS DE LA IMAGEN
    @property
    def de_bytes_img(self):    
        convertir_bit_img = numpy.frombuffer(self.render_img, dtype=numpy.uint8)
        return  convertir_bit_img

#--- LEE EL QR DE LA IMAGEN
class Leer_QR:

#--- TRANSFORMA LA IMAGEN RECIBIDA PARA PODER LEERLA
    def __init__(self, img):
        self.detector_qr = cv2.QRCodeDetector()
        self.arreglo = cv2.imdecode(img, cv2.IMREAD_COLOR)

#--- LEE EL QR DE LA IMAGEN Y RETORNA LA URL DE LA FC
    def leer_qr(self):
        datos_qr = self.detector_qr.detectAndDecode(self.arreglo)
        url = datos_qr[0]
        separar_url = urlparse(url)
        url_dato_fc = parse_qs(separar_url[4])
        return url_dato_fc

#--- PROCESA LOS DATROS DE UNA FACTURA
class Procesar_factura:
    def __init__(self, url):
        self.url = url

#--- DECODIFICA LOS DATOS DE LA URAL, LOS PASA A JSON Y LOS DEVULVE EN UN DICCIONARIO
    def datos_fc(self):
        try:
            decode_byte = b64decode(self.url)
            convertir_a_diccionarios = json.loads(decode_byte)
            return convertir_a_diccionarios
        except json.JSONDecodeError as e:
            return None
        except binascii.Error as e:
            return None       

#--- GESTIONA UN GRAN CUMULO DE FACTURAS.
class Gestionar_todas_las_fc:
    def __init__(self, ruta):
        self.gestor_archivo = Gestor_archivos(ruta) 
        self.errores = {}

#---- PROCESA UN PDF COMPLETO DEVOLVIENDO UN DICIONARIO CON UNA CLAVE['P'] Y SU URL
    def procesar_pdf(self, ruta):
        leerpdf = None
        try: 
            leerpdf = Lector_pdf(ruta)
            pasarImg = Convertir_a_Img(leerpdf.pagina_pdf)
            leerQR = Leer_QR(pasarImg.de_bytes_img)
            return leerQR
        except Exception as e:
            return e
        finally:
            if leerpdf:
                leerpdf.cerrar_pdf()

#---- PROCESA TODOS LOS PDF DE LA CARPETA DE GESTION DE ARCHIVOS Y DEVUELVE LOS DATOS DEL QR
    def procesar_todas(self):
        datos = []
        archivos_url = self.gestor_archivo.archivos_pdf()
        for url in archivos_url:
            qr = self.procesar_pdf(url)
            if isinstance(qr, Exception):
                self.errores[url.name] = str(qr)
                continue

            dato = qr.leer_qr()
            if dato and 'p' in dato and dato['p']:
                factura = Procesar_factura(dato['p'][0])
                datoFc = factura.datos_fc()
                if datoFc:
                    datos.append(datoFc)
                else:
                     self.errores[url.name] = 'Error en factura'
            else:
                 self.errores[url.name] = 'No se pudo leer'
        
        

#--- GUARDA LOS ARCHIVOS CON ERRORES PARA PODER IDENTIFICAR LOS PDF QUE FALLARON
    def verErrores(self):
        return self.errores



class Administrar_datos:
    def __init__(self, datos):
        self.guardar_datos = datos

    def cargarDatos(self,dato):
        self.guardar_datos.append(dato)


    def ver_datos(self):
        return self.guardar_datos


#gestionar_todo = Gestionar_todas_las_fc(ruta)
#todasLasFC = gestionar_todo.procesar_todas()
#administrar = Administrar_datos(todasLasFC)
#
#print(administrar.ver_datos())

gestor_archivo = Gestor_archivos(ruta)

gestor_archivo.name_archivo()

dataBase.close_dataBase()