# APPENDIX #2
import time

LAST_NAME = "MAKINANO"
SEED_NUM = 6
FAVORITE_ARTIST = "ADO"

SEED_DIGIT = SEED_NUM
ID_SUM = sum(int(d) for d in str(SEED_NUM) if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

recursive_call_count = 0

def generate_fault_code(last_name, seed_num, artist):
    base_calc = (len(last_name) * 100) + (seed_num * 15) + len(artist)
    return base_calc

def trace_fault_recursive(current_code):
    global recursive_call_count
    recursive_call_count += 1

    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    if current_code <= 10:
        print(f"[LOG] {current_time} - [Call #{recursive_call_count}] Base Case Reached! Code: {current_code}")
        return [current_code]

    print(f"[LOG] {current_time} - [Call #{recursive_call_count}] Processing Code: {current_code} -> De-escalating...")

    next_code = current_code // 2

    trace_path = trace_fault_recursive(next_code)

    return [current_code] + trace_path

def main():
    global recursive_call_count
    recursive_call_count = 0

    print("=" * 60)
    print(f"RECURSIVE FAULT TRACE SYSTEM - REPORT FOR STUDENT: {LAST_NAME}")
    print("=" * 60)

    initial_fault_code = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print(f"Generated Fault Data (Initial Code): {initial_fault_code}\n")

    print("--- Starting Execution Log & Recursive Trace ---")

    complete_path = trace_fault_recursive(initial_fault_code)
    print("--- End of Trace ---\n")

    print("=" * 60)
    print("FINAL DIAGNOSTICS SUMMARY")
    print("=" * 60)
    print(f"Student Identifier : {LAST_NAME}_{SEED_NUM}")
    print(f"Generated Fault Data : {initial_fault_code}")
    print(f"Recursive Trace Sequence : {complete_path}")
    print(f"Number of Recursive Calls : {recursive_call_count}")
    print(f"Final Termination Code : {complete_path[-1]}")
    print("=" * 60)

if __name__ == "__main__":
    main()