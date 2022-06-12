import ocrmypdf

if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr('HYUNDAI_VX380TD_schematy_elektryczne_gt65.pdf', 'output_ver2.pdf', output_type="pdf")
