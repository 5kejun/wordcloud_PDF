# word_cloud a PDF

from wordcloud import WordCloud
import matplotlib.pyplot as plt
try:
    import pyPdf, sys
except ImportError:
    print "You need to install the pyPdf package -- pip install pyPdf"

if len(sys.argv) < 2:
    print('You must specify a file path (PDF).')
    sys.exit()

def wordcloudPDF(path):

    content = ''
    pdf = pyPdf.PdfFileReader(file(path, 'rb'))

    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + '\n'

    wordcloud = WordCloud(font_path='/System/Library/Fonts/Helvetica.dfont',
                          background_color='white').generate(content)                     
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

for fp in sys.argv[1:]:
    wordcloudPDF(fp)
