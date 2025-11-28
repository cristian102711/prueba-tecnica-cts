from django.test import TestCase
from .models import Participante

class ParticipanteTestCase(TestCase):
    def setUp(self):
        self.participante = Participante.objects.create(
            nombre="Tester",
            apellido="Quality",
            email="test@quality.com"
        )

    def test_creacion_participante(self):
        """Valida que un usuario nace con estado PENDIENTE y tiene token"""
        self.assertEqual(self.participante.estado, 'PENDIENTE')
        self.assertIsNotNone(self.participante.token_verificacion)

    def test_email_unico(self):
        """Valida que no se puedan repetir correos (Regla de negocio)"""
        with self.assertRaises(Exception):
            Participante.objects.create(
                nombre="Hacker",
                apellido="Duplicado",
                email="test@quality.com" # Mismo email
            )