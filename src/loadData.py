from LoadDataset import LoadDataset
import pandas as pd
import os


def downloadData():

    path = '../data'
    
    # Susy
    _, _ = LoadDataset.load_susy(debug=True, save_path=path)

    # Higgs
    _, _ = LoadDataset.load_higgs(debug=True, save_path=path)

    # Adult
    _, _ = LoadDataset.load_adult(debug=True, save_path=path)

    # Covertype
    _, _ = LoadDataset.load_covertype(debug=True, save_path=path)

def loadData(dataset):

    if dataset == 'susy':
        return LoadDataset.load_susy(debug=False, load_path='data')
    elif dataset == 'higgs':
        return LoadDataset.load_higgs(debug=False, load_path='data')
    elif dataset == 'adult':
        return LoadDataset.load_adult(debug=False, load_path='data')
    elif dataset == 'covertype':
        return LoadDataset.load_covertype(debug=False, load_path='data')
    else:
        
        # verify if the dataset is in data folder
        if dataset not in os.listdir('data'):
            ValueError('Dataset not found in data folder')

        print(f"Loading dataset from {'data/' + dataset}")
        df = pd.read_csv(os.path.join('data', dataset))
 

        # Rename the first column to 'target' and separate it as a Series
        target = df.iloc[:, 0]
        target.name = 'target'

        # Get the remaining columns as a DataFrame
        data = df.iloc[:, 1:]

        return data, target
        