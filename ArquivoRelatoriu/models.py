from django.db import models
from custom.models import *
# from django.contrib.gis.db import models as gis_models

# from django.contrib.gis.db import models
class PDFUpload(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Diresaun(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Departamentu(models.Model):
    name = models.CharField(max_length=100, unique=True)
  
    def __str__(self): 
        return self.name 
from django.db import models

class ArquivuRelatoriu(models.Model):
    no_carta = models.CharField(max_length=50)
    data_Arquivu = models.DateField()
    departamento = models.ForeignKey(Departamentu, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=500)
    hato_o_ba = models.CharField(max_length=1000, null=True)
    
    # Field baru untuk upload file PDF
    documento_pdf = models.FileField(upload_to='arquivu_relatoriu_pdfs/', )

    def __str__(self):
        return self.titulo



class Funsionario(models.Model):
    nome = models.CharField(max_length=255)
    sexu = models.CharField( max_length=50, 
        choices=[
            ('Mane', 'Mane'),
            ('Feto', 'Feto'),
        ], 
        default='Mane'
    )
    cargo = models.CharField(max_length=100)
    regime = models.CharField( max_length=50, 
        choices=[
            ('Geral', 'Geral'),
            ('Espesial', 'Espesial'),
        ], 
        default='Geral'
    )
    grau = models.CharField( max_length=50, 
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
        ], 
        default='A'
    )
    level = models.CharField( max_length=50, 
        choices=[
            ('I', 'I'),
            ('II', 'II'),
            ('III', 'III'),
            ('IV', 'IV'),
            ('V', 'V'),
            ('VI', 'VI'),
        ], 
        default='I'
    )
    background = models.CharField(max_length=100, null=True,blank=True)
    scalaun = models.CharField(max_length=100, null=True,blank=True)
    diresaun = models.ForeignKey(Diresaun, on_delete=models.CASCADE,null=True, blank=True)
    departamentu = models.ForeignKey(Departamentu, on_delete=models.CASCADE,null=True, blank=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_entrada = models.DateField()
    image = models.ImageField(upload_to='Funsionariu/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'),('Leave', 'Leave'),
            ('Dismissed', 'Dismissed'),
        ],   
        default='Active'
    )
    
    status_profisaun = models.CharField( max_length=50, 
        choices=[
            ('Kontratadu', 'Kontratadu'),
            ('Permanente', 'Permanente'),
        ], 
        default='Permanente'
    )

    def __str__(self):
        return f"{self.nome} - {self.cargo}"

    class Meta:
        ordering = ['nome']



class KartaEntrada(models.Model):
    remetente = models.CharField(max_length=50, )
    destinatário = models.CharField(max_length=50,)
    no_karta = models.CharField(max_length=50, unique=True)
    data_entrada = models.DateField()
    data_dok = models.DateField()
    no_referensia = models.CharField(max_length=50, blank=True, null=True)
    assunto = models.CharField(max_length=255)
    hato_o_ba = models.CharField(max_length=255)
    husi = models.CharField(max_length=255)
    dokumen = models.FileField(upload_to='Arquivu/KartaSaida/', blank=True, null=True)
    despaixa=models.CharField(max_length=800,blank=True, null=True,)
    is_read=models.BooleanField(default=False,null=True, blank=True)
    def __str__(self):
        return f"Karta Entrada {self.no_karta} - {self.assunto}"

    class Meta:
        ordering = ['-data_entrada']


class KartaSaida(models.Model):
    no_karta = models.CharField(max_length=50, unique=True)
    data_saida = models.DateField()
    data_dok = models.DateField()
    no_referensia = models.CharField(max_length=50, blank=True, null=True)
    assunto = models.CharField(max_length=255)
    hato_o_ba = models.CharField(max_length=255)
    husi = models.CharField(max_length=255) 

    def __str__(self):
        return f"Karta Saida {self.no_karta} - {self.assunto}"

    class Meta:
        ordering = ['-data_saida']



class MapaKlinik(models.Model):
    TIPO_KLINIK = [
        ('Privadu', 'Privadu'),
        ('Publiku', 'Publiku'),
    ]

    naran_klinik = models.CharField(max_length=255, unique=True)
    tipo_klinik = models.CharField(max_length=50, choices=TIPO_KLINIK)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    responsavel = models.CharField(max_length=255, blank=True, null=True)
    aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,blank=True, related_name="VVillage")
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,blank=True, related_name="AAdministrativePost")
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,blank=True,related_name="MMunicipality")
    # lokasi = models.PointField(geography=True, blank=True, null=True)  # Koordinat (longitude, latitude)
    # image = models.ImageField(upload_to='MapaKlinik/', null=True, blank=True)
    data_registu = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.naran_klinik} - {self.municipality}"

    class Meta:
        ordering = ['naran_klinik']
        verbose_name = 'Mapa Klinik'
        verbose_name_plural = 'Mapa Klinik'

class ClienteRaiPoint(models.Model):
    klinika = models.ForeignKey(MapaKlinik, on_delete=models.CASCADE, related_name="clinikLocation")
    latitude = models.CharField(max_length=20, null=True, )
    longitude = models.CharField(max_length=20, null=True,)
    image = models.ImageField(upload_to='MapaKlinik/', null=True, blank=True)

    def __str__(self):
        return f"{self.klinika.naran_klinik} - ({self.latitude}, {self.longitude})"