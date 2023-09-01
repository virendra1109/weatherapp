# Weather Speaker README

## Introduction
The Weather Speaker is a Python program that uses the `requests` library to fetch weather data from the WeatherAPI and the `pyttsx3` library to read the temperature aloud. 
This README provides essential information about how to use the Weather Speaker code.

## Requirements
Before running the Weather Speaker, ensure you have the following prerequisites installed:

- Python: You need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Requests library: Install it using pip with the following command:

```
pip install requests
```

- pyttsx3 library: Install it using pip with the following command:

```
pip install pyttsx3
```

## Installation
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the Weather Speaker code.

## Usage
Follow these steps to use the Weather Speaker:

1. Open a terminal or command prompt.

2. Navigate to the directory where you saved the Weather Speaker code.

3. Run the code by executing the following command:

```
python weather_speaker.py
```

4. The program will prompt you to enter the name of your city.

5. Enter the city name for which you want to fetch the current temperature.

6. The program will use the WeatherAPI to retrieve the current temperature for the specified city and display it in Celsius.

7. The program will also use text-to-speech to read the temperature aloud.

## Example
Here's an example of how to use the Weather Speaker:

```
Enter the name of your city
New York
```

The program will display the current temperature in Celsius, like this:

```
23.7
```

The program will also say "23.7" out loud using the text-to-speech engine.

## Customization
You can modify the code to suit your needs. For example, you can customize the API key or change the data you fetch from the WeatherAPI.

## API Key
Make sure to replace the API key in the URL with your own WeatherAPI key. You can obtain a key by signing up at [WeatherAPI](https://www.weatherapi.com/).


## Acknowledgments
- This program uses the `requests` library for making HTTP requests.
- This program uses the `pyttsx3` library for text-to-speech conversion.
- Created by Virendra Singh

Feel free to contribute to this project or provide feedback. If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/virendra1109).
