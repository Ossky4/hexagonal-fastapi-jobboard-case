# Comparativa final — diez Case Projects

## Propósito
Comparar los diez casos realizados para identificar qué tipo de señal aporta cada uno, en qué condiciones Codex rinde mejor y qué hipótesis conviene probar a continuación.

## Caso 1 — mi-primer-repo
Este repositorio funcionó como sandbox inicial para validar el método base de trabajo con Codex en condiciones controladas.

### Qué se probó
- PRs pequeñas y de una sola intención.
- Cambios pequeños de código, tests y documentación.
- Bugfixes y mejoras de UX de bajo riesgo.
- Refactors pequeños, incluyendo un caso multiarchivo.

### Qué señal aportó
`mi-primer-repo` confirmó que el método base funciona bien cuando:
- el contexto es simple,
- el riesgo es bajo,
- la validación es barata,
- y el alcance está claramente delimitado.

También sirvió para fijar un patrón operativo:
- contrato claro,
- PR pequeña,
- checks explícitos,
- microevaluación humana al cierre.

## Caso 2 — csvtools-case
Este repositorio funcionó como primer Case Project de cleanup arquitectónico pequeño en un entorno más real que el sandbox inicial.

### Qué se probó
- PR1 documental para delimitar alcance y hotspots.
- Cleanup local mínimo.
- Cleanup multiarchivo real.
- Blindaje con tests sobre una frontera tratada.
- Mejora mínima del entorno de tests.
- Documentación reutilizable del método.

### Qué señal aportó
`csvtools-case` confirmó que Codex puede trabajar con control en un repo más real cuando:
- el hotspot está bien delimitado,
- el cambio sigue siendo pequeño y reversible,
- la validación mínima del repo es suficiente,
- y la revisión humana mantiene disciplina de alcance.

También mostró que mejorar pronto la infraestructura mínima de validación aumenta la calidad de las PRs posteriores.

## Caso 3 — timesheet-case
Este repositorio funcionó como caso para medir una hipótesis distinta: elección entre varias alternativas plausibles de cleanup.

### Qué se probó
- PR1 de selección explícita entre alternativas.
- Rechazo de una primera dirección menos conservadora.
- Reformulación de PR2 hacia una opción más prudente.
- Blindaje con tests.
- Ajuste mínimo de entorno para hacer ejecutable el blindaje.
- Retrospectiva breve de cierre.

### Qué señal aportó
`timesheet-case` añadió una señal nueva respecto a los casos anteriores:
no solo que Codex puede ejecutar cambios pequeños, sino que puede participar en una decisión local entre varias opciones plausibles, siempre que existan:
- alcance explícito,
- criterio conservador,
- revisión humana disciplinada,
- y validación mínima suficiente.

También mostró que la revisión humana no solo valida ejecución, sino calidad de decisión.

## Caso 4 — har-file-sanitiser-case
Este repositorio funcionó como caso para medir una hipótesis de dependencias internas más ricas entre módulos (`cli`, `core`, `utils`) sin abandonar el marco de PRs pequeñas.

### Qué se probó
- PR1 documental para delimitar la frontera bajo observación.
- PR2 técnica mínima sobre un ajuste conservador de límites entre CLI y core.
- PR3 de blindaje explícito de la delegación a streaming sin prelectura redundante.
- PR4 mínima de compatibilidad para hacer ejecutable el test objetivo en Python 3.10, sin abrir un frente amplio.

### Qué señal aportó
`har-file-sanitiser-case` aportó una señal útil sobre un contexto con dependencias internas más ricas:
- Codex puede mantener criterio conservador en una frontera más densa,
- puede sostener el cambio con blindaje específico,
- y puede aceptar una corrección mínima de compatibilidad cuando esa corrección sigue siendo local, explícita y de una sola intención.

También confirmó que no toda fricción de entorno justifica abrir una reforma amplia: a veces existe una salida pequeña y suficiente.

## Caso 5 — pytest-fastapi-crud-example-case
Este repositorio funcionó como caso para medir una ruta multicapa más explícita: API → lógica intermedia → acceso a base de datos, manteniendo PRs pequeñas.

### Qué se probó
- PR1 documental para delimitar la ruta multicapa bajo observación.
- PR2 técnica mínima con extracción local y conservadora de una operación repetida dentro de `app/user.py`.
- PR3 de blindaje específico sobre reutilización del helper compartido en `get_user` y `update_user`.
- PR4 documental de cierre, dejando explícito el límite de validación por entorno.

### Qué señal aportó
`pytest-fastapi-crud-example-case` añadió una señal distinta:
- Codex puede sostener un cambio pequeño dentro de una ruta que atraviesa varias capas internas,
- puede evitar un salto prematuro a una arquitectura más ambiciosa,
- y puede mantener disciplina de PR pequeña incluso en una ruta más densa que las tratadas antes.

