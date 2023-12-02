import mechanize
import http.cookiejar
from bs4 import BeautifulSoup

def date_pset():
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [("Accept", "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0")]

    br.open('https://docs.code-fu.net.ni/acceso')

    br.select_form(nr = 0)
    user = "y23c2-esaballos"
    password = "56db3df71e*"
    br.form['log'] = user
    br.form['pwd'] = password
    br.submit()

    resultados = []

    for i in range(10):
        url = f"https://docs.code-fu.net.ni/pset{i}-y23c2/"
        br.open(url)
        html_text = br.response().read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")
        
        try:
            date = soup.find("div", {"class":"ulist"}).find("ul").find("li").text
            resultados.append(f"Pset {i} fecha: {date}")

        except AttributeError:
            resultados.append(f"No se pudo encontrar la fecha para Pset {i}")
    
    return resultados