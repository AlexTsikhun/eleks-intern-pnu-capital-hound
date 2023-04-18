# eleks-intern-pnu-capital-hound
## The task provided by the company Eleks for an internship (8 semester).

### Task:
Capital Hound

Estimate - 120h (160h with additional challenges)

Develop an application for finding the capital of the country depending on the starting point.
The user enters the address, the program should calculate the capital of the country in which the city is located,
specified in the address.

It is also necessary to display the following data:
• Name of the country.

• The name of the capital.

• Distance from the entered address to the capital.

• Coordinates of the capital.

• Height of the capital above sea level.

• Data on how long it will take to travel to the city by car.

• Any other statistics at the discretion of the student are welcome.

• (additional) Population.

Additionally:
• Display a list of the 3 nearest capitals and the statistics listed above for them. Example
for Ivano-Frankivsk it will be Warsaw, Budapest and Kyiv.

## Solution
### Project Structure:
```
├───src                                 <- Code
|
├───main.py                             <- For console tests
|
├───.gitignore                          <- Ignore files
|
├───README.md
|
└───requirements.txt
```

For development, you need to use existing APIs for geolocation.

The application is written in Python. Django - for web, geopy and other idferent libraries and API. Geopy includes geocoder classes for the OpenStreetMap Nominatim, Google Geocoding API (V3), and many other geocoding services.

### An example of a completed task:
<img width="771" alt="image" src="https://user-images.githubusercontent.com/83775762/232803459-a67611ba-9ce0-4f2b-9253-dfb30534cf37.png">

![full](https://user-images.githubusercontent.com/83775762/232802607-00c307b3-7ebf-434a-b10e-0feba399868d.png)

Wrong input example:
![wrong_val](https://user-images.githubusercontent.com/83775762/232802891-4a1d1acf-f4ea-4905-8867-d9ca7c96d754.png)

### Run code in Windows:
```
cd src
py manage.py runserver
```
