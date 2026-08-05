# Desarrollo de una API REST para Gestión de Productos

El equipo de desarrollo necesita una API REST que permita la gestión de productos en un sistema de e-commerce. La API debe soportar autenticación y autorización para asegurar que solo usuarios autorizados puedan acceder a los datos. Los productos tendrán atributos como nombre, precio, stock y categoría. La API debe validar que los precios no sean negativos y que los nombres de los productos no se dupliquen. Además, debe manejar adecuadamente los errores y casos límite del dominio.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python Django REST |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del entorno y autenticación

**Objetivo:** Configurar el entorno de desarrollo y establecer la autenticación básica para la API.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Configurar el entorno de desarrollo con las dependencias necesarias.
- Implementar la autenticación básica utilizando tokens JWT.
- Asegurar que solo usuarios autorizados puedan acceder a los endpoints de la API.

**Entregable:** Entorno de desarrollo configurado con autenticación básica funcional.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo proteger los endpoints de la API para que solo usuarios autorizados puedan acceder.
- Piensa en la gestión de tokens y su validación.

</details>

### Fase 2: Creación y validación de productos

**Objetivo:** Implementar endpoints para crear y validar productos, asegurando que los precios no sean negativos y que los nombres no se dupliquen.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear un endpoint para registrar nuevos productos.
- Validar que el precio del producto no sea negativo.
- Validar que el nombre del producto no esté duplicado.
- Manejar adecuadamente los errores de validación.

**Entregable:** Endpoints funcionales para crear y validar productos con las restricciones especificadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo implementar las validaciones de negocio en tus endpoints.
- Piensa en cómo manejar los errores de validación y proporcionar respuestas significativas al usuario.

</details>

### Fase 3: Gestión de errores y casos límite

**Objetivo:** Mejorar la API para manejar errores y casos límite del dominio de manera adecuada.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Identificar y manejar diferentes tipos de errores que pueden ocurrir al crear productos.
- Implementar mecanismos para manejar casos límite, como stock cero o categorías inválidas.
- Asegurar que la API proporcione respuestas significativas en todos los casos.

**Entregable:** API mejorada para manejar errores y casos límite del dominio de manera adecuada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo categorizar y manejar diferentes tipos de errores.
- Piensa en cómo proporcionar respuestas significativas al usuario en todos los casos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un endpoint en una API REST y para qué sirve?
- **paraQueSirve**: ¿Para qué sirve la autenticación en una API REST y cómo se implementa?
- **comoSeUsa**: ¿Cómo se usa la validación de datos en una API REST para asegurar la integridad de los datos?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al crear productos en una API REST y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica el manejo de casos límite en una API REST y cómo se toman?

## Criterios de Evaluacion

- Configuración correcta del entorno de desarrollo y autenticación básica funcional.
- Implementación de endpoints para crear y validar productos con las restricciones especificadas.
- Manejo adecuado de errores y casos límite del dominio en la API.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
