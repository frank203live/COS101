def physics_formula_options():
    print('nPhysics formula option:')
    print('a. work')
    print('b. velocity')
    print('c. momentum')
    print('d. thermal energy')
    print('e. electric current')
    print('f. finished')


physics_formula_options()


options = input(' pick an option from a to f  ')
print(options)
if options == 'a':
    force = int(input('enter number  '))
    distance = int(input('enter number  '))
    work = force * distance
    print(work)

elif options == 'b':
    distance = int(input('enter value for distance  '))
    time = int(input('enter value for time  '))
    velocity = distance / time
    print(velocity)

elif options == 'c':
    mass = int(input('enter value of mass  '))
    velocity = int(input('enter value of velocity  '))
    momentum = mass * velocity
    print(momentum)

elif options == 'd':
    temperature = int(input('enter value of temperature  '))
    mass = int(input('enter value of mass  '))
    specific_heat_capacity = int(input('enter value  '))
    thermal_energy = mass * specific_heat_capacity * temperature
    print(thermal_energy)

elif options == 'e':
    voltage = int(input('enter voltage  '))
    resistance = int(input('enter value of resistance  '))
    electric_current = voltage * resistance
    print(electric_current)

elif options == 'f':
    close = "you will never walk alone  "
    matric = "matric. no bhu/24/04/05/0125"
    end = close + matric
    print(end)

else :
    print('you are only permitted to pick options from a to f ')