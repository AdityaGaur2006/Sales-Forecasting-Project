# Sales Forecasting Project

## Overview
This project uses **time series forecasting** to predict sales for future dates based on past sales data. It is implemented using Python libraries such as **Prophet**, **Pandas**, and **Matplotlib**.

## Installation

To run this project on your machine, follow these steps:

### Clone the Repository
1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/username/sales-forecasting-project.git
Step by Step Setup the Virtual Environment
Navigate to the project directory:
After cloning the repository, the client will need to navigate to the folder where the project was saved.
For example:

bash
Copy
Edit
cd sales-forecasting-project
Create a Virtual Environment:
This command creates an isolated Python environment in which only the required libraries for your project will be installed. It prevents conflicts with other projects they might be working on.

For Windows:

bash
Copy
Edit
python -m venv venv
For macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
This command will create a folder called venv in the project directory, which contains all the isolated dependencies for the project.

Activate the Virtual Environment:
After creating the virtual environment, it must be activated so that all Python commands (like pip install) will be applied to the virtual environment, not the global Python installation.

For Windows:

bash
Copy
Edit
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Once activated, the terminal should show something like this:

scss
Copy
Edit
(venv) C:\Users\YourUser\sales-forecasting-project>
This indicates that the virtual environment is active and any Python or pip commands will use the libraries installed inside this environment.

Step 4: Install Dependencies
Once the virtual environment is activated, your client will need to install the project’s dependencies (all the libraries required to run the app).

To do this, they simply run:

bash
Copy
Edit
pip install -r requirements.txt
This command will:

Read the requirements.txt file.

Install all the libraries listed in it (like streamlit, pandas, prophet, etc.) into the virtual environment.

After running this command, they should see something like this:

nginx
Copy
Edit
Successfully installed pandas-1.2.3 numpy-1.19.5 prophet-1.0 matplotlib-3.3.4
Step 5: Run the Project
Finally, after setting up the virtual environment and installing the dependencies, your client can run the project using:

bash
Copy
Edit
python app.py
This will execute the main script (app.py), which will forecast the sales and display the results.

