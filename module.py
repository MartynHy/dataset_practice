#funkcja wczytująca dataset

def data_imp(file_path = input('type in dataset path'), etykiety = input('does it contain headers? (Y/N)')):
    

    f = open(file_path, 'r')

    data_list = []
    header_list = []
    counter = 0

    for linia in f:

        linia_edited = linia.replace('\n', '')
        linia_edited2 = linia_edited.split(',')

        if etykiety == 'Y' and counter == 0:

            header_list = [i for i in linia_edited2] 
            counter += 1
            
        else:
            
            data_list.append(linia_edited2)

    return header_list
    

def header_check():

    header_list = data_imp()
    
    if bool(header_list) == False:

        print('zbiór nie posiada etykiet')
    
    else:

        print('data set zawiera następujące etykiety:')
    
        for i in header_list:
            print(i)