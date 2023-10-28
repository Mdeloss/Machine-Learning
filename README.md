# Machine Learning
 
User Guide
1.	Install Python 3.11
  a.	  From a browser, navigate to: “https://www.python.org/downloads/“
  b.	  Select “Download Python 3.11.3” or the latest version.
  c.	  Run the installation from your pc: 
	c1.	Select “Customize Installation”.
	c2.	Optional Features: Keep everything default, then select “Next” 
	c3.	Advanced Options: Select checkbox “Add Python to environment variables”. (This is important to properly run libraries). Keep everything else default.
	c4.	Select “Install”, then close the setup window after successful installation.

2.	On Windows 10, open cmd terminal and run: “python.exe -m pip install —upgrade pip”
  a.	  Installing Pandas. Run: “pip install pandas”
  b.	  Installing Sklearn. Run: “pip install -U scikit-learn” 
  c.	  Installing Matplotlib. Run: “python -m pip install -U matplotlib“
3.	Unzip and Open the “Capstone_Project” file location.
  a.	  Right-click “main.py”, then select “Create shortcut”.
  b.	  Move the shortcut to the desktop.
4.	Launch “main.py” shortcut from the desktop.

Description: 
	This Python application is used to determine ticket assignments when necessary. Categories are represented as numerical values in place of ticket 
attributes for easier processing by the model. An example of how categories would be matched with numerical 
values goes as follows: Location: Seattle - 45, Assignment Group: Networking Team - Group 30, CallerID: Jane Doe - 1. 
