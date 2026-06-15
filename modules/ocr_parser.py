import easyocr

# Load OCR model once
reader = easyocr.Reader(['en'])

def image_to_text(image_path):

    result = reader.readtext(image_path)

    text = []

    for item in result:
        text.append(item[1])

    return "\n".join(text)