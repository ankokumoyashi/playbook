import pandas as pd
import polars as pl
from stop_watch import stop_watch
import time

def main():
    input_csv = "./data/japanese_quiz_100000.csv"
    input_parquet = "./data/japanese_quiz_100000.parquet"

    #pd_df = pandas_read_csv(input_csv)
    pd_df = pandas_read_parquet(input_parquet)
    #pl_df = polars_read_csv(input_csv)
    pl_df = polars_read_parquet(input_parquet)

    function(pl_df)
    with pl.Config() as cfg:
        cfg.set_tbl_cols(-1)  
        cfg.set_tbl_rows(-1)  
        cfg.set_fmt_str_lengths(1000)  
        print(pl_df)

    pd_df = pandas_read_csv_filter_column(input_csv)
    pd_df = pandas_read_parquet_filter_column(input_parquet)
    pl_df = polars_read_csv_filter_column(input_csv)
    pl_df = polars_read_parquet_filter_column(input_parquet)

@stop_watch
def function(df):
    import ipdb;ipdb.set_trace()
    df = df.select(pl.col("qid").filter(pl.col("answer_entity") == "コックリさん"))
    #df = df.select([pl.col("qid").sort().head(2), pl.col("answer_entity")])
    return df

@stop_watch
def polars_read_csv(input_path):
    return pl.read_csv(input_path)

@stop_watch
def polars_read_parquet(input_path):
    return pl.scan_parquet(input_path)
    
@stop_watch
def pandas_read_csv(input_path):
    return pd.read_csv(input_path)

@stop_watch
def pandas_read_parquet(input_path):
    return pd.read_parquet(input_path)

@stop_watch
def polars_read_parquet_filter_column(input_path):
    return pl.read_parquet(input_path, columns=['answer_entity'])

@stop_watch
def polars_read_csv_filter_column(input_path):
    return pl.read_csv(input_path, columns=['answer_entity'])

@stop_watch
def pandas_read_parquet_filter_column(input_path):
    return pd.read_parquet(input_path, columns=['answer_entity'])

@stop_watch
def pandas_read_csv_filter_column(input_path):
    return pd.read_csv(input_path, usecols=['answer_entity'])

if __name__ == "__main__":
    main()
    if False:
        print(pl_df.filter(pl.col("sepal_length") > 5)
              .groupby("species", maintain_order=True)
              .agg(pl.all().sum())
        )
