# 🔗 Semana 2: Construye tu primera Blockchain en Python

## 📋 Descripción

Material educativo completo para aprender a construir una blockchain funcional en Python desde cero. Este módulo está diseñado para sesiones diarias de 20 minutos durante 5 días.

---

## 📁 Contenido de la Carpeta

### 📓 Archivos Principales

1. **`Semana2_Blockchain_Construccion.ipynb`**
   - Notebook Jupyter interactivo con todo el contenido
   - 46 celdas organizadas en 5 días de aprendizaje
   - Incluye teoría, código ejecutable, ejercicios y autoevaluaciones
   - **Este es el archivo principal para estudiantes**

2. **`Instructor_Semana2_Blockchain.md`**
   - Guía completa para el instructor
   - Objetivos específicos por día
   - Orientaciones pedagógicas
   - Rúbrica de evaluación
   - Recursos audiovisuales sugeridos
   - Vinculación con Semana 3
   - **Este es el archivo principal para instructores**

---

## 🎯 Objetivos de Aprendizaje

Al completar esta semana, los estudiantes serán capaces de:

1. ✅ Diseñar y crear la clase `Block` con atributos esenciales
2. ✅ Implementar funciones de hash criptográfico (SHA-256)
3. ✅ Construir la clase `Blockchain` para gestionar la cadena
4. ✅ Agregar bloques de forma segura manteniendo la integridad
5. ✅ Validar la integridad completa de la blockchain

---

## 📚 Estructura del Curso

### Día 1: Crear la clase `Block`
- Programación orientada a objetos
- Atributos esenciales del bloque
- Método constructor
- Bloque génesis

### Día 2: Hash Criptográfico
- Funciones hash SHA-256
- Propiedades criptográficas
- Efecto avalancha
- Verificación de integridad

### Día 3: Clase Blockchain
- Gestión de la cadena
- Estructura de datos (lista)
- Métodos principales
- Inicialización automática

### Día 4: Agregar Bloques
- Proceso de agregación
- Enlace criptográfico
- Inmutabilidad
- Visualización de la cadena

### Día 5: Validación
- Validación completa
- Detección de manipulaciones
- Verificación de enlaces
- Seguridad de la cadena

---

## 🚀 Cómo Usar Este Material

### Para Estudiantes

1. **Instalar Jupyter Notebook:**
   ```bash
   pip install jupyter
   ```

2. **Abrir el notebook:**
   ```bash
   cd Semana2
   jupyter notebook Semana2_Blockchain_Construccion.ipynb
   ```

3. **Seguir el orden:**
   - Leer la teoría de cada día
   - Ejecutar el código de ejemplo
   - Completar el ejercicio práctico
   - Verificar con la solución
   - Realizar la autoevaluación

4. **Dedicar 20 minutos diarios** durante 5 días

### Para Instructores

1. **Revisar la guía del instructor:**
   - Leer `Instructor_Semana2_Blockchain.md`
   - Familiarizarse con los objetivos por día
   - Preparar recursos adicionales

2. **Preparar el entorno:**
   - Verificar que Python 3.7+ esté instalado
   - Probar todo el código del notebook
   - Preparar ejemplos adicionales si es necesario

3. **Facilitar el aprendizaje:**
   - Seguir las orientaciones pedagógicas
   - Usar la rúbrica de evaluación
   - Adaptar según el nivel de los estudiantes

---

## 🛠️ Requisitos Técnicos

### Software Necesario

- **Python 3.7 o superior**
- **Jupyter Notebook 7.0+**
- **Bibliotecas estándar** (incluidas con Python):
  - `hashlib`
  - `datetime`
  - `json`

### Instalación

```bash
# Instalar Jupyter
pip install jupyter

# Verificar instalación
jupyter --version
python --version
```

---

## 📊 Evaluación

### Criterios de Evaluación

1. **Comprensión Conceptual (40%)**
   - Estructura del bloque
   - Funciones hash
   - Enlace entre bloques
   - Validación

2. **Ejecución de Código (30%)**
   - Ejercicios prácticos completados
   - Código funcional
   - Buenas prácticas

3. **Documentación y Reflexión (30%)**
   - Comentarios en código
   - Autoevaluación
   - Reflexión final

### Escala de Calificación

