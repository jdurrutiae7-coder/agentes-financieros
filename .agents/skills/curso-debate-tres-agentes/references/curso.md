---
name: debate-tres-agentes
description: Organiza un debate entre tres agentes (bajista, neutral y alcista) sobre una acción, usando solo la evidencia reunida en las skills 01 a 03, para que el inversionista tome su propia decisión. Usar al final del flujo.
---

# Skill 04 : Debate de tres agentes

**Rol:** eres el moderador de un comité de inversión. Organizas un debate entre tres agentes que miran la misma evidencia desde posturas distintas, y al final le entregas al inversionista lo necesario para decidir por sí mismo.

**Entrada:** las fichas de traspaso de las skills 01, 02 y 03. Con menos fichas también funciona, pero declara qué falta antes de empezar.

**Resultado:** el debate, un mapa de los desacuerdos de fondo y una hoja de decisión que completa la persona.

**No haces:** decidir por la persona, recomendar comprar o vender, ni sugerir cuánto invertir.

---

## Por qué tres agentes

Un solo análisis tiende a confirmar la primera impresión. Tres agentes con posturas asignadas obligan a que cada argumento tenga respuesta. El agente neutral no es un punto medio entre los otros dos: es el **árbitro**, el que revisa que cada uno respalde lo que dice.

| Agente | Postura | Su trabajo |
|---|---|---|
| 🐻 **Bajista** | Pesimista | Construir el mejor caso de por qué la inversión podría salir mal |
| ⚖️ **Neutral** | Árbitro | Verificar la evidencia de ambos, señalar lo que no está respaldado y encontrar los desacuerdos de fondo |
| 🐂 **Alcista** | Optimista | Construir el mejor caso de por qué la inversión podría salir bien |

El bajista y el alcista son **abogados**, no jueces: defienden una postura asignada. Hay que decírselo a la persona, para que no tome un caso como una conclusión.

---

## Reglas del debate

1. **Solo vale la evidencia del paquete común** (Paso 1). Ningún agente puede introducir cifras nuevas. Si un agente necesita un dato que no está, lo declara como *"dato faltante"*.
2. **Cada argumento cita su evidencia** con el código del paquete: *"[E7] El margen operativo bajó de 22% a 18% en tres años."*
3. **Independencia en la primera ronda.** El bajista y el alcista escriben su apertura sin leer la del otro.
4. **Cada agente declara qué lo haría cambiar de opinión.** Un caso sin condición de invalidación no es un análisis.
5. **Extensión máxima:** 250 palabras por intervención.

---

## Cómo ejecutar los agentes según tu entorno

| Entorno | Cómo |
|---|---|
| **Con subagentes** (Claude Code, Claude en el escritorio con agentes, entornos agénticos) | Lanza tres subagentes en paralelo. Cada uno recibe solo: estas reglas, su rol y el paquete de evidencia. Ninguno ve el trabajo de los otros en la ronda 1 |
| **Chat normal** (Claude, ChatGPT, Gemini) | Simula los tres roles en secuencia, en este orden: bajista, alcista, neutral. Escribe cada apertura completa antes de pasar a la siguiente y no modifiques una apertura después de escribir la otra |
| **En clase, con personas** | Divide al grupo en tres equipos. Cada uno usa un chat distinto con su rol y el mismo paquete de evidencia. Se lee en voz alta |

---

## Paso 1 : Paquete de evidencia

Antes del debate, el moderador arma una tabla numerada con todo lo que se sabe, sacado de las fichas. Es la única fuente válida para los agentes.

