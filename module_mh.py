#funkcja wczytująca dataset

def data_imp(file_path = input('type in dataset path'), headers = input('does it contain headers? (Y/N)'),
              separator = input('type in separator')):
    
    f = open(file_path, 'r')

    data_list = []
    header_list = []
    counter = 0

    for line in f:

        line_edited = line.replace('\n', '')
        line_edited2 = line_edited.split(separator)

        if headers == 'Y' and counter == 0:

            header_list = [i for i in line_edited2] 
            counter += 1
            
        else:
            
            data_list.append(line_edited2)
    
    data_list.pop() #pozbycie się pustej listy
    
    return header_list, data_list


def header_check():

    header_list, data_list = data_imp()
    
    if bool(header_list) == False:
        print('dataset does not contains headers')
    
    else:

        print('headers are:')
        for i in header_list:
            print(i)
        

def data_browser(start = 0, stop = None):

    header_list, data_list = data_imp()
    
    print(f'Dataset holds {len(data_list)} records total, indexed from "0"')

    print('Requested records are:')

    for i in data_list[start:stop]:
        
        print(i)


def data_split(tr = 0, te = 0, v = 0): 

    #podział data_list według wprowadzonych punktów procentówych na listy: train, test, validate

    import random

    header_list, data_list = data_imp()

    tr_n = tr / 100 * len(data_list)  # obliczenie liczby 'n' elementów losowanych z list
    te_n = te / 100 * len(data_list)
    v_n = v / 100 * len(data_list)
    
    random.shuffle(data_list) # wymieszanie kolejności elementów

    # dodanie indeksu do każdego rekordu żeby uniknąć wyeliminowania
    # z losowanej puli rekordów o takich samych parametrach

    index = 0
    for i in data_list:
        i.insert(0, index)
        index += 1
        
   
    train = [i for i in random.sample(data_list, round(tr_n))]

    data_list2 = [i for i in data_list if i not in train]
    
    test = [i for i in random.sample(data_list2, round(te_n))]

    data_list3 = [i for i in data_list2 if i not in test]

    validate = [i for i in random.sample(data_list3, round(v_n))]

    #usunięcie indeksów w gotowych listach

    for i in train:
        i.pop(0)

    for i in test:
        i.pop(0)

    for i in validate:
        i.pop(0)
        

    return train, test, validate
 

def decision_class_nr():

    header_list, data_list = data_imp()

    seto = []
    vers = []
    virg = []

    for i in data_list: #dystrybucja rekordów według klasy decyzyjnej

        if 'Iris-setosa' in i:
            seto.append(i)
            
        elif 'Iris-versicolor' in i:
            vers.append(i)
        
        else:
            virg.append(i)

        
    print('Pair (Decision classes, number) are:')
    print((seto[0][-1], len(seto)))
    print((vers[0][-1], len(vers)))
    print((virg[0][-1], len(virg)))



def pick_class():

    header_list, data_list = data_imp()

    class_name = input('type in decision class to view records')


    if class_name == 'Iris-setosa':

        for i in data_list:
            if i[-1] == class_name:
                print(i)

    elif class_name == 'Iris-versicolor':

        for i in data_list:
            if i[-1] == class_name:
                print(i)
    
    elif class_name == 'Iris-virginica':

        for i in data_list:
            if i[-1] == class_name:
                print(i)
    
    else:
        print('incorrect name of decision class')
    
        
def save_data(anylist):

    import csv

    header_list, data_list = data_imp()

    filename = input('Write a name file')

    with open(filename, 'x') as f:

        write = csv.writer(f)
        write.writerow(header_list)
        write.writerows(anylist)