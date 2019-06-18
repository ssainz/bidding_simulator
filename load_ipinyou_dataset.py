import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list_of_files_suffix = ["20130606.txt", "20130607.txt", "20130608.txt", "20130609.txt", "20130610.txt", "20130611.txt",
                        "20130612.txt"]
list_of_bidding_files = []
list_of_impression_files = []
list_of_click_files = []
list_of_conversion_files = []

for file_name in list_of_files_suffix:
    list_of_bidding_files.append("bid." + file_name)
    list_of_impression_files.append("imp." + file_name)
    list_of_click_files.append("clk." + file_name)
    list_of_conversion_files.append("conv." + file_name)

bidding_header = ["bid_id", "timestamp", "ipinyou_id", "user_agent", "ip", "region_id", "city_id", "ad_exchange",
                  "domain", "url", "anonymous_url", "ad_slot_id", "ad_slot_width", "ad_slot_height",
                  "ad_slot_visibility", "ad_slot_format", "ad_slot_floor_price", "creative_id", "bidding_price",
                  "advertiser_id", "user_profile_ids"]

datatypes_dict = {}
datatypes_dict["bid_id"]=np.str
datatypes_dict["timestamp"]=np.str
datatypes_dict["log_type"]=np.int64
datatypes_dict["ipinyou_id"]=np.str
datatypes_dict["user_agent"]=np.str
datatypes_dict["ip"]=np.str
datatypes_dict["region_id"]=np.int64
datatypes_dict["city_id"]=np.int64
datatypes_dict["ad_exchange"]=np.int64
datatypes_dict["domain"]=np.str
datatypes_dict["url"]=np.str
datatypes_dict["anonymous_url"]=np.str
datatypes_dict["ad_slot_id"]=np.str
datatypes_dict["ad_slot_width"]=np.int64
datatypes_dict["ad_slot_height"]=np.int64
datatypes_dict["ad_slot_visibility"]=np.str
datatypes_dict["ad_slot_format"]=np.str
datatypes_dict["ad_slot_floor_price"]=np.int64
datatypes_dict["creative_id"]=np.str
datatypes_dict["bidding_price"]=np.int64
datatypes_dict["paying_price"]=np.int64
datatypes_dict["landing_page_url"]=np.str
datatypes_dict["advertiser_id"]=np.str
datatypes_dict["user_profile_ids"]=np.str

other_header = ["bid_id", "timestamp", "log_type", "ipinyou_id", "user_agent", "ip", "region_id", "city_id",
                "ad_exchange", "domain", "url", "anonymous_url", "ad_slot_id", "ad_slot_width", "ad_slot_height",
                "ad_slot_visibility", "ad_slot_format", "ad_slot_floor_price", "creative_id", "bidding_price",
                "paying_price", "landing_page_url", "advertiser_id", "user_profile_ids"]

folder_path = "/media/onetbssd/bidding_simulator/ipinyou.contest.dataset-season2/training2nd/"


def load_set_files(list_of_files, folder_path, headers, dtypes_list):
    list_of_df = []
    for file_name in list_of_files:
        df = pd.read_csv(folder_path + file_name, sep='\t', header=None, names=headers, dtype=dtypes_list)
        list_of_df.append(df)
    df = pd.concat(list_of_df)
    return df

def print_histogram(column, prefix_title):
    m_title = prefix_title + ":" + column.name
    m_title_file = prefix_title + "_" + column.name
    bins_number = 100
    if column.dtype == np.dtype("object"):
        fig = column.value_counts().hist(bins=bins_number)
        fig.set_title(m_title)
        #plt.show()
        plt.savefig("images/" +m_title_file + ".png")
        plt.close()
    elif column.dtype == np.dtype("int64"):
        fig = column.hist(bins=bins_number)
        fig.set_title(m_title)
        #plt.show()
        plt.savefig("images/" +m_title_file + ".png")
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
    unique_val = str(df_desc[column.name]["unique"])
    example_val = str(df_desc[column.name]["top"])
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


conversion_df = load_set_files(list_of_conversion_files,folder_path ,  other_header, datatypes_dict)
conversion_description = conversion_df.describe(include="all")
print_dataframe_histogram(conversion_df, "conversion")
print_latex(conversion_df, conversion_description, "conversion")
print("Finish with conversions")


click_df = load_set_files(list_of_click_files,folder_path ,  other_header, datatypes_dict)
click_description = click_df.describe(include="all")
print_dataframe_histogram(click_df, "click")
print_latex(click_df, click_description, "click")

print("Finish with clicks")


impression_df = load_set_files(list_of_impression_files,folder_path ,  other_header, datatypes_dict)
impression_description = impression_df.describe(include="all")
print_dataframe_histogram(impression_df, "impression")
print_latex(impression_df, impression_description, "impression")

print("Finish with impressions")

bid_df = load_set_files(list_of_bidding_files, folder_path , bidding_header, datatypes_dict)
bid_description = bid_df.describe(include="all")
print_dataframe_histogram(bid_df, "bids")
print_latex(bid_df, bid_description, "bids")

print("Finish with bids")




