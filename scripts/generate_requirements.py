# scripts/generate_requirements.py
import json
import re
import argparse

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate requirement JSON from CFR Markdown")
parser.add_argument("--input", "-i", required=True, help="Input Markdown file (.md)")
parser.add_argument("--output", "-o", required=True, help="Output JSON file")
parser.add_argument("--cfr", "-c", required=True, help="CFR section (e.g., 21 CFR 117.130)")
args = parser.parse_args()

INPUT_MD = args.input
OUTPUT_JSON = args.output
CFR_SECTION = args.cfr

# ---------- Read File ----------
with open(INPUT_MD, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

requirements = []
current_req = None

# ---------- Parse ----------
for line in lines:

    # Capture REQ ID
    req_match = re.search(r"→\s*(REQ-[\d\.]+-\d+)", line)
    if req_match:
        current_req = req_match.group(1)
        continue

    # Capture atomic rules
    atomic_match = re.match(r"^(.*?)\s*→\s*([A-Z]\d*)$", line)
    if atomic_match and current_req:
        description = atomic_match.group(1).strip()
        suffix = atomic_match.group(2)

        requirement_id = f"{current_req}{suffix}"

        # Parent logic
        if len(suffix) == 1:
            parent = current_req
        else:
            parent = f"{current_req}{suffix[0]}"

        requirements.append({
            "requirement_id": requirement_id,
            "description": description,
            "source": CFR_SECTION,
            "parent": parent
        })

expected_structure = {}
MAX_REQ = 10
num_req = 0

for req in requirements:
    req_parent = req["parent"]
    suffix = req["requirement_id"][len(req_parent):]

    bucket = expected_structure.setdefault(req_parent, [])
    if suffix not in bucket:
        expected_structure[req_parent].append(suffix)
        num_req += 1

    if num_req >= MAX_REQ:
        break


# ---------- Save ----------
with open(OUTPUT_JSON, "w") as f:
    json.dump(requirements, f, indent=2)

print(f"Saved {len(requirements)} requirements → {OUTPUT_JSON}")

with open("expected_structure.json", "w") as f:
    json.dump(expected_structure, f, indent=2)

print(f"Saved {num_req} to expected_structure.json")
