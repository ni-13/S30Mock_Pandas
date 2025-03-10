# Mock_Pandas

# 620. Not Boring Movies_Solution

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')].sort_values('rating', ascending=False)

______________________________________________________________________________________________________________________________________

# 619. Biggest Single Number_Solution

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    unique_numbers = my_numbers.groupby('num').filter(lambda x: len(x) == 1)
    max_value = unique_numbers['num'].max()    
    return pd.DataFrame({'num': [max_value]})

______________________________________________________________________________________________________________________________________

# 1084. Sales Analysis III_Solution

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby(['product_id'], as_index = False).agg(min=('sale_date', 'min'), max=('sale_date', 'max'))
    df= df[(df['min'] >='2019-01-01') & (df['max'] <='2019-03-31')].merge(product).iloc[:,[0,3]]
    return df

______________________________________________________________________________________________________________________________________

# 1158. Market Analysis I_Solution

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] < '2020-01-01')][['order_id', 'buyer_id']]
    orders = orders.groupby('buyer_id').count().reset_index()
    df = users.merge(orders, how='left', left_on='user_id', right_on='buyer_id').rename(columns={'order_id': 'orders_in_2019'})
    df = df[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id': 'buyer_id'})
    return df.fillna(0)       
