# fususONE_Python
selenium Python based project includes allure report , parallel execution in 3 browsers (chrome, firefox and edge) , Page object Model design pattern

IMPORTING THE PROJECT IN PYCHARM!!
once project is opened/imported in Pycharm please download and install dependencies listed in requirements.txt

please note you need to download allure from here and set it as path in environment variables

https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.12.0/

under project path > utils > config.json file set browser as chrome/firefox

to run a test navigate to the tests/fususone_tests folder example below

(venv) E:\selenium-python-framework-master\tests\fususone_tests>pytest -v -s --alluredir="E:\selenium-python-framework-master\allure-results" test_homepage.py


and run this command

"pytest -v -s --alluredir="E:\selenium-python-framework-master\allure-results" test_homepage.py"

once scripts are executed allure report files will be generated which will be saved in project path > allure-results folder

navigate to that folder in CMD window then run this command to open allure in browser
"allure serve {your driver letter here}:\selenium-python-framework-master\allure-results"

IMPORTANT!!

username/password to login to fususone is set at project directory > base > page_base.py file
under enterEmailAndNext email is set which can be changed
under enterPass password to login is set which can be changed


NEW CHANGES
parallel execution functionality added... to use the same please run this command "pip install pytest-xdist"
Added Edge driver code in driver_factory to execute scripts in Edge browser
Added 3 different test files under test_homepage.py each will execute in different browser to trigger the execution run this command in terminal by navigating to the test folder named fususone_test : **pytest -v -s --alluredir="{driver letter}:\selenium-python-framework-master\allure-results" test_homepage.py**

