# 📚 Guía del Instructor - Semana 1: Fundamentos de Blockchain

---

## 📋 Información General del Curso

**Curso:** Introducción a Blockchain y Programación  
**Semana:** 1 - Fundamentos de Blockchain  
**Duración por sesión:** 20 minutos  
**Nivel:** Introductorio (pregrado/bootcamp)  
**Prerrequisitos:** Conocimientos básicos de Python  
**Modalidad:** Autoaprendizaje con notebooks Jupyter

---

## 🎯 Objetivos de Aprendizaje de la Semana

Al finalizar la Semana 1, los estudiantes serán capaces de:

1. **Conceptual:**
   - Definir blockchain y explicar sus componentes fundamentales
   - Identificar las propiedades de las funciones hash criptográficas
   - Explicar por qué blockchain es inmutable en la práctica
   - Distinguir entre descentralización, distribución y consenso

2. **Procedimental:**
   - Crear bloques usando diccionarios de Python
   - Calcular hashes SHA-256 usando la librería `hashlib`
   - Implementar encadenamiento de bloques mediante `previous_hash`
   - Desarrollar funciones de validación de cadenas

3. **Actitudinal:**
   - Valorar la importancia de la inmutabilidad en sistemas de confianza
   - Desarrollar pensamiento crítico sobre casos de uso apropiados de blockchain
   - Fomentar la experimentación y el aprendizaje autónomo

---

## 📅 Estructura Semanal

| Día | Tema | Archivo | Tiempo | Prioridad |
|-----|------|---------|--------|-----------|
| 1 | ¿Qué es Blockchain? | `Dia1_Que_es_Blockchain.ipynb` | 20 min | Obligatorio |
| 2 | Estructura de un Bloque | `Dia2_Estructura_Bloque.ipynb` | 20 min | Obligatorio |
| 3 | Hash y SHA-256 | `Dia3_Hash_SHA256.ipynb` | 20 min | Obligatorio |
| 4 | Encadenar Bloques | `Dia4_Encadenar_Bloques.ipynb` | 20 min | Obligatorio |
| 5 | Revisión y Resumen | `Dia5_Revision_Resumen.ipynb` | 20 min | Obligatorio |
| 6 | Recursos Audiovisuales | `Dia6_Recursos_Audiovisuales.ipynb` | Variable | Opcional |

---

## 🗓️ Planificación Diaria Detallada

### **Día 1: ¿Qué es Blockchain?**

#### Objetivos Específicos
- Comprender la definición de blockchain
- Identificar componentes básicos de un bloque
- Crear representaciones simples en Python

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Lectura teórica | 5 min | Definición, analogía del libro contable, mini-glosario |
| Código de ejemplo | 5 min | Ejecutar y analizar el bloque génesis |
| Ejercicio práctico | 7 min | Crear bloque_1 personalizado |
| Autoevaluación | 3 min | Responder 3 preguntas de opción múltiple |

#### Indicaciones Pedagógicas

**Inicio (Minutos 0-5):**
- Comenzar con la analogía del libro contable para anclar el concepto
- Enfatizar que blockchain es simplemente una estructura de datos (desmitificar)
- Presentar el mini-glosario como referencia rápida

**Desarrollo (Minutos 5-17):**
- Ejecutar el código de ejemplo paso a paso
- Explicar cada campo del diccionario y su propósito
- Dar tiempo para que los estudiantes experimenten con el ejercicio
- Fomentar la modificación de valores para ver qué sucede

**Cierre (Minutos 17-20):**
- Resolver la autoevaluación
- Verificar comprensión de conceptos clave
- Adelantar brevemente el tema del Día 2

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- El campo `previous_hash` es lo que "encadena" los bloques
- Por ahora los hashes son temporales (se calcularán en Día 3)
- Un bloque es solo un contenedor de información

⚠️ **Errores comunes de estudiantes:**
- Confundir "hash" con "encriptación" (aclarar que son diferentes)
- Pensar que blockchain es sinónimo de Bitcoin (explicar que Bitcoin usa blockchain, no al revés)
- No entender por qué el bloque génesis tiene `previous_hash = '0'`

#### Recursos Adicionales Sugeridos
- Video: "How does a blockchain work - Simply Explained" (5 min)
- Herramienta: Blockchain Demo de Anders Brownworth

---

### **Día 2: Estructura de un Bloque**

#### Objetivos Específicos
- Describir los 6 campos esenciales de un bloque
- Usar `datetime` para timestamps automáticos
- Comprender el concepto y función del `nonce`

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Lectura teórica | 6 min | Anatomía del bloque, visualización ASCII |
| Código de ejemplo | 5 min | Función `crear_bloque()` con datetime |
| Ejercicio práctico | 6 min | Agregar campo nonce y crear bloque |
| Autoevaluación | 3 min | 3 preguntas sobre estructura y nonce |

