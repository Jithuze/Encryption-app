from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def images_to_pdf(image_files, pdf_file):

    try:
        images = image_files.split(", ")

        c = canvas.Canvas(pdf_file, pagesize=letter)
        width, height = letter

        for image_file in images:
            img = Image.open(image_file)
            img_width, img_height = img.size

            # Calculate aspect ratio to fit the image into the page
            aspect_ratio = img_width / img_height
            if aspect_ratio > 1:
                img_width = width
                img_height = width / aspect_ratio
            else:
                img_height = height
                img_width = height * aspect_ratio

            # Draw the image on the canvas
            c.drawImage(image_file, 0, 0, width=img_width, height=img_height)

            # Add a new page for the next image
            c.showPage()

        c.save()
        return True
    except:
        return False

# # Example usage
# image_files = ['image1.jpg', 'image2.png', 'image3.jpeg']
# pdf_file = 'output.pdf'

# images_to_pdf(image_files, pdf_file)