#OPEN ONION LINKS WITH PYTHON AND FIREFOX.
##REQUIREMENTS:
	- tor
	- firefox(you need an browser, watch webdriver in lauch_browser.py)
	- geckodriver(of firefox)
	- python.
          ###PYTHON REQUIREMENTS:
                - selenium
##CONFIGURE:
    - config tor: Edit tor_port and specify the variables.
	- Edit lauch_browser.py: place the SOCKSPort of tor_port; also  you can  change  browser.
##HOW TO USE?:
	- excecute in terminal:
			sudo tor -f tor_port &
	- and in other terminal, inside of proyect folder:
			python launch_browser.py
	Note: if you want to change your fake ip, you have to restart tor service. Example in debian: service tor restart.
