from django.db import models

# Modelos Principales            
class Disa(models.Model):
    cod_disa = models.CharField('cod_disa', max_length=2, null=True, blank=True)
    desc_disa = models.CharField('desc_disa', max_length=40, null=True, blank=True) 
    def __str__(self):
        return self.desc_disa            

class Red(models.Model):
    nombre_red = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="", null=True, blank=True)
    cod_enlace = models.CharField(max_length=10, default="", null=True, blank=True)
    disa = models.ForeignKey(Disa, on_delete=models.CASCADE, related_name='disas', null=True, blank=True)    
    def __str__(self):
        return self.nombre_red
    
class Microred(models.Model):
    nombre_microred = models.CharField(max_length=100,null=True, blank=True)
    cod_mic = models.CharField(max_length=10, default="",null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="",null=True, blank=True)
    cod_enlace_mr = models.CharField(max_length=10, default="",null=True, blank=True)
    cod_enlace_r = models.CharField(max_length=10, default="",null=True, blank=True)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, related_name='redes',null=True, blank=True)  
    def __str__(self):
        return self.nombre_microred
    
class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=100, null=True, blank=True)
    codigo_unico = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_enlace_mr = models.CharField(max_length=10, default="",null=True, blank=True)
    id_red = models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    microred = models.ForeignKey(Microred, on_delete=models.CASCADE, related_name='microredes', null=True, blank=True)  
    def __str__(self):
        return self.nombre_establecimiento
        
class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.nombre_provincia
        
class Distrito(models.Model):
    nombre_distrito = models.CharField(max_length=100, null=True, blank=True)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='provincias', null=True, blank=True)  
    def __str__(self):
        return self.nombre_distrito
    
class Anio(models.Model):
    nombre_anio = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre_anio
    
class Mes(models.Model):
    nombre_mes = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre_mes
        
class Tipo_reporte(models.Model):
    nombre_tipo_reporte = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_tipo_reporte
    
# Modelos reportes
class rpt_metales(models.Model):
    cod_estab = models.CharField('cod_estab', max_length=9, null=True, blank=True)
    anio = models.CharField('anio', max_length=4, null=True, blank=True) 
    mes = models.CharField('mes', max_length=4, null=True, blank=True) 
    fichafam = models.CharField('fichafam', max_length=4, null=True, blank=True)
    sexo = models.CharField('sexo', max_length=4, null=True, blank=True)
    establec = models.CharField('establec', max_length=4, null=True, blank=True)
    servicio = models.CharField('servicio', max_length=4, null=True, blank=True)
    id_cita = models.CharField('id_cita', max_length=40, null=True, blank=True)
    fecha_atendido = models.CharField('fecha_atendido', max_length=40, null=True, blank=True)
    num_doc = models.CharField('num_doc', max_length=40, null=True, blank=True)
    cod_item = models.CharField('cod_item', max_length=40, null=True, blank=True)
    valor_lab = models.CharField('valor_lab', max_length=40, null=True, blank=True)
    edad = models.CharField('edad', max_length=40, null=True, blank=True)
    ubigeo = models.CharField('ubigeo', max_length=40, null=True, blank=True)
    codpsal = models.CharField('codpsal', max_length=40, null=True, blank=True)
    cod_prof = models.CharField('cod_prof', max_length=40, null=True, blank=True)
    tipo_estab = models.CharField('tipo_estab', max_length=40, null=True, blank=True)
    
    def __str__(self):
        return self.cod_estab

# Modelos reportes
class nominal_trama_nuevo(models.Model):
    Id_Cita = models.CharField('Id_Cita', max_length=50, null=True, blank=True)
    Anio = models.CharField('Anio', max_length=4, null=True, blank=True)
    Mes = models.CharField('Mes', max_length=2, null=True, blank=True)
    Dia = models.CharField('Dia', max_length=2, null=True, blank=True)
    Fecha_Atencion =  models.DateField('Fecha_Atencion', max_length=20, null=True, blank=True)
    Lote = models.CharField('Lote', max_length=3, null=True, blank=True)
    Num_Pag = models.IntegerField('Num_Pag', null=True, blank=True)
    Num_Reg = models.IntegerField('Num_Reg', null=True, blank=True)
    Id_Ups = models.CharField('Id_Ups', max_length=6, null=True, blank=True)
    Id_Establecimiento = models.IntegerField('Id_Establecimiento', null=True, blank=True)
    Id_Paciente = models.CharField('Id_Paciente', max_length=50, null=True, blank=True)
    Id_Personal = models.CharField('Id_Personal', max_length=50, null=True, blank=True)
    Id_Registrador = models.CharField('Id_Registrador', max_length=50, null=True, blank=True)
    Id_Financiador = models.CharField('Id_Financiador', max_length=2, null=True, blank=True)
    Id_Condicion_Establecimiento = models.CharField('Id_Condicion_Establecimiento', max_length=1, null=True, blank=True)
    Id_Condicion_Servicio = models.CharField('Id_Condicion_Servicio', max_length=1, null=True, blank=True)
    Edad_Reg = models.IntegerField('Edad_Reg', null=True, blank=True)
    Tipo_Edad = models.CharField('Tipo_Edad', max_length=1, null=True, blank=True)
    Anio_Actual_Paciente = models.IntegerField('Anio_Actual_Paciente', null=True, blank=True)
    Mes_Actual_Paciente = models.IntegerField('Mes_Actual_Paciente', null=True, blank=True)
    Dia_Actual_Paciente = models.IntegerField('Dia_Actual_Paciente', null=True, blank=True)
    Id_Turno = models.CharField('Id_Turno', max_length=1, null=True, blank=True)
    Codigo_Item = models.CharField('Codigo_Item', max_length=15, null=True, blank=True)
    Tipo_Diagnostico = models.CharField('Tipo_Diagnostico', max_length=1, null=True, blank=True)
    Valor_Lab = models.CharField('Valor_Lab', max_length=50, null=True, blank=True)
    Id_Correlativo_Item = models.IntegerField('Id_Correlativo_Item', null=True, blank=True)
    Id_Correlativo_Lab = models.IntegerField('Id_Correlativo_Lab', null=True, blank=True)
    Peso = models.DecimalField('Peso', max_digits=10, decimal_places=3, null=True, blank=True)
    Talla = models.DecimalField('Talla',max_digits=10, decimal_places=2, null=True, blank=True)
    Hemoglobina = models.DecimalField('Hemoglobina', max_digits=6, decimal_places=2, null=True, blank=True)
    Perimetro_Abdominal = models.DecimalField('Perimetro_Abdominal', max_digits=10, decimal_places=2,null=True, blank=True)
    Perimetro_Cefalico = models.DecimalField('Perimetro_Cefalico', max_digits=10, decimal_places=2, null=True, blank=True)
    Id_Otra_Condicion = models.IntegerField('Id_Otra_Condicion', null=True, blank=True)
    Id_Centro_Poblado = models.CharField('Id_Centro_Poblado', max_length=10, null=True, blank=True)
    Fecha_Ultima_Regla = models.DateField('Fecha_Ultima_Regla', null=True, blank=True)
    Fecha_Solicitud_Hb = models.DateField('Fecha_Solicitud_Hb', null=True, blank=True)
    Fecha_Resultado_Hb = models.DateField('Fecha_Resultado_Hb', null=True, blank=True)
    Fecha_Registro = models.DateTimeField('Fecha_Registro', null=True, blank=True)
    Fecha_Modificacion = models.DateTimeField('Fecha_Modificacion', null=True, blank=True)
    Id_Pais = models.CharField('Id_Pais', max_length=3, null=True, blank=True)
