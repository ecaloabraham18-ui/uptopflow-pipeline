import os
import time
from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

def parse_commissioning_doc(input_path, output_path):
    print(f"Parsing: {input_path}")
    
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",
        verbose=True,
        language="en",
        parsing_instruction="""
        This is a data center commissioning report or engineering 
        document. It contains technical tables, equipment test results, 
        torque values, electrical readings, and system configurations. 
        Preserve all table structures. Keep all numerical values exact. 
        Maintain equipment names and model numbers precisely. Do not 
        summarize or skip any content.
        """
    )
    
    documents = parser.load_data(input_path)
    
    full_text = "\n\n---PAGE BREAK---\n\n".join(
        [doc.text for doc in documents]
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Parsed successfully. Output saved to: {output_path}")
    print(f"Total characters extracted: {len(full_text)}")
    
    return full_text


if __name__ == "__main__":
    input_file = "../inputs/test_commission.pdf"
    output_file = "../outputs/parsed_raw.md"
    
    result = parse_commissioning_doc(input_file, output_file)
    print("\nFirst 500 characters of output:")
    print(result[:500])