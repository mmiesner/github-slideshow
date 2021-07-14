
def docpile (doctype, save_as):
    if doctype = "eval
        document =  Document('Psychevaltemplate2.docx')
    if doctype = "physletter"
        document =  Document(r'C:\Users\My PC\Dropbox\psychpile\ReferralLetterTemplate.docx')
    if doctype = "fax"
        document = Document(r'C:\Users\My PC\Dropbox\psychpile\faxsheet.docx' )


   if saveas = "eval":
       save_filename = "%s Full Evaluation.docx" % lastname
        document.save(save_filename)
   if saveas = "physletter": "%s physicianletter.docx" % lastname
         document.save(save_filename)
   if saveas = "fax": save_filename = "%s physicianfaxsheet.docx" % lastname
        document.save(save_filename)

    for paragraph in document.paragraphs:
        find_replace("PTFN", firstname, paragraph)
        find_replace("PTLN", lastname, paragraph)
        find_replace("DOBI", DOB, paragraph)
        find_replace("DOI", DOI, paragraph)
        find_replace("DOT", DOT, paragraph)
        find_replace("GD", GD, paragraph)
#for header in document.header:
    #find_replace("PTFN", firstname, paragraph)
    #find_replace("PTLN", lastname, paragraph)


    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    for paragraph in document.paragraphs:
        paragraph.style = document.styles['Normal']


def createf()

    if sys.platform == 'win32':
         os.chdir('C:\\Users\My PC\Dropbox\written evaluations' )
    else: os.chdir('/users/michael/Dropbox/written_evaluations' )

    os.chdir(lastname + ", " + firstname)

#end  functions; start iterations