El límite principal fue que la validación dinámica final quedó condicionada por fricción de entorno ajena al hotspot trabajado.

## Caso 6 — fastapi-onion-architecture-case
Este repositorio funcionó como caso para medir una ruta multicapa más profunda, con coordinación entre router, service y repository, y con dependencias internas más densas que en los casos anteriores.

### Qué se probó
- PR1 documental para delimitar la ruta bajo observación.
- PR2 técnica mínima de alineación de contrato interno entre `UserService.get_users_by_filters(...)` y `UserRepository.get_users_by_filters(...)`.
- PR3 de blindaje pequeño con test focalizado sobre `GET /user/filters/` para fijar la delegación del contrato interno.
- Evaluación explícita de viabilidad de PR4 mínima, concluyendo que corregir la fricción de entorno excedía el perímetro acordado.
- Cierre del caso sin expandir alcance.

### Qué señal aportó
`fastapi-onion-architecture-case` añadió una señal útil sobre un nivel más alto de densidad interna:
- Codex puede sostener una decisión conservadora en una ruta con varias capas más profundas,
- puede alinear un contrato interno pequeño sin rediseño de arquitectura,
- y puede blindar esa decisión con un test focalizado.

También aportó una señal metodológica importante:
cuando la fricción final pertenece al entorno y la corrección mínima real excede el perímetro experimental, la decisión correcta puede ser cerrar el caso con trazabilidad en lugar de seguir abriendo PRs.

## Caso 7 — layered-architecture-case
Este repositorio funcionó como caso para medir una ruta multicapa profunda con una frontera interna más densa entre `dependency` y `factory`, y para evaluar si una PR4 mínima de entorno merecía realmente la pena.

### Qué se probó
- PR1 documental para delimitar una ruta multicapa profunda y varias alternativas competitivas.
- PR2 técnica mínima sobre el borde `services/dependency.py` ↔ `factories/order.py`, aclarando que `dependency` recibe `db` explícitamente y delega la construcción al factory.
- PR3 de blindaje pequeño con tests unitarios focalizados sobre esa delegación.
- Evaluación de viabilidad de PR4 mínima.
- PR4 efectiva en `tests/conftest.py`, con lazy init del session factory para evitar que infraestructura DB bloquee tests unitarios que no la necesitan.

### Qué señal aportó
`layered-architecture-case` añade una señal especialmente valiosa:
- Codex puede sostener una intervención pequeña y conservadora en una frontera interna más profunda,
- puede blindar esa decisión con tests unitarios bien focalizados,
- y puede ejecutar una PR4 de entorno realmente mínima cuando la causa está bien aislada y el beneficio es directo.

Este caso ayuda a distinguir dos situaciones metodológicas:
- cuando conviene cerrar el caso sin expandir alcance,
- y cuando sí existe una corrección local de entorno que merece ejecutarse porque mejora la validación sin abrir un frente amplio.

## Caso 8 — fastapi-clean-example-case
Este repositorio funcionó como caso para medir una ruta profunda con varias capas (`inbound -> core -> outbound`) y, además, con alternativas pequeñas realmente competitivas dentro del mismo hotspot.

### Qué se probó
- PR1 documental para delimitar la ruta **Create User** como hipótesis de trabajo.
- PR2 técnica mínima en el borde `core ↔ outbound`, eliminando un `try/except UsernameAlreadyExistsError: raise` redundante en `CreateUser.execute`.
- PR3 de blindaje pequeño con un test unitario focalizado para fijar que `CreateUser.execute` propaga `UsernameAlreadyExistsError` emitido por `Flusher.flush()` y no alcanza `commit` en ese camino.
- Evaluación de viabilidad de PR4 mínima en el entorno disponible.
- Cierre documental del caso al concluir que no existía una PR4 mínima real bajo Python 3.10, dado que el proyecto apunta a un runtime más moderno y usa features fuera del contrato de ese entorno.

### Qué señal aportó
`fastapi-clean-example-case` añade una señal importante sobre un salto más exigente:
- había competencia real entre alternativas pequeñas dentro del mismo hotspot,
- Codex pudo elegir una opción conservadora sin derivar a refactor amplio,
- y se reforzó metodológicamente que no conviene introducir workarounds técnicos en un runtime fuera del contrato declarado del proyecto.

También aportó una señal de gobernanza útil:
la validación recuperada fue focalizada en el test objetivo del caso, sin perseguir green completo del runner estándar.

Y, cuando el bloqueo final dejó de ser una fricción local para convertirse en incompatibilidad estructural de versión, la decisión correcta fue cerrar el caso con trazabilidad.

## Caso 9 — hexagonal-architecture-python-case
Este repositorio funcionó como caso para medir una ruta profunda de exportación (`POST /clients/exports`) en una arquitectura hexagonal, con varias capas internas y alternativas pequeñas realmente competitivas dentro del mismo hotspot.

