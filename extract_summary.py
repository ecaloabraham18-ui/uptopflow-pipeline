import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def extract_operational_summary(parsed_doc_path, output_path):
    
    with open(parsed_doc_path, 'r', encoding='utf-8') as f:
        document_text = f.read()
    
    prompt = f"""You are a data center documentation specialist analyzing a technical engineering document. Extract only the operationally relevant information and organize it clearly.

From the document below extract and organize:

1. DOCUMENT OVERVIEW
   What this document covers and its main purpose

2. KEY SYSTEMS AND EQUIPMENT MENTIONED
   List every piece of equipment or system with specs and values

3. CRITICAL OPERATIONAL PARAMETERS
   Every measurement, setpoint, threshold, or operational value mentioned

4. KEY PROCEDURES OR PROCESSES DESCRIBED
   Any step by step processes or operational sequences

5. IMPORTANT WARNINGS OR RISK FACTORS
   Safety warnings, failure modes, or risk considerations

6. THINGS AN OPERATOR NEEDS TO KNOW
   Practical takeaways for someone running this type of facility

Strip out marketing language, executive summaries, and anything that does not affect how equipment gets operated day to day.

DOCUMENT:
{document_text}"""

    print("Sending to Claude for extraction...")
    print(f"Document size: {len(document_text)} characters")
    
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8096,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    summary = message.content[0].text
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"Extraction complete. Saved to: {output_path}")
    print(f"\nFirst 500 characters of summary:")
    print(summary[:500])
    
    return summary


if __name__ == "__main__":
    extract_operational_summary(
        "../outputs/parsed_raw.md",
        "../outputs/operational_summary.md"
    )