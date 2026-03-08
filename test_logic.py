from utils.matcher import identify_medicine


def run_system_tests():
    print("--- 🧪 Starting Activity 4.1: Component Testing ---")

    # Test 1: Exact Match check
    test_1 = identify_medicine("Paracetamol")
    if test_1["found"]:
        print("✅ Test 1 Passed: Exact match found.")

    # Test 2: Fuzzy Match check (Handling typos)
    test_2 = identify_medicine("Asprin")  # Common typo
    if test_2["name"] == "Aspirin":
        print("✅ Test 2 Passed: Fuzzy logic corrected 'Asprin' to 'Aspirin'.")

    # Test 3: Risk Level Validation (Activity 4.2)
    if test_2["risk"] == "High":
        print("✅ Test 3 Passed: Correct risk level assigned to Aspirin.")


if __name__ == "__main__":
    run_system_tests()