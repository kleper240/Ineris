import numpy as np
import pandas as pd

# FUNCTION TO FORMAT COLUMNS TITLE
def columns_title_format(self):
    data_columns = list(self.processed_data.columns)
    data_columns = [col.replace(' ', '_').capitalize() for col in data_columns]
    self.processed_data.columns = data_columns
    print("Formatted columns title")
    return self.processed_data
# FUNCTION TO REPLACE EMPTY SPACES IN DATAFRAME
def replace_space(self):
        df = self.processed_data.select_dtypes(include=['object'])
        df = df.stack().str.replace(' ', '_').unstack()
        # modif du 8/2/2023
        for col in df.columns:
            self.processed_data[col] = df[col]
        return self.processed_data
# FUNCTION TO CALL METHODS FOR DESCRIBING DATAFRAME
def data_desc(self):
        print(self.processed_data.dropna(how = 'all').shape) #pour voir si certaines lignes comportent des valeurs NaN partout (Non)
        return(self.processed_data.info())

# function to transform all "object" variable to lower case
def unify_objectvariables_case(dataset):
    object_cols = dataset.select_dtypes(include=['object'])
    for col in object_cols.columns:
        dataset[col] = dataset[col].str.lower()
    print('Case-formatted data shape is:', dataset.shape)
    return dataset

# Function to create a new dataframe with column types
def col_type_table(df_clean):
# Create a dataframe to store the column names and data types
    df_data_type = pd.DataFrame({'Colonne' : list(df_clean.columns)})

# Add a new column to indicate the type of each column
def get_column_type(col):
    if address_pattern.search(col):
        return 'adresse'
    elif date_pattern.search(col):
        return 'date'
    elif geo_pattern.search(col):
        return 'coordonnées géographiques'
    else:
        return 'autre'

#Method to convert any date columns to datetime : 1st method 
# (takes into account only cases where date formats vary across columns)
def convert_to_datetime(df, date_columns):
    for col in date_columns:
        # Try different date formats one by one
        for fmt in [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d-%m-%Y %H:%M:%S',
        '%d-%m-%Y',
        '%m/%d/%Y %H:%M:%S',
        '%m/%d/%Y',
        '%m-%d-%Y %H:%M:%S',
        '%m-%d-%Y',
        '%d/%m/%Y %H:%M:%S',
        '%d/%m/%Y_%H:%M',
        '%d/%m/%Y']:
            try:
                # Try to convert the column to datetime using the current format
                df[col] = pd.to_datetime(df[col], format=fmt)
                print(f"Format {fmt} worked for column {col}")
                break # If successful, break out of the loop and move to the next column
            except:
                print(f"Format {fmt} didn't work for column {col}")
                pass # If conversion fails, move to the next format
    return df

#Method to convert any date columns to datetime : 2nd method 
# (takes into account cases where date formats vary across rows within the same column)
def convert_to_datetime_bis(df, date_columns):
    for col in date_columns:
        # Check if the column contains any non-string values
        if np.issubdtype(df[col].dtype, np.number):
            # Convert float values to string
            df[col] = df[col].astype(str)
        # Iterate over each value in the column
        # Convert string values to datetime using dateutil.parser.parse
        df[col] = [dateutil.parser.parse(x) for x in df[col]]
    return df
# Methode redondante avec la detection des types de colonnes plus haut

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

# Function to detect projections in Geocoordinates
def detect_projection(df, lon_col, lat_col):
    
    # Check if the values in the longitude and latitude columns are within geographic coordinate range
    geo_mask = (df[lon_col] >= -180) & (df[lon_col] <= 180) & \
               (df[lat_col] >= -90) & (df[lat_col] <= 90)
    
    # Create a new column 'Projection' with the corresponding values
    df['Projection'] = np.where(geo_mask, 'Not_projected', 'Projected')
    
    return df