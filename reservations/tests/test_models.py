from django.test import TestCase 
from reservations.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item.Title) +": "+ str(float(item.Price)) , "IceCream: 80.0")

    def test_default_inventory(self):
        item = Menu.objects.create(Title="Cake", Price=Decimal('50'))
        self.assertEqual(item.Inventory, 5)

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            Name="John Doe",
            No_of_guests=4,
            BookingDate=datetime(2023, 6, 24, 18, 0)
        )
        expected_str = "John Doe for 4 guests on 2023-06-24 18:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            Name="Jane Doe",
            BookingDate=datetime(2023, 6, 24, 19, 0)
        )
        self.assertEqual(booking.No_of_guests, 6)