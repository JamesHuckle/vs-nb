import os

def convert(file_name):
    if f'{file_name}.ipynb' not in os.listdir():  
        print('Save .py file as .ipynb because no such file already exists.')            
        os.system(f'jupytext --to notebook {file_name}.py')
    else:
        print('Save .ipynb file as .py with interactive syntax') 
        os.system(f'jupytext --to py:percent {file_name}.ipynb')
    