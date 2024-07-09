import sqlite3
from smart_home.utils.logger import get_logger

logger = get_logger(__name__)

class Device:
    def __init__(self, device_id, name, state):
        self.device_id = device_id
        self.name = name
        self.state = state

    def __repr__(self):
        return f"<Device(id={self.device_id}, name={self.name}, state={self.state})>"

class DeviceDatabase:
    def __init__(self, db_name='smart_home.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                '''CREATE TABLE IF NOT EXISTS devices (
                    device_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    state TEXT NOT NULL
                )'''
            )
        logger.info("Device table created.")

    def add_device(self, device):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                'INSERT INTO devices (name, state) VALUES (?, ?)',
                (device.name, device.state)
            )
            device_id = cursor.lastrowid
            logger.info(f"Device {device.name} added to database with id {device_id}.")
            return Device(device_id=device_id, name=device.name, state=device.state)

    def get_device(self, device_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM devices WHERE device_id=?', (device_id,))
        row = cursor.fetchone()
        if row:
            device = Device(*row)
            return device
        else:
            logger.warning(f"No device found with id {device_id}.")
            return None

    def update_device_state(self, device_id, new_state):
        with self.connection:
            self.connection.execute(
                'UPDATE devices SET state=? WHERE device_id=?',
                (new_state, device_id)
            )
        logger.info(f"Device {device_id} state updated to {new_state}.")

    def delete_device(self, device_id):
        with self.connection:
            self.connection.execute(
                'DELETE FROM devices WHERE device_id=?',
                (device_id,)
            )
        logger.info(f"Device {device_id} deleted from database.")
        