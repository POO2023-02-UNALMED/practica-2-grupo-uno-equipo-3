from gestorAplicacion.administracion.sucursal import Sucursal

class Opinion:
    todasLasOpiniones = []
    
    def __init__(self, opinionPunt, opinionInt, sucursal):
        self.opinionIntegridad = []
        self.opinionPuntualidad = []
        self.opinionIntegridad.append(opinionInt)
        self.opinionPuntualidad.append(opinionPunt)
        self.sucursal = sucursal
        
        self.sucursal.setOpinionSucursal(self)
        Opinion.todasLasOpiniones.append(self)
    
    def promedioPuntualidad(self):
        suma = sum(self.opinionPuntualidad)
        return suma/ len(self.opinionPuntualidad)
    
    def promedioIntegridad(self):
        suma = sum(self.opinionIntegridad)
        return suma/ len(self.opinionIntegridad)
    
    @staticmethod
    def generar_tabla_sucursales():
        tabla = []
        tabla.append("{:<20} {:>20} {:>20}".format("Sucursales", "Punt. Puntualidad", "Punt. Integridad"))
        tabla.append("------------------------------------------------------------")

        todas_las_sucursales = Sucursal.getTodasLasSucursales() 
        for sucursal in todas_las_sucursales:
            tabla.append("{:<20} {:>15.2f} {:>15.2f}".format(
                sucursal.getNombre(),
                sucursal.getOpinionSucursal().promedioPuntualidad(),
                sucursal.getOpinionSucursal().promedioIntegridad()
            ))

        tabla.append("------------------------------------------------------------")
        return '\n'.join(tabla)
    
    def getOpinionPuntualidad(self):
        return self.opinionPuntualidad
    def setOpinionPuntualidad(self,lista):
        self.opinionPuntualidad = lista
    
    def getOpinionIntegridad(self):
        return self.opinionIntegridad
    def setOpinionIntegridad(self,lista):
        self.opinionIntegridad = lista
    
    def getSucursal(self):
        return self.sucursal
    def setSucursal(self, sucursal):
        self.sucursal = sucursal
    
    @classmethod
    def getTodasLasOpiniones(cls):
        return cls.todasLasOpiniones
    @classmethod
    def setTodasLasOpiniones(cls, lista):
        cls.todasLasOpiniones = lista