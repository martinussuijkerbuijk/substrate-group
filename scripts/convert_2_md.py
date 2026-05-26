import fitz  # PyMuPDF
import os

input_dir = r"raw/papers"
output_dir = r"raw/papers"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_clean_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = []
    
    for page in doc:
        # "blocks" returns a list of items: (x0, y0, x1, y1, "text", block_no, block_type)
        blocks = page.get_text("blocks")
        
        # Sort blocks: first by vertical position (y0), then horizontal (x0)
        # This helps maintain reading order in multi-column documents
        blocks.sort(key=lambda b: (b[1], b[0]))
        
        for b in blocks:
            if b[6] == 0:  # Block type 0 is text (ignore images/drawings)
                full_text.append(b[4])
                
    return "\n".join(full_text)

# Batch process
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".pdf"):
        print(f"Processing: {filename}...")
        try:
            path = os.path.join(input_dir, filename)
            content = extract_clean_text(path)
            
            md_path = os.path.join(output_dir, filename.replace(".pdf", ".md"))
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print(f"Done! Check your '{output_dir}' folder.")