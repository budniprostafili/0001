from smart_home.controllers.device_controller import DeviceController

def main():
    controller = DeviceController()
    # Пример использования
    device = controller.add_device("Lamp", "off")
    print(device)
    device = controller.get_device(device.device_id)
    print(device)
    controller.update_device_state(device.device_id, "on")
    device = controller.get_device(device.device_id)
    print(device)
    controller.delete_device(device.device_id)

if __name__ == "__main__":
    main()