# Página Web Responsive con Flet

Una aplicación web moderna, responsive y multiidioma construida con Python y Flet.

## Características

- ✅ **Completamente responsive**: Optimizada para desktop, tablet y móvil
- ✅ **Multiidioma**: Soporte para español, inglés y portugués
- ✅ **Navegación intuitiva**: Menú hamburguesa en móviles
- ✅ **Formulario de contacto**: Completamente funcional
- ✅ **Iconos y banderas**: Cambio de idioma visual
- ✅ **Footer con redes sociales**: Enlaces a todas las plataformas
- ✅ **Diseño moderno**: Sombras, bordes redondeados y colores atractivos

## Instalación

### Requisitos previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Instalar dependencias**:
   ```bash
   pip install flet python-dotenv
   ```

2. **Configurar variables de entorno**:
   
   a. Copia el archivo de ejemplo:
   ```bash
   cp .env.example .env
   ```
   
   b. Edita el archivo `.env` y completa con tus credenciales:
   ```bash
   EMAIL_SENDER=info.sifex@gmail.com
   EMAIL_RECEIVER=sifex.soft@gmail.com
   EMAIL_PASSWORD=tu_contraseña_de_aplicación_aquí
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```
   
   c. **Obtener contraseña de aplicación de Gmail**:
   - Ve a https://myaccount.google.com/security
   - Activa la "Verificación en dos pasos" si no está activada
   - Busca "Contraseñas de aplicaciones"
   - Genera una nueva contraseña para "Correo"
   - Copia esa contraseña de 16 caracteres en `EMAIL_PASSWORD`

3. **Descargar los archivos**:
   - `main.py` - Aplicación principal
   - `dict_textos.py` - Diccionario de textos multiidioma
   - `.env` - Variables de entorno (configurar con tus credenciales)
   - `.env.example` - Plantilla de ejemplo
   - `.gitignore` - Archivos a ignorar en Git

4. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

5. **Acceder a la aplicación**:
   - Se abrirá automáticamente en tu navegador
   - URL: `http://localhost:8000`

## Estructura del Proyecto

```
proyecto/
├── main.py          # Aplicación principal de Flet
├── dict_textos.py   # Diccionarios de texto multiidioma
└── README.md        # Este archivo
```

## Funcionalidades

### Header
- **Desktop**: Logo clickeable, menú horizontal, banderas de idioma
- **Móvil**: Menú hamburguesa con drawer de navegación

### Páginas
1. **Home**: Página de bienvenida con imagen y título
2. **Quiénes Somos**: Información de la empresa con imagen y texto
3. **Servicios**: Tarjetas de servicios con iconos y descripciones
4. **Blog**: Página informativa con enlace externo
5. **Contacto**: Formulario funcional de solicitud de servicios

### Footer
- Logo clickeable (más pequeño)
- Copyright
- Enlaces a redes sociales (YouTube, Facebook, Instagram, LinkedIn, X)

### Idiomas Soportados
- 🇪🇸 **Español** (por defecto)
- 🇺🇸 **Inglés**
- 🇧🇷 **Portugués**

## Personalización

### Cambiar textos
Edita el archivo `dict_textos.py` para modificar cualquier texto de la aplicación.

### Agregar nuevo idioma
1. Añade una nueva entrada en el diccionario `textos` en `dict_textos.py`
2. Agrega la nueva bandera en el método `create_flag_button()` en `main.py`

### Modificar estilos
Los colores y estilos se pueden modificar en los métodos de creación de componentes en `main.py`.

### Configurar email
Para hacer funcional el formulario de contacto:
1. Instalar biblioteca de email: Ya incluida en Python estándar
2. Configurar las variables de entorno en el archivo `.env`
3. Usar contraseña de aplicación de Gmail (no tu contraseña normal)
4. El método `send_email()` ya está implementado y listo

**IMPORTANTE DE SEGURIDAD:**
- ✅ El archivo `.env` está en `.gitignore` y NO se subirá a Git
- ✅ Usa `.env.example` como plantilla para compartir
- ✅ NUNCA subas contraseñas al repositorio
- ✅ Usa contraseñas de aplicación, no tu contraseña principal de Gmail

## Componentes Responsive

La aplicación detecta automáticamente el tamaño de pantalla y adapta:
- Menú: Horizontal en desktop, hamburguesa en móvil
- Layout: Columnas en desktop, apilar en móvil
- Tamaños de texto: Más grandes en desktop
- Espaciado: Adaptado según dispositivo

## Tecnologías Utilizadas

- **Flet**: Framework de UI para Python
- **Python**: Lenguaje de programación
- **Material Design**: Sistema de diseño de Google (a través de Flet)

## Posibles Mejoras

- [ ] Integración con base de datos
- [ ] Sistema de autenticación
- [ ] CMS para gestión de contenido
- [ ] Optimización SEO
- [ ] Analytics
- [ ] Carga de imágenes reales
- [ ] Sistema de comentarios en blog
- [ ] Carrito de compras

## Soporte

Si encuentras algún problema o tienes sugerencias, puedes:
1. Revisar la documentación de Flet: https://flet.dev
2. Verificar que tienes la versión correcta de Python
3. Comprobar que Flet está correctamente instalado

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.