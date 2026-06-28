import os
import sys
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from parse_document import parse_commissioning_doc
from extract_summary import extract_operational_summary
from generate_procedures import generate_mop, generate_eop, generate_quick_reference
from generate_sop import generate_sop

def run_pipeline(pdf_path, facility_name):

    print("=" * 60)
    print("UPTOPFLOW PIPELINE")
    print(f"Facility: {facility_name}")
    print(f"Input: {pdf_path}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found at {pdf_path}")
        sys.exit(1)

    parsed_path = "../outputs/parsed_raw.md"
    summary_path = "../outputs/operational_summary.md"

    print("\n[1/6] Parsing PDF with LlamaParse...")
    try:
        parse_commissioning_doc(pdf_path, parsed_path)
        print("✓ PDF parsed successfully")
    except Exception as e:
        print(f"ERROR in parsing: {e}")
        sys.exit(1)

    print("\n[2/6] Extracting operational summary with Claude...")
    try:
        extract_operational_summary(parsed_path, summary_path)
        print("✓ Summary extracted successfully")
    except Exception as e:
        print(f"ERROR in extraction: {e}")
        sys.exit(1)

    print("\n[3/6] Generating MOP...")
    try:
        generate_mop(
            summary_path=summary_path,
            task_name="Critical Systems Power Inspection",
            equipment_name="Power Distribution and UPS Systems",
            system_type="Power",
            facility_name=facility_name,
            output_path="../outputs/MOP-POW-001.md"
        )
        print("✓ MOP generated successfully")
    except Exception as e:
        print(f"ERROR generating MOP: {e}")
        sys.exit(1)

    print("\n[4/6] Generating SOP...")
    try:
        generate_sop(
            summary_path=summary_path,
            routine_name="Daily Infrastructure Walkthrough",
            systems_covered="Power, Cooling, BMS, Compute Racks",
            frequency="Daily — Every Shift",
            facility_name=facility_name,
            output_path="../outputs/SOP-OPS-001.md"
        )
        print("✓ SOP generated successfully")
    except Exception as e:
        print(f"ERROR generating SOP: {e}")
        sys.exit(1)

    print("\n[5/6] Generating EOP...")
    try:
        generate_eop(
            summary_path=summary_path,
            emergency_scenario="Critical Cooling System Failure",
            systems_affected="Cooling, Power, Compute Racks",
            facility_name=facility_name,
            output_path="../outputs/EOP-COOL-001.md"
        )
        print("✓ EOP generated successfully")
    except Exception as e:
        print(f"ERROR generating EOP: {e}")
        sys.exit(1)

    print("\n[6/6] Generating Quick Reference Card...")
    try:
        generate_quick_reference(
            summary_path=summary_path,
            procedure_title="Critical Systems Power Inspection",
            system_type="Power",
            facility_name=facility_name,
            output_path="../outputs/QUICK-REF-POW-001.md"
        )
        print("✓ Quick reference generated successfully")
    except Exception as e:
        print(f"ERROR generating quick reference: {e}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nOutput files:")
    output_dir = "../outputs"
    for f in sorted(os.listdir(output_dir)):
        size = os.path.getsize(os.path.join(output_dir, f))
        print(f"  {f} ({size:,} bytes)")
    print("=" * 60)
    print("\nPlaybook ready. Review output files before client delivery.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="UpTopFlow Pipeline — PDF to Operational Playbook"
    )
    parser.add_argument(
        "--pdf",
        required=True,
        help="Path to the commissioning PDF file"
    )
    parser.add_argument(
        "--facility",
        required=True,
        help="Name of the facility"
    )
    args = parser.parse_args()

    run_pipeline(args.pdf, args.facility)