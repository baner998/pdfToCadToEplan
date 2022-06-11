import ocrmypdf

if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr('cemb_bef.pdf', 'output.pdf', deskew=True)