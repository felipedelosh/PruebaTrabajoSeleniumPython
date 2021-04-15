"""
Python+Selenium

Entrar a www.viajesexito.com
selecciona el primer vuelo
llene los datos de pasajeros
pereira bogota

2 + Adultos + 1 infante
"""
# -⁻- coding: UTF-8 -*-
from Controladora import Controladora
import pandas
import time
from datetime import date
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec 



controladoraPersonas = Controladora()

#Se Crea la persona que comprara los tiquetes
persona1 = controladoraPersonas.generarAdultoAlAzar()


#Se crea el otro adulto
persona2 = controladoraPersonas.generarAdultoAlAzar()

# Se crea el infante
infante = controladoraPersonas.generarBebeAlAzar()



# Capturar el url
url = "https://www.viajesexito.com/paquetes"


# Se crean los selectores para dar click
selectorVuelo = "#menu > div:nth-child(2) > a > span" # Este es el selector para ir a vuelos
selectorIngresarOrigen = "#CityPredictiveFrom_netactica_air"
selectorIngresarDestino = "#CityPredictiveTo_netactica_air"
selectorCajaMeVoyElDia = "#AirFlightRTOW > div > div.col-12.col-xl-4.bd-right > div > div.colWidgetMitad.colWidget-date.Show.soloIda"
selectorFechaMeVoyElDia = "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr:nth-child(3) > td.ui-datepicker-days-cell-over > a"
selectorFechaRegresoElDia = "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr:nth-child(4) > td:nth-child(4)"
selectorClickPasajeros = "#AirFlightRTOW > div > div:nth-child(3) > div > div > div > div > div > label"
selectorCajaPasajerosCantidadAdultosMas = "#pasajerosvuelos > div > div:nth-child(2) > div > div.col-7.col-sm-6 > div > span:nth-child(3) > button > span"
selectorCajaPasajerosCantidadInfantesMas = "#pasajerosvuelos > div > div:nth-child(4) > div > div.col-7.col-sm-6 > div > span:nth-child(3) > button > span"
selectorCantidadPasajerosOK = "#btbClosePaxPopup"
selectorBuscarVuelo = "#sbm_netactica_air"
# Comprar vuelo
selectorComprarPrimerVuelo = "#divAirResults > div:nth-child(1) > div > div > div.medium-3.column > div > div:nth-child(2) > div:nth-child(3) > div > input"
selectorContinuarCompra = "#total-row > div.row.nts-section > div > button"
selectorChckAceptarTerminosYCondiciones = "#chkTermsAndConditions"
selectorFinCompra = "#submitButtonId"
# Ingresar datos de usuario
# Usuarrio reesponsable del vuelo
selectorComboBoxRespetoMaster = "#Travelers_0__Title"
selectoNombreDeUsuarioMaster = "#Travelers_0__FirstName"
selectoApellidoDeUsuarioMaster = "#Travelers_0__LastName"
selectorComboBoxTipoDocumentoMaster = "#Travelers_0__DocumentType"
selectorNroDocumentoMaster = "#Travelers_0__DucumentNumber"
selectorComboBoxDiaNacimientoMaster = "#Travelers\\[0\\]\\.DOB_d"
selectorComboBoxMesNacimientoMaster = "#Travelers\\[0\\]\\.DOB_m"
selectorComboBoxAnhioNaciminetoMaster = "#Travelers\\[0\\]\\.DOB_y"
# Correo y telefono
selectorCorreoMaster = "#ContactEmail"
selectorTelefonoMaster = "#ContactPhone"


# Ingresar datos del adulto acompañante
selectorComboBoxrespetoAcompa = "#Travelers_1__Title"
selectorNombreUsuarioAcompa = "#Travelers_1__FirstName"
selectorApellidoDeUsuarioAcompa = "#Travelers_1__LastName"
selectorComboBoxTipoDocumentoAcompa = "#Travelers_1__DocumentType"
selectorNroDocumentoAcompa = "#Travelers_1__DucumentNumber"
selectorComboBoxDiaNacimientoAcompa = "#Travelers\\[1\\]\\.DOB_d"
selectorComboBoxMesNacimientoAcompa = "#Travelers\\[1\\]\\.DOB_m"
selectorComboBoxAnhioNaciminetoAcompa = "#Travelers\\[1\\]\\.DOB_y"

