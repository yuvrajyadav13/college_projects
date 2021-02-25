from datetime import date

stock_name = ''
start_date = date.today()
end_date = date.today()


def set(a, b, c):
    global stock_name, start_date, end_date
    stock_name = a
    start_date = b
    end_date = c
    trans_var()


def get():
    return stock_name, start_date, end_date


def trans_var():
    var = [stock_name, start_date, end_date]
    f = open("notebooks/var.txt", 'w+')
    f.write(str(var))
