import random

index_car = 0
wainting_gasoline: list[str] = []
pump_in_use = False
time_fueling = -1
oil_change_in_use = False
wainting_oil_change: list[str] = []
time_oil_change = -1
payment_in_use = False
wainting_payment: list[str] = []
time_payment = -1
name_car_fueling = ''
name_car_payment = ''
name_car_oil = ''
cars_arrived = 0
cars_left = 0
max_size_gas_queue = 0
max_size_oil_queue = 0
max_size_payment_queue = 0

clock = 0
while clock < 240:
    if random.randrange(100) < 15:
        car_name = f'carro_{index_car}'
        cars_arrived += 1
        if pump_in_use:
            wainting_gasoline.append(car_name)
        else:
            pump_in_use = True
            name_car_fueling = car_name
            time_fueling = random.randint(5, 10)
        index_car += 1

    if time_fueling == 0:
        if random.randrange(100) < 20:
            if oil_change_in_use:
                wainting_oil_change.append(name_car_fueling)
            else:
                oil_change_in_use = True
                name_car_oil = name_car_fueling
                time_oil_change = random.randint(20, 30)
        else:
            if payment_in_use:
                wainting_payment.append(name_car_fueling)
            else:
                payment_in_use = True
                name_car_payment = name_car_fueling
                time_payment = random.randint(2, 8)
        pump_in_use = False
        name_car_fueling = ''

    if time_oil_change == 0:
        if payment_in_use:
            wainting_payment.append(name_car_oil)
        else:
            payment_in_use = True
            name_car_payment = name_car_oil
            time_payment = random.randint(2, 8)
        oil_change_in_use = False

    if time_payment == 0:
        print(f'The car {name_car_payment} left the gas station')
        cars_left += 1
        payment_in_use = False
        name_car_payment = ''

    if len(wainting_gasoline) > max_size_gas_queue:
        max_size_gas_queue = len(wainting_gasoline)

    if len(wainting_oil_change) > max_size_oil_queue:
        max_size_oil_queue = len(wainting_oil_change)

    if len(wainting_payment) > max_size_payment_queue:
        max_size_payment_queue = len(wainting_payment)

    if not pump_in_use and len(wainting_gasoline) > 0:
        car = wainting_gasoline.pop(0)
        time_fueling = random.randint(5, 10)
        pump_in_use = True
        name_car_fueling = car

    if not oil_change_in_use and len(wainting_oil_change) > 0:
        car_oil = wainting_oil_change.pop(0)
        time_oil_change = random.randint(20, 30)
        oil_change_in_use = True
        name_car_oil = car_oil

    if not payment_in_use and len(wainting_payment) > 0:
        car_payment = wainting_payment.pop(0)
        time_payment = random.randint(2, 8)
        payment_in_use = True
        name_car_payment = car_payment

    time_fueling -= 1
    time_oil_change -= 1
    time_payment -= 1
    clock += 1

    print(f'clock = {clock}\n Car Fueling = {name_car_fueling}\n' + \
        f'Car changing the oil = {name_car_oil}\n' + \
        f'Car at checkout = {name_car_payment}\n' + \
        f'Queue to supply = {wainting_gasoline}\n' + \
        f'Queue to change oil = {wainting_oil_change}\n' + \
        f'Queue to checkout = {wainting_payment}')

print('\n------------------------------------------------------------\n')

print(f'Total cars that arrived = {cars_arrived}\n' + \
    f'Total cars that left = {cars_left}\n' + \
    f'Maximum queue size to fill = {max_size_gas_queue}\n' + \
    f'Maximum queue size for changing oil = {max_size_oil_queue}\n' + \
    f'Maximum queue size for checkout = {max_size_payment_queue}\n' + \
    f'Cars still in the line to fill up = {len(wainting_gasoline)}\n' + \
    f'Cars still in the line to changing oil = {len(wainting_oil_change)}\n' + \
    f'Cars still in the line to checkout = {len(wainting_payment)}')
