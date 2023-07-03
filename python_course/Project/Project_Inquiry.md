# Project inquiry: MVP application for portfolio overview

Dear Python Experts, 

we reach you to ask your assistance in programming an MVP for a new
portfolio application.

During this project phase, we would like to work with you on the first functionalities to showcase
the potential final product.

The following features we see as vital to have in an MVP:
- **showcase visualizations for the user**
  - **Crucial**:
    - price of each position over time
    - portfolio aggregated profit and loss figures including top 2 and flop 2 assets
  - any thing more is nice to have. Mid-term vision: industry leading visualizations and UI
- although you can expect us to have a working python 3.10 and conda setup, **please provide us 
with installation and run documentation**.
- find a test portfolio attached together with historic data to start with.
  - If you could make the portfolio assets configurable, this would be greatly appreciated. An easy text base interface that could, if needed, be filled by the user, should be preferred (e.g. in a json file).
  - If you would like to update the data or download newer data, always be aware of violation of Terms and Services. These are no joke.

Further features could be interesting but have lower priority. If you have time, you could possibly have a look into:
- Include an automatic update to the application
- Enable the application to run as a python script
- Add information and interactive elements to the visualizations
- Provide an asset price prediction over an adequate period of time (minimum next closing day)
- make an application user interface (GUI or web based)

First __MVP evaluation__ should be ready until __13th of July 3pm__. __Final pitch is Friday 15th of July__ with the opportunity to present the solution during a __certificates ceremony event in the afternoon (max. 5 minutes)__.

Thanks for considering being our implementation partner.

---

Find some historic data, here:
- [Stock Market data](https://1drv.ms/u/s!Ar_sBvdvknEqhlR8uBwgckiC5atW?e=cTdq8f)
- Example portfolio:

```json
{'GOOGL': {'order_volume': [100], 'order_date': ['2010-07-09']},
 'TM': {'order_volume': [132], 'order_date': ['1997-05-01']},
 'TSM': {'order_volume': [5], 'order_date': ['2009-11-3']},
 'LPL': {'order_volume': [186], 'order_date': ['2011-12-06']},
 'PLUG': {'order_volume': [86], 'order_date': ['2018-08-24']},
 'ED': {'order_volume': [10], 'order_date': ['2007-01-03']},
 'ICLN': {'order_volume': [251], 'order_date': ['2009-07-01']}}
 ```

 - Portfolio of the test users

 ```json
 portfolio_test = {
    "BABA": {
        "order_volume": [42],
        "order_date": ["2017-06-30"]
    },
    "CEA": {
        "order_volume": [261],
        "order_date": ["2012-12-27"]
    },
    "AIIQ": {
        "order_volume": [27],
        "order_date": ["2018-06-06"]
    }, 
    "DBEM": {
        "order_volume": [99],
        "order_date": ["2016-03-21"]
    },
    "URTH": {
        "order_volume": [426],
        "order_date": ["2012-01-17"]
    },
    "AIO": {
        "order_volume": [25],
        "order_date": ["2007-12-06"]
    },
    "BST": {
        "order_volume": [1002],
        "order_date": ["2005-01-13"]
    }
}
```
