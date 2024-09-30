settings = 0b00011011 
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
setting = input("Enter the setting to check: ")

enabled = bool(settings & setting_map[setting])

print(f"The '{setting}' setting is enabled: {enabled}")