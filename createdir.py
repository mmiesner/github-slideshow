import os
import sys
print(sys.platform)

firstname = input("What is the patient's first name? ")
lastname = input("What is the patient's last name? ")

if sys.platform == 'win32':
    os.chdir('C:\\Users\My PC\Dropbox\written evaluations' )
else: os.chdir('/users/michael/Dropbox/written_evaluations' )

os.mkdir(lastname + ", " + firstname)
save_filename = "%s.docx" % lastname


if sys.platform == 'win32':
    save_path = ('C:\\Users\My PC\Dropbox\written evaluations' + lastname + ", " + firstname)
    save_filename = "%s psycheval.docx" % lastname
else: save_path = ('/users/michael/Dropbox/written_evaluations' + lastname + ", " + firstname)
    save_filename = "%s psycheval.docx" % lastname


