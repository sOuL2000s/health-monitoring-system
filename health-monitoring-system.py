# Sample daily health data
health_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "HeartRate_bpm": [72, 85, 95, 78, 68],
    "Temperature_C": [36.5, 37.0, 39.2, 36.8, 37.1]
}

# Define normal ranges
normal_heart_rate = (60, 100)  # bpm
normal_temperature = (36.1, 37.2)  # Celsius

# Function to check vitals
def check_vitals(heart_rate, temperature):
    heart_ok = normal_heart_rate[0] <= heart_rate <= normal_heart_rate[1]
    temp_ok = normal_temperature[0] <= temperature <= normal_temperature[1]
    if not heart_ok or not temp_ok:
        return "Warning: Abnormal vital sign detected!"
    return "Vitals are normal."

# Check each day's vitals
for day, hr, temp in zip(health_data["Day"], health_data["HeartRate_bpm"], health_data["Temperature_C"]):
    result = check_vitals(hr, temp)
    print(f"{day} - Heart Rate: {hr} bpm, Temperature: {temp} °C - {result}")
