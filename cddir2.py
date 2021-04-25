import os
import sys
print(sys.platform)

firstname = input("What is the patient's first name? ")
lastname = input("What is the patient's last name? ")


if sys.platform == 'win32':
    save_path = ('C:\\Users\My PC\Dropbox\written evaluations' + lastname + ", " + firstname)
    save_filename = "%s, %s Evaluation.docx" % (lastname, firstname)
else:  save_path = ('/users/michael/Dropbox/written_evaluations' + lastname + ", " + firstname)

save_filename = "%s, %s Evaluation.docx" % (lastname, firstname)