### Qué se probó
- PR1 documental para delimitar la ruta **`/clients/exports`** como hipótesis de trabajo.
- PR2 técnica mínima en `ParserFactory`, haciendo explícito el matching por `ExportFormat` en lugar de literales string.
- PR3 de blindaje pequeño con un test unitario parametrizado para fijar que `ParserFactory.build(...)` resuelve el parser correcto a partir de `ExportFormat`.
- Evaluación de viabilidad de PR4 mínima en el entorno disponible.
- PR4 efectiva en `tests/conftest.py`, con import diferido de `src.app` y valor local por defecto para `S3_CLIENTS_BUCKET`, para evitar side-effects de collection no relacionados con el test objetivo.

### Qué señal aportó
`hexagonal-architecture-python-case` añadió una señal especialmente útil porque combina varios elementos a la vez:
- había competencia real entre alternativas pequeñas dentro de una ruta profunda,
- Codex pudo ejecutar una decisión conservadora y bien localizada en el punto de selección del parser,
- la validación recuperada fue focalizada sobre el test objetivo del caso,
- y sí existió una PR4 mínima de entorno que merecía ejecutarse.

Este caso añadió un matiz metodológico importante:
esa validación focalizada no equivalió a green completo del comando estándar de `pytest`, cuyo fallo restante quedó fuera del alcance acotado de la PR4.

## Caso 10 — hexagonal-fastapi-jobboard-case
Este repositorio funcionó como caso para medir una ruta profunda en arquitectura hexagonal con varias capas internas (`route -> service -> uow -> repository`) y alternativas pequeñas realmente competitivas dentro del mismo hotspot.

### Qué se probó
- PR1 documental para delimitar la ruta de Jobs como hipótesis de trabajo.
- PR2 técnica mínima en `use_cases/jobs.py`, aclarando la asignación de `owner_id` en update sin mutar indirectamente el DTO de entrada.
- PR3 de blindaje pequeño con un test unitario focalizado para fijar que `update_job_by_id` asigna `owner_id` al registro persistente sin mutar el DTO.
- Evaluación de viabilidad de PR4 mínima en el entorno disponible.
- PR4 efectiva en `tests/conftest.py`, reduciendo side-effects de import durante collection para tests unitarios no relacionados.

### Qué señal aportó
`hexagonal-fastapi-jobboard-case` aportó señal útil sobre una ruta profunda con alternativas pequeñas pero competitivas.  
Se tomó una decisión conservadora y bien blindada.  
La validación recuperada fue focalizada en el test objetivo del caso, y sí existió una PR4 mínima de entorno que efectivamente justificaba su ejecución.

También reforzó una distinción metodológica importante:
- existencia de una PR4 mínima viable,
- validación focalizada suficiente para cerrar la hipótesis del caso,
- y green completo del runner o de la suite dependiente de `app`, que puede quedar legítimamente fuera de alcance cuando el bootstrap pesado está fuera del perímetro acordado.

## Diferencias clave entre los diez casos

### mi-primer-repo
- mayor control,
- menor complejidad,
- señal rápida,
- mejor para fijar el método base.

### csvtools-case
- más real que el sandbox,
- útil para medir cleanup multiarchivo pequeño,
- buena base para consolidar método reusable.

### timesheet-case
- mejor para medir elección entre alternativas plausibles,
- más dependiente de revisión humana para distinguir una solución válida de la opción más conservadora,
- buena señal sobre reformulación prudente.

### har-file-sanitiser-case
- mejor para medir criterio conservador en una frontera con dependencias internas más ricas,
- buena señal sobre correcciones mínimas de compatibilidad sin expansión innecesaria.

### pytest-fastapi-crud-example-case
- mejor para medir disciplina conservadora dentro de una ruta multicapa más explícita,
- buena señal sobre coordinación local entre API, lógica intermedia y acceso a datos,
- con límite claro de validación condicionado por el entorno.

### fastapi-onion-architecture-case
- mejor para medir coordinación en una ruta multicapa más profunda y con mayor densidad entre capas,
- buena señal sobre alineación mínima de contrato interno entre service y repository,
- y buena señal de gobernanza experimental al cerrar el caso sin forzar una expansión de alcance.

### layered-architecture-case
- mejor para medir una frontera profunda entre capas intermedias (`dependency` ↔ `factory`),
- buena señal sobre blindaje unitario de una aclaración pequeña de borde,
- y primera evidencia clara de una PR4 mínima de entorno que sí merecía ejecutarse.

### fastapi-clean-example-case
- mejor para medir competencia real entre varias alternativas pequeñas dentro de una ruta profunda,
- buena señal sobre limpieza conservadora del borde `core ↔ outbound`,
- y buena señal metodológica al no aceptar workarounds en un runtime fuera del contrato del proyecto.

