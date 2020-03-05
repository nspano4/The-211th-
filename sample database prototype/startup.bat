IF EXIST "venv" (
    ECHO "venv already exists"
) ELSE (
    virtualenv venv ::Create the virtualenv directory
    %CD%\venv\Scripts\activate.bat  ::Start the virtual environment
)
    pip install .   ::Run the setup file to install needed packages
