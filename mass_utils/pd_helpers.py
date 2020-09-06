# Dupe check

def dupe_check(df, field):
    """
     Returns a single column Pandas DataFrame that displays all columns
     with % missing greater than 0

     Args:
        df (Pandas dataframe): Dataframe of interest
        field (Pandas dataframe column): The column that you want to check for duplicates. Usually an ID key


     Returns: A raw count of the duplicate records and the total row length of the data frame

     """
    df_size = len(df)
    acc_size = len((set(df[field])))
    print("There are " + str((df_size - acc_size)) + " duplicate ids out of " + str(df_size) + "  total")


# missing check

def missing_check(df):
    """
     Returns a single column Pandas DataFrame lat displays all columns
     with % missing greater than 0

     Args:
        df (Pandas dataframe): Dataframe of interest



     Returns: A sorted dataframe displaying columns with missing values

     """
    missing = pd.DataFrame(100 * df.isnull().sum() / len(df))
    missing['pct_missing'] = missing[0]
    return missing[missing['pct_missing'] > 0].sort_values(by="pct_missing", ascending=False).drop([missing.columns[0]],
                                                                                                   axis='columns')


# Displays all the  columns of a data frame

def col_check(df):
    """
     Returns and prints a data frame listing all the columns
     in a given data set

     Args:
        df (Pandas dataframe): Dataframe of interest


     Returns: A printed dataframe displaying columns

    """
    cols = pd.DataFrame(df.columns)
    print(cols)


# Function to do frequency anlaysis

def freq_iter(df, cols):
    """


     Args:
       df(Pandas dataframe)
       cols (Pandas dataframe columns): A list of  categorical columns in a pandas data frame

     Returns: A list of dataa frames that have frequency distributions

    """
    dflist = []
    for i in cols:
        series = df[i]
        # Count the discrete values
        type_count = [[k, v] for k, v in Counter(series).items()]
        # Find the count of all discrete elements
        j = pd.DataFrame.from_records(type_count,
                                      index=range(len(type_count)),
                                      columns=['value', 'frequency'])
        j['percent'] = j.frequency / j.frequency.sum()
        j['cumulative_frequency'] = j.frequency.cumsum()
        j['cumulative_percent'] = j.cumulative_frequency / j.frequency.sum()
        j.columns = [series.name + '_' + i for i in j.columns]
        dflist.append(j)
    return dflist


# Function to do isolate mismatched records between pandas dataframes

def anti_join(df1, df2, on=None, left_on=None, right_on=None,
              index=False, left_index=False, right_index=False):
    """
    Selects entries from df1 that are not in df2, indexing by your choice of
    columns and indices from the right and left.

    Args:
        df1 (Pandas dataframe): Left dataframe.
        df2 (Pandas dataframe): Right dataframe.
        on (String): Columns if using the same one on both
        left_on (String): Left column if using a different one on each)
        right_on (String): Left column if using a different one on each
        index (Boolean): Whether or not to perform the antijoin on both index.
        left_index (Boolean): Whether to join on the left index.
        right_index (Boolean): Whether to join on the left index.

    Returns: A dataframe with the relevant entries removed.

    """
    if left_on and right_on:
        left = df1[left_on]
        right = df2[right_on]

    elif left_on and right_index:
        left = df1[left_on]
        right = df2.index

    elif left_index and right_on:
        left = df1.index
        right = df2[right_on]

    elif left_index and right_index:
        left = df1.index
        right = df2.index

    elif on:
        left = df1[on]
        right = df2[on]

    elif index:
        left = df1.index
        right = df2.index
    else:
        raise KeyError("Join on something!")

    return df1[~left.isin(right)]


# Hist function
def hist(df, target_variable):
    """

    """
    dist = df.hist(column=target_variable)
    display()
    return dist

# to - drop list
