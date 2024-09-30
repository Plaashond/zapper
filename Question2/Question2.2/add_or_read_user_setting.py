import csv

csv_file = "settings.csv"

setting_map = {
    'SMS Notifications': 0b00000001,
    'Push Notifications': 0b00000010,
    'Bio-metrics': 0b00000100,
    'Camera': 0b00001000,
    'Location': 0b00010000,
    'NFC': 0b00100000,
    'Vouchers': 0b01000000,
    'Loyalty': 0b10000000
}

def read_settings():
    settings = {}
    try:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                settings[int(row[0])] = int(row[1], 16)
    except FileNotFoundError:
        pass
    return settings

def write_settings(settings):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        for id, value in settings.items():
            print(f"if:{id} value: {value}")
            writer.writerow([id, hex(value)[2:] if value is not None else ''])

while True:
    settings = read_settings()
    print("Current settings:")
    for id, value in settings.items():
        enabled_settings = [setting for setting, bit in setting_map.items() if value & bit]
        print(f"ID: {id}, Settings: {', '.join(enabled_settings)}")
    id = input("Enter the ID (or 'exit' to quit): ")
    if id.lower() == 'exit':
        break
    setting = input("Enter the setting to update (in hexadecimal): ")

    try:
        setting_value = int(setting, 16)
    except ValueError:
        print("Invalid setting value. Please enter a hexadecimal value.")
        continue

    settings[int(id)] = setting_value
    write_settings(settings)


