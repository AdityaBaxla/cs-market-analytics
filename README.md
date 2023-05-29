# cs-market-analytics
different tools to get some insigths into csgo marketplace 

# To-Do list

## Get intrinsic value of csgo items

## predit movement of prices

### analytics of price history :
-   get realtime data from csgo community market 
-   example https://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name=Falchion%20Case
-   cleanup the data
-   use data science models to best fit approximation
-   take new price data and imporve the model
-   A Vector Autoregressive (VAR) might be suitable for this problem. Consider a vector of yt=(y1,t,y2,t,…,yn,t)′
 where the different y
s are the variables you have collected, and for example y1
 is the variable you are interested in modelling, status of a system, and the n
 other variables you mentioned. You can fit the following model, yt=β0+β1yt−1+β2yt−2+⋯+βpyt−p+ϵt
, by OLS/GLS, where ϵt
 is the residuals which is IIDN N(0,Σϵ)
. You can use this model to predict the future values of you dependent variable, by regressing on the past values of the dependent variable and the other variables you have collected. Is this what you are looking for? I'd recommend testing the individual series for unit roots first, and difference the series if there are unit roots present.

## currency codes in steam
1 - USD / United States Dollar
2 - GBP / United Kingdom Pound
3 - EUR / European Union Euro
4 - CHF / Swiss Francs
5 - RUB / Russian Rouble
6 - PLN / Polish Złoty
7 - BRL / Brazilian Reals
8 - JPY / Japanese Yen
9 - NOK / Norwegian Krone
10 - IDR / Indonesian Rupiah
11 - MYR / Malaysian Ringgit
12 - PHP / Philippine Peso
13 - SGD / Singapore Dollar
14 - THB / Thai Baht
15 - VND / Vietnamese Dong
16 - KRW / South Korean Won
17 - TRY / Turkish Lira
18 - UAH / Ukrainian Hryvnia
19 - MXN / Mexican Peso
20 - CAD / Canadian Dollars
21 - AUD / Australian Dollars
22 - NZD / New Zealand Dollar
23 - CNY / Chinese Renminbi (yuan)
24 - INR / Indian Rupee
25 - CLP / Chilean Peso
26 - PEN / Peruvian Sol
27 - COP / Colombian Peso
28 - ZAR / South African Rand
29 - HKD / Hong Kong Dollar
30 - TWD / New Taiwan Dollar
31 - SAR / Saudi Riyal
32 - AED / United Arab Emirates Dirham
33 - SEK / Swedish Krona
34 - ARS / Argentine Peso
35 - ILS / Israeli New Shekel
36 - BYN / Belarusian Ruble
37 - KZT / Kazakhstani Tenge
38 - KWD / Kuwaiti Dinar
39 - QAR / Qatari Riyal
40 - CRC / Costa Rican Colón
41 - UYU / Uruguayan Peso
42 - BGN / Bulgarian Lev
43 - HRK / Croatian Kuna
44 - CZK / Czech Koruna
45 - DKK / Danish Krone
46 - HUF / Hungarian Forint
47 - RON / Romanian Leu

### analyise supply:
-   keep a tab on all the listings and sales to get the data
-   use data to predict the supply and demand of the items
-   how may majors a team has participated in

### assess looks of the skins/ stickers
- make an ai model to rate the looks of skins on objective measures from the scale of 1 - 10 or 1 - 100

### social metrics 
- monitor what social media is talking about what skins and rate the popularity index from 1 - 10

### uniqueness and authenticity
- items by famous artists
- some sentimental value of items to the community

### utility and functionality
- scratch patterns
- hidden eatereggs
