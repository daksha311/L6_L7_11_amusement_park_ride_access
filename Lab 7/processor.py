
import math


def validate_height_and_fastpass(rider_spec):
    try:
        if not isinstance(rider_spec, str):
            return "Invalid rider specification"

        parts = rider_spec.strip().split(':')
        if len(parts) != 2:
            return "Invalid rider specification"

        height_str, pass_str = parts
        height = int(height_str.strip())

        pass_map = {"YES": True, "NO": False}
        pass_value = pass_str.strip().upper()

        if height < 0 or pass_value not in pass_map:
            return "Invalid rider specification"

        has_fastpass = pass_map[pass_value]
        eligible = height >= 120
        status = "FastPass Priority" if has_fastpass else "Standard Entry"

        return f"Height {height}cm: {'Approved' if eligible else 'Denied'} ({status})"

    except (ValueError, TypeError, AttributeError):
        return "Invalid rider specification"


def compute_dispatch_throughput(ride_metric_str):
    try:
        if not isinstance(ride_metric_str, str):
            return "Invalid throughput input"

        parts = ride_metric_str.strip().split('/')
        if len(parts) != 2:
            return "Invalid throughput input"

        riders_str, mins_str = parts
        riders = float(riders_str.strip())
        cycle_mins = float(mins_str.strip())

        if not math.isfinite(riders) or not math.isfinite(cycle_mins):
            return "Invalid throughput input"

        if riders < 0 or cycle_mins <= 0:
            return "Invalid throughput input"

        rate = riders / cycle_mins

        if not math.isfinite(rate):
            return "Invalid throughput input"

        return round(rate, 2)

    except (ValueError, TypeError, AttributeError, ZeroDivisionError, OverflowError):
        return "Invalid throughput input"


def resolve_safety_restraint_code(zone_code):
    try:
        if not isinstance(zone_code, str):
            return "Unknown ride zone code"

        prefix = zone_code.strip().upper()[:3]

        restraint_types = {
            "CST": "Over-the-Shoulder Harness",
            "WTR": "Lap Bar and Seatbelt",
            "DRP": "Hydraulic Shoulder Vest",
            "WHL": "Manual Safety Bar"
        }

        return restraint_types.get(prefix, "Unknown ride zone code")

    except (TypeError, AttributeError):
        return "Unknown ride zone code"


def main():
    print("==== Running validate_height_and_fastpass ====")
    r_input = input("Enter rider spec (Height:FastPass, e.g. 140:YES): ")
    print(validate_height_and_fastpass(r_input))

    print("\n==== Running compute_dispatch_throughput ====")
    t_input = input("Enter riders/mins (e.g. 48/2.5): ")
    print("Throughput (riders/min):", compute_dispatch_throughput(t_input))

    print("\n==== Running resolve_safety_restraint_code ====")
    z_input = input("Enter ride zone code (e.g. CST_01, WTR_A): ")
    print("Restraint:", resolve_safety_restraint_code(z_input))


if __name__ == "__main__":
    main()
