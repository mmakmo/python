from datetime import datetime
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'Hiragino Kaku Gothic Pro, MigMix 1P'


def main():
    df_exchange = pd.read_csv(
        'boj/exchange.csv', encoding='cp932', header=1, names=['date', 'USD', 'rate'],
        skipinitialspace=True, index_col=0, parse_dates=True)
    df_jgbcm = pd.read_csv(
        'mof/jgbcm_all.csv', encoding='cp932', header=1, index_col=0, parse_dates=True,
        date_parser=parse_japanese_date, na_values=['-'])
    df_jobs = pd.read_excel('mhlw/第3表.xls', skiprows=3, skip_footer=2, parse_cols='W,Y:AJ', index_col=0)
    s_jobs = df_jobs.stack()
    s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]

    print(df_jgbcm)

    min_date = datetime(1973, 1, 1)
    max_date = datetime.now()

    plt.subplot(3, 1, 1)
    plt.plot(df_exchange.index, df_exchange.USD, label='ドル・円')
    plt.xlim(min_date, max_date)
    plt.ylim(50, 250)
    plt.legend(loc='best')

    plt.subplot(3, 1, 2)
    plt.plot(df_jgbcm.index, df_jgbcm['1'], label='1年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['5'], label='5年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['10'], label='10年国債金利')
    plt.xlim(min_date, max_date)
    plt.legend(loc='best')

    plt.subplot(3, 1, 3)
    plt.plot(s_jobs.index, s_jobs, label='有効求人倍率(季節調整値)')
    plt.xlim(min_date, max_date)
    plt.ylim(0.0, 2.0)
    plt.axhline(y=1, color='gray')
    plt.legend(loc='best')

    plt.savefig('historical_data.png', dpi=300)


def parse_japanese_date(s):
    """
    """
    base_years = {'S': 1925, 'H': 1988}
    era = s[0]
    year, month, day = s[1:].split('.')
    year = base_years[era] + int(year)
    return datetime(year, int(month), int(day))


def parse_year_and_month(year, month):
    """
    """
    year = int(year[:-1])
    month = int(month[:-1])
    year += (1990 if year >= 63 else 2000)
    return datetime(year, month, 1)


if __name__ == '__main__':
    main()
