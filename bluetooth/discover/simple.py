import bluetooth

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print(f'{bdaddr}: {bluetooth.lookup_name(bdaddr)}')
