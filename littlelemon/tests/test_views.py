from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
import json
from restaurant.serializers import MenuItemSerializer

# Test for MenuItemView
class MenuItemViewTest(TestCase):
    def setUp(self) -> None:
        MenuItem.objects.create(title="fried fish", price="7.50", inventory="50")       
        MenuItem.objects.create(title="chicken roll", price="4.50", inventory="60")
        # MenuItem.objects.create(title="butter chicken", price="8.50", inventory="50")        
        # MenuItem.objects.create(title="chole bhature", price="7.50", inventory="5")
        
    def test_get_all(self):
        retrieved_object = MenuItem.objects.all()

        serialized_object = MenuItemSerializer(retrieved_object, many=True)
        serialized_object = json.loads(json.dumps(serialized_object.data))
        
        response = self.client.get(reverse('menu-items'))       
        response = str(response.content, 'UTF-8')
        response = json.loads(response)
        
        self.assertEqual(response, serialized_object)