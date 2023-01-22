#funkcja wczytująca dataset

def data_imp(file_path = input('data set path')):  #, etykiety = input('contain headers? (Y/N)')):
    

    f = open(file_path, 'r')

    data_list = []
    # header_list = []

    for linia in f:

        linia_edited = linia.replace('\n', '')

        linia_edited2 = linia_edited.split(',')

        data_list.append(linia_edited2)
        # data_list.append(linia2)

    print(data_list)
    # print(header_list)