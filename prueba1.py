import re
frase = "agregar parrafo"
nueva_frase = frase.replace('á', '&aacute;').replace('é', '&eacute;').replace('í', '&iacute;').replace('ó', '&oacute;').replace('ú', '&uacute;').replace('ñ', '&ntilde;')
print (nueva_frase)