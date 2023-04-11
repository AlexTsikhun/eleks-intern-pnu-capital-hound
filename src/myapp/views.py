from django.shortcuts import render
from .forms import InputForm
from .main import *
import requests

def input_view(request):
    try:
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                # str to float for caclucation
                lat = float(form.cleaned_data['input_field1'])
                lon = float(form.cleaned_data['input_field2'])
                show_info = request.POST.get('show_info')

                # name tuple for distance 
                input_coord = (lat, lon)

                country = get_country_name(lat, lon)
                # print('---------------')
                capital = get_capital(country)
                print(*capital)
                ## +
                altitude = get_altitude(lat, lon)
                print("=====")
                coord_capital = get_coord_capital(country)

                distance = get_distance_inpPoint_capital(input_coord, coord_capital)

                population = get_population(country)
                outputs = [country, *capital, altitude, coord_capital, distance, population]

                if show_info == 'on':
                # Render template with additional info
                    countries = three_nearest_country(input_coord)

                    # Render the template with results as context data
                    return render(request, 'input.html', {'form': form, 
                                                    'outputs': outputs,
                                                    'countries': countries})
                else:
                    return render(request, 'input.html', {'form': form, 
                                                    'outputs': outputs,})
        else:
            form = InputForm()
        return render(request, 'input.html', {'form': form})
    except Exception:
        error_message = "Please, try another values"
        return render(request, 'input.html', {'form': form,
                                              'error_message': error_message,})

# def get_country_name(lat, lon):
#     """
#     Given a latitude and longitude, returns the name of the country
#     using the Nominatim API.
#     """
#     print(lat, lon)
#     url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=jsonv2"
#     headers = {'accept-language': 'en-US'}
#     # url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
#     response = requests.get(url, headers=headers).json()
#     # print(response)
#     # print(response["address"]["country"])
#     return response["address"]["country"]