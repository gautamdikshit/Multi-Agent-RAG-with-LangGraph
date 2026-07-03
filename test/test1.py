from docling.document_converter import DocumentConverter
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os 

def parse_with_docling(pdf_path):
    """
    Parse a PDF using Docling, extracts markdown content,
    and prints the full extracted content.
    """
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")
        
        converter = DocumentConverter()
        markdown_document = converter.convert(pdf_path).document.export_to_markdown()

        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        docs_list = markdown_splitter.split_text(markdown_document)

        print("\n ✅ Full Extracted Content (Docling):")
        for idx, doc in enumerate(docs_list):
            print(f"\n 🔹 Section {idx + 1}: \n{doc}\n" + "-"*80)

        return docs_list
    except Exception as e:
        print(f"Error during docling processing: {str(e)}")
        return []
    

def main():
    ocr_path = "test/ocr_test.pdf"
    scanned_pdf_path = "test/sample.png"

    print("\n🔍 Running Docling Extraction for OCR...")
    docling_docs = parse_with_docling(ocr_path)

    print("\n🔍 Running Docling Extraction for scanned PDF...")
    docling_docs = parse_with_docling(scanned_pdf_path)


if __name__ == "__main__":
    main()