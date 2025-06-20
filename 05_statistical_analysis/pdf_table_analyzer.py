#!/usr/bin/env python3
"""
PDF Table Analyzer - Tool to analyze PDF formatting issues, particularly for tables
"""

import sys
import fitz  # PyMuPDF
import argparse
from pathlib import Path


def analyze_pdf_tables(pdf_path):
    """Analyze tables in a PDF to identify formatting issues."""
    
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        print(f"\nAnalyzing PDF: {pdf_path}")
        print(f"Total pages: {len(doc)}\n")
        
        # Track table-related issues
        issues = []
        table_pages = []
        landscape_pages = []
        
        for page_num, page in enumerate(doc, 1):
            # Get page dimensions
            rect = page.rect
            width = rect.width
            height = rect.height
            
            # Check if page is landscape
            if width > height:
                landscape_pages.append(page_num)
            
            # Extract text
            text = page.get_text()
            
            # Look for table indicators
            if any(indicator in text for indicator in ["\\toprule", "\\midrule", "\\bottomrule", "\\begin{table}", "\\end{table}"]):
                table_pages.append(page_num)
            
            # Check for potential cut-off issues
            # Tables that continue to next page often have text at bottom edge
            text_blocks = page.get_text("blocks")
            for block in text_blocks:
                x0, y0, x1, y1 = block[:4]
                block_text = block[4]
                
                # Check if text is near bottom edge (within 50 points)
                if y1 > height - 50:
                    if any(table_indicator in str(block_text) for table_indicator in ["&", "\\\\", "Significance", "Note:", "p-value"]):
                        issues.append({
                            'page': page_num,
                            'type': 'potential_cutoff',
                            'detail': f'Table content near bottom edge at y={y1:.1f} (page height={height:.1f})',
                            'text_preview': str(block_text)[:100].replace('\n', ' ')
                        })
            
            # Check for "Summary of" in text which might indicate summary table
            if "Summary of" in text and "Significant" in text:
                # Look for table structure
                lines = text.split('\n')
                table_lines = [line for line in lines if '&' in line or '\\\\' in line]
                if len(table_lines) > 20:  # Large table
                    issues.append({
                        'page': page_num,
                        'type': 'large_summary_table',
                        'detail': f'Large summary table with {len(table_lines)} rows detected',
                        'text_preview': 'Summary table found'
                    })
        
        # Report findings
        print("=== PDF Analysis Results ===\n")
        
        print(f"Pages with tables: {len(table_pages)}")
        if table_pages:
            print(f"  Table pages: {table_pages[:10]}{'...' if len(table_pages) > 10 else ''}")
        
        print(f"\nLandscape pages: {len(landscape_pages)}")
        if landscape_pages:
            print(f"  Landscape pages: {landscape_pages}")
        
        print(f"\nPotential issues found: {len(issues)}")
        for issue in issues:
            print(f"\nPage {issue['page']} - {issue['type']}:")
            print(f"  {issue['detail']}")
            if len(issue['text_preview']) > 0:
                print(f"  Preview: {issue['text_preview'][:80]}...")
        
        # Look specifically for the summary table
        print("\n=== Summary Table Analysis ===")
        summary_found = False
        for page_num, page in enumerate(doc, 1):
            text = page.get_text()
            if "Summary of All Significant Results" in text or "Summary of Significant Findings" in text:
                summary_found = True
                print(f"\nSummary table found on page {page_num}")
                
                # Count table rows
                lines = text.split('\n')
                data_lines = [line for line in lines if any(c in line for c in ['&', '0.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.'])]
                print(f"Estimated data rows: {len(data_lines)}")
                
                # Check if it spans multiple pages
                if page_num < len(doc):
                    next_page_text = doc[page_num].get_text()
                    if any(indicator in next_page_text for indicator in ['&', 'Extended', 'Simple', 'Treatment']):
                        print("Table appears to continue on next page")
                
                # Check page orientation
                rect = page.rect
                if rect.width > rect.height:
                    print("Page is in LANDSCAPE orientation")
                else:
                    print("Page is in PORTRAIT orientation")
                    print(f"Page dimensions: {rect.width:.1f} x {rect.height:.1f} points")
        
        if not summary_found:
            print("Summary table not found in PDF")
        
        doc.close()
        
    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description='Analyze PDF tables for formatting issues')
    parser.add_argument('pdf_path', help='Path to the PDF file to analyze')
    
    args = parser.parse_args()
    
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    analyze_pdf_tables(pdf_path)


if __name__ == "__main__":
    main()