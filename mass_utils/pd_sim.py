from typing import List, Any, Union
from faker import Faker
import pandas as pd
import numpy as np
from numpy.core._multiarray_umath import ndarray

fake = Faker()


def fake_boolean(n):
    """
        Generates a random list of unique company names that can be used as id keys

        Args:
            n (integer of sample size to be generated)

        Returns: A list of random booleans
    """
    boolean: List[Any] = []
    for _ in range(n):
        boolean.append((fake.pybool()))
    return boolean


def fake_category(n, p=(0.49, 0.29, 0.21, 0.01), c=("Medium", "Low", "High", "Unknown")):
    """
        Generates a categorical variable that can be used for one hotting

        Args:
            n (integer of sample size to be generated)
            p (a tuple of probabilities for the categorical distributions, must add to 1)
            c (a tuple of category string names, must match the number of discrete 'p')
        Returns: A list of string names
    """
    if not p:
        # default probabilities
        p = p
    c = c
    return np.random.choice(c, size=n, p=p).astype('str')

def fake_company(n):
    """
        Generates a random list of unique company names that can be used as id keys

        Args:
            n (integer of sample size to be generated)

        Returns: A list of string names
    """
    company: List[Any] = []
    for _ in range(n):
        company.append((fake.company()))
    return company


def random_normal(n, mu=0, sigma=0.1):
    """
        Generates a continuous random normal variable

        Args:
            n (integer of sample size to be generated)
            mu (float indicating the mean)
            sigma (the desired )
        Returns: An nd array of length n
    """
    mu, sigma = 0, 0.1  # mean and standard deviation
    rn: Union[ndarray, int, float, complex] = np.random.normal(mu, sigma, n)
    return rn


def random_dates(start, end, n):
    """
        Generates pandas datetime index of randomly selected dates
        Args:
            n (integer of dates to be samples)
            start (a string beginning date in the format 'YYYY-MM-DD')
            end (a string beginning date in the format 'YYYY-MM-DD')
    Returns pandas.core.indexes.datetimes.DatetimeIndex
    """

    start_u = start.value // 10 ** 9
    end_u = end.value // 10 ** 9

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


def fake_df(n):

    """
            Uses simulating functions to return a pandas Dataframe with mixed data types
            Args:
                n (number of rows in data set)

    Returns Pandas dataframe
    """
    df = pd.DataFrame(columns=['company', 'category', 'X1_normal_float', 'X2_normal_int64', 'X3_bool', 'date', 'date2',
                               'constant_int', 'constant_string', 'X3_normal_accidental_string',
                               'X4 !@#$%^&*() UNSafeInt', 'X5 )* :".,<>" UNSafeInt'])
    # Fake company name/id
    df['company'] = fake_company(n)
    # Fake string categorical with 4 categories default 0.49/0.29/0.21/0.01
    df['category'] = fake_category(n)
    # Fake random normal float
    df['X1_normal_float64'] = random_normal(n).astype('float64')
    # Simulated random normal int64
    df['X2_normal_int64'] = random_normal(n, 0, 10).astype('int64')
    # Simulated Boolean
    df['X3_bool'] = fake_boolean(n)
    # Simulated date field
    df['date'] = random_dates(pd.to_datetime('2020-01-01'), pd.to_datetime('2020-12-31'), n)
    # Second simulated date field for date diffs
    df['date2'] = random_dates(pd.to_datetime('2019-01-01'), pd.to_datetime('2019-12-31'), n)
    # Constant field
    df['constant_int'] = 2
    # Constant string field
    df['constant_string'] = 'thesamethingoverandover'
    # Numeric field 'accidentally in string format'
    df['X3_normal_accidental_string'] = random_normal(n, 5000, 100).astype('str')
    # Unsafe named variable
    df['X4 !@#$%^&*() UNSafeInt'] = random_normal(n, 200, 10).astype('int64')
    # Second unsafe named variable to apply batcxh safename function
    df['X5 )* :".,<>" UNSafeInt'] = random_normal(n, 10, 0.75).astype('float64')
    return df