- **90-100:** Excelente - Dominio completo
- **75-89:** Bueno - Comprensión sólida
- **60-74:** Suficiente - Comprensión básica
- **<60:** Insuficiente - Requiere refuerzo

---

## 🎓 Recursos Adicionales

### Videos Recomendados

- **"But how does bitcoin actually work?"** - 3Blue1Brown (26 min)
  - Excelente explicación visual de hash y blockchain
  - https://www.youtube.com/watch?v=bBC-nXj3Ng4

- **"Blockchain 101 - A Visual Demo"** - Anders Brownworth (17 min)
  - Demostración interactiva de blockchain
  - https://www.youtube.com/watch?v=_160oMzblY8

### Herramientas Interactivas

- **Anders Brownworth's Blockchain Demo**
  - https://andersbrownworth.com/blockchain/
  - Visualización interactiva perfecta para aprender

- **SHA256 Hash Generator**
  - https://emn178.github.io/online-tools/sha256.html
  - Para experimentar con hashes

### Lecturas

- **Bitcoin Whitepaper** - Satoshi Nakamoto
  - Paper original que introdujo blockchain
  
- **Documentación de Python**
  - hashlib: https://docs.python.org/3/library/hashlib.html
  - datetime: https://docs.python.org/3/library/datetime.html

---

## 🔗 Conexión con Otras Semanas

### Prerequisitos (Semana 1)
- Conceptos básicos de hash
- Introducción a blockchain
- Fundamentos de Python

### Siguiente Módulo (Semana 3)
- Proof of Work (minería)
- Consenso distribuido
- Ataques y defensas
- Escalabilidad

---

## 💡 Consejos para el Éxito

### Para Estudiantes

✅ **Práctica constante:** Ejecuta todo el código, no solo lo leas
✅ **Experimenta:** Modifica valores y observa qué pasa
✅ **Intenta primero:** No veas las soluciones inmediatamente
✅ **Pregunta:** Si algo no está claro, busca ayuda
✅ **Documenta:** Agrega tus propios comentarios al código

### Para Instructores

✅ **Monitorea progreso:** Identifica estudiantes con dificultades temprano
✅ **Adapta ritmo:** Ajusta según el nivel del grupo
✅ **Fomenta colaboración:** Permite que estudiantes se ayuden entre sí
✅ **Usa ejemplos reales:** Relaciona con Bitcoin, Ethereum, etc.
✅ **Celebra logros:** Reconoce el progreso de los estudiantes

---

## 🐛 Problemas Comunes y Soluciones

### Problema: "ImportError: No module named hashlib"
**Solución:** Reinstalar Python desde python.org (hashlib viene incluido)

### Problema: Timestamps idénticos en bloques
**Solución:** Agregar `time.sleep(0.001)` entre creaciones de bloques

### Problema: Validación siempre retorna False
**Solución:** No modificar atributos del bloque después de crearlo

### Problema: Jupyter no inicia
**Solución:** 
```bash
pip install --upgrade jupyter
jupyter notebook --version
```

---

## 📞 Soporte

### Para Dudas Técnicas
- Revisar documentación de Python
- Consultar videos recomendados
- Stack Overflow: https://stackoverflow.com/questions/tagged/blockchain

### Para Reportar Errores
- Documentar el error con screenshot
- Incluir versión de Python y sistema operativo
- Proporcionar código que genera el error

---

## 📄 Licencia

Material educativo diseñado para uso académico.

**Atribuciones:**
- Conceptos basados en el paper de Satoshi Nakamoto
- Código original para fines educativos
- Estructura pedagógica basada en metodologías de aprendizaje activo

---

## ✨ Contribuciones

Este material puede ser mejorado. Sugerencias bienvenidas:
- Ejercicios adicionales
- Mejoras en explicaciones
- Recursos complementarios
- Correcciones de errores

---

**Última actualización:** Octubre 2025  
**Versión:** 1.0  
**Nivel:** Introductorio a Intermedio  
**Duración:** 5 días × 20 minutos

---

## 🎉 ¡Comienza tu Viaje en Blockchain!

Este es el punto de partida para comprender cómo funcionan las tecnologías descentralizadas que están transformando el mundo digital.

**¡Éxito en tu aprendizaje!** 🚀
