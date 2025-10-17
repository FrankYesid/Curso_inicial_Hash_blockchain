# 📋 Fragmentos de Ejemplo - Verificación de Formato

Este documento muestra ejemplos del contenido generado para que puedas verificar la calidad y formato del material.

---

## 📓 Ejemplo: Fragmento del Día 1 (Markdown)

```markdown
# 📘 Semana 1 - Día 1: ¿Qué es Blockchain?

## 📖 Contenido Teórico

### ¿Qué es Blockchain?

**Definición académica:**  
Blockchain (cadena de bloques) es una estructura de datos distribuida y descentralizada 
que almacena información en bloques enlazados criptográficamente. Cada bloque contiene 
un conjunto de transacciones o datos, y está vinculado al bloque anterior mediante un 
hash criptográfico, creando una cadena inmutable y verificable.

**Analogía sencilla:**  
Imagina un **libro contable compartido** que vive simultáneamente en miles de computadoras...
```

---

## 💻 Ejemplo: Fragmento de Código (Día 1)

```python
# Ejemplo: Crear un bloque simple usando un diccionario

# Un bloque es esencialmente un contenedor de información
bloque_genesis = {
    'index': 0,                          # Posición del bloque en la cadena
    'timestamp': '2025-10-16 23:00:00',  # Momento en que se creó el bloque
    'data': 'Bloque Génesis',            # Información almacenada
    'previous_hash': '0',                # Hash del bloque anterior
    'hash': 'abc123...'                  # Hash único de este bloque
}

# Mostrar el bloque
print("=" * 50)
print("BLOQUE GÉNESIS (Primer bloque de la cadena)")
print("=" * 50)

for clave, valor in bloque_genesis.items():
    print(f"{clave.upper():15} : {valor}")

print("=" * 50)
```

---

## ✏️ Ejemplo: Ejercicio Práctico (Día 3)

```markdown
## ✏️ Ejercicio Práctico

**Instrucciones:**  
Genera 3 hashes SHA-256 cambiando una sola letra cada vez en la frase base. 
Documenta los resultados.

**Frase base:** `"La blockchain garantiza transparencia"`

**Tareas:**
1. Calcula el hash de la frase original
2. Cambia una letra (ej: "blockchain" → "Blockchain") y calcula el nuevo hash
3. Cambia otra letra diferente y calcula otro hash
4. Compara los 3 hashes y documenta tus observaciones

**💡 Pista:** El nonce es un número que los mineros ajustan repetidamente...
```

---

## ✅ Ejemplo: Solución Comentada (Día 4)

```python
# SOLUCIÓN COMENTADA

import hashlib
import json
from datetime import datetime

# Funciones auxiliares
def calcular_hash_bloque(bloque):
    bloque_sin_hash = {k: v for k, v in bloque.items() if k != 'hash'}
    bloque_string = json.dumps(bloque_sin_hash, sort_keys=True)
    return hashlib.sha256(bloque_string.encode('utf-8')).hexdigest()

# Recrear la blockchain
bloque_0 = crear_bloque(0, 'Bloque Génesis', '0')
bloque_1 = crear_bloque(1, 'Alice → Bob: 10 BTC', bloque_0['hash'])

# DEMOSTRACIÓN DE ALTERACIÓN
print("=" * 70)
print("DEMOSTRACIÓN: DETECCIÓN DE ALTERACIONES")
print("=" * 70)

# Alterar el Bloque 1 (simular ataque)
print("\n🚨 ALTERANDO BLOQUE 1...")
bloque_1['data'] = 'Mallory → Bob: 10 BTC'  # Cambio malicioso

# Recalcular el hash del bloque alterado
nuevo_hash_bloque1 = calcular_hash_bloque(bloque_1)

print("\nCONCLUSIÓN:")
print("El hash del Bloque 1 cambió completamente.")
print("¡La alteración es EVIDENTE! La cadena está rota.")
```

---

## 📝 Ejemplo: Autoevaluación (Día 2)

