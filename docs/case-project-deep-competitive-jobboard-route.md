# Case Project (PR1): ruta profunda con alternativas competitivas en `jobboard`

## Propósito del caso
Delimitar una hipótesis **conservadora y verificable** para un cleanup pequeño en una ruta interna de `src/jobboard`, antes de cualquier cambio técnico.

## Hipótesis del experimento
Codex puede sostener criterio conservador en una ruta profunda con varias capas internas cuando existen 2–3 alternativas pequeñas realmente competitivas dentro del mismo hotspot, manteniendo PR pequeña y validación clara.

## Capas o módulos bajo observación
A partir de la estructura visible y tests existentes, la observación se centra en el flujo de Jobs entre:

- Entrada HTTP (`adapters/entrypoints/api/v1/route_jobs.py`)
- Caso de uso (`adapters/use_cases/jobs.py`)
- Unit of Work (`adapters/unit_of_works/jobs.py` + `domain/ports/unit_of_works/jobs.py`)
- Repositorio (`adapters/repositories/jobs.py` + `domain/ports/repositories/jobs.py`)
- Cobertura de ruta (`tests/test_routes/test_jobs.py`)

## Ruta interna bajo observación (hipótesis de trabajo)
Ruta profunda candidata: `update/delete` de Jobs en API, atravesando `route -> service -> uow -> repository` y regresando a la capa HTTP.

> Esta ruta se toma como **hipótesis de trabajo** por su carácter multicapa y su presencia en tests de rutas; no se declara aún un defecto interno demostrado.

## Alternativas plausibles y competitivas (cleanup pequeño)
1. **Normalización mínima de respuestas HTTP en `route_jobs.py`**  
   Reducir duplicación de construcción de `Response` (json + status + media type) con helper local de una sola intención.

2. **Ajuste mínimo de contrato en update de Jobs (`use_cases/jobs.py`)**  
   Evitar mutación indirecta del DTO en update y hacer explícita la asignación de campos de actualización/ownership, sin rediseñar capas.

3. **Alineación mínima `service/repository` para operación de update**  
   Homogeneizar la forma de obtención/uso del registro para update (manteniendo interfaz actual), buscando legibilidad y menor ambigüedad operacional.

## Criterio para elegir entre alternativas
Elegir primero la alternativa que maximice simultáneamente:

- **Menor superficie de cambio** (pocos archivos y bajo riesgo).
- **Una sola intención técnica** claramente revisable en PR.
- **Validación directa con tests existentes** (o ajustes mínimos y locales de pruebas).
- **Sin impacto arquitectónico amplio** ni cambios de comportamiento no necesarios.

## Fuera de alcance en esta PR1
- Implementar el cleanup técnico.
- Cambiar dominio, arquitectura hexagonal o contratos amplios entre capas.
- Reorganizar módulos o carpetas.
- Cambiar setup, CI, README, workflows o configuración.

## Secuencia prevista de PRs
- **PR1 (actual):** delimitación documental de ruta/hipótesis y alternativas competitivas.
- **PR2 (técnica, pequeña):** ejecutar **una** alternativa elegida con una sola intención.
- **PR3 (opcional):** segunda mejora pequeña en el mismo hotspot, solo si PR2 confirma que sigue siendo conservador.
