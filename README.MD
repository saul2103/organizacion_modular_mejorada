# Sistema de Gestión de Restaurante
**Estudiante:** Bryan Saul Iza Llano

# Organización Modular Mejorada

Este documento proporciona una descripción técnica detallada del sistema, explicando de forma clara y accesible su diseño, estructura y las decisiones de arquitectura aplicadas para asegurar un desarrollo limpio y escalable.

## Descripción del Sistema

El sistema consiste en una aplicación orientada a objetos diseñada para gestionar un catálogo de productos comerciales, enfocándose en la clasificación de elementos y el cálculo parametrizado de precios o impuestos. Su arquitectura divide claramente las entidades del negocio de los mecanismos de presentación y de ejecución. Esto permite realizar modificaciones rápidas y aisladas sin alterar el funcionamiento global de la aplicación.

## Estructura del Proyecto

El código se organiza siguiendo un enfoque de modularidad estructurada bajo un único paquete raíz. La disposición de sus componentes se detalla a continuación:

* **App.java**: Clase principal que actúa como punto de entrada (Main) del sistema, encargada de inicializar los objetos y simular el flujo del negocio.
* **Producto.java**: Clase abstracta base que modela los atributos y comportamientos comunes de cualquier artículo comercial.
* **Bebida.java**: Clase concreta que extiende a Producto para representar artículos líquidos con dinámicas específicas de empaque y volumen.

## Responsabilidad de cada Clase

Para mantener una separación clara de funciones, cada archivo tiene asignada una única misión dentro del sistema:

* **App**: Centraliza la lógica de ejecución del programa. Su única tarea es instanciar los productos o bebidas, definir los escenarios de prueba y mostrar los resultados por consola. No almacena datos lógicos ni realiza cálculos aritméticos internos.
* **Producto**: Define la plantilla y el contrato esencial para todos los artículos. Establece las propiedades raíz (como el nombre y el precio base) y declara métodos comunes que las subclases deben implementar de forma obligatoria.
* **Bebida**: Gestiona exclusivamente la información específica del producto de tipo líquido. Se encarga de evaluar cómo las propiedades particulares (por ejemplo, los mililitros o el tipo de envase) alteran el cálculo del precio final o la descripción del objeto.

## Relación entre Producto y Bebida

La conexión entre estas dos clases se define mediante el concepto de **Herencia** (una relación del tipo "Es Un"). 

* **Clase Base**: Producto funciona como la superclase abstracta. Esto significa que no se pueden crear objetos genéricos de tipo Producto directamente; sirve únicamente como un molde conceptual.
* **Clase Hija**: Bebida es una subclase concreta que hereda todos los campos y métodos de Producto. 
* **Especialización**: Al heredar, Bebida reutiliza la infraestructura existente de Producto pero sobrescribe o especializa ciertos comportamientos esenciales (Polimorfismo), adaptando las reglas de negocio a las propiedades de un artículo bebible.

## Principios SOLID Aplicados

El diseño del código incorpora de manera explícita tres de los principios fundamentales de la ingeniería de software limpia:

### Principio de Responsabilidad Única (SRP)
Cada componente tiene un único motivo para cambiar. La clase Bebida solo se modifica si cambian las reglas de las bebidas, mientras que App solo se altera si se requiere modificar la interacción con el usuario o la simulación principal.

### Principio de Abierto/Cerrado (OCP)
El diseño está abierto a la extensión pero cerrado a la modificación. Si en el futuro el negocio requiere añadir productos de tipo "Alimento" o "Electrónico", se pueden crear nuevas clases que hereden de Producto sin necesidad de alterar una sola línea de código en las clases existentes.

### Principio de Sustitución de Liskov (LSP)
Las subclases pueden reemplazar por completo a sus clases base sin alterar el comportamiento correcto del programa. Una colección declarada bajo el tipo general Producto puede almacenar y procesar objetos de tipo Bebida sin generar errores de consistencia ni requerir validaciones manuales de tipo.

## Instrucciones de Ejecución

Para compilar y ejecutar este proyecto en su entorno local, siga los pasos descritos a continuación:

1. **Clonar el repositorio**: Descargue una copia local del código utilizando el comando Git en su terminal:
   ```bash
   git clone https://github.com/saul2103/organizacion_modular_mejorada.git
   ```
2. **Navegar al directorio**: Acceda a la carpeta raíz del proyecto clonado:
   ```bash
   cd organizacion_modular_mejorada
   ```
3. **Compilar el código**: Si utiliza las herramientas de línea de comandos de Java, compile los archivos fuente:
   ```bash
   javac App.java Producto.java Bebida.java
   ```
4. **Ejecutar la aplicación**: Inicie el flujo principal del programa:
   ```bash
   java App
   ```

*(Nota: Si utiliza entornos de desarrollo como Visual Studio Code, IntelliJ IDEA o NetBeans, puede abrir la carpeta directamente y presionar el botón "Run" en la clase).*

## Importancia de Diseñar Proyectos Mantenibles

Construir software no se limita a escribir código que funcione en el momento presente; el verdadero reto radica en prepararlo para el futuro. Un diseño basado en módulos limpios y principios arquitectónicos reduce el acoplamiento y mitiga el riesgo de introducir errores colaterales cuando se solicitan nuevas funciones. 

Invertir tiempo en una estructura ordenada desde el inicio garantiza que el software pueda crecer, ser depurado con facilidad y transferido a nuevos desarrolladores sin transformarse en una base de código frágil o inmanejable.