#### Indicaciones Pedagógicas

**Inicio (Minutos 0-6):**
- Revisar brevemente los conceptos del Día 1
- Presentar la visualización ASCII para comprensión visual
- Explicar cada campo en detalle (usar la tabla del notebook)

**Desarrollo (Minutos 6-17):**
- Demostrar el uso de `datetime.now()` en vivo
- Explicar por qué necesitamos `.strftime()` para formatear
- Introducir el concepto de `nonce` sin entrar en minería aún (adelantar que se verá en Semana 2)
- Guiar en el ejercicio de agregar el campo nonce

**Cierre (Minutos 17-20):**
- Resolver autoevaluación
- Conectar el nonce con el concepto de minería (breve adelanto)
- Preparar para el Día 3 (funciones hash)

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- `datetime` es una librería estándar (no requiere instalación)
- El nonce es crucial para Proof of Work (se verá en detalle después)
- La función `crear_bloque()` encapsula lógica reutilizable

⚠️ **Errores comunes de estudiantes:**
- Olvidar el `.encode('utf-8')` al trabajar con strings
- No entender por qué el nonce es un número (explicar que se incrementa en minería)
- Confundir timestamp con index

#### Evaluación Formativa
- Observar si los estudiantes pueden crear bloques sin copiar código
- Verificar comprensión del propósito de cada campo
- Evaluar capacidad de explicar el nonce con sus propias palabras

---

### **Día 3: Hash y SHA-256**

#### Objetivos Específicos
- Explicar qué es una función hash y sus propiedades
- Utilizar `hashlib` para calcular hashes SHA-256
- Demostrar el efecto avalancha

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Lectura teórica | 6 min | Propiedades de hash, tabla comparativa |
| Código de ejemplo | 5 min | Función `calcular_hash()` y demostración |
| Ejercicio práctico | 6 min | Generar 3 hashes con cambios mínimos |
| Autoevaluación | 3 min | 3 preguntas sobre propiedades de hash |

#### Indicaciones Pedagógicas

**Inicio (Minutos 0-6):**
- Usar la analogía de "huella digital" para explicar hash
- Presentar la tabla de propiedades (determinista, irreversible, etc.)
- Explicar por qué SHA-256 es el estándar en blockchain

**Desarrollo (Minutos 6-17):**
- Ejecutar ejemplos en vivo mostrando el efecto avalancha
- Hacer que los estudiantes predigan si dos textos similares tendrán hashes similares (respuesta: NO)
- Guiar en el ejercicio de comparación de hashes
- Enfatizar que el hash siempre tiene 64 caracteres

**Cierre (Minutos 17-20):**
- Resolver autoevaluación
- Conectar hashes con inmutabilidad de blockchain
- Adelantar que en Día 4 usarán hashes para encadenar bloques

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- Hash ≠ Encriptación (hash es unidireccional)
- El efecto avalancha hace imposible predecir cambios
- SHA-256 produce siempre 256 bits (64 caracteres hex)

⚠️ **Errores comunes de estudiantes:**
- Intentar "revertir" un hash (recordar que es irreversible)
- Pensar que hashes similares indican datos similares
- No usar `.encode()` antes de hashear

#### Actividades de Extensión
- Comparar MD5, SHA1, SHA256, SHA512 (velocidad vs seguridad)
- Investigar colisiones de hash (teóricas vs prácticas)
- Explorar generadores de hash online

---

### **Día 4: Encadenar Bloques**

#### Objetivos Específicos
- Calcular el hash de un bloque completo
- Crear bloques encadenados mediante `previous_hash`
- Detectar alteraciones en la cadena

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Lectura teórica | 5 min | Concepto de encadenamiento, inmutabilidad |
| Código de ejemplo | 6 min | Función `calcular_hash_bloque()` y cadena |
| Ejercicio práctico | 6 min | Alterar bloque y detectar inconsistencia |
| Autoevaluación | 3 min | 3 preguntas sobre encadenamiento |

#### Indicaciones Pedagógicas

**Inicio (Minutos 0-5):**
- Revisar conceptos de hash del Día 3
- Explicar cómo `previous_hash` crea el enlace
- Usar diagrama ASCII para visualizar la cadena

**Desarrollo (Minutos 5-17):**
- Demostrar `json.dumps()` para serialización consistente
- Explicar por qué `sort_keys=True` es importante
- Crear cadena de 3 bloques en vivo
- Guiar en el ejercicio de alteración y detección

