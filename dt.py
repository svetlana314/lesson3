from datetime import datetime, timedelta
def main():
    delta1 = timedelta(days = 1)
    yesterday = datetime.now().date() - delta1
    delta2 = timedelta(days = 30)
    month_ago = datetime.now().date() - delta2
    print(f"Yesterday: {yesterday}. \nToday: {datetime.now().date()}. \nMonth ago: {month_ago}.")

    str1 = "01/01/25 12:10:03.234567"
    dt = datetime.strptime(str1, '%y/%m/%d %H:%M:%S.%f')
    print(dt)


if __name__ == "__main__":
    main()