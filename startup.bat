IF EXIST "venv" (
    ECHO "venv already exists"
) ELSE (
    virtualenv venv
    %CD%\venv\Scripts\activate.bat
)
    pip install .