**Cierre (Minutos 17-20):**
- Resolver autoevaluación
- Discutir: ¿Por qué es computacionalmente imposible alterar bloques antiguos?
- Preparar para Día 5 (integración completa)

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- `json.dumps()` convierte diccionario a string para hashear
- Alterar un bloque rompe TODA la cadena posterior
- La inmutabilidad es práctica, no absoluta

⚠️ **Errores comunes de estudiantes:**
- Incluir el campo 'hash' al calcular el hash (recursión)
- No entender por qué alterar un bloque rompe los siguientes
- Pensar que recalcular un hash oculta la alteración

#### Evaluación Formativa
- Pedir a estudiantes que expliquen el encadenamiento con sus palabras
- Verificar que pueden implementar validación básica
- Evaluar comprensión de inmutabilidad práctica

---

### **Día 5: Revisión y Resumen**

#### Objetivos Específicos
- Consolidar todos los conceptos de la semana
- Crear una blockchain funcional completa
- Implementar validación robusta

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Recapitulación | 4 min | Tabla resumen, preguntas de reflexión |
| Código integrado | 8 min | Clase `Blockchain` completa |
| Ejercicio final | 5 min | Demostrar inmutabilidad con validación |
| Autoevaluación | 3 min | 3 preguntas integradoras |

#### Indicaciones Pedagógicas

**Inicio (Minutos 0-4):**
- Revisar la tabla resumen de la semana
- Facilitar discusión sobre las preguntas de reflexión
- Conectar todos los conceptos aprendidos

**Desarrollo (Minutos 4-17):**
- Presentar la clase `Blockchain` como integración
- Explicar programación orientada a objetos (si es necesario)
- Demostrar la función `is_chain_valid()` paso a paso
- Guiar en el ejercicio de alteración y validación

**Cierre (Minutos 17-20):**
- Resolver autoevaluación final
- Celebrar logros de la semana
- Adelantar temas de Semana 2 (Proof of Work, API, red distribuida)

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- La blockchain es solo el comienzo (falta consenso, red, etc.)
- Blockchain no es apropiada para todos los casos de uso
- La importancia de entender fundamentos antes de frameworks

⚠️ **Errores comunes de estudiantes:**
- Pensar que ya saben todo sobre blockchain (es solo el inicio)
- No entender las limitaciones de blockchain
- Confundir la estructura de datos con el sistema completo

#### Actividades de Extensión
- Agregar campos personalizados a los bloques
- Implementar diferentes funciones hash
- Crear visualizaciones gráficas de la cadena

---

### **Día 6: Recursos Audiovisuales (Opcional)**

#### Objetivos
- Reforzar conceptos mediante contenido multimedia
- Proporcionar recursos para aprendizaje autónomo
- Fomentar exploración independiente

#### Indicaciones Pedagógicas

**Uso recomendado:**
- Asignar como tarea para casa
- Crear foro de discusión sobre los recursos
- Pedir a estudiantes que compartan recursos adicionales que encuentren

**Verificación de enlaces:**
⚠️ **IMPORTANTE:** Verificar todos los enlaces antes de compartir con estudiantes. El contenido web puede cambiar o volverse obsoleto.

**Sugerencias:**
- Crear lista de reproducción curada en YouTube
- Compartir solo 2-3 recursos clave (evitar sobrecarga)
- Adaptar según nivel e intereses del grupo

---

## 🎓 Metodología de Enseñanza

### Enfoque Pedagógico

Este curso utiliza un enfoque **constructivista** donde los estudiantes:
- Construyen conocimiento mediante experimentación práctica
- Aprenden haciendo (código ejecutable en cada sesión)
- Reflexionan sobre conceptos mediante autoevaluaciones
- Conectan teoría con aplicaciones reales

### Estrategias Didácticas

1. **Aprendizaje Incremental:**
   - Cada día construye sobre el anterior
   - Conceptos complejos se descomponen en partes manejables
   - Repetición espaciada de conceptos clave

2. **Código como Herramienta de Pensamiento:**
   - Los estudiantes no solo leen sobre blockchain, la construyen
   - El código hace tangibles conceptos abstractos
   - Errores son oportunidades de aprendizaje

3. **Analogías y Visualizaciones:**
   - Libro contable distribuido (Día 1)
   - Huella digital (Día 3)
   - Diagramas ASCII para visualizar cadenas

4. **Evaluación Formativa Continua:**
   - Autoevaluaciones al final de cada día
   - Ejercicios prácticos con soluciones comentadas
   - Preguntas de reflexión para metacognición

