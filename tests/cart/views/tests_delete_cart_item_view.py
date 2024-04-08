from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from CycleShop.cart.models import Cart, CartItem
from CycleShop.bicycles.models import Bicycle


class DeleteCartItemViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.bicycle = Bicycle.objects.create(name="Test Bicycle", price=1000, quantity=5)
        self.cart = Cart.objects.create(user=self.user)

    def test_delete_cart_item(self):
        cart_item = CartItem.objects.create(cart=self.cart, product_type="bicycles.Bicycle", product_id=self.bicycle.id,
                                            price=self.bicycle.price, quantity=2)

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("delete_cart_item", args=[cart_item.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("cart"))
        self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())
        self.bicycle.refresh_from_db()
        self.assertEqual(self.bicycle.quantity, 7)

    def test_delete_cart_item_unauthenticated_user(self):
        cart_item = CartItem.objects.create(cart=self.cart, product_type="bicycles.Bicycle", product_id=self.bicycle.id,
                                            price=self.bicycle.price, quantity=1)

        response = self.client.post(reverse("delete_cart_item", args=[cart_item.id]))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
        self.assertTrue(CartItem.objects.filter(id=cart_item.id).exists())
        self.bicycle.refresh_from_db()
        self.assertEqual(self.bicycle.quantity, 5)