# Ingresar datos del adulto acompañante
selectorComboBoxrespetoBebe = "#Travelers_2__Title"
selectorNombreUsuarioBebe = "#Travelers_2__FirstName"
selectorApellidoDeUsuarioBebe = "#Travelers_2__LastName"
selectorComboBoxTipoDocumentoBebe = "#Travelers_2__DocumentType"
selectorNroDocumentoBebe = "#Travelers_2__DucumentNumber"
selectorComboBoxDiaNacimientoBebe = "#Travelers\\[2\\]\\.DOB_d"
selectorComboBoxMesNacimientoBebe = "#Travelers\\[2\\]\\.DOB_m"
selectorComboBoxAnhioNaciminetoBebe = "#Travelers\\[2\\]\\.DOB_y"


# Variables txt
dataOrigenVuelo = "Bogotá, Colombia (BOG)"
dataDestinoVuelo = "Pereira, Colombia (PEI)"


# Abrir Chrome
driver = webdriver.Chrome()
time.sleep(4)
# Maximinar Pantalla
driver.maximize_window()
#Abrir url 
driver.get(url)
#Esperamos unos segundos  que cargue la pantalla
time.sleep(3)
# Abrir vuelos
driver.find_element_by_css_selector(selectorVuelo).click()
# buscar Vuelo bogota
time.sleep(1)
driver.find_element_by_css_selector(selectorIngresarOrigen).click()
driver.find_element_by_css_selector(selectorIngresarOrigen).send_keys(dataOrigenVuelo)
# Buscar vuelo pereira
time.sleep(1)
driver.find_element_by_css_selector(selectorIngresarDestino).click()
driver.find_element_by_css_selector(selectorIngresarDestino).send_keys(dataDestinoVuelo)
# Se ingresa la fecha
time.sleep(1)
driver.find_element_by_css_selector(selectorCajaMeVoyElDia).click()
time.sleep(1)
driver.find_element_by_css_selector(selectorFechaMeVoyElDia).click()
driver.find_element_by_css_selector(selectorFechaRegresoElDia).click()
# Se Configura el ingreso de pasajeros
driver.find_element_by_css_selector(selectorClickPasajeros).click()
time.sleep(1)
# Se agrega un adulto
driver.find_element_by_css_selector(selectorCajaPasajerosCantidadAdultosMas).click()
# Se Agrega un infante
driver.find_element_by_css_selector(selectorCajaPasajerosCantidadInfantesMas).click()
# Se Determina que la cantidad de pasajeros es correcta
time.sleep(2)
driver.find_element_by_css_selector(selectorCantidadPasajerosOK).click()
# Busca el vuelo
driver.find_element_by_css_selector(selectorBuscarVuelo).click()
# Se procede a esperar y comprar el primer vuelo disponible
time.sleep(12)
driver.find_element_by_css_selector(selectorComprarPrimerVuelo).click()
time.sleep(10)
driver.find_element_by_css_selector(selectorContinuarCompra).click()
# Espero a que carguen los formularios de llenar los datos
time.sleep(10)

# LLeno los datos del master

# Respeto
if persona1.sexo == "F":
    select = Select(driver.find_element_by_css_selector(selectorComboBoxRespetoMaster))
    select.select_by_index(2)
else:
    select = Select(driver.find_element_by_css_selector(selectorComboBoxRespetoMaster))
    select.select_by_index(1)

# Datos Personales
driver.find_element_by_css_selector(selectoNombreDeUsuarioMaster).click()
driver.find_element_by_css_selector(selectoNombreDeUsuarioMaster).send_keys(persona1.nombre)
driver.find_element_by_css_selector(selectoApellidoDeUsuarioMaster).click()
driver.find_element_by_css_selector(selectoApellidoDeUsuarioMaster).send_keys(persona1.apellidos)

# Cedula
select = Select(driver.find_element_by_css_selector(selectorComboBoxTipoDocumentoMaster))
select.select_by_index(0)
driver.find_element_by_css_selector(selectorNroDocumentoMaster).click()
driver.find_element_by_css_selector(selectorNroDocumentoMaster).send_keys(str(persona1.numeroDedocumento))

