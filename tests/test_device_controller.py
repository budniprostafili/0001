import unittest
from smart_home.controllers.device_controller import DeviceController

class TestDeviceController(unittest.TestCase):
    def setUp(self):
        self.controller = DeviceController(db_name=':memory:')

    def test_add_device(self):
        device = self.controller.add_device("Test Lamp", "off")
        self.assertIsNotNone(device.device_id)
        self.assertEqual(device.name, "Test Lamp")
        self.assertEqual(device.state, "off")

    def test_get_device(self):
        device = self.controller.add_device("Test Lamp", "off")
        fetched_device = self.controller.get_device(device.device_id)
        self.assertEqual(fetched_device.device_id, device.device_id)
        self.assertEqual(fetched_device.name, "Test Lamp")
        self.assertEqual(fetched_device.state, "off")

    def test_update_device_state(self):
        device = self.controller.add_device("Test Lamp", "off")
        self.controller.update_device_state(device.device_id, "on")
        updated_device = self.controller.get_device(device.device_id)
        self.assertEqual(updated_device.state, "on")

    def test_delete_device(self):
        device = self.controller.add_device("Test Lamp", "off")
        self.controller.delete_device(device.device_id)
        self.assertIsNone(self.controller.get_device(device.device_id))

if __name__ == "__main__":
    unittest.main()