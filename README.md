# Taxi Lakehouse Pipeline

## Diccionario de datos: `TaxiTripRaw`

Modelo de ingesta cruda para viajes de taxi amarillo de NYC. Estos campos llegan desde la fuente original y se conservan con su semantica de origen para permitir validaciones posteriores de calidad de datos.

### Identificacion / proveedor

| Campo | Descripcion |
| --- | --- |
| `VendorID` | Proveedor del taxi. Normalmente identifica la empresa o sistema que registro el viaje, con valores esperados `1` o `2`. |

### Tiempos

| Campo | Descripcion |
| --- | --- |
| `tpep_pickup_datetime` | Fecha y hora de inicio del viaje. Es un campo critico para detectar timestamps invalidos, viajes con duracion negativa y outliers temporales. |
| `tpep_dropoff_datetime` | Fecha y hora de finalizacion del viaje. Se usa junto con `tpep_pickup_datetime` para validar duracion, orden temporal y valores extremos. |

### Viaje

| Campo | Descripcion |
| --- | --- |
| `passenger_count` | Numero de pasajeros registrados en el viaje. Permite detectar problemas reales como valores nulos, negativos o conteos fuera de rango. |
| `trip_distance` | Distancia recorrida durante el viaje. Es clave para identificar distancias `0`, negativas, nulas o outliers. |

### Localizacion

| Campo | Descripcion |
| --- | --- |
| `PULocationID` | Identificador de la zona de recogida. Se cruza con `taxi_zone_lookup` para enriquecer el viaje con informacion geografica. |
| `DOLocationID` | Identificador de la zona de destino. Se cruza con `taxi_zone_lookup` para enriquecer el viaje con informacion geografica. |

### Pago

| Campo | Descripcion |
| --- | --- |
| `payment_type` | Tipo de pago registrado para el viaje. Sirve para analizar patrones de pago y validar coherencia con importes como propina o total. |

### Tarifas

| Campo | Descripcion |
| --- | --- |
| `fare_amount` | Importe base de la tarifa del viaje. Se valida para detectar importes negativos, nulos o inconsistentes. |
| `extra` | Cargos extra aplicados al viaje. Forma parte del calculo esperado del total. |
| `mta_tax` | Impuesto MTA aplicado al viaje. Se usa en validaciones de consistencia tarifaria. |
| `tip_amount` | Propina registrada. Permite detectar propinas negativas, absurdamente altas o incoherentes con el tipo de pago. |
| `tolls_amount` | Peajes aplicados al viaje. Se valida como parte del desglose de costes. |
| `improvement_surcharge` | Recargo de mejora aplicado al viaje. Forma parte del calculo esperado del total. |
| `total_amount` | Importe total del viaje. Es un campo clave para detectar totales inconsistentes, negativos o desviaciones frente a la suma de componentes. |
| `congestion_surcharge` | Recargo por congestion aplicado al viaje. Se utiliza en validaciones de tarifa y consistencia geografica. |
| `airport_fee` | Tasa de aeropuerto aplicada cuando corresponde. En la fuente puede aparecer como `Airport_fee`. |

### Otros

| Campo | Descripcion |
| --- | --- |
| `store_and_fwd_flag` | Indica si el viaje se almaceno offline antes de enviarse al proveedor. Ayuda a identificar registros capturados fuera de linea. |
