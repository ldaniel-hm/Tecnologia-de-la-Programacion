def get_pib(url, country='ES'):
    '''
    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
        country: Es una cadena con el código del país.
    Devuelve:
        Un diccionario con pares año:pib del país country que hay en el fichero con la url dada.
    '''
    from urllib import request
    from urllib.error import URLError

    try:
        f = request.urlopen(url)  # request. permite manipular fichero URL
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        data = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista
        data = [i.split('\t') for i in data] # Dividir cada línea por el tabulador
        data = [list(map(str.strip, i)) for i in data] # Eliminar espacios en blanco
        for i in data:
            i[0] = i[0].split(',')[-1] # Obtener el código del país del primer elemento de la lista
        data[0][0] = 'years'
        data = {i[0]:i[1:] for i in data}
        result = {data['years'][i]:data[country][i] for i in range(len(data['years']))}
        return result

country = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', country)
print('Año', '\t', 'PIB')
for year, pib in get_pib('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items():
    print(year, '\t', pib)