months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    get_date()

def get_date():
    while True:
        date = input("Date: ")
        try:
            m,d,y = date.split("/")
            m = int(m)
            y = int(y)
            d = int(d)
            if d < 31 and m < 12:
                m = str(m)
                d = str(d)
                if len(m) == 1 and len(d) == 1:
                    m = int(m)
                    d = int(d)
                    print((f"{y}-{m:02}-{d:02}"))
                    break
                elif len(m) == 1:
                    m = int(m)
                    d = int(d)
                    print((f"{y}-{m:02}-{d}"))
                    break
                elif len(d) == 1:
                    m = int(m)
                    d = int(d)
                    print((f"{y}-{m}-{d:02}"))
                    break





        except ValueError:
            try:
                md,y = date.split(",")
                m,d = md.split(" ")
                if m in months:
                    m = months.index(m)
                    m = int(m) + 1
                    d = int(d)
                    y = int(y)
                    if d < 31 and m < 12:
                        m = str(m)
                        d = str(d)
                        if len(m) == 1 and len(d) == 1:
                            m = int(m)
                            d = int(d)
                            print((f"{y}-{m:02}-{d:02}"))
                            break
                        elif len(m) == 1:
                            m = int(m)
                            d = int(d)
                            print((f"{y}-{m:02}-{d}"))
                            break
                        elif len(d) == 1:
                            m = int(m)
                            d = int(d)
                            print((f"{y}-{m}-{d:02}"))
                            break
            except ValueError:
                pass



            else:
                pass
        else:
            pass

main()





