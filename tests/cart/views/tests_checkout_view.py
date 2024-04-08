from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from CycleShop.accounts.models import Profile
from CycleShop.common.models import Order, OrderItem
from CycleShop.cart.models import Cart, CartItem
from CycleShop.accessories.models import Accessories
from CycleShop.bicycles.models import Bicycle



class CheckoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)

        self.bicycle = Bicycle.objects.create(name='Test Bicycle', price=1000, quantity=5)
        self.accessory = Accessories.objects.create(name='Test Accessory', price=100, quantity=10)
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=self.cart, product_type='bicycles.Bicycle', product_id=self.bicycle.id,
                                price=self.bicycle.price, quantity=2)
        CartItem.objects.create(cart=self.cart, product_type='accessories.Accessories', product_id=self.accessory.id,
                                price=self.accessory.price, quantity=1)

    def test_checkout_with_complete_profile(self):
        self.client.login(username='testuser', password='testpassword')

        self.profile.first_name = 'John'
        self.profile.last_name = 'Doe'
        self.profile.email = 'johndoe@example.com'
        self.profile.town = 'Test Town'
        self.profile.address = 'Test Address'
        self.profile.postcode = '1234'
        self.profile.save()

        form_data = {
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'town': 'Test Town',
            'address': 'Test Address',
            'postcode': '1234',
        }

        response = self.client.post(reverse('checkout'), data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/checkout_success.html')
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 2)
        self.assertEqual(CartItem.objects.count(), 0)

    def test_checkout_with_incomplete_profile(self):
        self.profile.town = ''
        self.profile.save()

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('checkout'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             reverse('profile_edit', kwargs={'pk': self.profile.pk}) + '?next=' + reverse('checkout'))

    def test_checkout_unauthenticated_user(self):
        response = self.client.get(reverse('checkout'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)