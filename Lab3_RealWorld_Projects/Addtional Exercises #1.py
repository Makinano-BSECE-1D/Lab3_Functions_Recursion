# APPENDIX #1
import random
import time

LAST_NAME = "MAKINANO"
SEED_NUM = 6
FAVORITE_ARTIST = "ADO"

SEED_DIGIT = SEED_NUM
ID_SUM = sum(int(d) for d in str(SEED_NUM) if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

def diagnostics_process(func):
    def wrapper (*args, **kwargs):
        print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - Starting execution of: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - Successfully completed: {func.__name__}")
        return result
    return wrapper

@diagnostics_process
def generate_readings(last_name, seed_sum, artist):
    unique_seed = sum(ord(c) for c in last_name) + seed_sum + sum(ord(c) for c in artist)
    random.seed (unique_seed)

    readings = [round(random.uniform(50.0, 150.0),) for _ in range(4)]
    readings.append(-15.5)
    return readings

@diagnostics_process
def validate_reading(value):
   """validates if a reading falls within standard physical bounds (0 to 200)."""
   if not isinstance(value, (int, float)):
      raise TypeError (f"Invalid data type: {type(value)}. Must be numerical.")
   if value < 0 or value > 200:
      raise ValueError(f"Reading {value} is out of safe physical bounds (0 - 200)!")
   return True

@diagnostics_process
def calculate_average(valid_readings):
   """Calculates the average value of valid readings."""
   if not valid_readings:
    return 0
   return round(sum(valid_readings) / len(valid_readings), 2)

@diagnostics_process
def classify_status(average_value):
   """Classifies system condition based on the calculated average."""
   if average_value == 0:
      return "CRITICAL FAILURE (No Data)"
   elif average_value < 75:
      return "LOW PERFORMANCE"
   elif average_value <= 125:
      return "OPTIMAL OPERATING CONDITION"
   else:
      return "OVERHEATING / WARNING"

def main():
   print("=" * 60)
   print(f"EQUIPMENT DIAGNOSTIC SYSTEM - REPORT FOR STUDENT: {LAST_NAME}")
   print(f"Seed Configuration: {SEED_NUM} | Reference Artist: {FAVORITE_ARTIST}")
   print("=" * 60)

   raw_readings = generate_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
   print(f"\nGenerated Raw Readings: {raw_readings}")

   valid_readings = []
   print("\n--- Processing & Validating Readings ---")
   for reading in raw_readings:
      try:
         validate_reading(reading)
         valid_readings.append(reading)
         print(f" Reading {reading}: VALID")
      except (ValueError, TypeError) as e:
         print (f" Reading {reading}: INVALID -> Handled Exception: {e}")

   avg_reading = calculate_average(valid_readings)

   system_status = classify_status(avg_reading)

   print("\n" + "=" * 60)
   print("FINAL DIAGNOSTICS SUMMARY")
   print("=" * 60)
   print(f"Student Identifier : {LAST_NAME}_{SEED_NUM}")
   print(f"Total Raw Readings : {len(raw_readings)}")
   print(f"Valid Readings Used : {valid_readings}")
   print(f"calculated Average : {avg_reading}")
   print(f"Equipment Condition : {system_status}")
   print("=" * 60)

if __name__ == "__main__":
   main()