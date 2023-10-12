from FrancoSolanoApp.models import vendedor
from django.test import TestCase
from django.urls import reverse

## En la siguiente prueba:
# 1) Se crea un vendedor
# 2) Se elimina el vendedor


class EliminarVendedorTest(TestCase):

    def setUp(self):
        self.vendedor = vendedor.objects.create(nombre="Juan", apellido="Perez", numero_empleado="56789432")
        self.url = reverse('EliminarVendedor', args=[self.vendedor.nombre])

    def test_eliminar_vendedor(self):
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'vendedores.html')
        self.assertQuerysetEqual(vendedor.objects.all(), [])