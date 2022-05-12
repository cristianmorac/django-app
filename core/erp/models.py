from django.db import models
from datetime import datetime
from core.erp.choices import gender_choices

#convertir el objeto a tipo diccionario
from django.forms import model_to_dict
# Create your models here.

class  Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', null=True,unique=True)
    description = models.TextField(max_length=150, verbose_name='Descripción',default='')
    def __str__(self):
        ''' 
        Se puede escribir tambien asi:
        return 'Nro: {} / Nombre: {}.format(self.id, self.name)
        '''
        return self.name 

    # metodo para devolver un diccionario con todos los atributos
    def toJson(self):
        ''' 
        una opcion
        item = {'id':self.id,'name':self.name} '''
        item = model_to_dict(self   )
        return item
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']
     
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre',unique=True)
    cate = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00,max_digits=3,decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']

class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    surname = models.CharField(max_length=150, verbose_name='Apellido')
    dni = models.CharField(max_length=12,unique=True,verbose_name='DNI')
    birthday = models.DateField(default=datetime.now,verbose_name='Fecha Nacimiento')
    address = models.CharField(max_length=150,null=True,blank=True,verbose_name='Direccion')
    sexo = models.CharField(max_length=10, choices=gender_choices,default='F',verbose_name='Genero')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Client,on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00,max_digits=3,decimal_places=2)
    iva = models.DecimalField(default=0.00,max_digits=3,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=3,decimal_places=2)

    def __str__(self):
        return self.cli.name
    
    class Meta:
        verbose_name ='Venta'
        verbose_name_plural ='Ventas'
        db_table='Venta'
        ordering = ['id']

class DetSale(models.Model):
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00,max_digits=2,decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00,max_digits=2,decimal_places=2)

    def __str__(self):
        self.prod.name
    
    class Meta:
        verbose_name ='Factura'
        verbose_name_plural ='Facturas'
        db_table='Factura'
        ordering = ['id']