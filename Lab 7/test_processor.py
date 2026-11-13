
from hypothesis import given, strategies as st, example
from processor import (
    validate_height_and_fastpass,
    compute_dispatch_throughput,
    resolve_safety_restraint_code
)


# Test 1: validate_height_and_fastpass
@given(st.text() | st.none())
@example(None)
@example("")
@example("abc:YES")
@example("140:")
@example("140:YES:EXTRA")
def test_validate_height_and_fastpass_no_crash(s):
    try:
        validate_height_and_fastpass(s)
    except Exception as e:
        assert False, f"validate_height_and_fastpass crashed with input {s!r}: {e}"


# Test 2: compute_dispatch_throughput
@given(st.text() | st.none())
@example(None)
@example("")
@example("abc/2")
@example("48/0")
@example("48/-2")
@example("nan/2")
def test_compute_dispatch_throughput_safe(s):
    try:
        compute_dispatch_throughput(s)
    except Exception as e:
        assert False, f"compute_dispatch_throughput crashed with input {s!r}: {e}"


# Test 3: resolve_safety_restraint_code
@given(st.text() | st.none())
@example(None)
@example("")
@example("XYZ_01")
@example("C")
@example("UNKNOWN")
def test_resolve_safety_restraint_code_safe(s):
    try:
        resolve_safety_restraint_code(s)
    except Exception as e:
        assert False, f"resolve_safety_restraint_code crashed with input {s!r}: {e}"