# Datos de nacimiento 
# Esperar a que cargue el combo box
time.sleep(10)
selectDN = Select(driver.find_element_by_css_selector(selectorComboBoxDiaNacimientoMaster))
selectDN.select_by_value(str(persona1.diaDeNacimiento))
time.sleep(10)
selectMN = Select(driver.find_element_by_css_selector(selectorComboBoxMesNacimientoMaster))
selectMN.select_by_value(str(persona1.nroMesNaciemiento))
selectAN = Select(driver.find_element_by_css_selector(selectorComboBoxAnhioNaciminetoMaster))
selectAN.select_by_value(str(persona1.anoNacimiento))


# Respeto
if persona2.sexo == "F":
    select = Select(driver.find_element_by_css_selector(selectorComboBoxrespetoAcompa))
    select.select_by_index(2)
else:
    select = Select(driver.find_element_by_css_selector(selectorComboBoxrespetoAcompa))
    select.select_by_index(1)


# Datos Personales
driver.find_element_by_css_selector(selectorNombreUsuarioAcompa).click()
driver.find_element_by_css_selector(selectorNombreUsuarioAcompa).send_keys(persona2.nombre)
driver.find_element_by_css_selector(selectorApellidoDeUsuarioAcompa).click()
driver.find_element_by_css_selector(selectorApellidoDeUsuarioAcompa).send_keys(persona2.apellidos)

# Cedula
select = Select(driver.find_element_by_css_selector(selectorComboBoxTipoDocumentoAcompa))
select.select_by_index(0)
driver.find_element_by_css_selector(selectorNroDocumentoAcompa).click()
driver.find_element_by_css_selector(selectorNroDocumentoAcompa).send_keys(str(persona2.numeroDedocumento))

# Datos de nacimiento 
# Esperar a que cargue el combo box
time.sleep(10)
selectDN = Select(driver.find_element_by_css_selector(selectorComboBoxDiaNacimientoAcompa))
selectDN.select_by_value(str(persona2.diaDeNacimiento))
time.sleep(10)
selectMN = Select(driver.find_element_by_css_selector(selectorComboBoxMesNacimientoAcompa))
selectMN.select_by_value(str(persona2.nroMesNaciemiento))
selectAN = Select(driver.find_element_by_css_selector(selectorComboBoxAnhioNaciminetoAcompa))
selectAN.select_by_value(str(persona2.anoNacimiento))


# Datos del bebe
# Respeto
if infante.sexo == "F":
    select = Select(driver.find_element_by_css_selector(selectorComboBoxrespetoBebe))
    select.select_by_index(2)
else:
    select = Select(driver.find_element_by_css_selector(selectorComboBoxrespetoBebe))
    select.select_by_index(4)


# Datos Personales
driver.find_element_by_css_selector(selectorNombreUsuarioBebe).click()
driver.find_element_by_css_selector(selectorNombreUsuarioBebe).send_keys(persona2.nombre)
driver.find_element_by_css_selector(selectorApellidoDeUsuarioBebe).click()
driver.find_element_by_css_selector(selectorApellidoDeUsuarioBebe).send_keys(persona2.apellidos)

# Cedula
select = Select(driver.find_element_by_css_selector(selectorComboBoxTipoDocumentoBebe))
select.select_by_index(1)
driver.find_element_by_css_selector(selectorNroDocumentoBebe).click()
driver.find_element_by_css_selector(selectorNroDocumentoBebe).send_keys(str(infante.numeroDedocumento))

# Datos de nacimiento 
# Esperar a que cargue el combo box
time.sleep(10)
selectDN = Select(driver.find_element_by_css_selector(selectorComboBoxDiaNacimientoBebe))
selectDN.select_by_value(str(infante.diaDeNacimiento))
time.sleep(10)
selectMN = Select(driver.find_element_by_css_selector(selectorComboBoxMesNacimientoBebe))
selectMN.select_by_value(str(infante.nroMesNaciemiento))
selectAN = Select(driver.find_element_by_css_selector(selectorComboBoxAnhioNaciminetoBebe))
selectAN.select_by_value(str(infante.anoNacimiento))

# Correo y telefono

driver.find_element_by_css_selector(selectorCorreoMaster).click()
driver.find_element_by_css_selector(selectorCorreoMaster).send_keys(persona1.correoelectronico)
driver.find_element_by_css_selector(selectorTelefonoMaster).click()
driver.find_element_by_css_selector(selectorTelefonoMaster).send_keys(persona1.telefonoCelular)

# Fin de la compra de tiquetes
driver.find_element_by_css_selector(selectorChckAceptarTerminosYCondiciones).click()
driver.find_element_by_css_selector(selectorFinCompra).click()