# This test will be combined with the user's code
try:
    result = hello()
except Exception as e:
    print(f"Error: {e}")
    exit(1)

expected = "Hello, World!"
if result != expected:
    print(f"Expected: '{expected}', but got: '{result}'")
    exit(1)

print("OK")