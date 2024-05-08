# Author: Mengfei Zhao
# Date: 2024.05.08

import csv
import pandas as pd
import numpy as np
import os
import sys


def show_help_info():
    print("\nAuthor: Mengfei Zhao")
    print("Mail: 18037198823@163.com")
    print("Date: 2024.05.08")
    print("Version: v1\n")
    print("This is the help information.")
    print("Please delete all headers and tails (include the END word and the blank lines after it) of your .csv file, and make sure your .csv file look like this:")
    print("Freq(Hz),S11(DB),S11(DEG),S22(DB),S22(DEG),S21(DB),S21(DEG)")
    print("10000000,-27.235962,7.171164,-25.624048,-13.239027,-0.28209287,-66.807648")
    print("...")
    print("...")
    print("500000000,-27.235962,7.171164,-25.624048,-13.239027,-0.28209287,-66.807648\n\n")
    print("You can modify this script file according to your condition.\n")


def convert_csv_to_s2p(csv_filename):
    with open(csv_filename, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    # get the name of column
    header = data[0]

    # convert to DataFrame
    df = pd.DataFrame(data[1:], columns=header)

    # convert column to numerical type
    df["Freq(Hz)"] = df["Freq(Hz)"].astype(float)
    df["S11(DB)"] = df["S11(DB)"].astype(float)
    df["S11(DEG)"] = df["S11(DEG)"].astype(float)
    df["S22(DB)"] = df["S22(DB)"].astype(float)
    df["S22(DEG)"] = df["S22(DEG)"].astype(float)
    df["S21(DB)"] = df["S21(DB)"].astype(float)
    df["S21(DEG)"] = df["S21(DEG)"].astype(float)

    # calculate Real part and Imaginary part
    # S11
    S11_term1 = (10 ** (df["S11(DB)"] / 20)) ** 2
    S11_term2 = 1 + (np.tan(df["S11(DEG)"]))**2
    S11_R = (S11_term1 / S11_term2) ** 0.5
    S11_I = S11_R * np.tan(df["S11(DEG)"])

    # S22
    S22_term1 = (10 ** (df["S22(DB)"] / 20)) ** 2
    S22_term2 = 1 + (np.tan(df["S22(DEG)"]))**2
    S22_R = (S22_term1 / S22_term2) ** 0.5
    S22_I = S22_R * np.tan(df["S22(DEG)"])

    # S21
    S21_term1 = (10 ** (df["S21(DB)"] / 20)) ** 2
    S21_term2 = 1 + (np.tan(df["S21(DEG)"]))**2
    S21_R = (S21_term1 / S21_term2) ** 0.5
    S21_I = S21_R * np.tan(df["S21(DEG)"])

    # S12
    S12_R = S21_R
    S12_I = S21_I

    # write content to a file
    arr_Hz = np.array([df["Freq(Hz)"].values])  # unit is Hz
    arr_S11_R = np.array([S11_R.values])
    arr_S11_I = np.array([S11_I.values])
    arr_S21_R = np.array([S21_R.values])
    arr_S21_I = np.array([S21_I.values])
    arr_S12_R = np.array([S12_R.values])
    arr_S12_I = np.array([S12_I.values])
    arr_S22_R = np.array([S22_R.values])
    arr_S22_I = np.array([S22_I.values])

    arr_out = (np.concatenate((arr_Hz, arr_S11_R, arr_S11_I, arr_S21_R,
               arr_S21_I, arr_S12_R, arr_S12_I, arr_S22_R, arr_S22_I), axis=0)).T
    output_filename = "out.csv"
    np.savetxt(output_filename, arr_out, delimiter=" ")

    # insert header into this file,
    header = "!Keysight Technologies\n!Date: 2024.05.08\n!Correction: S11(Full 2 Port(1,2))\n!S21(Full 2 Port(1,2))\n!S12(Full 2 Port(1,2))\n!S22(Full 2 Port(1,2))\n!S2P File: Measurements: S11, S21, S12, S22:\n# Hz S  RI   R 50\n"
    with open(output_filename, 'r+') as f:
        original_content = f.read()
        f.seek(0)  # move pointer to the start of the file
        f.write(header)
        f.write(original_content)
    f.close()

    out_filename = "out.s2p"
    os.remove(out_filename)
    os.rename(output_filename, out_filename)
    print("\nConversion done.\n\n")
    print("The out.s2p is the generated s2p file.\n")


arg1 = sys.argv[1]

if arg1 == "-h":
    show_help_info()
else:
    csv_filename = arg1
    convert_csv_to_s2p(csv_filename)
