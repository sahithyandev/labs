totalUnits = float(input("Total number of units of electricity (in kWh): "))

if totalUnits < 0:
    print("Invalid value provided")
    exit(1)


def calculateInHigherTariffScheme(units: float):
    _units = units
    fixed = 0
    varyingTariff = 0
    if _units > 180:
        fixed = 2000
        varyingTariff += (_units - 180) * 75
        _units = 180
    if _units > 90:
        if fixed == 0:
            fixed = 1500
        varyingTariff += (_units - 90) * 50
        _units = 90

    if fixed == 0:
        fixed = 650

    varyingTariff += _units * 42
    print("fixed", fixed)
    print("varying", varyingTariff)
    return fixed + varyingTariff


def calculateInLowerTariffScheme(units: float):
    _units = units
    fixed = 0
    varyingTariff = 0
    if _units > 30:
        fixed = 550
        varyingTariff += (_units - 30) * 37
        _units = 30

    if fixed == 0:
        fixed = 400
    varyingTariff += _units * 30
    return fixed + varyingTariff


if totalUnits > 60:
    output = calculateInHigherTariffScheme(totalUnits)
    print(int(output))
else:
    output = calculateInLowerTariffScheme(totalUnits)
    print(int(output))
