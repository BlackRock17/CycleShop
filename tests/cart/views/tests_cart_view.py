from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from CycleShop.cart.models import Cart, CartItem
from CycleShop.accessories.models import Accessories
from CycleShop.bicycles.models import Bicycle
from CycleShop.equipment.models import Equipment
from CycleShop.components.models import Components


class CartViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.bicycle = Bicycle.objects.create(name="Test Bicycle", price=1000, quantity=5)
        self.accessory = Accessories.objects.create(name="Test Accessory", price=100, quantity=10)
        self.component = Components.objects.create(name="Test Component", price=200, quantity=8)
        self.equipment = Equipment.objects.create(name="Test Equipment", price=500, quantity=3)

    def test_cart_view_with_empty_cart(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("cart"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/empty_cart.html")
        self.assertContains(response, "Your basket is empty")

    def test_cart_view_with_items_in_cart(self):
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product_type="bicycles.Bicycle", product_id=self.bicycle.id,
                                price=self.bicycle.price, quantity=2)
        CartItem.objects.create(cart=cart, product_type="accessories.Accessories", product_id=self.accessory.id,
                                price=self.accessory.price, quantity=1)

        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("cart"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertContains(response, self.bicycle.name)
        self.assertContains(response, self.accessory.name)
        self.assertContains(response, f"Total: ${2100:.2f}")

    def test_cart_view_unauthenticated_user(self):
        response = self.client.get(reverse("cart"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={reverse("cart")}')

    def test_cart_view_with_deleted_product(self):
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product_type="components.Components", product_id=self.component.id,
                                price=self.component.price, quantity=1)
        self.component.delete()

        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("cart"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertNotContains(response, self.component.name)
