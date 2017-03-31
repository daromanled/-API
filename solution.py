import osa

def temperature():
    client = osa.client.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    
    sum = 0
    number = 0
    
    with open('temps.txt', 'r') as file:
        for line in file:
            response = client.service.ConvertTemp(Temperature = line.split(' ')[0], FromUnit = 'degreeFahrenheit', ToUnit = 'degreeCelsius')
            sum += response
            number += 1
            
    return round(sum / number, 1)

def currency():
    client = osa.client.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    
    result = 0
    
    with open('currencies.txt', 'r') as file:
        for line in file:
            array = line.strip().split(' ')
            response = client.service.ConvertToNum(toCurrency = 'RUB', fromCurrency = array[2], amount = int(array[1]), rounding = True)
            result += response

    return round(result)

def travel():
    client = osa.client.Client('http://www.webservicex.net/length.asmx?WSDL')
    
    result = 0
    
    with open('travel.txt', 'r') as file:
        for line in file:
            array = line.strip().split(' ')
            response = client.service.ChangeLengthUnit(LengthValue = array[1].replace(',', ''), fromLengthUnit = 'Miles', toLengthUnit = 'Kilometers')
            result += response
    
    return round(result, 2)

print(temperature())
print(currency())
print(travel())
