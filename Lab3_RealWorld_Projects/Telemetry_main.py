# APPENDIX #3
import time
import Telemetry_data

LAST_NAME = "MAKINANO"
SEED_NUM = 6
FAVORITE_ARTIST = "ADO"

SEED_DIGIT = SEED_NUM
ID_SUM = sum(int(d) for d in str(SEED_NUM) if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

metrics = {"processed": 0, "valid": 0,"invalid": 0, "abnormal": 0}

def monitor_pipeline(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - Initializing core execution: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start_time) * 1000
        print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - Concluded {func.__name__} in {elapsed:.2f}ms")
        return result
    return wrapper

def analyze_abnormal_condition(value, depth=1):
    """Recursively de-escalates or steps down an abnormal reading to safe limits."""

    if value <= 100.0:
        print(f" [Recursive Trace Depth {depth}] -> Stabilized safely down to: {value}")
        return [round(value, 2)]

    print(f" [Recursive Trace Depth {depth}] -> Mitigation layer running on value: {value:.2f}")

    mitigated_value = value * 0.75
    return [round(value, 2)] + analyze_abnormal_condition(mitigated_value, depth + 1)


@monitor_pipeline
def run_intelligent_pipeline():
    print("--- Stream Processing Engine Ignited ---")

    scale_transformer = lambda x: round(x * 1.05, 2) if isinstance(x, (int, float)) else x

    stream_source = Telemetry_data.telemetry_generator(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)

    recursive_logs = {}

    for raw_reading in stream_source:
        metrics["processed"] += 1
        print(f"\nIncoming Raw Feed Line: {raw_reading}")

        try:
            if not isinstance(raw_reading, (int, float)):
                raise TypeError(f"System hardware telemetry rejected corupted data from: '{type(raw_reading).__name__}'")
            if raw_reading < 0:
                raise ValueError(f"Sensor critical voltage drop alert: {raw_reading} falls under minimum threshold 0!")

            transformed_reading = scale_transformer(raw_reading)
            metrics["valid"] += 1
            print(f" -> Transformed Telemetry (lambda): {transformed_reading}")

            if transformed_reading > 140.0:
                metrics["abnormal"] += 1
                print(f" ⚠️ ALERT: Abnormal high operation detected ({transformed_reading})! Branching to recursive trace fallback:")

                trace_sequence = analyze_abnormal_condition(transformed_reading)
                recursive_logs[transformed_reading] = trace_sequence

        except (ValueError, TypeError) as exception_error:
            metrics["invalid"] +=1
            print(f" ❌ Handled Pipeline Interruption: (exception_error)")

    return recursive_logs

def main():
    print("=" * 70)
    print(f"INTELLIGENT EQUIPMENT MONITORING PIPELINE REPORT: {LAST_NAME}")
    print("=" * 70)
    print(f"Student Profile Token: {LAST_NAME}_{SEED_NUM} | Reference Artist: {FAVORITE_ARTIST}\n")

    recursive_traces = run_intelligent_pipeline()

    print("\n" + "=" * 70)
    print("FINAL DIAGNOSTIC SUMMARY")
    print("=" * 70)
    print(f"Student Identifier : {LAST_NAME}_{SEED_NUM}")
    print(f"Total Streamed Readings : {metrics['processed']}")
    print(f"Valid Clared Records : {metrics['valid']}")
    print(f"Invalid Dropped Records : {metrics['invalid']}")
    print(f"Abnormal Flags Tripped : {metrics['abnormal']}")
    print("\n[Recursive Fallback Trace Matrix Data]:")
    for triggered_val, sequence in recursive_traces.items():
        print("\nOverall Equipment Status: ", end="")
        if metrics["invalid"] > 2 or metrics["abnormal"] > 3:
            print("🔴 CRITICAL SERVICE FAILURE ALERT")
        else:
            print("🟢 OPERATIONAL OPTIMAL / ACTIVE MONITORING")
        print("=" * 70)

if __name__ == "__main__":
    main()