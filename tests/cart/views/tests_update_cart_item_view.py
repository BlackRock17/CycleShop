from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from CycleShop.cart.models import Cart, CartItem
from CycleShop.accessories.models import Accessories
from CycleShop.bicycles.models import Bicycle


class UpdateCartItemViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.bicycle = Bicycle.objects.create(name="Test Bicycle", price=1000, quantity=5)
        self.accessory = Accessories.objects.create(name="Test Accessory", price=100, quantity=10)
        self.cart = Cart.objects.create(user=self.user)

    def test_update_cart_item_quantity(self):
        cart_item = CartItem.objects.create(cart=self.cart, product_type="bicycles.Bicycle", product_id=self.bicycle.id,
                                            price=self.bicycle.price, quantity=1)

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("update_cart_item", args=[cart_item.id]), {"quantity": 3})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("cart"))
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 3)
        self.bicycle.refresh_from_db()
        self.assertEqual(self.bicycle.quantity, 3)

    def test_update_cart_item_insufficient_quantity(self):
        cart_item = CartItem.objects.create(cart=self.cart, product_type="accessories.Accessories",
                                            product_id=self.accessory.id, price=self.accessory.price, quantity=2)

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("update_cart_item", args=[cart_item.id]), {"quantity": 15})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("cart"))
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 2)
        self.accessory.refresh_from_db()
        self.assertEqual(self.accessory.quantity, 10)

    def test_update_cart_item_unauthenticated_user(self):
        cart_item = CartItem.objects.create(cart=self.cart, product_type="products.Bicycle", product_id=self.bicycle.id,
                                            price=self.bicycle.price, quantity=1)

        response = self.client.post(reverse("update_cart_item", args=[cart_item.id]), {"quantity": 3})

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 1)
        self.bicycle.refresh_from_db()
        self.assertEqual(self.bicycle.quantity, 5)
        