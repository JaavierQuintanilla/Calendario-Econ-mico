# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:10:32 2026

@author: Javier
"""

"""
API Calendario Económico Chileno
Indicadores: IPC, IMACEC, PIB, Tasa de Política Monetaria, Balanza Comercial, etc.
Fuentes: Banco Central de Chile (BCCh) e INE
"""

from flask import Flask, jsonify, request
from datetime import date, datetime
import json

app = Flask(__name__)

EVENTOS = [
    # ══════════════════════════════════════════════════════════════
    # IPC - Índice de Precios al Consumidor (INE, ~día 8 de cada mes)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IPC-2026-01",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-01-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de diciembre 2025",
        "periodo": "diciembre 2025",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": 0.4,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-02",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-02-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de enero 2026",
        "periodo": "enero 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.4,
        "valor_actual": 0.0,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-03",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-03-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.0,
        "valor_actual": 1.0,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-04",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-04-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.0,
        "valor_actual": 1.3,
        "unidad": "% mensual"
    },
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
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-06",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-06-05",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-07",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-07-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de junio 2026",
        "periodo": "junio 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-08",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-08-07",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de julio 2026",
        "periodo": "julio 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-09",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-09-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-10",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-10-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-11",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-11-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPC-2026-12",
        "indicador": "IPC",
        "nombre": "Índice de Precios al Consumidor",
        "fecha": "2026-12-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación mensual del IPC de noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 1.3,
        "valor_actual": None,
        "unidad": "% mensual"
    },

    # ══════════════════════════════════════════════════════════════
    # IPCSAE - IPC sin Alimentos y Energía (INE, misma fecha que IPC)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IPCSAE-2026-01",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-01-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente diciembre 2025",
        "periodo": "diciembre 2025",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": 0.3,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-02",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-02-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente enero 2026",
        "periodo": "enero 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.3,
        "valor_actual": 0.1,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-03",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-03-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.1,
        "valor_actual": 0.7,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-04",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-04-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.7,
        "valor_actual": 0.8,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-05",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-05-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente abril 2026",
        "periodo": "abril 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.8,
        "valor_actual": 0.9,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-06",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-06-05",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-07",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-07-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente junio 2026",
        "periodo": "junio 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-08",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-08-07",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente julio 2026",
        "periodo": "julio 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-09",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-09-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-10",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-10-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-11",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-11-06",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },
    {
        "id": "IPCSAE-2026-12",
        "indicador": "IPCSAE",
        "nombre": "IPC sin Alimentos y Energía (IPCSAE)",
        "fecha": "2026-12-08",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Inflación subyacente noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "inflacion",
        "impacto": "alto",
        "valor_anterior": 0.9,
        "valor_actual": None,
        "unidad": "% mensual"
    },

    # ══════════════════════════════════════════════════════════════
    # IMACEC - Indicador Mensual de Actividad Económica (BCCh)
    # Publicación: ~2° día hábil, dos meses después del período
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IMACEC-2026-01",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-03-03",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de enero 2026",
        "periodo": "enero 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": -0.1,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-02",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-04-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": -0.3,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-03",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-05-05",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.3,
        "valor_actual": -0.1,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-04",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-06-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de abril 2026",
        "periodo": "abril 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-05",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-07-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-06",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-08-04",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de junio 2026",
        "periodo": "junio 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-07",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-09-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de julio 2026",
        "periodo": "julio 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-08",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-10-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-09",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-11-03",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IMACEC-2026-10",
        "indicador": "IMACEC",
        "nombre": "Indicador Mensual de Actividad Económica",
        "fecha": "2026-12-02",
        "hora": "08:30",
        "entidad": "BCCh",
        "descripcion": "IMACEC de octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": -0.1,
        "valor_actual": None,
        "unidad": "% anual"
    },

    # ══════════════════════════════════════════════════════════════
    # TPM - Tasa de Política Monetaria (BCCh, 8 reuniones al año)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "TPM-2026-01",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-01-27",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°1 - decisión de TPM",
        "periodo": "enero 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.75,
        "valor_actual": 4.5,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-02",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-03-17",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°2 - decisión de TPM",
        "periodo": "marzo 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": 4.5,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-03",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-04-28",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°3 - decisión de TPM",
        "periodo": "abril 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": 4.5,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-04",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-06-16",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°4 - decisión de TPM",
        "periodo": "junio 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-05",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-07-28",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°5 - decisión de TPM",
        "periodo": "julio 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-06",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-09-15",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°6 - decisión de TPM",
        "periodo": "septiembre 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-07",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-10-27",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°7 - decisión de TPM",
        "periodo": "octubre 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "TPM-2026-08",
        "indicador": "TPM",
        "nombre": "Tasa de Política Monetaria",
        "fecha": "2026-12-15",
        "hora": "18:00",
        "entidad": "BCCh",
        "descripcion": "Reunión de Política Monetaria N°8 - decisión de TPM",
        "periodo": "diciembre 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 4.5,
        "valor_actual": None,
        "unidad": "% anual"
    },

    # ══════════════════════════════════════════════════════════════
    # IPoM - Informe de Política Monetaria (BCCh, trimestral)
    # Publicación: enero, abril, julio, octubre (día siguiente a TPM)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IPOM-2026-01",
        "indicador": "IPoM",
        "nombre": "Informe de Política Monetaria",
        "fecha": "2026-01-28",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "IPoM enero 2026 - proyecciones de inflación y crecimiento",
        "periodo": "enero 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": None,
        "valor_actual": 2.5,
        "unidad": "informe"
    },
    {
        "id": "IPOM-2026-02",
        "indicador": "IPoM",
        "nombre": "Informe de Política Monetaria",
        "fecha": "2026-04-29",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "IPoM abril 2026 - proyecciones de inflación y crecimiento",
        "periodo": "abril 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 2.5,
        "valor_actual": 2.0,
        "unidad": "informe"
    },
    {
        "id": "IPOM-2026-03",
        "indicador": "IPoM",
        "nombre": "Informe de Política Monetaria",
        "fecha": "2026-07-29",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "IPoM julio 2026 - proyecciones de inflación y crecimiento",
        "periodo": "julio 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 2.0,
        "valor_actual": None,
        "unidad": "informe"
    },
    {
        "id": "IPOM-2026-04",
        "indicador": "IPoM",
        "nombre": "Informe de Política Monetaria",
        "fecha": "2026-10-28",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "IPoM octubre 2026 - proyecciones de inflación y crecimiento",
        "periodo": "octubre 2026",
        "categoria": "politica_monetaria",
        "impacto": "muy_alto",
        "valor_anterior": 2.0,
        "valor_actual": None,
        "unidad": "informe"
    },

    # ══════════════════════════════════════════════════════════════
    # PIB - Producto Interno Bruto trimestral (BCCh)
    # Publicación: ~3 meses después del cierre del trimestre
    # ══════════════════════════════════════════════════════════════
    {
        "id": "PIB-2026-Q1",
        "indicador": "PIB",
        "nombre": "Producto Interno Bruto",
        "fecha": "2026-03-18",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "PIB tercer trimestre 2025 (cifras definitivas)",
        "periodo": "Q3 2025",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": 2.5,
        "unidad": "% anual"
    },
    {
        "id": "PIB-2026-Q2",
        "indicador": "PIB",
        "nombre": "Producto Interno Bruto",
        "fecha": "2026-06-17",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "PIB cuarto trimestre 2025 (cifras definitivas)",
        "periodo": "Q4 2025",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "PIB-2026-Q3",
        "indicador": "PIB",
        "nombre": "Producto Interno Bruto",
        "fecha": "2026-09-16",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "PIB primer trimestre 2026 (cifras definitivas)",
        "periodo": "Q1 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "PIB-2026-Q4",
        "indicador": "PIB",
        "nombre": "Producto Interno Bruto",
        "fecha": "2026-12-16",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "PIB segundo trimestre 2026 (cifras definitivas)",
        "periodo": "Q2 2026",
        "categoria": "actividad",
        "impacto": "alto",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },

    # ══════════════════════════════════════════════════════════════
    # TASA DE DESEMPLEO - Encuesta Nacional de Empleo (INE, mensual)
    # Publicación: ~último día hábil del mes siguiente
    # ══════════════════════════════════════════════════════════════
    {
        "id": "DESEMPLEO-2026-01",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-01-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil nov 2025 - ene 2026",
        "periodo": "noviembre 2025 - enero 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": 8.3,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-02",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-02-27",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil dic 2025 - feb 2026",
        "periodo": "diciembre 2025 - febrero 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.3,
        "valor_actual": 8.3,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-03",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-03-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil ene - mar 2026",
        "periodo": "enero - marzo 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.3,
        "valor_actual": 8.9,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-04",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-04-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil feb - abr 2026",
        "periodo": "febrero - abril 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": 8.9,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-05",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-05-29",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil mar - may 2026",
        "periodo": "marzo - mayo 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-06",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-06-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil abr - jun 2026",
        "periodo": "abril - junio 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-07",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-07-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil may - jul 2026",
        "periodo": "mayo - julio 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-08",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-08-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil jun - ago 2026",
        "periodo": "junio - agosto 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-09",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-09-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil jul - sep 2026",
        "periodo": "julio - septiembre 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-10",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-10-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil ago - oct 2026",
        "periodo": "agosto - octubre 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-11",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-11-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil sep - nov 2026",
        "periodo": "septiembre - noviembre 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },
    {
        "id": "DESEMPLEO-2026-12",
        "indicador": "TASA_DESEMPLEO",
        "nombre": "Tasa de Desempleo",
        "fecha": "2026-12-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Encuesta Nacional de Empleo - trimestre móvil oct - dic 2026",
        "periodo": "octubre - diciembre 2026",
        "categoria": "mercado_laboral",
        "impacto": "alto",
        "valor_anterior": 8.9,
        "valor_actual": None,
        "unidad": "% fuerza de trabajo"
    },

    # ══════════════════════════════════════════════════════════════
    # BALANZA COMERCIAL (BCCh, mensual, ~último día hábil del mes)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "BC-2026-01",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-01-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de diciembre 2025",
        "periodo": "diciembre 2025",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": None,
        "valor_actual": 3600.0,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-02",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-02-27",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de enero 2026",
        "periodo": "enero 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 3600.0,
        "valor_actual": 3811.0,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-03",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-03-31",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 3811.0,
        "valor_actual": 2785.0,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-04",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-04-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 2785.0,
        "valor_actual": 1500.0,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-05",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-05-29",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de abril 2026",
        "periodo": "abril 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-06",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-06-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-07",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-07-31",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de junio 2026",
        "periodo": "junio 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-08",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-08-31",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de julio 2026",
        "periodo": "julio 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-09",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-09-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-10",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-10-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-11",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-11-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BC-2026-12",
        "indicador": "BALANZA_COMERCIAL",
        "nombre": "Balanza Comercial",
        "fecha": "2026-12-30",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Exportaciones e importaciones de noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "comercio_exterior",
        "impacto": "medio",
        "valor_anterior": 1500.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },

    # ══════════════════════════════════════════════════════════════
    # IEF - Informe de Estabilidad Financiera (BCCh, semestral)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IEF-2026-01",
        "indicador": "IEF",
        "nombre": "Informe de Estabilidad Financiera",
        "fecha": "2026-06-09",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Informe de Estabilidad Financiera primer semestre 2026",
        "periodo": "H1 2026",
        "categoria": "estabilidad_financiera",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": None,
        "unidad": "informe"
    },
    {
        "id": "IEF-2026-02",
        "indicador": "IEF",
        "nombre": "Informe de Estabilidad Financiera",
        "fecha": "2026-11-17",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Informe de Estabilidad Financiera segundo semestre 2026",
        "periodo": "H2 2026",
        "categoria": "estabilidad_financiera",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": None,
        "unidad": "informe"
    },

    # ══════════════════════════════════════════════════════════════
    # BALANZA DE PAGOS (BCCh, trimestral)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "BALANZA_PAGOS-2026-Q1",
        "indicador": "BALANZA_PAGOS",
        "nombre": "Balanza de Pagos",
        "fecha": "2026-03-31",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Balanza de pagos Q3 2025",
        "periodo": "Q3 2025",
        "categoria": "sector_externo",
        "impacto": "medio",
        "valor_anterior": None,
        "valor_actual": -2100.0,
        "unidad": "USD millones"
    },
    {
        "id": "BALANZA_PAGOS-2026-Q2",
        "indicador": "BALANZA_PAGOS",
        "nombre": "Balanza de Pagos",
        "fecha": "2026-06-30",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Balanza de pagos Q4 2025",
        "periodo": "Q4 2025",
        "categoria": "sector_externo",
        "impacto": "medio",
        "valor_anterior": -2100.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BALANZA_PAGOS-2026-Q3",
        "indicador": "BALANZA_PAGOS",
        "nombre": "Balanza de Pagos",
        "fecha": "2026-09-30",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Balanza de pagos Q1 2026",
        "periodo": "Q1 2026",
        "categoria": "sector_externo",
        "impacto": "medio",
        "valor_anterior": -2100.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },
    {
        "id": "BALANZA_PAGOS-2026-Q4",
        "indicador": "BALANZA_PAGOS",
        "nombre": "Balanza de Pagos",
        "fecha": "2026-12-30",
        "hora": "10:00",
        "entidad": "BCCh",
        "descripcion": "Balanza de pagos Q2 2026",
        "periodo": "Q2 2026",
        "categoria": "sector_externo",
        "impacto": "medio",
        "valor_anterior": -2100.0,
        "valor_actual": None,
        "unidad": "USD millones"
    },

    # ══════════════════════════════════════════════════════════════
    # PRECIO DEL COBRE - Informe Mensual (BCCh, ~día 15 de cada mes)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "COBRE-2026-01",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-01-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre diciembre 2025",
        "periodo": "diciembre 2025",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": None,
        "valor_actual": 4.2,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-02",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-02-13",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre enero 2026",
        "periodo": "enero 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.2,
        "valor_actual": 4.55,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-03",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-03-13",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.55,
        "valor_actual": 4.72,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-04",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-04-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.72,
        "valor_actual": 4.85,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-05",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-05-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre abril 2026",
        "periodo": "abril 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-06",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-06-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-07",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-07-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre junio 2026",
        "periodo": "junio 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-08",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-08-14",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre julio 2026",
        "periodo": "julio 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-09",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-09-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-10",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-10-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-11",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-11-13",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },
    {
        "id": "COBRE-2026-12",
        "indicador": "PRECIO_COBRE",
        "nombre": "Precio del Cobre - Informe Mensual",
        "fecha": "2026-12-15",
        "hora": "09:00",
        "entidad": "BCCh",
        "descripcion": "Estadísticas de precio del cobre noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "commodities",
        "impacto": "alto",
        "valor_anterior": 4.85,
        "valor_actual": None,
        "unidad": "USD/libra"
    },

    # ══════════════════════════════════════════════════════════════
    # VENTAS MINORISTAS (INE, mensual, ~día 14 del mes siguiente)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "VENTAS-2026-01",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-02-13",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas enero 2026",
        "periodo": "enero 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": None,
        "valor_actual": 2.8,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-02",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-03-13",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.8,
        "valor_actual": 3.1,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-03",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-04-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 3.1,
        "valor_actual": 2.5,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-04",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-05-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas abril 2026",
        "periodo": "abril 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-05",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-06-12",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-06",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-07-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas junio 2026",
        "periodo": "junio 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-07",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-08-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas julio 2026",
        "periodo": "julio 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-08",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-09-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-09",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-10-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-10",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-11-13",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "VENTAS-2026-11",
        "indicador": "VENTAS_COMERCIO",
        "nombre": "Índice de Ventas de Comercio al por Menor",
        "fecha": "2026-12-14",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Variación de ventas minoristas noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "consumo",
        "impacto": "medio",
        "valor_anterior": 2.5,
        "valor_actual": None,
        "unidad": "% anual"
    },

    # ══════════════════════════════════════════════════════════════
    # IPI - Índice de Producción Industrial (INE, mensual)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "IPI-2026-01",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-02-27",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial enero 2026",
        "periodo": "enero 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": None,
        "valor_actual": -1.2,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-02",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-03-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial febrero 2026",
        "periodo": "febrero 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -1.2,
        "valor_actual": -3.7,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-03",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-04-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial marzo 2026",
        "periodo": "marzo 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -3.7,
        "valor_actual": -5.2,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-04",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-05-29",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial abril 2026",
        "periodo": "abril 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-05",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-06-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial mayo 2026",
        "periodo": "mayo 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-06",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-07-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial junio 2026",
        "periodo": "junio 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-07",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-08-31",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial julio 2026",
        "periodo": "julio 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-08",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-09-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial agosto 2026",
        "periodo": "agosto 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-09",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-10-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial septiembre 2026",
        "periodo": "septiembre 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-10",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-11-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial octubre 2026",
        "periodo": "octubre 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },
    {
        "id": "IPI-2026-11",
        "indicador": "IPI",
        "nombre": "Índice de Producción Industrial",
        "fecha": "2026-12-30",
        "hora": "09:00",
        "entidad": "INE",
        "descripcion": "Producción industrial noviembre 2026",
        "periodo": "noviembre 2026",
        "categoria": "produccion",
        "impacto": "medio",
        "valor_anterior": -5.2,
        "valor_actual": None,
        "unidad": "% anual"
    },

    # ══════════════════════════════════════════════════════════════
    # DEUDA PÚBLICA (Ministerio de Hacienda, trimestral)
    # ══════════════════════════════════════════════════════════════
    {
        "id": "DEUDA-2026-Q1",
        "indicador": "DEUDA_PUBLICA",
        "nombre": "Informe de Deuda Pública",
        "fecha": "2026-04-30",
        "hora": "12:00",
        "entidad": "Ministerio de Hacienda",
        "descripcion": "Estadísticas de deuda pública Q4 2025",
        "periodo": "Q4 2025",
        "categoria": "finanzas_publicas",
        "impacto": "medio",
        "valor_anterior": None,
        "valor_actual": 38.5,
        "unidad": "% del PIB"
    },
    {
        "id": "DEUDA-2026-Q2",
        "indicador": "DEUDA_PUBLICA",
        "nombre": "Informe de Deuda Pública",
        "fecha": "2026-07-31",
        "hora": "12:00",
        "entidad": "Ministerio de Hacienda",
        "descripcion": "Estadísticas de deuda pública Q1 2026",
        "periodo": "Q1 2026",
        "categoria": "finanzas_publicas",
        "impacto": "medio",
        "valor_anterior": 38.5,
        "valor_actual": None,
        "unidad": "% del PIB"
    },
    {
        "id": "DEUDA-2026-Q3",
        "indicador": "DEUDA_PUBLICA",
        "nombre": "Informe de Deuda Pública",
        "fecha": "2026-10-30",
        "hora": "12:00",
        "entidad": "Ministerio de Hacienda",
        "descripcion": "Estadísticas de deuda pública Q2 2026",
        "periodo": "Q2 2026",
        "categoria": "finanzas_publicas",
        "impacto": "medio",
        "valor_anterior": 38.5,
        "valor_actual": None,
        "unidad": "% del PIB"
    },
]

# ─── HELPERS ───────────────────────────────────────────────────────────────────

def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except:
        return None

def agregar_estado(evento):
    hoy = date.today()
    fecha = parse_date(evento["fecha"])
    e = evento.copy()
    if fecha:
        if fecha < hoy:
            e["estado"] = "publicado"
        elif fecha == hoy:
            e["estado"] = "hoy"
        else:
            e["estado"] = "proximo"
    else:
        e["estado"] = "sin_fecha"
    return e

def filtrar_eventos(eventos, params):
    resultado = [agregar_estado(ev) for ev in eventos]

    if "indicador" in params:
        indicador = params["indicador"].upper()
        resultado = [e for e in resultado if e["indicador"].upper() == indicador]

    if "categoria" in params:
        resultado = [e for e in resultado if e["categoria"] == params["categoria"].lower()]

    if "entidad" in params:
        resultado = [e for e in resultado if e["entidad"].upper() == params["entidad"].upper()]

    if "anio" in params:
        try:
            anio = int(params["anio"])
            resultado = [e for e in resultado if e["fecha"].startswith(str(anio))]
        except:
            pass

    if "mes" in params:
        try:
            mes = int(params["mes"])
            resultado = [e for e in resultado if parse_date(e["fecha"]) and parse_date(e["fecha"]).month == mes]
        except:
            pass

    if "impacto" in params:
        resultado = [e for e in resultado if e["impacto"] == params["impacto"].lower()]

    if "estado" in params:
        resultado = [e for e in resultado if e["estado"] == params["estado"].lower()]

    if "desde" in params:
        desde = parse_date(params["desde"])
        if desde:
            resultado = [e for e in resultado if parse_date(e["fecha"]) and parse_date(e["fecha"]) >= desde]

    if "hasta" in params:
        hasta = parse_date(params["hasta"])
        if hasta:
            resultado = [e for e in resultado if parse_date(e["fecha"]) and parse_date(e["fecha"]) <= hasta]

    resultado.sort(key=lambda e: e["fecha"])
    return resultado


# ─── RUTAS ─────────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET"])
def root():
    from flask import redirect
    return redirect("/calendario")

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "api": "Calendario Económico Chileno",
        "version": "2.0.0",
        "anio": 2026,
        "descripcion": "API con fechas de publicación de indicadores económicos de Chile 2026",
        "fuentes": ["Banco Central de Chile (BCCh)", "Instituto Nacional de Estadísticas (INE)", "Ministerio de Hacienda"],
        "endpoints": {
            "GET /calendario": "Interfaz visual del calendario",
            "GET /eventos": "Todos los eventos (con filtros opcionales)",
            "GET /eventos/<id>": "Evento por ID",
            "GET /eventos/proximos": "Próximos eventos",
            "GET /eventos/hoy": "Eventos de hoy",
            "GET /indicadores": "Lista de indicadores",
            "GET /categorias": "Lista de categorías",
            "GET /resumen": "Resumen estadístico",
        },
        "filtros_disponibles": {
            "indicador": "IPC | IPCSAE | IMACEC | PIB | TPM | IPoM | TASA_DESEMPLEO | BALANZA_COMERCIAL | IEF | PRECIO_COBRE | VENTAS_COMERCIO | IPI | DEUDA_PUBLICA | BALANZA_PAGOS",
            "categoria": "inflacion | actividad | politica_monetaria | mercado_laboral | comercio_exterior | commodities | estabilidad_financiera | finanzas_publicas | consumo | produccion | sector_externo",
            "entidad": "BCCh | INE | Ministerio de Hacienda",
            "anio": "2026",
            "mes": "1-12",
            "impacto": "bajo | medio | alto | muy_alto",
            "estado": "publicado | hoy | proximo",
            "desde": "YYYY-MM-DD",
            "hasta": "YYYY-MM-DD",
        },
        "ejemplo": "/eventos?indicador=IPC&anio=2026"
    })


@app.route("/eventos", methods=["GET"])
def get_eventos():
    params = request.args.to_dict()
    resultado = filtrar_eventos(EVENTOS, params)
    return jsonify({
        "total": len(resultado),
        "filtros_aplicados": params or None,
        "datos": resultado
    })


@app.route("/eventos/proximos", methods=["GET"])
def get_proximos():
    hoy = date.today()
    resultado = [agregar_estado(e) for e in EVENTOS if parse_date(e["fecha"]) and parse_date(e["fecha"]) >= hoy]
    resultado.sort(key=lambda e: e["fecha"])
    params = request.args.to_dict()
    if "indicador" in params:
        resultado = [e for e in resultado if e["indicador"].upper() == params["indicador"].upper()]
    if "categoria" in params:
        resultado = [e for e in resultado if e["categoria"] == params["categoria"]]
    if "limite" in params:
        try:
            resultado = resultado[:int(params["limite"])]
        except:
            pass
    return jsonify({"total": len(resultado), "desde": str(hoy), "datos": resultado})


@app.route("/eventos/hoy", methods=["GET"])
def get_hoy():
    hoy = date.today()
    resultado = [agregar_estado(e) for e in EVENTOS if parse_date(e["fecha"]) == hoy]
    return jsonify({"fecha": str(hoy), "total": len(resultado), "datos": resultado})


@app.route("/eventos/<string:evento_id>", methods=["GET"])
def get_evento(evento_id):
    evento = next((e for e in EVENTOS if e["id"] == evento_id), None)
    if not evento:
        return jsonify({"error": f"Evento '{evento_id}' no encontrado"}), 404
    return jsonify(agregar_estado(evento))


@app.route("/indicadores", methods=["GET"])
def get_indicadores():
    indicadores = {}
    for e in EVENTOS:
        ind = e["indicador"]
        if ind not in indicadores:
            indicadores[ind] = {
                "indicador": ind,
                "nombre": e["nombre"],
                "entidad": e["entidad"],
                "categoria": e["categoria"],
                "impacto": e["impacto"],
                "unidad": e["unidad"],
                "total_eventos_2026": 0
            }
        indicadores[ind]["total_eventos_2026"] += 1
    return jsonify({"total": len(indicadores), "indicadores": sorted(indicadores.values(), key=lambda x: x["nombre"])})


@app.route("/categorias", methods=["GET"])
def get_categorias():
    cat_map = {
        "inflacion": "Índices de Precios (IPC, IPCSAE)",
        "actividad": "Actividad Económica (IMACEC, PIB)",
        "politica_monetaria": "Política Monetaria (TPM, IPoM)",
        "mercado_laboral": "Empleo y Desempleo",
        "comercio_exterior": "Balanza Comercial y Exportaciones",
        "commodities": "Cobre y Materias Primas",
        "estabilidad_financiera": "Sistema Financiero (IEF)",
        "finanzas_publicas": "Sector Fiscal (Deuda Pública)",
        "consumo": "Ventas y Consumo",
        "produccion": "Producción Industrial",
        "sector_externo": "Balanza de Pagos",
    }
    categorias = {}
    for e in EVENTOS:
        cat = e["categoria"]
        if cat not in categorias:
            categorias[cat] = {"categoria": cat, "descripcion": cat_map.get(cat, cat), "total_eventos": 0}
        categorias[cat]["total_eventos"] += 1
    return jsonify({"total": len(categorias), "categorias": sorted(categorias.values(), key=lambda x: x["categoria"])})


@app.route("/calendario", methods=["GET"])
def calendario_ui():
    html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calendario Económico Chile 2026</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700;800&display=swap');
  :root {
    --bg:#0a0a0f;--surface:#13131a;--surface2:#1c1c27;--border:#2a2a3a;
    --accent:#c8ff00;--accent2:#00d4ff;--text:#e8e8f0;--muted:#6b6b85;
    --muy_alto:#ff4444;--alto:#ff9900;--medio:#00d4ff;--bajo:#6b6b85;
    --inflacion:#ff6b35;--actividad:#00d4ff;--politica_monetaria:#c8ff00;
    --mercado_laboral:#a855f7;--comercio_exterior:#22d3ee;--commodities:#fbbf24;
    --estabilidad_financiera:#34d399;--finanzas_publicas:#f472b6;
    --consumo:#60a5fa;--produccion:#94a3b8;--sector_externo:#4ade80;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:var(--bg);color:var(--text);font-family:'Syne',sans-serif;min-height:100vh;}
  header{background:var(--surface);border-bottom:1px solid var(--border);padding:20px 32px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;}
  .logo{display:flex;align-items:center;gap:12px;}
  .logo-icon{width:36px;height:36px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;}
  .logo h1{font-size:16px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;}
  .logo span{font-size:11px;color:var(--muted);font-family:'DM Mono',monospace;display:block;margin-top:1px;}
  .view-toggle{display:flex;background:var(--surface2);border:1px solid var(--border);border-radius:8px;overflow:hidden;}
  .view-btn{padding:8px 20px;background:none;border:none;color:var(--muted);font-family:'Syne',sans-serif;font-size:13px;font-weight:600;cursor:pointer;transition:all .2s;text-transform:uppercase;letter-spacing:.05em;}
  .view-btn.active{background:var(--accent);color:#000;}
  .container{display:grid;grid-template-columns:260px 1fr;height:calc(100vh - 77px);}
  .sidebar{background:var(--surface);border-right:1px solid var(--border);padding:24px 20px;overflow-y:auto;display:flex;flex-direction:column;gap:24px;}
  .sidebar-section h3{font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:10px;}
  .mini-nav{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
  .mini-nav button{background:none;border:1px solid var(--border);border-radius:6px;color:var(--text);width:28px;height:28px;cursor:pointer;font-size:14px;display:flex;align-items:center;justify-content:center;transition:border-color .2s;}
  .mini-nav button:hover{border-color:var(--accent);color:var(--accent);}
  .mini-nav .month-label{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;}
  .mini-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;}
  .mini-day-label{font-size:9px;font-family:'DM Mono',monospace;color:var(--muted);text-align:center;padding:4px 0;text-transform:uppercase;}
  .mini-day{aspect-ratio:1;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:11px;font-family:'DM Mono',monospace;cursor:pointer;transition:all .15s;position:relative;color:var(--muted);border:1px solid transparent;}
  .mini-day:hover{background:var(--surface2);color:var(--text);}
  .mini-day.has-event{color:var(--text);font-weight:500;}
  .mini-day.has-event::after{content:'';position:absolute;bottom:2px;left:50%;transform:translateX(-50%);width:4px;height:4px;border-radius:50%;background:var(--accent);}
  .mini-day.today{border-color:var(--accent);color:var(--accent);}
  .mini-day.selected{background:var(--accent);color:#000;font-weight:700;}
  .mini-day.selected::after{background:#000;}
  .mini-day.other-month{opacity:.2;}
  .filter-group{display:flex;flex-direction:column;gap:6px;}
  .filter-chip{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:6px;cursor:pointer;transition:background .15s;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);border:1px solid transparent;user-select:none;}
  .filter-chip:hover{background:var(--surface2);}
  .filter-chip.active{background:var(--surface2);border-color:var(--border);color:var(--text);}
  .filter-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
  .filter-count{margin-left:auto;font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);}
  .main{overflow-y:auto;padding:28px 32px;}
  .month-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;}
  .month-title{font-size:28px;font-weight:800;text-transform:uppercase;letter-spacing:.04em;}
  .month-subtitle{font-size:12px;font-family:'DM Mono',monospace;color:var(--muted);margin-top:2px;}
  .month-nav{display:flex;gap:8px;}
  .month-nav button{background:var(--surface);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:8px 16px;cursor:pointer;font-family:'Syne',sans-serif;font-size:13px;font-weight:600;transition:all .2s;}
  .month-nav button:hover{border-color:var(--accent);color:var(--accent);}
  .calendar-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:1px;background:var(--border);border:1px solid var(--border);border-radius:12px;overflow:hidden;}
  .cal-header{background:var(--surface2);padding:10px;text-align:center;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
  .cal-cell{background:var(--surface);min-height:110px;padding:8px;cursor:pointer;transition:background .15s;position:relative;}
  .cal-cell:hover{background:var(--surface2);}
  .cal-cell.today{background:#1a1a24;}
  .cal-cell.today .cal-day-num{color:var(--accent);}
  .cal-cell.selected{background:#1e2010;}
  .cal-cell.other-month{opacity:.35;}
  .cal-day-num{font-size:12px;font-family:'DM Mono',monospace;color:var(--muted);margin-bottom:6px;font-weight:500;}
  .cal-event{font-size:10px;padding:3px 6px;border-radius:4px;margin-bottom:2px;font-weight:600;letter-spacing:.03em;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;cursor:pointer;}
  .cal-event.muy_alto{background:rgba(255,68,68,.2);color:#ff6666;border-left:2px solid #ff4444;}
  .cal-event.alto{background:rgba(255,153,0,.2);color:#ffaa33;border-left:2px solid #ff9900;}
  .cal-event.medio{background:rgba(0,212,255,.15);color:#33ddff;border-left:2px solid #00d4ff;}
  .cal-event.bajo{background:rgba(107,107,133,.2);color:#8888aa;border-left:2px solid #6b6b85;}
  .cal-more{font-size:10px;color:var(--muted);font-family:'DM Mono',monospace;padding:2px 4px;}
  .day-view{display:none;}
  .day-header{margin-bottom:28px;}
  .day-date-big{font-size:48px;font-weight:800;line-height:1;letter-spacing:-.02em;}
  .day-date-big span{color:var(--accent);}
  .day-month-year{font-size:16px;color:var(--muted);font-family:'DM Mono',monospace;margin-top:4px;text-transform:uppercase;}
  .day-no-events{text-align:center;padding:60px 20px;color:var(--muted);font-size:14px;}
  .day-no-events .icon{font-size:48px;margin-bottom:16px;opacity:.4;}
  .event-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px 24px;margin-bottom:12px;display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:start;transition:border-color .2s;}
  .event-card:hover{border-color:var(--accent);}
  .event-card.muy_alto{border-left:3px solid var(--muy_alto);}
  .event-card.alto{border-left:3px solid var(--alto);}
  .event-card.medio{border-left:3px solid var(--medio);}
  .event-time{font-family:'DM Mono',monospace;font-size:13px;color:var(--muted);padding-top:2px;white-space:nowrap;}
  .event-indicador{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;}
  .event-nombre{font-size:15px;font-weight:600;margin-bottom:4px;}
  .event-desc{font-size:12px;color:var(--muted);line-height:1.5;}
  .event-meta{display:flex;flex-direction:column;align-items:flex-end;gap:6px;}
  .badge{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:3px 8px;border-radius:4px;white-space:nowrap;}
  .badge.muy_alto{background:rgba(255,68,68,.2);color:#ff6666;}
  .badge.alto{background:rgba(255,153,0,.2);color:#ffaa33;}
  .badge.medio{background:rgba(0,212,255,.15);color:#33ddff;}
  .badge.bajo{background:rgba(107,107,133,.2);color:#8888aa;}
  .badge-entidad{font-size:10px;font-family:'DM Mono',monospace;color:var(--muted);background:var(--surface2);padding:3px 8px;border-radius:4px;border:1px solid var(--border);}
  .valor-box{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap;}
  .valor-item{background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:6px 10px;font-family:'DM Mono',monospace;font-size:11px;}
  .valor-label{color:var(--muted);display:block;font-size:9px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:2px;}
  .valor-num{color:var(--accent);font-weight:500;font-size:13px;}
  .valor-num.pending{color:var(--muted);font-style:italic;}
  .today-badge{background:var(--accent);color:#000;font-size:10px;font-weight:700;padding:2px 8px;border-radius:20px;text-transform:uppercase;letter-spacing:.08em;margin-left:8px;}
  .legend-item{display:flex;align-items:center;gap:6px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);}
  .legend-dot{width:8px;height:8px;border-radius:50%;}
  ::-webkit-scrollbar{width:6px;}
  ::-webkit-scrollbar-track{background:transparent;}
  ::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
</style>
</head>
<body>
<header>
  <div class="logo">
    <div class="logo-icon">📊</div>
    <div>
      <h1>Calendario Económico</h1>
      <span>Chile 2026 · BCCh &amp; INE</span>
    </div>
  </div>
  <div class="view-toggle">
    <button class="view-btn active" onclick="setView('month')">Mes</button>
    <button class="view-btn" onclick="setView('day')">Día</button>
  </div>
</header>
<div class="container">
  <div class="sidebar">
    <div class="sidebar-section">
      <h3>Navegación</h3>
      <div class="mini-nav">
        <button onclick="prevMonth()">&#8592;</button>
        <span class="month-label" id="mini-month-label"></span>
        <button onclick="nextMonth()">&#8594;</button>
      </div>
      <div class="mini-grid" id="mini-grid"></div>
    </div>
    <div class="sidebar-section">
      <h3>Categorías</h3>
      <div class="filter-group" id="filter-group"></div>
    </div>
    <div class="sidebar-section">
      <h3>Nivel de impacto</h3>
      <div style="display:flex;flex-direction:column;gap:6px">
        <div class="legend-item"><span class="legend-dot" style="background:#ff4444"></span> Muy alto</div>
        <div class="legend-item"><span class="legend-dot" style="background:#ff9900"></span> Alto</div>
        <div class="legend-item"><span class="legend-dot" style="background:#00d4ff"></span> Medio</div>
        <div class="legend-item"><span class="legend-dot" style="background:#6b6b85"></span> Bajo</div>
      </div>
    </div>
  </div>
  <div class="main">
    <div id="month-view">
      <div class="month-header">
        <div>
          <div class="month-title" id="month-title"></div>
          <div class="month-subtitle" id="month-subtitle"></div>
        </div>
        <div class="month-nav">
          <button onclick="prevMonth()">&#8592; Anterior</button>
          <button onclick="goToday()">Hoy</button>
          <button onclick="nextMonth()">Siguiente &#8594;</button>
        </div>
      </div>
      <div class="calendar-grid" id="calendar-grid"></div>
    </div>
    <div id="day-view" class="day-view">
      <div class="day-header">
        <div class="day-date-big" id="day-date-big"></div>
        <div class="day-month-year" id="day-month-year"></div>
      </div>
      <div id="day-events-list"></div>
    </div>
  </div>
</div>
<script>
let EVENTOS=[];
let currentView='month';
let currentYear=2026;
let currentMonth=0;
let selectedDay=null;
let activeFilters=new Set();

const MESES=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
const DIAS=['Dom','Lun','Mar','Mié','Jue','Vie','Sáb'];
const CAT_LABELS={inflacion:'Inflación',actividad:'Actividad',politica_monetaria:'Pol. Monetaria',mercado_laboral:'Empleo',comercio_exterior:'Com. Exterior',commodities:'Commodities',estabilidad_financiera:'Est. Financiera',finanzas_publicas:'Fin. Públicas',consumo:'Consumo',produccion:'Producción',sector_externo:'Sect. Externo'};

async function loadData(){
  const res=await fetch('/eventos?anio=2026');
  const json=await res.json();
  EVENTOS=json.datos;
  // Arrancar en el mes actual si estamos en 2026, si no en enero
  const hoy=new Date();
  if(hoy.getFullYear()===2026){currentYear=2026;currentMonth=hoy.getMonth();}
  else{currentYear=2026;currentMonth=0;}
  buildFilters();
  render();
}

function eventosDelDia(y,m,d){
  const s=`${y}-${String(m+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
  return EVENTOS.filter(e=>e.fecha===s&&(activeFilters.size===0||activeFilters.has(e.categoria)));
}
function eventosDelMes(y,m){
  const p=`${y}-${String(m+1).padStart(2,'0')}`;
  return EVENTOS.filter(e=>e.fecha.startsWith(p)&&(activeFilters.size===0||activeFilters.has(e.categoria)));
}

function buildFilters(){
  const cats={};
  EVENTOS.forEach(e=>{cats[e.categoria]=(cats[e.categoria]||0)+1;});
  const g=document.getElementById('filter-group');
  g.innerHTML='';
  Object.entries(cats).sort((a,b)=>b[1]-a[1]).forEach(([cat,count])=>{
    const chip=document.createElement('div');
    chip.className='filter-chip';
    chip.innerHTML=`<span class="filter-dot" style="background:var(--${cat},#6b6b85)"></span>${CAT_LABELS[cat]||cat}<span class="filter-count">${count}</span>`;
    chip.onclick=()=>{
      if(activeFilters.has(cat))activeFilters.delete(cat);else activeFilters.add(cat);
      chip.classList.toggle('active',activeFilters.has(cat));
      render();
    };
    g.appendChild(chip);
  });
}

function setView(v){
  currentView=v;
  document.querySelectorAll('.view-btn').forEach((b,i)=>b.classList.toggle('active',(i===0&&v==='month')||(i===1&&v==='day')));
  document.getElementById('month-view').style.display=v==='month'?'block':'none';
  document.getElementById('day-view').style.display=v==='day'?'block':'none';
  render();
}

function render(){renderMiniCalendar();if(currentView==='month')renderMonth();else renderDay();}

function renderMonth(){
  const today=new Date();
  document.getElementById('month-title').textContent=`${MESES[currentMonth]} ${currentYear}`;
  const evMes=eventosDelMes(currentYear,currentMonth);
  document.getElementById('month-subtitle').innerHTML=
    `${evMes.length} evento${evMes.length!==1?'s':''} este mes`+
    (today.getMonth()===currentMonth&&today.getFullYear()===currentYear?
      `<span class="today-badge">Hoy: ${today.getDate()}</span>`:'');
  const grid=document.getElementById('calendar-grid');
  grid.innerHTML='';
  DIAS.forEach(d=>{const h=document.createElement('div');h.className='cal-header';h.textContent=d;grid.appendChild(h);});
  const firstDay=new Date(currentYear,currentMonth,1).getDay();
  const daysInMonth=new Date(currentYear,currentMonth+1,0).getDate();
  const daysInPrev=new Date(currentYear,currentMonth,0).getDate();
  for(let i=firstDay-1;i>=0;i--){const c=document.createElement('div');c.className='cal-cell other-month';c.innerHTML=`<div class="cal-day-num">${daysInPrev-i}</div>`;grid.appendChild(c);}
  for(let d=1;d<=daysInMonth;d++){
    const cell=document.createElement('div');
    const isToday=today.getDate()===d&&today.getMonth()===currentMonth&&today.getFullYear()===currentYear;
    const isSel=selectedDay&&selectedDay.d===d&&selectedDay.m===currentMonth&&selectedDay.y===currentYear;
    cell.className=`cal-cell${isToday?' today':''}${isSel?' selected':''}`;
    const evs=eventosDelDia(currentYear,currentMonth,d);
    let html=`<div class="cal-day-num">${d}</div>`;
    evs.slice(0,3).forEach(e=>{html+=`<div class="cal-event ${e.impacto}" title="${e.nombre}">${e.indicador}</div>`;});
    if(evs.length>3)html+=`<div class="cal-more">+${evs.length-3} más</div>`;
    cell.innerHTML=html;
    cell.onclick=()=>{selectedDay={d,m:currentMonth,y:currentYear};setView('day');};
    grid.appendChild(cell);
  }
  const total=firstDay+daysInMonth;
  const rem=total%7===0?0:7-(total%7);
  for(let d=1;d<=rem;d++){const c=document.createElement('div');c.className='cal-cell other-month';c.innerHTML=`<div class="cal-day-num">${d}</div>`;grid.appendChild(c);}
}

function renderDay(){
  const day=selectedDay||{d:new Date().getDate(),m:new Date().getMonth(),y:new Date().getFullYear()};
  if(!selectedDay)selectedDay=day;
  const weekday=DIAS[(new Date(day.y,day.m,day.d)).getDay()];
  document.getElementById('day-date-big').innerHTML=`<span>${weekday}</span> ${day.d}`;
  document.getElementById('day-month-year').textContent=`${MESES[day.m]} ${day.y}`;
  const evs=eventosDelDia(day.y,day.m,day.d);
  const list=document.getElementById('day-events-list');
  if(evs.length===0){list.innerHTML=`<div class="day-no-events"><div class="icon">📭</div>No hay publicaciones para este día.</div>`;return;}
  list.innerHTML=evs.map(e=>{
    const vA=e.valor_actual!==null&&e.valor_actual!==undefined?`<span class="valor-num">${e.valor_actual} ${e.unidad}</span>`:`<span class="valor-num pending">Pendiente</span>`;
    const vP=e.valor_anterior!==null&&e.valor_anterior!==undefined?`<span class="valor-num">${e.valor_anterior} ${e.unidad}</span>`:`<span class="valor-num pending">—</span>`;
    return `<div class="event-card ${e.impacto}">
      <div class="event-time">${e.hora}</div>
      <div class="event-body">
        <div class="event-indicador" style="color:var(--${e.categoria},#c8ff00)">${e.indicador}</div>
        <div class="event-nombre">${e.nombre}</div>
        <div class="event-desc">${e.descripcion} · Período: ${e.periodo}</div>
        <div class="valor-box">
          <div class="valor-item"><span class="valor-label">Anterior</span>${vP}</div>
          <div class="valor-item"><span class="valor-label">Actual</span>${vA}</div>
        </div>
      </div>
      <div class="event-meta">
        <span class="badge ${e.impacto}">${e.impacto.replace('_',' ')}</span>
        <span class="badge-entidad">${e.entidad}</span>
        <span class="badge-entidad" style="color:var(--${e.estado==='publicado'?'accent2':'alto'})">${e.estado}</span>
      </div>
    </div>`;
  }).join('');
}

function renderMiniCalendar(){
  const today=new Date();
  document.getElementById('mini-month-label').textContent=MESES[currentMonth].substring(0,3).toUpperCase()+' '+currentYear;
  const grid=document.getElementById('mini-grid');
  grid.innerHTML='';
  ['D','L','M','X','J','V','S'].forEach(d=>{const el=document.createElement('div');el.className='mini-day-label';el.textContent=d;grid.appendChild(el);});
  const firstDay=new Date(currentYear,currentMonth,1).getDay();
  const daysInMonth=new Date(currentYear,currentMonth+1,0).getDate();
  const daysInPrev=new Date(currentYear,currentMonth,0).getDate();
  for(let i=firstDay-1;i>=0;i--){const el=document.createElement('div');el.className='mini-day other-month';el.textContent=daysInPrev-i;grid.appendChild(el);}
  for(let d=1;d<=daysInMonth;d++){
    const el=document.createElement('div');
    const isToday=today.getDate()===d&&today.getMonth()===currentMonth&&today.getFullYear()===currentYear;
    const isSel=selectedDay&&selectedDay.d===d&&selectedDay.m===currentMonth&&selectedDay.y===currentYear;
    const hasEv=eventosDelDia(currentYear,currentMonth,d).length>0;
    el.className=`mini-day${hasEv?' has-event':''}${isToday?' today':''}${isSel?' selected':''}`;
    el.textContent=d;
    el.onclick=()=>{selectedDay={d,m:currentMonth,y:currentYear};setView('day');};
    grid.appendChild(el);
  }
  const total=firstDay+daysInMonth;
  const rem=total%7===0?0:7-(total%7);
  for(let d=1;d<=rem;d++){const el=document.createElement('div');el.className='mini-day other-month';el.textContent=d;grid.appendChild(el);}
}

function prevMonth(){
  if(currentMonth===0&&currentYear===2026)return;
  currentMonth--;
  if(currentMonth<0){currentMonth=11;currentYear--;}
  render();
}
function nextMonth(){
  if(currentMonth===11&&currentYear===2026)return;
  currentMonth++;
  if(currentMonth>11){currentMonth=0;currentYear++;}
  render();
}
function goToday(){
  const t=new Date();
  currentYear=2026;
  currentMonth=t.getFullYear()===2026?t.getMonth():0;
  selectedDay=null;
  setView('month');
}
loadData();
</script>
</body>
</html>"""
    return html


