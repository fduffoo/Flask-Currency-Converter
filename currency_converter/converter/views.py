import requests
from django.shortcuts import render


def convert_currency(request):
    error_message = ''  # Define a default value for error_message
    converted_amount = None

    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency').upper()
        to_currency = request.POST.get('to_currency').upper()

        # Make a request to Open Exchange Rates API
        api_key = '5a96da934f-3d98927201-sd4x8o'
        url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}&base={from_currency}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if to_currency in data['rates']:
                exchange_rate = data['rates'][to_currency]
                converted_amount = round(float(amount) * exchange_rate, 2)
            else:
                error_message = 'Invalid currency code.'
        else:
            error_message = 'Failed to fetch exchange rates from the API.'

    return render(request, 'convert.html', {'error_message': error_message, 'converted_amount': converted_amount})

