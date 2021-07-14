import PySimpleGUI as sg
import os


#help(sg.FolderBrowse)
#help(sg.FileBrowse)


layout = [
    [sg.Text('Lets Compile this PsychFile. Woooo.',justification='center',size=(70,1))],
    [sg.Text('Patient Pronoun', size =(20, 1)), sg.InputText(key='GD')],
    [sg.Text('Patient First Name', size =(20, 1)), sg.InputText(key='firstname')],
    [sg.Text('Patient Last Name', size =(20, 1)), sg.InputText(key='lastname')],
    [sg.Text('Date of Birth', size =(20, 1)), sg.InputText(key='DOB')],
    [sg.Text('Clinical Interview Date', size =(20, 1)), sg.InputText(key='DOI')],
    [sg.Text('Date of Testing', size =(20, 1)), sg.InputText(key='DOT')],
    [sg.Text('Report Feedback Date', size =(20, 1)), sg.InputText(key='DOR')],
    [sg.Text('Referrer', size =(20, 1)), sg.InputText(key='PHYS')],
    [sg.T("")], [sg.Text("Choose a  background file: "), sg.Input(), sg.FileBrowse(key="BKGRD-KEY-")],
    [sg.T("")], [sg.Text("Choose a  testing file: "), sg.Input(), sg.FileBrowse(key="-TESTING-KEY-")],
    [sg.Button("Submit")]]



window = sg.Window('PsychPile 1.0.0', layout)

while True:
    event, values = window.read()
    #print('event:', event)
    #print('values:', values)
    #print('FolderBrowse:', values['FolderBrowse'])
  #  print('FileBrowse:', values['FileBrowse'])

    if event is None or event == 'Cancel':
        break

    if event == 'Submit':
        # if folder was not selected then use current folder `.`
        foldername = values['FolderBrowse'] or '.'

        filenames = os.listdir(foldername)

      #  print('folder:', foldername)
      # print('files:', filenames)
      #  print("\n".join(filenames))

window.close()
exit()
