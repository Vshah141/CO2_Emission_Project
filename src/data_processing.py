import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Data_Ingestion(path):
    df = pd.read_csv(path)
    return df

def Data_Analysis(data):
    # print(data.head(5))
    # print(data.dtypes)
    make_counts = data['MAKE'].value_counts()
    # Plot bar chart for 'MAKE'
    # plt.figure(figsize=(10, 6))
    # make_counts.plot(kind='bar')
    # plt.title('Counts of Vehicles by Make')
    # plt.xlabel('Make')
    # plt.ylabel('Count')
    # plt.xticks(rotation=90)
    # plt.show()

    # Counts of unique values in 'VEHICLECLASS'
    vehicle_class_counts = data['VEHICLECLASS'].value_counts()
    # Plot bar chart for 'VEHICLECLASS'
    # plt.figure(figsize=(10, 6))
    # vehicle_class_counts.plot(kind='bar', color='orange')
    # plt.title('Counts of Vehicles by Vehicle Class')
    # plt.xlabel('Vehicle Class')
    # plt.ylabel('Count')
    # plt.xticks(rotation=90)
    # plt.show()
    print(data.isnull().sum())

def Data_Visualisation(data):
    new_df = data[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    # plt.scatter(new_df.FUELCONSUMPTION_COMB, new_df.CO2EMISSIONS,  color='blue')
    # plt.xlabel("FUELCONSUMPTION_COMB")
    # plt.ylabel("Emission")
    # plt.show()
    # plt.scatter(new_df.ENGINESIZE, new_df.CO2EMISSIONS,  color='red')
    # plt.xlabel("Engine size")
    # plt.ylabel("Emission")
    # plt.show()
    # plt.scatter(new_df.CYLINDERS, new_df.CO2EMISSIONS,  color='green')
    # plt.xlabel("Cylinders")
    # plt.ylabel("Emission")
    # plt.show()
    return new_df