---

## 📊 Evaluación y Rúbricas

### Rúbrica de Evaluación Rápida (Por Día)

| Criterio | Insuficiente (0-2) | Básico (3-4) | Competente (5) |
|----------|-------------------|--------------|----------------|
| **Comprensión Teórica** | No puede explicar conceptos clave | Explica con ayuda o parcialmente | Explica claramente con ejemplos |
| **Ejecución de Código** | Código no ejecuta o tiene múltiples errores | Código ejecuta con ayuda | Código ejecuta correctamente |
| **Ejercicios Prácticos** | No completa o copia sin entender | Completa con ayuda | Completa independientemente |
| **Autoevaluación** | 0-1 respuestas correctas | 2 respuestas correctas | 3 respuestas correctas |

### Evaluación Sumativa (Fin de Semana)

**Proyecto Integrador (Opcional):**
Crear una blockchain personalizada con:
- Al menos 5 bloques
- Campos personalizados (ej: autor, categoría)
- Función de validación
- Documentación en comentarios

**Criterios de Evaluación:**
- Funcionalidad (40%): El código ejecuta sin errores
- Creatividad (20%): Campos o funcionalidades adicionales
- Documentación (20%): Comentarios claros y explicativos
- Comprensión (20%): Capacidad de explicar el código

---

## 🛠️ Recursos Técnicos Necesarios

### Software Requerido

| Herramienta | Versión Mínima | Propósito |
|-------------|----------------|-----------|
| Python | 3.10+ | Lenguaje de programación |
| Jupyter Notebook | Última | Entorno interactivo |
| Editor de texto | Cualquiera | Visualizar código (opcional) |

### Librerías Python Utilizadas

Todas las librerías son **estándar** (vienen con Python):
- `hashlib` - Funciones hash criptográficas
- `json` - Serialización de datos
- `datetime` - Manejo de fechas y horas
- `time` - Medición de tiempo (Día 6)

**No se requieren instalaciones adicionales para la Semana 1.**

### Configuración del Entorno

**Opción 1: Jupyter Notebook Local**
```bash
# Instalar Jupyter (si no está instalado)
pip install notebook

# Iniciar Jupyter
jupyter notebook
```

**Opción 2: Google Colab**
- Subir los archivos `.ipynb` a Google Drive
- Abrir con Google Colab (gratuito, no requiere instalación)

**Opción 3: VS Code con extensión Jupyter**
- Instalar extensión "Jupyter" en VS Code
- Abrir archivos `.ipynb` directamente

---

## 💡 Consejos para el Instructor

### Antes de la Semana

✅ **Preparación:**
- [ ] Ejecutar todos los notebooks para verificar que funcionan
- [ ] Familiarizarse con el contenido de cada día
- [ ] Preparar respuestas a preguntas frecuentes
- [ ] Verificar enlaces de recursos audiovisuales (Día 6)
- [ ] Configurar foro o canal de comunicación con estudiantes

### Durante la Semana

✅ **Facilitación:**
- [ ] Estar disponible para consultas (establecer horarios de oficina virtual)
- [ ] Monitorear progreso de estudiantes
- [ ] Compartir recursos adicionales según necesidades
- [ ] Fomentar discusión entre pares
- [ ] Celebrar logros y avances

### Después de la Semana

✅ **Retroalimentación:**
- [ ] Recopilar feedback de estudiantes
- [ ] Identificar conceptos que causaron más dificultad
- [ ] Ajustar material para futuras iteraciones
- [ ] Preparar Semana 2 basándose en nivel del grupo

---

## ❓ Preguntas Frecuentes de Estudiantes

### Técnicas

**P: ¿Por qué uso `encode('utf-8')` al calcular hashes?**  
R: Las funciones hash trabajan con bytes, no con strings. `encode()` convierte el string a bytes usando codificación UTF-8.

**P: ¿Qué pasa si dos bloques tienen el mismo timestamp?**  
R: Es posible en teoría, pero improbable en la práctica. En blockchains reales, el timestamp es solo uno de varios campos que se hashean, por lo que el hash final será diferente.

**P: ¿Por qué usar `json.dumps()` en lugar de `str()`?**  
R: `json.dumps()` con `sort_keys=True` garantiza que el orden de las claves sea siempre el mismo, produciendo hashes consistentes. `str()` no garantiza orden.

**P: ¿Puedo usar otro algoritmo hash en lugar de SHA-256?**  
R: Sí, técnicamente puedes usar MD5, SHA1, SHA512, etc. Pero SHA-256 es el estándar en blockchain por su balance entre seguridad y velocidad.

### Conceptuales

