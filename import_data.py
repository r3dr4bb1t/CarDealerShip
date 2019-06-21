import pandas
from .search.models import Car

def get_categories():
    df = pandas.read_excel('Car_Category_data.xlsx')

    #print the column names
    print(df.columns)

    #get the values for a given column
    brand = df['브랜드'].values
    print (brand)
    #get a data frame with selected columns
    FORMAT = [ '브랜드', '차종','모델' ]
    print(df[FORMAT])
    return
