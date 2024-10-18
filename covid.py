from covid import covid

covid = covid()
cases = covid.get_status_by_country_name("us")
for x in cases:
    print(x, ":", cases[x])