**P: ¿Blockchain es lo mismo que Bitcoin?**  
R: No. Bitcoin es una criptomoneda que **usa** blockchain como su tecnología subyacente. Blockchain es la estructura de datos; Bitcoin es una aplicación de esa estructura.

**P: Si blockchain es inmutable, ¿cómo se corrigen errores?**  
R: No se "corrigen" bloques antiguos. En su lugar, se agregan nuevos bloques con transacciones correctivas. La historia completa (incluyendo errores) permanece visible.

**P: ¿Blockchain es realmente segura?**  
R: La estructura de datos es muy segura contra alteraciones. Pero la seguridad completa depende de: consenso, criptografía de claves, implementación del código, y seguridad de la red.

**P: ¿Para qué sirve blockchain fuera de criptomonedas?**  
R: Casos de uso incluyen: cadenas de suministro, registros médicos, votación electrónica, propiedad intelectual, contratos inteligentes, etc. Pero no es apropiada para todos los casos.

---

## 📚 Bibliografía y Referencias

### Documentos Fundacionales

1. **Nakamoto, S. (2008).** "Bitcoin: A Peer-to-Peer Electronic Cash System"  
   - Whitepaper original que introduce blockchain
   - Disponible en: bitcoin.org/bitcoin.pdf

### Libros Recomendados

2. **Antonopoulos, A. M. (2017).** "Mastering Bitcoin: Programming the Open Blockchain" (2nd ed.)  
   - Referencia técnica completa
   - Versión digital gratuita en GitHub

3. **Drescher, D. (2017).** "Blockchain Basics: A Non-Technical Introduction in 25 Steps"  
   - Excelente para fundamentos conceptuales
   - Apto para audiencias no técnicas

### Recursos Online

4. **Python hashlib Documentation**  
   - docs.python.org/3/library/hashlib.html
   - Referencia oficial de funciones hash

5. **Blockchain Demo - Anders Brownworth**  
   - andersbrownworth.com/blockchain
   - Simulador interactivo educativo

---

## 🔄 Mejora Continua

### Métricas de Éxito

Indicadores para evaluar efectividad del curso:

- **Tasa de finalización:** % de estudiantes que completan los 5 días obligatorios
- **Puntuación en autoevaluaciones:** Promedio de respuestas correctas
- **Tiempo de completación:** ¿Se ajusta a los 20 minutos por día?
- **Satisfacción:** Encuesta post-semana (escala 1-5)
- **Retención:** ¿Cuántos continúan a Semana 2?

### Áreas de Mejora Potencial

Basándose en feedback, considerar:

- Agregar más visualizaciones gráficas
- Incluir videos cortos explicativos propios
- Crear ejercicios adicionales de diferentes niveles
- Desarrollar un proyecto integrador más elaborado
- Añadir gamificación (badges, puntos, etc.)

---

## 📞 Soporte y Contacto

### Para Estudiantes

**Canales de comunicación recomendados:**
- Foro de discusión (Discord, Slack, Moodle)
- Horarios de oficina virtual (Zoom, Google Meet)
- Email para consultas individuales
- Repositorio GitHub para issues técnicos

**Tiempo de respuesta esperado:**
- Consultas técnicas: 24-48 horas
- Consultas conceptuales: 24 horas
- Emergencias: Mismo día

### Para Instructores

**Recursos adicionales:**
- Comunidad de educadores en blockchain
- Repositorio de material didáctico actualizado
- Webinars de actualización tecnológica

---

## ✅ Checklist del Instructor

### Antes de Iniciar

- [ ] Verificar que todos los notebooks ejecutan sin errores
- [ ] Configurar entorno de comunicación con estudiantes
- [ ] Preparar calendario de sesiones
- [ ] Revisar preguntas frecuentes
- [ ] Verificar enlaces de recursos externos

### Durante la Semana

- [ ] Monitorear progreso diario
- [ ] Responder consultas oportunamente
- [ ] Compartir recursos adicionales según necesidad
- [ ] Motivar y celebrar avances

### Al Finalizar

- [ ] Recopilar feedback
- [ ] Evaluar proyectos integradores (si aplica)
- [ ] Identificar áreas de mejora
- [ ] Preparar transición a Semana 2

---

**¡Éxito en tu labor docente! 🎓**

*Este material está diseñado para ser flexible y adaptable. Siéntete libre de ajustarlo según las necesidades específicas de tu grupo de estudiantes.*

---

**Versión:** 1.0  
**Última actualización:** Octubre 2025  
**Autor:** Material pedagógico generado para curso de Blockchain  
**Licencia:** Uso educativo libre
