import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


headers = ["click" , "market_price", "theta_x"]
datatypes_dict = {}
datatypes_dict["click"] = np.int64
datatypes_dict["market_price"] = np.int64
datatypes_dict["theta_x"] = np.double


def get_dataframe(file_name):
    m_df = pd.read_csv(file_name, sep=' ', header=None, names=headers)
    return m_df



def print_histogram(column, prefix_title):
    m_title = prefix_title + ":" + column.name
    m_title_file = "preprocessed_" + column.name
    bins_number = 100
    if column.dtype == np.dtype("object"):
        fig = column.value_counts().hist(bins=bins_number)
        fig.set_title(m_title)
        #plt.show()
        plt.savefig("images_hancai/" +m_title_file + ".png")
        plt.close()
    elif column.dtype == np.dtype("int64"):
        fig = column.hist(bins=bins_number)
        fig.set_title(m_title)
        #plt.show()
        plt.savefig("images_hancai/" +m_title_file + ".png")
        plt.close()
    elif column.dtype == np.dtype("double"):
        fig = column.hist(bins=bins_number)
        fig.set_title(m_title)
        #plt.show()
        plt.savefig("images_hancai/" +m_title_file + ".png")
        plt.close()

def print_dataframe_histogram(df, prefix_title):
    columns = list(df)
    for i in columns:
        print_histogram(df[i],prefix_title)


def print_latex(df, df_desc, prefix_title):
    columns = list(df)
    for i in columns:
        print_latex_column(df[i],df_desc,prefix_title)

def escape_underscore(strr):
    return strr.replace("_", "\\_")


def print_latex_column(column, df_desc, prefix_title):
    m_title = prefix_title + " : " + escape_underscore(column.name)
    file_name = prefix_title + "_" + column.name + ".png"
    max_val = str(df_desc[column.name]["max"])
    min_val = str(df_desc[column.name]["min"])
    avg_val = str(df_desc[column.name]["mean"])
    std_val = str(df_desc[column.name]["std"])
    count_val = str(df_desc[column.name]["count"])
    unique_val = str(column.nunique())
    is_number = True
    if column.dtype == np.dtype("object"):
        is_number = False
    print("\\subsection{" + m_title + "}" )
    print("\\begin{figure}" )
    print("\\centering" )
    print("\\includegraphics[width=\\linewidth]{images/" + file_name + "}" )
    print("\\caption{" + m_title + " histogram} " )
    print("\\label{fig:" + prefix_title + "\\_" + escape_underscore(column.name) + "}" )
    print("\\end{figure}" )
    print("\\begin{table}[]" )
    print("\\begin{tabular}{ll}")
    print("\\multicolumn{3}{c}{" + m_title + " stats} \\\\")
    print("\\hline \\\\")
    print("Count        & "+count_val+"  \\\\")
    print("Unique       & "+unique_val+" \\\\")
    if is_number:
        print("Avg       & " + avg_val + " \\\\")
        print("Std        & " + std_val + "  \\\\")
        print("Max        & " + max_val + "  \\\\")
        print("Min       & " + min_val + " \\\\")
    #print("Example       & " + example_val + " \\\\")
    print("\\end{tabular}")
    print("\\end{table}")


list_of_file_set = ["1458", "2259" , "2261", "2821", "2997", "3358","3386","3427","3476"]
folder_prefx = "/home/sergio/Projects/han-cai/rlb-dp/data/ipinyou-data/"
list_of_df = []
for file_set in list_of_file_set:
    print("loading dataset " + file_set)
    m_file = folder_prefx + file_set + "/test.theta.txt"
    df = get_dataframe(m_file)
    list_of_df.append(df)


df = pd.concat(list_of_df, axis=0)
df.reset_index(drop=True, inplace=True)
df_description = df.describe(include="all")
print_dataframe_histogram(df, "preprocessed")
print_latex(df, df_description, "preprocessed")
print("Finish with Real time bidding by Reinforcement Learning in Display Advertising dataset")





