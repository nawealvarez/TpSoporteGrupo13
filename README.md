# TpSoporteGrupo13
Compumundoimpermegared. Mejor tp del universo cuantico


El sistema debe ser capaz de:

  -Introducir el saldo (posibilidad de modificarlo)
  -Permitir al usuario setear un costo fijo que se descuente todos los meses.
  - Resgistrar costos ocasionales
  -Registrar ingresos 
  -Establecer que se realizo alguna transferencia
  -Notificar al usuario cuando le queda menos del %15 de saldo
  -Permitir al usuario visualizar mediante greficos gastos e ingresos(graficos separados) mes a mes
  -Permitir visualizar grafico de movimientos historicos.
  -Permitir al usuario registrar ya sea una deuda a pagar en una fecha o a recibir un pago

Algunas aclaraciones...

  Cuentas: Distinto lugares donde se mueve el dinero, o desde donde se obtiene los ingresos. Ejemplo: efectivo, debito, etc… 
  puede ser bancos tambien o si son 2 personas que usan el mismo usuario. 
  
 Monedas: moneda que va a manejar. Una de las monedas es “Referencial” osea que es la moneda de uso corriente.
  Ejemplo: Peso Argentino ($), dolar (u$d), etc.. 
 Categorias: son las categorías que se van a utilizar para ingresos y egresos. 
  Ejemplo: comida, compras, vivienda, transporte, etc… (ver las de la aplicación)
Etiquetas: Se utilizan para filtrar mejor. Ejemplo: “mi trabajo”. Atributos:

Estado:
  Conciliado
  Procesado
  Pendiente
  Inválido
  lugar (para saber donde se gasta más) (gmaps)

Transferencias: Esta opcion generaria 2 registros, uno de egreso (cuenta_origen) y otra de ingreso (cuenta_destino).
