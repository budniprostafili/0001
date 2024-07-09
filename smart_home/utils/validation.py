def validate_device_name(name):
    return isinstance(name, str) and len(name) > 0

def validate_device_state(state):
    return state in ['on', 'off']