from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from CycleShop.cart.models import Cart, CartItem
from CycleShop.accessories.models import Accessories
from CycleShop.bicycles.models import Bicycle
from CycleShop.equipment.models import Equipment
from CycleShop.components.models import Components


class AddToCartViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.bicycle = Bicycle.objects.create(name="Test Bicycle", price=1000, quantity=5)
        self.accessory = Accessories.objects.create(name="Test Accessory", price=100, quantity=10)
        self.component = Components.objects.create(name="Test Component", price=200, quantity=8)
        self.equipment = Equipment.objects.create(name="Test Equipment", price=500, quantity=3)

    def test_add_to_cart_authenticated_user(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("add_to_cart", args=["bicycles.Bicycle", self.bicycle.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("cart"))
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(Bicycle.objects.get(id=self.bicycle.id).quantity, 4)

    def test_add_to_cart_unauthenticated_user(self):
        response = self.client.post(reverse("add_to_cart", args=["accessories.Accessory", self.accessory.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         f'/accounts/login/?next={reverse("add_to_cart", args=["accessories.Accessory", self.accessory.id])}')
        self.assertEqual(CartItem.objects.count(), 0)
        self.assertEqual(Accessories.objects.get(id=self.accessory.id).quantity, 10)

    def test_add_to_cart_existing_cart_item(self):
        self.client.login(username="testuser", password="testpassword")
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product_type="components.Components", product_id=self.component.id,
                                price=self.component.price, quantity=1)

        response = self.client.post(reverse("add_to_cart", args=["components.Components", self.component.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("cart"))
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.first().quantity, 2)
        self.assertEqual(Components.objects.get(id=self.component.id).quantity, 7)

    def test_add_to_cart_insufficient_quantity(self):
        self.client.login(username="testuser", password="testpassword")
        self.equipment.quantity = 0
        self.equipment.save()

        response = self.client.post(reverse("add_to_cart", args=["equipment.Equipment", self.equipment.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("cart"))
        self.assertEqual(CartItem.objects.count(), 0)
        self.assertEqual(Equipment.objects.get(id=self.equipment.id).quantity, 0)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f"Insufficient quantity for {self.equipment.name}")
