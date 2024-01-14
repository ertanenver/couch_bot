from datetime import datetime

months = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль', '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}

def get_month():
    month = {}
    now = datetime.now().strftime("%m")
    prvs_mnth = str(int(now) - 1) if now != '01' else '12'
    previous_month = months[prvs_mnth if len(prvs_mnth) == 2 else '0' + prvs_mnth]
    current_month = months[now]
    flwng_mnth = str(int(now) + 1) if now != '12' else '01'
    following_month = months[flwng_mnth if len(flwng_mnth) == 2 else '0' + flwng_mnth]
    month["previous_month"] = previous_month
    month["current_month"] = current_month
    month["following_month"] = following_month
    return month