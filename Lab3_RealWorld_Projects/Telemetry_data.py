# APPENDIX #3
import random

def get_unique_seed(last_name, seed_num, artist):
    """Generates a deterministic seed value from student details."""
    return sum(ord(c) for c in last_name) + seed_num + sum(ord(c) for c in artist)

def telemetry_generator(last_name, seed_num, artist, sample_count=10):
    """
    REQUIREMENT 1 & 3: Generator that yields student-specific telemetry
    readings streaming data one-by-one without memory storage.
    """
    seed_value = get_unique_seed(last_name, seed_num, artist)
    random.seed(seed_value)

    for i in range(sample_count):
        if i == 5:
            yield -99.9
        elif i == 8:
            yield "INVALID_STRING"
        else:
            yield round(random.uniform(20.0, 180.0), 2)