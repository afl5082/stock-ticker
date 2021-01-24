import requests
from bs4 import BeautifulSoup
import time
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import pygame
import urllib

internet = False


def tickers():
    i = 1
    while True:
        day_end = False
        # ticker1
        current_hour = datetime.today().hour
        current_hr_min = str((datetime.today().strftime("%I:%M")))

        if current_hour >= 16 or current_hr_min <= "09:29":
            day_end = True

        symbol = '^DJI'
        tickerData = yf.Ticker(symbol)
        tickerDF = tickerData.history(period='1d', interval='1m')
        tickerDF_yesterday = tickerData.history(period='2d')

        if day_end == False:
            price = float(tickerDF.iloc[-1]['Close'])
        else:
            price = float(tickerDF_yesterday.iloc[-1]['Close'])

        open_ = float(tickerDF_yesterday.iloc[0]['Close'])

        change_ = float((price / open_) - 1)
        o_ch = ("{:.2f}".format(price - open_))
        percent_change = ("{:.2f}".format((change_ * 100)) + '%')

        if change_ == 0:
            ourColor = white
        elif change_ > 0:
            ourColor = green
        else:
            ourColor = red
        # ticker2

        symbol2 = '^GSPC'
        tickerData2 = yf.Ticker(symbol2)
        tickerDF2 = tickerData2.history(period='1d', interval='1m')
        tickerDF_yesterday2 = tickerData2.history(period='2d')

        if day_end == False:
            price2 = float(tickerDF2.iloc[-1]['Close'])
        else:
            price2 = float(tickerDF_yesterday2.iloc[-1]['Close'])

        open_2 = float(tickerDF_yesterday2.iloc[0]['Close'])

        change_2 = float((price2 / open_2) - 1)
        o_ch2 = ("{:.2f}".format(price2 - open_2))
        percent_change2 = ("{:.2f}".format((change_2 * 100)) + '%')

        if change_2 == 0:
            ourColor2 = white
        elif change_2 > 0:
            ourColor2 = green
        else:
            ourColor2 = red
        # ticker 3
        symbol3 = '^IXIC'
        tickerData3 = yf.Ticker(symbol3)
        tickerDF3 = tickerData3.history(period='1d', interval='1m')
        tickerDF_yesterday3 = tickerData3.history(period='2d')

        if day_end == False:
            price3 = float(tickerDF3.iloc[-1]['Close'])
        else:
            price3 = float(tickerDF_yesterday3.iloc[-1]['Close'])

        open_3 = float(tickerDF_yesterday3.iloc[0]['Close'])

        change_3 = float((price3 / open_3) - 1)
        o_ch3 = ("{:.2f}".format(price3 - open_3))
        percent_change3 = ("{:.2f}".format((change_3 * 100)) + '%')

        if change_3 == 0:
            ourColor3 = white
        elif change_3 > 0:
            ourColor3 = green
        else:
            ourColor3 = red

        if price - open_ > 0:
            plus = '+'
        else:
            plus = ''
        if price2 - open_2 > 0:
            plus2 = '+'
        else:
            plus2 = ''
        if price3 - open_3 > 0:
            plus3 = '+'
        else:
            plus3 = ''

        # displaying rendering, placement on the screen
        stockname = font.render('DJIA' + '    ' + ("{:.2f}".format(price)),
                                True, white)
        stocknameRect = stockname.get_rect()
        stocknameRect.center = (infoObject.current_w / 2,
                                infoObject.current_h / 2 - 80)
        text = font.render(
            '(' + plus + str(o_ch) + '  ,  ' + plus + percent_change + ')',
            True, ourColor)
        textRect = text.get_rect()
        textRect.center = (infoObject.current_w / 2,
                           infoObject.current_h / 2 - 40)

        stockname2 = font.render('S&P' + '    ' + ("{:.2f}".format(price2)),
                                 True, white)
        stocknameRect2 = stockname2.get_rect()
        stocknameRect2.center = (infoObject.current_w / 2,
                                 infoObject.current_h / 2 - 180)
        text2 = font.render(
            '(' + plus2 + str(o_ch2) + '  ,  ' + plus2 + percent_change2 + ')',
            True, ourColor2)
        textRect2 = text2.get_rect()
        textRect2.center = (infoObject.current_w / 2,
                            infoObject.current_h / 2 - 140)

        stockname3 = font.render('NASDAQ' + '    ' + ("{:.2f}".format(price3)),
                                 True, white)
        stocknameRect3 = stockname3.get_rect()
        stocknameRect3.center = (infoObject.current_w / 2,
                                 infoObject.current_h / 2 + 20)
        text3 = font.render(
            '(' + plus3 + str(o_ch3) + '  ,  ' + plus3 + percent_change3 + ')',
            True, ourColor3)
        textRect3 = text3.get_rect()
        textRect3.center = (infoObject.current_w / 2,
                            infoObject.current_h / 2 + 60)

        today = str(datetime.today().strftime("%B %d, %Y - %I:%M%p"))

        text4 = font_date.render(today, True, grey)
        textRect4 = text4.get_rect()
        textRect4.center = (infoObject.current_w / 2,
                            infoObject.current_h / 2 + 300)

        #loop to display all texts
        if i > 0:
            display_surface.fill(black)
            display_surface.blit(stockname, stocknameRect)
            display_surface.blit(text, textRect)
            display_surface.blit(stockname2, stocknameRect2)
            display_surface.blit(text2, textRect2)
            display_surface.blit(stockname3, stocknameRect3)
            display_surface.blit(text3, textRect3)
            display_surface.blit(text4, textRect4)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            i += 1
        pygame.time.wait(60)  # 1 second = 1000
        #https://stackoverflow.com/questions/51411713/pygame-time-wait-crashes-the-program


def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


while internet == False:

    connected = connected()
    if connected == True:
        pygame.init()
        X = 480
        Y = 320

        infoObject = pygame.display.Info()
        display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        font = pygame.font.Font('Bebas-Regular.otf', 40, bold=True)
        font_date = pygame.font.Font('Bebas-Regular.otf', 30, bold=True)

        # colors
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        black = (0, 0, 0)
        grey = (220, 220, 220)
        internet = True
        tickers()

    else:
        #sleep for 5 minutes and check internet again
        time.sleep(300)
