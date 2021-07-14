#main file for psychpile, to call modules in order as needed
import PySimpleGUI as sg

#help(sg.FolderBrowse)
#help(sg.FileBrowse)


layout = [
    [sg.Text('Lets Compile this PsychFile. Woooo.',justification='center',size=(70,1))],
    [sg.Text('Patient Pronoun', size =(20, 1)), sg.InputText(key='input_GD')],
    [sg.Text('Patient First Name', size =(20, 1)), sg.InputText(key='input_firstname')],
    [sg.Text('Patient Last Name', size =(20, 1)), sg.InputText(key='input_lastname')],
    [sg.Text('Date of Birth', size =(20, 1)), sg.InputText(key='input_DOB')],
    [sg.Text('Clinical Interview Date', size =(20, 1)), sg.InputText(key='input_DOI')],
    [sg.Text('Date of Testing', size =(20, 1)), sg.InputText(key='input_DOT')],
    [sg.Text('Report Feedback Date', size =(20, 1)), sg.InputText(key='input_DOR')],
    [sg.Text('Referrer', size =(20, 1)), sg.InputText(key='input_PHYS')],
    [sg.T("")], [sg.Text("Choose a  background file: "), sg.Input(), sg.FileBrowse(key="input_BKGRD-KEY-")],
    [sg.T("")], [sg.Text("Choose a  testing file: "), sg.Input(), sg.FileBrowse(key="input_TESTING-KEY-")],
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

        GD = (values['input_GD'])
        firstname = (values['input_firstname'])
        lastname = (values['input_lastname'])
        DOB = (values['input_DOB'])
        DOI = (values['input_DOI'])
        DOT = (values['input_DOT'])
        DOR = (values['input_DOR'])
        PHYS = (values['input_PHYS'])
        combine_func()
    #  print('folder:', foldername)
      # print('files:', filenames)
      #  print("\n".join(filenames))

window.close()
exit()

