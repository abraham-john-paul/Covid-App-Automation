# Setup
1. Install python 3.8 and pip
2. Install virtualenv using pip 
```pip install virtualenv```
3. Clone the code
4. Create a virtualenv and install selenium package to it.
```
virtualenv env
env\Scripts\activate
pip install selenium
deactivate
```
5. Download Gecko Driver if using firefox or chromedriver if using Chrome(make sure the driver version and browser version matches)
6. Edit automation_data.json
7. Run the automation file in the virtual environment created.
```
{path_to_virtualenv_folder}\env\Scripts\python.exe automation.py
```