```markdown
## 📝 Autoevaluación — Respuestas al final de la sección

### Pregunta 1
**¿Cuál es la función principal del campo `previous_hash` en un bloque?**

A) Almacenar la contraseña del bloque anterior  
B) Enlazar criptográficamente el bloque con su predecesor  
C) Identificar al creador del bloque  
D) Calcular el timestamp automáticamente  

### Pregunta 2
**Verdadero o Falso: El `nonce` es un valor que permanece constante en 
todos los bloques de una blockchain.**

A) Verdadero  
B) Falso  

---

### 🔑 Respuestas

1. **Respuesta: B**  
   *Explicación:* El `previous_hash` crea el enlace criptográfico entre bloques...

2. **Respuesta: B (Falso)**  
   *Explicación:* El nonce varía en cada bloque. Durante la minería...
```

---

## 📊 Ejemplo: Tabla Comparativa (Día 3)

```markdown
### 🔐 Propiedades Fundamentales de las Funciones Hash

| Propiedad | Descripción | Importancia en Blockchain |
|-----------|-------------|---------------------------|
| **Determinista** | La misma entrada siempre produce el mismo hash | Permite verificar que los datos no han cambiado |
| **Rápida de calcular** | Se puede generar el hash eficientemente | Permite validar bloques rápidamente |
| **Irreversible** | Imposible obtener la entrada original desde el hash | Protege la privacidad de los datos |
| **Efecto avalancha** | Un cambio mínimo produce un hash completamente diferente | Detecta cualquier alteración |
| **Resistente a colisiones** | Difícil encontrar dos entradas con el mismo hash | Garantiza identificadores únicos |
```

---

## 🎓 Ejemplo: Guía del Instructor

```markdown
### **Día 3: Hash y SHA-256**

#### Estructura de la Sesión (20 minutos)

| Actividad | Tiempo | Descripción |
|-----------|--------|-------------|
| Lectura teórica | 6 min | Propiedades de hash, tabla comparativa |
| Código de ejemplo | 5 min | Función `calcular_hash()` y demostración |
| Ejercicio práctico | 6 min | Generar 3 hashes con cambios mínimos |
| Autoevaluación | 3 min | 3 preguntas sobre propiedades de hash |

#### Puntos Críticos de Enseñanza

✅ **Hacer énfasis en:**
- Hash ≠ Encriptación (hash es unidireccional)
- El efecto avalancha hace imposible predecir cambios
- SHA-256 produce siempre 256 bits (64 caracteres hex)

⚠️ **Errores comunes de estudiantes:**
- Intentar "revertir" un hash (recordar que es irreversible)
- Pensar que hashes similares indican datos similares
- No usar `.encode()` antes de hashear
```

---

## 📚 Ejemplo: Guía Rápida del Estudiante

```markdown
### **Día 3 - Miércoles: Hash y SHA-256**
📁 Archivo: `Dia3_Hash_SHA256.ipynb`

**Lo que aprenderás:**
- Qué es una función hash
- Propiedades de SHA-256
- El "efecto avalancha"

**Consejo del día:** 💡  
Este es el día más importante. Los hashes son el corazón de blockchain. 
Tómate tu tiempo.

---

### ✅ Mejores Prácticas

1. **Sé Consistente**
   - Dedica 20 minutos diarios
   - Mejor poco cada día que mucho de golpe
   - Establece un horario fijo

2. **Toma Notas**
   - Escribe conceptos clave con tus palabras
   - Dibuja diagramas si te ayuda
   - Anota preguntas para investigar después
```

---

## 🎨 Ejemplo: Visualización ASCII (Día 2)

```
┌─────────────────────────────────────────────────┐
│              BLOQUE #1                          │
├─────────────────────────────────────────────────┤
│ Index:          1                               │
│ Timestamp:      2025-10-16 23:10:00             │
│ Data:           "Juan → María: 10 BTC"          │
│ Previous Hash:  0000abc123...                   │
│ Nonce:          45821                           │
│ Hash:           0000def456...                   │
└─────────────────────────────────────────────────┘
         ↓ (previous_hash del siguiente bloque)
┌─────────────────────────────────────────────────┐
│              BLOQUE #2                          │
├─────────────────────────────────────────────────┤
│ Index:          2                               │
│ Timestamp:      2025-10-16 23:15:00             │
│ Data:           "María → Pedro: 5 BTC"          │
│ Previous Hash:  0000def456...  ← (enlace!)      │
│ Nonce:          78234                           │
│ Hash:           0000ghi789...                   │
└─────────────────────────────────────────────────┘
```

---

## 💻 Ejemplo: Clase Completa (Día 5)

