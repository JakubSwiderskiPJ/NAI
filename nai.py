from simpful import *
"""
Jakub Świderski s19443
Paweł Dondziak s
Program helps to determine the process of meat preparation in electric oven.
The program takes three numeric variables:
  - Temperature
  - Mass
  - Time
The solution uses the Mandami algorithm to interpret linguistic variables.
"""

FS = FuzzySystem()

temperature_low = FuzzySet(function=Triangular_MF(a=0, b=50, c=100), term="temp_low")
temperature_medium = FuzzySet(function=Triangular_MF(a=101, b=201, c=220), term="temp_medium")
temperature_high = FuzzySet(function=Triangular_MF(a=221, b=300, c=320), term="temp_high")
LV1 = LinguisticVariable(
    [temperature_low, temperature_medium, temperature_high], concept="Temperature",
    universe_of_discourse=[10, 94])
FS.add_linguistic_variable("Temperature", LV1)
"""
Linguistic variable responsible for interpretation of temperature in three levels
"""

time_short = FuzzySet(function=Triangular_MF(
    a=0, b=30, c=35), term="short")
time_medium = FuzzySet(function=Triangular_MF(
    a=30, b=60, c=70), term="medium")
time_long = FuzzySet(function=Triangular_MF(
    a=60, b=80, c=120), term="long")
LV2 = LinguisticVariable(
    [time_short, time_medium, time_long], concept="Time",
    universe_of_discourse=[2, 70])
FS.add_linguistic_variable("Time", LV2)
"""
Linguistic variable responsible for interpretation of time in three levels
"""

mass_small = FuzzySet(function=Triangular_MF(
    a=1, b=1.5, c=1.7), term="small")
mass_medium = FuzzySet(function=Triangular_MF(
    a=1.4, b=1.8, c=2.3), term="medium")
mass_big = FuzzySet(function=Triangular_MF(
    a=2.0, b=2.4, c=2.7), term="big")
LV4 = LinguisticVariable(
    [mass_small, mass_medium, mass_big], concept="Mass",
    universe_of_discourse=[1000, 2700])
FS.add_linguistic_variable("Mass", LV4)
"""
Linguistic variable responsible for the interpretation of mass.
"""

preparation_raw = FuzzySet(function=Triangular_MF(
    a=-1., b=-.7, c=-0.5), term="Raw")
preparation_medium = FuzzySet(function=Triangular_MF(
    a=-.6, b=-.3, c=0.), term="Medium")
preparation_Done = FuzzySet(function=Triangular_MF(
    a=0, b=0.1, c=0.4), term="Well_Done")
LV3 = LinguisticVariable(
    [preparation_raw, preparation_medium,
        preparation_Done],
    concept="Preparation", universe_of_discourse=[-1, 1])
FS.add_linguistic_variable("Preparation", LV3)
"""
The linguistic variable responsible for the interpretation of the above three inputs
"""

FS.add_rules_from_file(path='rules.txt')
"""
Upload list of rules from an file
"""

FS.set_variable("Temperature", 100)
FS.set_variable("Time", 30)
FS.set_variable("Mass", 1.8)

print(FS.Mamdani_inference(["Preparation"]))