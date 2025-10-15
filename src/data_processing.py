"""
Data Processing Module for DATA1002 Project

This module contains utility functions for data loading, cleaning, and preprocessing.
"""

import numpy as np
import pandas as pd
from typing import Optional, List, Tuple


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        raise
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        raise


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Check for missing values in the dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.Series: Count of missing values per column
    """
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'Missing_Count': missing,
        'Percentage': missing_pct
    })
    
    return missing_df[missing_df['Missing_Count'] > 0]


def handle_missing_values(df: pd.DataFrame, 
                         strategy: str = 'drop',
                         columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Handle missing values in the dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        strategy (str): Strategy for handling missing values ('drop', 'mean', 'median', 'mode')
        columns (List[str], optional): Specific columns to process
        
    Returns:
        pd.DataFrame: Dataframe with missing values handled
    """
    df_copy = df.copy()
    
    if columns is None:
        columns = df_copy.columns
    
    if strategy == 'drop':
        df_copy = df_copy.dropna(subset=columns)
    elif strategy == 'mean':
        for col in columns:
            if df_copy[col].dtype in ['float64', 'int64']:
                df_copy[col].fillna(df_copy[col].mean(), inplace=True)
    elif strategy == 'median':
        for col in columns:
            if df_copy[col].dtype in ['float64', 'int64']:
                df_copy[col].fillna(df_copy[col].median(), inplace=True)
    elif strategy == 'mode':
        for col in columns:
            mode_values = df_copy[col].mode()
            if not mode_values.empty:
                df_copy[col].fillna(mode_values[0], inplace=True)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    
    return df_copy


def detect_outliers(df: pd.DataFrame, 
                    column: str, 
                    method: str = 'iqr',
                    threshold: float = 1.5) -> Tuple[pd.Series, int]:
    """
    Detect outliers in a numerical column.
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column name to check for outliers
        method (str): Method for outlier detection ('iqr' or 'zscore')
        threshold (float): Threshold for outlier detection
        
    Returns:
        Tuple[pd.Series, int]: Boolean series indicating outliers and count
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        outliers = (df[column] < lower_bound) | (df[column] > upper_bound)
    
    elif method == 'zscore':
        std_val = df[column].std()
        if std_val != 0:
            z_scores = np.abs((df[column] - df[column].mean()) / std_val)
            outliers = z_scores > threshold
        else:
            # If std is 0, all values are identical, so no outliers
            outliers = pd.Series([False] * len(df[column]), index=df[column].index)
    
    else:
        raise ValueError(f"Unknown method: {method}")
    
    outlier_count = outliers.sum()
    print(f"Detected {outlier_count} outliers in column '{column}' using {method} method")
    
    return outliers, outlier_count


def normalize_data(df: pd.DataFrame, 
                   columns: List[str],
                   method: str = 'minmax') -> pd.DataFrame:
    """
    Normalize numerical columns in the dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (List[str]): Columns to normalize
        method (str): Normalization method ('minmax' or 'zscore')
        
    Returns:
        pd.DataFrame: Dataframe with normalized columns
    """
    df_copy = df.copy()
    
    for col in columns:
        if method == 'minmax':
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            if max_val != min_val:
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
            else:
                # If all values are identical, set to 0
                df_copy[col] = 0
        
        elif method == 'zscore':
            mean_val = df_copy[col].mean()
            std_val = df_copy[col].std()
            if std_val != 0:
                df_copy[col] = (df_copy[col] - mean_val) / std_val
            else:
                df_copy[col] = 0
        
        else:
            raise ValueError(f"Unknown normalization method: {method}")
    
    return df_copy


def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get comprehensive summary statistics for the dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Summary statistics
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    summary = df[numeric_cols].describe()
    
    # Add additional statistics
    summary.loc['variance'] = df[numeric_cols].var()
    summary.loc['skewness'] = df[numeric_cols].skew()
    summary.loc['kurtosis'] = df[numeric_cols].kurtosis()
    
    return summary


if __name__ == "__main__":
    # Example usage
    print("Data Processing Module for DATA1002 Project")
    print("Import this module to use the data processing functions")
