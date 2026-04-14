import json

if __name__ == "__main__":
    # Match requuirement id with description
    with open("requirements.json", "r") as f:
        requirements = json.load(f)

    descriptions = {}

    for entry in requirements:
        descriptions[entry["requirement_id"]] = entry["description"]

    # Build the output
    with open("expected_structure.json", "r") as f:
        expected_structure = json.load(f)

    output = []
    case = 0

    for req_id, t in expected_structure.items():
        for item in t:
            output.append({
                "test_case_id": f"TC-{case + 1:03d}",
                "requirement_id": req_id + item,
                "description": descriptions[req_id + item]
            })

            case += 1

    # Store the output in test_cases.json
    with open("test_cases.json", "w") as f:
        json.dump(output, f, indent=2)

    print("Output written to test_cases.json")
