import numpy as np
import pandas as pd
import math

df = pd.read_excel(r"I:\MECH\SEH\Calculators/Pretension_Calculator.xlsx")

disp_belts = df.iloc[15:21,4]
print(disp_belts)

select_belt_brand = input(" Select the brand of tensioning belt. \n As you can see, there is a number to the left of the brands (15 through 20). \n Simply type the corresponding number: ")

density_data = {
    "15" : df.iloc[15,5],
    "16" : df.iloc[16,5],
    "17" : df.iloc[17,5],
    "18" : df.iloc[18,5],
    "19" : df.iloc[19,5],
    "20" : df.iloc[20,5]
}

span_length = float(input("span length [mm]: "))
belt_mass = density_data[select_belt_brand]
belt_width = float(input("belt width [mm]: "))
pulley_diameter = float(input("pulley diameter [mm]: "))
RMS_Torque = float(input("RMS Torque [N*m]: "))
Tension = RMS_Torque / (pulley_diameter/2000)

Frequency = np.sqrt(Tension / (belt_width * belt_mass * 4 * (((span_length)/1000)**2) ))
margin = 0.05 * Frequency

upper_margin = (round(math.ceil((Frequency + margin))))+1
lower_margin =  (round(math.floor((Frequency - margin))))-1

print("\n Between:\n", upper_margin," Hz","\n", lower_margin," Hz")
