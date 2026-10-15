import random
from datetime import datetime

# This function simulates 3 plant sensors: soil moisture, light level, temperature
# Returns 3 float values with realistic ranges for houseplants
def read_sensors():
    # Soil moisture: percentage from 10% to 90%
    soil_moisture = random.uniform(10, 90)
    # Light level: lux, range 50 ~ 1000 lux
    light_level = random.uniform(50, 1000)
    # Temperature: Celsius, range 15 ~ 32 °C
    temperature = random.uniform(15, 32)
    return soil_moisture, light_level, temperature

# Check if sensor values are within healthy plant ranges
# Collect warning messages into a list and return the list
def check_plant_health(moisture, light, temp):
    alerts = []
    # Moisture rules
    if moisture < 25:
        alerts.append("⚠️ Low soil moisture! Please water your plant.")
    elif moisture > 75:
        alerts.append("⚠️ Soil too wet! Risk of root rot.")

    # Light rules
    if light < 150:
        alerts.append("⚠️ Not enough sunlight.")
    elif light > 800:
        alerts.append("⚠️ Too much bright light, may burn leaves.")

    # Temperature rules
    if temp < 18:
        alerts.append("⚠️ Temperature too low.")
    elif temp > 28:
        alerts.append("⚠️ Temperature too hot.")

    # If no warnings, plant is healthy
    if not alerts:
        alerts.append("✅ All conditions are good. Plant is healthy.")
    return alerts

# Save sensor data + timestamp + alerts into plant_log.txt
# "a" = append mode: add new lines without deleting old data
# encoding="utf-8" fixes Windows emoji Unicode error
def log_data(moisture, light, temp, alerts):
    # Get current system time and format it
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = (f"{timestamp} | Moisture: {moisture:.1f}% | "
                f"Light: {light:.0f} lux | Temp: {temp:.1f}°C | Alerts: {alerts}\n")
    with open("plant_log.txt", "a", encoding="utf-8") as f:
        f.write(log_line)
    print("✅ Reading saved to plant_log.txt")

# Main function: controls the whole program flow
def main():
    print("===== Plant Monitoring System =====")
    # Get simulated sensor readings
    moist, light, temp = read_sensors()
    print("\nCurrent Readings:")
    print(f"Soil Moisture: {moist:.1f} %")
    print(f"Light Level: {light:.0f} lux")
    print(f"Temperature: {temp:.1f} °C")

    # Run health check
    health_messages = check_plant_health(moist, light, temp)
    print("\nPlant Health Status:")
    for msg in health_messages:
        print(msg)

    # Write data to log file
    log_data(moist, light, temp, health_messages)

# Only run main() when we directly execute this python file
if __name__ == "__main__":
    main()