```python
class Blockchain:
    """
    Clase que representa una blockchain completa.
    """
    
    def __init__(self):
        """Inicializa la blockchain con el bloque génesis."""
        self.chain = []
        self.crear_bloque_genesis()
    
    def crear_bloque_genesis(self):
        """Crea el primer bloque de la cadena."""
        bloque_genesis = self.crear_bloque(
            data='Bloque Génesis - Inicio de la Blockchain',
            previous_hash='0'
        )
        self.chain.append(bloque_genesis)
    
    def calcular_hash(self, bloque):
        """
        Calcula el hash SHA-256 de un bloque.
        """
        bloque_sin_hash = {k: v for k, v in bloque.items() if k != 'hash'}
        bloque_string = json.dumps(bloque_sin_hash, sort_keys=True)
        return hashlib.sha256(bloque_string.encode('utf-8')).hexdigest()
    
    def agregar_bloque(self, data, nonce=0):
        """
        Agrega un nuevo bloque a la cadena.
        """
        ultimo_bloque = self.chain[-1]
        previous_hash = ultimo_bloque['hash']
        
        nuevo_bloque = self.crear_bloque(data, previous_hash, nonce)
        self.chain.append(nuevo_bloque)
        
        print(f"✅ Bloque #{nuevo_bloque['index']} agregado exitosamente")
```

---

## 📖 Ejemplo: README Principal

```markdown
# 🔗 Curso Inicial: Hash y Blockchain

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Nivel](https://img.shields.io/badge/Nivel-Introductorio-green)

## 📚 Descripción del Proyecto

Curso educativo completo y autoguiado para aprender los **fundamentos de Blockchain** 
desde cero, utilizando Python y Jupyter Notebooks. Diseñado para sesiones diarias de 
**20 minutos**, ideal para estudiantes de pregrado, bootcamps o autodidactas.

## 🎯 Objetivos de Aprendizaje

Al completar la **Semana 1**, serás capaz de:

✅ Explicar qué es blockchain y cómo funciona  
✅ Identificar los componentes de un bloque  
✅ Calcular hashes SHA-256 usando Python  
✅ Implementar encadenamiento de bloques  
✅ Crear una blockchain funcional desde cero  
✅ Validar la integridad de una cadena de bloques  
```

---

## 🎯 Verificación de Calidad

### ✅ Formato de Notebooks
- [x] Celdas Markdown con formato correcto
- [x] Código Python con sintaxis válida
- [x] Comentarios explicativos en español
- [x] Estructura JSON válida para .ipynb

### ✅ Contenido Pedagógico
- [x] Progresión lógica de conceptos
- [x] Ejercicios con soluciones
- [x] Autoevaluaciones con respuestas
- [x] Tiempo estimado realista (20 min)

### ✅ Documentación
- [x] README completo y profesional
- [x] Guía del instructor detallada
- [x] Guía rápida para estudiantes
- [x] Requirements.txt actualizado

---

## 📦 Archivos Listos para Descargar

Todos los archivos están en:
```
d:\GitHub\Curso_inicial_Hash_blockchain\
```

**Notebooks Jupyter:**
- ✅ `Semana1/Dia1_Que_es_Blockchain.ipynb`
- ✅ `Semana1/Dia2_Estructura_Bloque.ipynb`
- ✅ `Semana1/Dia3_Hash_SHA256.ipynb`
- ✅ `Semana1/Dia4_Encadenar_Bloques.ipynb`
- ✅ `Semana1/Dia5_Revision_Resumen.ipynb`
- ✅ `Semana1/Dia6_Recursos_Audiovisuales.ipynb`

**Documentación:**
- ✅ `README.md`
- ✅ `Semana1/Instructor_Semana1_Blockchain.md`
- ✅ `Semana1/GUIA_RAPIDA_ESTUDIANTE.md`
- ✅ `requirements.txt`
- ✅ `RESUMEN_PROYECTO.md`
- ✅ `EJEMPLO_FRAGMENTOS.md` (este archivo)

---

## 🚀 Próximos Pasos

### Para usar el material:

1. **Abre Jupyter Notebook:**
   ```bash
   cd d:\GitHub\Curso_inicial_Hash_blockchain
   jupyter notebook
   ```

2. **Navega a la carpeta Semana1/**

3. **Abre el Día 1 y comienza a aprender!**

---

**¡Todo el material está listo para usar! 🎉**
