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
                capital = get_capital(country)
                print(*capital)
                ## +
                altitude = get_altitude(lat, lon)
                coord_capital = get_coord_capital(country)

                distance = get_distance_inpPoint_capital(input_coord, coord_capital)

                population = get_population(country)

                travel_on_car = time_on_car(lat, lon)

                # Don't use it, becouse can't show list beautiful
                # outputs = [country, *capital, altitude, coord_capital, distance, population]

                if show_info == 'on':
                    capitals = three_nearest_country(input_coord)

                    # Render the template with results as context data
                    return render(request, 'input.html', {'form': form, 
                                                    'country': country,
                                                    'capital': capital,
                                                    'altitude': altitude,
                                                    'coord_capital': coord_capital,
                                                    'distance': distance,
                                                    'population': population,
                                                    'travel_on_car': travel_on_car,
                                                    'capitals': capitals,})
                else:
                    return render(request, 'input.html', {'form': form, 
                                                    'country': country,
                                                    'capital': capital,
                                                    'altitude': altitude,
                                                    'coord_capital': coord_capital,
                                                    'distance': distance,
                                                    'population': population,
                                                    'travel_on_car': travel_on_car,
})
        else:
            form = InputForm()
        return render(request, 'input.html', {'form': form})
    except Exception:
        error_message = "Please, try another values"
        return render(request, 'input.html', {'form': form,
                                              'error_message': error_message,})