@app.route("/resumen", methods=["GET"])
def get_resumen():
    hoy = date.today()
    todos = [agregar_estado(e) for e in EVENTOS]
    publicados = [e for e in todos if e["estado"] == "publicado"]
    proximos = [e for e in todos if e["estado"] in ("proximo", "hoy")]
    entidades = {}
    for e in todos:
        ent = e["entidad"]
        entidades[ent] = entidades.get(ent, 0) + 1
    impactos = {}
    for e in todos:
        imp = e["impacto"]
        impactos[imp] = impactos.get(imp, 0) + 1
    categorias = {}
    for e in todos:
        cat = e["categoria"]
        categorias[cat] = categorias.get(cat, 0) + 1
    return jsonify({
        "fecha_consulta": str(hoy),
        "anio_calendario": 2026,
        "total_eventos": len(todos),
        "publicados": len(publicados),
        "proximos": len(proximos),
        "por_entidad": entidades,
        "por_impacto": impactos,
        "por_categoria": categorias,
        "proximo_evento": proximos[0] if proximos else None
    })


# ─── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("╔════════════════════════════════════════════════╗")
    print("║   Calendario Económico Chileno 2026           ║")
    print("╠════════════════════════════════════════════════╣")
    print("║  http://localhost:5000/                        ║")
    print("╚════════════════════════════════════════════════╝")
    app.run(debug=False, use_reloader=False, port=5000)