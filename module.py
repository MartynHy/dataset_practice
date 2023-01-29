#funkcja wczytująca dataset

def data_imp(file_path = input('type in dataset path'), headers = input('does it contain headers? (Y/N)')):
    
    f = open(file_path, 'r')

    data_list = []
    header_list = []
    counter = 0

    for line in f:
        
        line_edited = line.replace('\n', '')
        line_edited2 = line_edited.split(',')

        if headers == 'Y' and counter == 0:

            header_list = [i for i in line_edited2] 
            counter += 1
            
        else:
            
            data_list.append(line_edited2)
    
    data_list.pop() #pozbycie się pustej listy
    
    return (header_list, data_list)


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

    #krotki 'tr/te/v_n' przechowujące liczbę 'n' elementów poszczególnych klas decyzyjnych,
    # jakie mają trafić do list: train, test, validate

    tr_n = tr / 100 * len(seto), tr / 100 * len(vers), tr / 100 * len(virg) w
    seto_tr_n, vers_tr_n, virg_tr_n = tr_n

    te_n = te / 100 * len(seto), te / 100 * len(vers), te / 100 * len(virg)
    seto_te_n, vers_te_n, virg_te_n = te_n

    v_n = v / 100 * len(seto), v / 100 * len(vers), v / 100 * len(virg)
    seto_v_n, vers_v_n, virg_v_n = v_n
 
    #funkcja random.sample pobiera
    train = [i for i in random.sample(seto, round(seto_tr_n))]
        
    for i in random.sample(vers, round(vers_tr_n)):
        train.append(i)
        
    for i in random.sample(virg, round(virg_tr_n)):
        train.append(i)
     

    test = [i for i in random.sample(seto, round(seto_te_n))]     

    for i in random.sample(vers, round(vers_te_n)):
        test.append(i)

    for i in random.sample(virg, round(virg_te_n)):
        test.append(i)

    
    validate = [i for i in random.sample(seto, round(seto_v_n))]

    for i in random.sample(vers, round(vers_v_n)):
        validate.append(i)
        
    for i in random.sample(virg, round(virg_v_n)):
        validate.append(i)

    return (seto, vers, virg)

    

def decision_class_nr():

    seto, vers, virg = data_split()
    
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
    
        
def save_data():

    import csv

    header_list, data_list = data_imp()

    filename = input('Write a name file')

    with open(filename, 'x') as f:

        write = csv.writer(f)
        write.writerow(header_list)
        write.writerows(data_list)


#C:\Users\Legion\Desktop\studia podyplomowe\python projekt\data_set\iris.data
