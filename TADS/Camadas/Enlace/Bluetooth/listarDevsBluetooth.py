import bluetooth
nearby_devices = bluetooth.discover_devices()
print("Encontrados", len(nearby_devices), "dispositivos: ")
for bdaddr in nearby_devices:
    print("\t", nearby_devices.index(bdaddr), ":", bluetooth.lookup_name( bdaddr ))