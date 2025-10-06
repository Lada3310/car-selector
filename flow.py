carnames = ['volvo', 'bmw', 'audi']
colours = ['red', 'blue', 'green', 'yellow']
models = ['sedan', 'suv', 'coupe']

car_choice = input(f'Choose a brand {carnames}')
colour_choice = input(f'Choose a colour {colours}')
model_choice = input(f'Choose a model {models}')

suggestions = {
    ('volvo', 'sedan'): 'Volvo S60',
    ('volvo', 'suv'): 'Volvo XC60',
    ('volvo', 'coupe'): 'Volvo C30',

    ('bmw', 'sedan'): 'BMW 3 Series',
    ('bmw', 'suv'): 'BMW X5',
    ('bmw', 'coupe'): 'BMW 4 Series',

    ('audi', 'sedan'): 'Audi A4',
    ('audi', 'suv'): 'Audi Q5',
    ('audi', 'coupe'): 'Audi TT',
}


if car_choice in carnames and colour_choice in colours and model_choice in models:
    car_key = (car_choice, model_choice)


if car_key in suggestions:
    proposed_car = suggestions[car_key]
    print(f"\nYou chose a {colour_choice} {car_choice} {model_choice}.")
    print(f"Based on your taste, we recommend: {proposed_car}")
    

else:
    print("Sorry, no matching car found in our database.")

