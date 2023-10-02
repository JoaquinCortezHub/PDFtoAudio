import pyttsx3
import PyPDF2

readPdf = PyPDF2.PdfReader(open('Zen-in-the-art-of-archery.pdf', 'rb'))
speaker = pyttsx3.init()

for pageNumber in range(len(readPdf.pages)):
    content = readPdf.pages[pageNumber].extract_text()
    cleanContent = content.strip().replace('/n', ' ')

speaker.save_to_file(cleanContent, 'Zen in the art of archery.mp3')
speaker.runAndWait()
speaker.stop()
