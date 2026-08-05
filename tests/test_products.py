from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        url = reverse('create-product')
        data = {
            'name': 'Test Product',
            'price': '10.00',
            'stock': 100,
            'category': 'Test Category'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_get_product_list(self):
        Product.objects.create(name='Test Product', price='10.00', stock=100, category='Test Category')
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_product(self):
        product = Product.objects.create(name='Test Product', price='10.00', stock=100, category='Test Category')
        url = reverse('update-product', args=[product.id])
        data = {
            'name': 'Updated Product',
            'price': '15.00',
            'stock': 200,
            'category': 'Updated Category'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(name='Test Product', price='10.00', stock=100, category='Test Category')
        url = reverse('delete-product', args=[product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)