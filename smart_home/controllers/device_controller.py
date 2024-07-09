from smart_home.models.device import Device, DeviceDatabase
from smart_home.utils.validation import validate_device_name, validate_device_state

class DeviceController:
    def __init__(self, db_name='smart_home.db'):
        self.db = DeviceDatabase(db_name)

    def add_device(self, name, state):
        if validate_device_name(name) and validate_device_state(state):
            device = Device(device_id=None, name=name, state=state)
            return self.db.add_device(device)
        else:
            raise ValueError("Invalid device name or state.")

    def get_device(self, device_id):
        return self.db.get_device(device_id)

    def update_device_state(self, device_id, new_state):
        if validate_device_state(new_state):
            self.db.update_device_state(device_id, new_state)
        else:
            raise ValueError("Invalid device state.")

    def delete_device(self, device_id):
        self.db.delete_device(device_id)
        