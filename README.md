# Calendario Económico Chileno 2026

API REST con interfaz de calendario visual para el seguimiento de fechas de publicación de los principales indicadores económicos de Chile durante el año 2026.

> Desarrollado para el curso de **Gestión de Inversiones** · Universidad de Santiago de Chile (USACH)

---

## Vista previa

El calendario presenta una interfaz visual con vista mensual y diaria, filtros por categoría y código de colores por nivel de impacto.

```
Vista mensual → navegación por mes con eventos marcados por día
Vista diaria  → detalle de cada indicador con valor anterior y actual
```

---

## Indicadores incluidos

| Código | Indicador | Entidad | Frecuencia | Impacto |
|---|---|---|---|---|
| `IPC` | Índice de Precios al Consumidor | INE | Mensual | Alto |
| `IPCSAE` | IPC sin Alimentos y Energía | INE | Mensual | Alto |
| `IMACEC` | Indicador Mensual de Actividad Económica | BCCh | Mensual | Alto |
| `PIB` | Producto Interno Bruto | BCCh | Trimestral | Alto |
| `TPM` | Tasa de Política Monetaria | BCCh | ~8 veces/año | Muy alto |
| `IPoM` | Informe de Política Monetaria | BCCh | Trimestral | Muy alto |
| `IEF` | Informe de Estabilidad Financiera | BCCh | Semestral | Alto |
| `TASA_DESEMPLEO` | Tasa de Desempleo (ENE) | INE | Mensual | Alto |
| `BALANZA_COMERCIAL` | Balanza Comercial | BCCh | Mensual | Medio |
| `BALANZA_PAGOS` | Balanza de Pagos | BCCh | Trimestral | Medio |
| `PRECIO_COBRE` | Precio del Cobre | BCCh | Mensual | Alto |
| `VENTAS_COMERCIO` | Índice de Ventas Minoristas | INE | Mensual | Medio |
| `IPI` | Índice de Producción Industrial | INE | Mensual | Medio |
| `DEUDA_PUBLICA` | Informe de Deuda Pública | Ministerio de Hacienda | Trimestral | Medio |

**Total: 117 eventos distribuidos entre el 1 de enero y el 31 de diciembre de 2026.**

---

## Instalación y uso

### Requisitos

- Python 3.8 o superior
- pip

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/JaavierQuintanilla/Calendario-Econ-mico.git
# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la API
python app.py
```

### Acceso

Una vez ejecutado, abrir el navegador en:

```
http://127.0.0.1:5000
```

El calendario se carga automáticamente.

---

## Estructura del proyecto

```
calendario-economico-chile/
├── app.py              # API Flask + interfaz del calendario
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación
```

---

## Endpoints de la API

Además de la interfaz visual, la API expone endpoints REST consultables directamente:

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Abre el calendario visual |
| `GET` | `/eventos` | Lista todos los eventos (acepta filtros) |
| `GET` | `/eventos/proximos` | Eventos aún no publicados |
| `GET` | `/eventos/hoy` | Eventos del día actual |
| `GET` | `/eventos/<id>` | Detalle de un evento por ID |
| `GET` | `/indicadores` | Catálogo de indicadores |
| `GET` | `/categorias` | Categorías disponibles |
| `GET` | `/resumen` | Estadísticas generales |
| `GET` | `/info` | Información de la API |

### Filtros disponibles para `/eventos`

```
/eventos?indicador=IPC
/eventos?categoria=politica_monetaria
/eventos?impacto=muy_alto
/eventos?estado=proximo
/eventos?mes=6
/eventos?desde=2026-07-01&hasta=2026-09-30
```

### Ejemplo de respuesta JSON

```json
{
  "id": "IPC-2026-05",
  "indicador": "IPC",
  "nombre": "Índice de Precios al Consumidor",
  "fecha": "2026-05-08",
  "hora": "09:00",
  "entidad": "INE",
  "descripcion": "Variación mensual del IPC de abril 2026",
  "periodo": "abril 2026",
  "categoria": "inflacion",
  "impacto": "alto",
  "valor_anterior": 1.3,
  "valor_actual": 1.3,
  "unidad": "% mensual",
  "estado": "publicado"
}
```

---

## Interfaz visual

### Vista mensual
Grilla de 7 columnas con los eventos del mes marcados con etiquetas de color según impacto. Hacer clic en cualquier día abre la vista diaria.

### Vista diaria
Detalle completo de cada evento: hora, descripción, período, valor anterior y valor actual.

### Filtros por categoría
Panel lateral para activar/desactivar categorías temáticas (inflación, actividad, política monetaria, empleo, etc.).

### Código de colores por impacto
| Color | Nivel | Indicadores |
|---|---|---|
| 🔴 Rojo | Muy alto | TPM, IPoM |
| 🟠 Naranja | Alto | IPC, IPCSAE, IMACEC, PIB, Desempleo, Cobre |
| 🔵 Celeste | Medio | Balanza Comercial, IPI, Ventas, Deuda |

---

## Fuentes de datos

- **Banco Central de Chile (BCCh):** [bcentral.cl](https://www.bcentral.cl)
- **Instituto Nacional de Estadísticas (INE):** [ine.gob.cl](https://www.ine.gob.cl)
- **Ministerio de Hacienda:** [hacienda.cl](https://www.hacienda.cl)

---

## Tecnologías

- **Backend:** Python 3 · Flask
- **Frontend:** HTML5 · CSS3 · JavaScript (vanilla)
- **Tipografía:** Syne + DM Mono (Google Fonts)
