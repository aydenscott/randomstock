# randomstock
Simple python program that uses Selenium to retrieve random stock tickers that automatically open in a tab

## Usage
Program opens a website that displays a random stock ticker (https://raybb.github.io/random-stock-picker/) and saves the ticker to a list. The program can be configured to as many tickers as the user desires. This functionality is altered in the following code 

```while count != 5:```

where the integer (in this case 5) is the amount of tickers desired. Once all tickers are received after refreshing the page x amount of times, the program uses pyautogui to use (ctrl + t) to open a tab for each ticker plus the str(stock) to ensure google results are the stock. Thus, the limit to the amount of tickers you specify is in relation to your computer's power as x tickers means x amount of tabs opening simultaneously. 
