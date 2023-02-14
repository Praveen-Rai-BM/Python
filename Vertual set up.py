Virtual Environment Setup and Folder and Sub Folder and Project folder creation and activation  

PYTHON PRACTICE-PraveenBon007-praveen_07

PS D:\PYTHON PRACTICE\PraveenBond007> python -m venv praveen_07
PS D:\PYTHON PRACTICE\PraveenBond007> cd .\praveen_07
PS D:\PYTHON PRACTICE\PraveenBond007\praveen_07> .\Scripts\activate
(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007\praveen_07> cd ..
(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007> 
After creating a project folder needs do activate the same using cd command (Change Directory).
Activation process is completed have to come out of the process using cd ..

Test.py folder needs to be created under the project 
and install required application/software .Python needs django we have to install
commands on Terminal Header
import django
print(djang"__version__")


Terminal Code editor
----------------------
(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007> python .\Test.py
  File "D:\PYTHON PRACTICE\PraveenBond007\Test.py", line 2
    print(django"__version__")
                ^^^^^^^^^^^^^
SyntaxError: invalid syntax
(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007> pip install django
Collecting django
  Using cached Django-4.1.6-py3-none-any.whl (8.1 MB)
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.3-py3-none-any.whl (42 kB)
Collecting tzdata
  Using cached tzdata-2022.7-py2.py3-none-any.whl (340 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.6.0 django-4.1.6 sqlparse-0.4.3 tzdata-2022.7
[notice] A new release of pip available: 22.3.1 -> 23.0
[notice] To update, run: python.exe -m pip install --upgrade pip


Install Requiremnts.txt file (This folder is must be created for all the dependents for the project placed) and deactivate after installation codes given below.

(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007> pip freeze >requirements.txt
(praveen_07) PS D:\PYTHON PRACTICE\PraveenBond007> deactivate

