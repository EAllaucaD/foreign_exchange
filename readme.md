

<!-- ABOUT THE PROJECT -->
## About The Project :DIVISAS

This Python project uses Docker and a currency conversion API, providing an automated and scalable solution for performing currency conversions. Docker ensures the portability and consistency of the development environment, while the API allows access to up-to-date exchange rates. This tool is ideal for financial, commercial applications or any environment that requires accurate and timely conversions between different currencies.
Why this program fills a need

    Efficiency: Automates the currency conversion process, eliminating the need for repetitive manual calculations.
    Accuracy: Uses an updated API to ensure accurate and reliable exchange rates.
    Portability: Encapsulation in Docker ensures that the program runs consistently on various systems and platforms.

This project offers a robust and easy to implement solution for any application requiring automated currency conversion functionalities.



### Built With
Python
Flask



## Getting Started and Prerequisites
Prerequisites and Installation

1. Get a free API Key at  https://www.exchangerate-api.com/

        API_KEY= 'API KEY ' in .env

2. This is an example of how to list things you need execute.
    pip install -r requirements.txt




<!-- USAGE EXAMPLES -->
## Usage
You can use this project:
1. Download the app or the zip from github.
2. To run through the console the application is python divisas.py

OTHER:
3. Have docker installed.
4. Opening a terminal and then the docker file we can execute the command docker build -t divisas .
5. To run the application       docker run -it --publish 5000:5000 divisas
6. Or run using        docker -compose up

## Example

Once the application has been executed, you can enter the value of money to be converted.

In this case, the currency that has the value is USD and you want to transform it you must enter the EUR.
