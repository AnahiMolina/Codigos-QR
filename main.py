import segno
import segno.helpers

#QR para texto
holamundo = segno.make('hola mundo')
holamundo.save('hola.png', scale=10)

#QR para Wi-fi
wifi = segno.helpers.make_wifi(ssid='Ejemplo-Red-6500',password='xxxxx',security='WPA',hidden='False')
wifi.save('wifi.png', scale=10)

#QR para coordenadas
coors = segno.helpers.make_geo(lat='19.80708752727613',lng='-97.36434377461046')
coors.save('coordenada.png', scale=10)