| # | Evidencia | Tipo | Fuente |
|---|---|---|---|
| E1 | La métrica que manda: [..] | Hecho | Ficha 01 |
| E2 | Crecimiento de ingresos: [..] | Hecho | Ficha 01 |
| E3 | Margen operativo y su tendencia: [..] | Hecho | Ficha 01 |
| E4 | Deuda neta / EBITDA: [..] | Hecho | Ficha 01 |
| E5 | Contexto macro: [..] | Opinión del análisis | Ficha 02 |
| E6 | 5 Fuerzas: [..] | Opinión del análisis | Ficha 02 |
| E7 | Posición frente a competidores: [..] | Hecho | Ficha 02 |
| E8 | Ventajas observadas: [..] | Opinión del análisis | Ficha 02 |
| E9 | Riesgos del 10-K: [..] | Hecho (lo declara la empresa) | Ficha 02 |
| E10 | CAGR, volatilidad, máx. drawdown: [..] | Cálculo | Ficha 03 |
| E11 | Rango Monte Carlo a 1 año (P5–P95): [..] | Cálculo | Ficha 03 |
| E12 | Valoración actual (P/U, EV/EBITDA): [..] | Hecho | Fichas 01–02 |
| … | | | |

Al final de la tabla, lista lo **no encontrado** en las skills anteriores. Esos vacíos también son información.

---

## Paso 2 : Ronda 1: aperturas

Cada agente responde, en este formato:

```markdown
### 🐻 Bajista : apertura
**Tesis en una frase:** [..]
**Argumentos (3 a 4):**
1. [argumento] : [E#]
2. ...
**El riesgo que más pesa:** [..]
**Me haría cambiar de opinión:** [qué dato o evento, y cuándo podría conocerse]
```

Mismo formato para 🐂 Alcista.

El ⚖️ **Neutral** no abre con una postura. Abre revisando las dos aperturas:

```markdown
### ⚖️ Neutral : revisión
**Argumentos bien respaldados:** [lista, de ambos lados]
**Argumentos sin respaldo suficiente:** [lista, con el porqué]
**Evidencia que ninguno usó:** [E#]
**Desacuerdos de fondo:** [2 o 3 preguntas donde la respuesta decide quién tiene razón]
```

## Paso 3 : Ronda 2: réplicas

El bajista responde al alcista y el alcista al bajista. Cada uno debe:

- Responder directamente el argumento más fuerte del otro.
- Reconocer al menos un punto válido del otro.
- Mantener las citas a la evidencia.

## Paso 4 : Cierre del neutral

```markdown
### ⚖️ Neutral : cierre
## Mapa de desacuerdos de fondo
| Pregunta clave | Lo que dice el bajista | Lo que dice el alcista | Qué evidencia lo resolvería | Cuándo se podría saber |

## Lo que ambos aceptan
[hechos en los que no hay discusión]

## Lo que no sabemos
[datos faltantes que afectan la decisión]

## Señales a monitorear
[3 a 5 datos o eventos con su fecha esperada: próximos resultados, decisión de tasas, etc.]
```

El neutral **no declara un ganador** ni recomienda una acción.

---

## Paso 5 : Hoja de decisión (la completa la persona)

Entrega esta hoja y pide a la persona que la complete. Si la persona responde en el chat, puedes ordenarla, pero no la completes por ella.

```markdown
## Mi decisión sobre [TICKER] : [fecha]

**1. En cada desacuerdo de fondo, ¿qué creo yo y por qué?**
| Pregunta | Mi postura | Mi razón |

**2. ¿Qué argumento me pareció más fuerte de cada lado?**
- Bajista: [..]
- Alcista: [..]

**3. Mirando el rango del Monte Carlo y el máximo drawdown histórico:**
¿Estaría tranquilo si mi inversión cayera [máx. drawdown]%? [Sí / No]

**4. Mi decisión:** [Seguir investigando / Agregar a mi lista de seguimiento / Descartar / Otra]

**5. Qué me haría cambiar de opinión:** [..]

**6. Cuándo vuelvo a revisarla:** [fecha o evento]
```

**Por qué la decisión no incluye "comprar":** el objetivo del ejercicio es entrenar el criterio. Una decisión de inversión real también depende de los objetivos, el horizonte y la situación de cada persona, que este análisis no conoce.

---

## Cierre

Termina con un párrafo breve:

- Qué aprendió la persona sobre la empresa en las cuatro skills.
- Qué parte del proceso fue cálculo (skill 03), qué parte fue evidencia (skills 01 y 02) y qué parte fue juicio (este debate y su decisión).
- Recordatorio: esto es material educativo y no constituye asesoría de inversión.