### hexagonal-architecture-python-case
- mejor para medir competencia real entre alternativas pequeñas dentro de una ruta profunda hexagonal con salida a infraestructura,
- buena señal sobre cleanup conservador en un punto de selección interna (`ParserFactory`),
- y buena señal sobre PR4 mínima de entorno que recupera validación focalizada, no green completo del runner estándar.

### hexagonal-fastapi-jobboard-case
- mejor para medir competencia real entre alternativas pequeñas dentro de una ruta profunda `route -> service -> uow -> repository`,
- buena señal sobre cleanup conservador en el caso de uso sin tocar arquitectura,
- y buena señal sobre PR4 mínima de entorno que recupera validación focalizada, no green completo de los tests que usan `app`.

## Aprendizajes operativos comunes
En los diez casos, Codex rindió mejor cuando se mantuvieron estas condiciones:
- una sola intención por PR,
- cambios pequeños y revisables,
- restricciones explícitas,
- checks claros,
- separación entre fallo del entorno y efecto del cambio,
- microevaluación humana breve tras cada revisión.

## Qué parece funcionar mejor
Codex aporta más valor cuando trabaja como:
- operador técnico de ejecución,
- sobre hotspots acotados,
- con decisiones reversibles,
- en repos con validación razonablemente barata,
- y con revisión humana que discipline alcance y criterio.

## Límites observados
- El valor cae cuando la PR aporta más higiene local que señal estructural.
- La señal empeora cuando el entorno de validación introduce demasiado ruido.
- Ya hay evidencia sólida sobre cleanup pequeño, multiarchivo pequeño, elección conservadora local, fronteras con dependencias internas más ricas y rutas multicapa explícitas.
- También hay evidencia de que la gobernanza del experimento importa: no toda fricción merece una PR adicional, no toda “solución local” debe mergearse si el runtime o el bootstrap pesado siguen fuera de contrato, y no toda PR4 mínima implica green completo del runner estándar o de los tests que dependen de `app`.
- Aún no se ha probado con suficiente claridad una situación donde, dentro de una misma ruta profunda, dos o tres alternativas pequeñas igualmente razonables sigan compitiendo hasta el final con validación completa en entorno alineado y runner estándar en verde.

## Conclusión
Los diez casos, en conjunto, sugieren que Codex funciona bien en cambios pequeños, acotados, reversibles y bien revisados.

La evidencia acumulada es especialmente sólida en diez planos:
1. ejecución disciplinada de PRs pequeñas,
2. cleanup multiarchivo pequeño con validación suficiente,
3. elección conservadora entre alternativas plausibles,
4. mantenimiento del criterio en fronteras con dependencias internas más ricas,
5. disciplina de alcance dentro de rutas multicapa explícitas,
6. capacidad de cerrar un caso correctamente cuando el entorno ya no justifica expandir alcance,
7. capacidad de ejecutar una PR4 mínima de entorno cuando la causa está bien aislada y el beneficio es directo,
8. capacidad de distinguir entre una fricción local corregible y una incompatibilidad estructural que no debe resolverse con workarounds,
9. capacidad de distinguir entre validación focalizada suficiente para cerrar la hipótesis del caso y normalización completa del entorno de test,
10. capacidad de recuperar validación focalizada en repos con bootstrap pesado sin confundir ese logro con un green completo del runner o de los tests de rutas.

## Recomendación de la siguiente hipótesis experimental
No seguir por inercia en ninguno de estos diez repositorios.

La siguiente hipótesis debería subir un nivel y probar esto:

**Codex puede sostener criterio conservador en una ruta profunda con varias capas internas cuando dos o tres alternativas pequeñas realmente competitivas siguen siendo plausibles hasta la fase técnica, y puede cerrarla con buena gobernanza experimental sin perder disciplina de PR pequeña ni claridad de validación, distinguiendo correctamente entre validación focalizada suficiente, PR4 mínima viable y green completo del runner estándar.**

## Qué debería tener el siguiente repo
- entrypoint claro,
- coordinador o capa intermedia explícita,
- lógica central distinguible,
- adaptador o persistencia ligera,
- tests locales suficientes para validar una ruta concreta,
- ausencia de infraestructura pesada o dependencias externas dominantes,
- y un hotspot donde varias alternativas pequeñas sigan siendo competitivas también después de la inspección técnica inicial.

## Recomendación final
Usar esta comparativa como documento de cierre del bloque actual y como base para seleccionar el siguiente repositorio candidato, evitando repetir hipótesis ya suficientemente medidas y priorizando ahora un caso donde la competencia entre alternativas pequeñas se mantenga fuerte también durante la PR técnica y donde la calidad de validación recuperada pueda evaluarse con más precisión.
