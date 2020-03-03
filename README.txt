To run the program on Windows

	-Run the startup.bat file
		The file should:
			setup the virtualenv if it isn't already setup
			activate the virtual elvironment
			install all needed packages
				flask, flask_security, flask_sqlalchemy	

    -Starting the program
        run ".\flaskrun.bat"

        if that doesn't work for some reason type these in the terminal
            set FLASK_APP=flaskr
            set FLASK_ENV=development
            flask run

    -After the program is started just click on the link generated to open the website locally
        http://127.0.0.1:5000/


To run the program on Mac/Linux

	create the virtual environment
		run 'virtualenv venv'

	activate the virtual environment
		run 'source ./venv/bin/activate'

	run the startup file (This will install all the packages needed)
		run 'pip install .'
		
    -Starting the program
        run "./flaskrun"

        if that doesn't work for some reason type these in the terminal
            export FLASK_APP=flaskr
            export FLASK_ENV=development
            flask run

    -after the program is started just click on the link generated to open the website locally
        http://127.0.0.1:5000/

