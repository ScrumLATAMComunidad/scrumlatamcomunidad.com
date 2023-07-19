# Portal Web de SCRUM LATAM Comunidad

Repositorio del Portal Web de [Scrum Latam Comunidad](https://www.scrumlatamcomunidad.com/).

[English](README.md)

[![Construido con Cookiecutter Plone Starter](https://img.shields.io/badge/built%20with-Cookiecutter%20Plone%20Starter-0083be.svg?logo=cookiecutter)](https://github.com/collective/cookiecutter-plone-starter/)
[![Estilo de código Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Pruebas Backend](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml)
[![Pruebas Frontend](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml)
[![Todos los colaboradores](https://img.shields.io/github/all-contributors/ScrumLATAMComunidad/scrumlatamcomunidad.com?color=ee8449&style=flat-square)](#contributors)

El nuevo portal Web de SCRUM LATAM Comunidad usa tecnologías
Plone 6 y Volto.

## Inicio rápido

### Stack de desarrollo

-   Python 3.9, 3.10, 3.11
-   Node 16
-   yarn
-   Docker

### Instalación

Instale las dependencias de requisitos, ejecutando el siguiente comando:

```shell
sudo apt install build-essential python3-dev python3-venv git tree curl
```

Descargar e instalar [Node Version Manager -
NVM](https://github.com/nvm-sh/nvm/blob/master/README.md), ejecutando el
siguiente comando:

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

Configurando el script `nvm` en entornos de consola para usarlo, ejecutando
el siguiente comando:

```shell
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" \
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

Para reflejar los cambios del script `nvm` en los entornos de terminal para
usarlo, ejecute el siguiente comando:

```shell
source ~/.bashrc && exit
```

Inicie la terminal nuevamente y continúe con la ejecución de los siguientes comandos.

Instalar [Node 16 Version](https://nodejs.org/en/blog/release/v16.16.0):

Descargar e instalar la versión de Node 16, ejecutando el siguiente comando:

```shell
nvm install 16
```

Habilite la versión de Node 16 a usar, ejecutando el siguiente comando:

```shell
nvm use 16
```

Instalar la herramienta [yarn](https://yarnpkg.com/) tool, ejecutando el siguiente
comando:

```shell
npm install --global yarn
```

Clonar e instalar el repositorio git, ejecutando el siguiente comando:

```shell
git clone git@github.com:ScrumLATAMComunidad/scrumlatamcomunidad.com.git scrumlatamcomunidad-com && cd $_
```

Instalar el stack de desarrollado, ejecutando el siguiente comando:

```shell
make install
```

### Iniciar

Abra dos consolas para ejecutar cada uno de los siguientes comandos en cada
una de ellas:

Iniciar el Backend (<http://localhost:8080/>)

```shell
make start-backend
```

Iniciar el Frontend (<http://localhost:3000/>)

```shell
make start-frontend
```

### Ayuda

Para obtener más información detallada sobre las tareas disponibles
para el comando `make`, ejecute el siguiente comando:

```shell
make help
```

## Estructura

Este repositorio monolítico por dos bases de código distintas: api
(backend) y frontend.

-   **backend**: Instalación de API (Backend) Plone usando `pip` (no
    *buildout*). Incluye un paquete de políticas denominado `slc_web`. Más
    información detallada en el archivo 
    [backend/src/slc\_web](backend/src/slc_web/README.md).
-   **devops**: Scripts de despliegues Devops para este repositorio monolítico. Más
    información detallada en el archivo [devops/README.md](devops/README.md).
-   **frontend**: Paquete React (Volto) llamado frontend. Más información detallada
    en el archivo [frontend/README.md](frontend/README.md).

### Razonamiento

-   El repositorio contiene todo el código base necesario para ejecutar el portal
    (excluyendo complementos existentes para Plone y React).
-   Los flujos de trabajo de Github se activan en función de los cambios en cada base de código
    (ver el directorio `.github/workflows`)
-   Más fácil de crear imágenes de Docker para cada base de código
-   Instalación/configuración de Showcase Plone sin compilación

## Linters y formateo

Hay algunos ganchos para ejecutar controles de pelusa en el código. Si desea
formatearlos automáticamente, puede ejecutar

`make format`

en la carpeta raíz o específicamente en cada carpeta de backend o frontend.

Los comandos de Linters están disponibles en cada carpeta de backend y frontend.

## Pruebas de aceptación

Hay comandos `Makefile` en su lugar:

`build-test-acceptance-server`: Construir la imagen Docker de aceptación
del servidor backend que se está utilizando después. Debe ejecutarse antes
de ejecutar las pruebas, si el código de backend ha cambiado.

`build-test-acceptance-server`: Build Acceptance Backend Server Docker
image that it's being used afterwards. Must be run before running the
tests, if the backend code has changed.

`start-test-acceptance-server`: Inicie el servidor fixture en Docker (construcción
previa es requerida)

`start-test-acceptance-frontend`: Inicie los Fixture de Frontend de aceptación del Core
en modo desarrollador

`test-acceptance`: Inicie las pruebas de aceptación de Core Cypress en modo desarrollo

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/leonardojcaballerog"><img src="https://avatars.githubusercontent.com/u/185395?v=4?s=75" width="75px;" alt="Leonardo J. Caballero G."/><br /><sub><b>Leonardo J. Caballero G.</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Amacagua" title="Informes de errores">🐛</a> <a href="#maintenance-macagua" title="Mantenimiento">🚧</a> <a href="#infra-macagua" title="Infraestructura (Hosting, Build-Tools, etc.)">🚇</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Documentación">📖</a> <a href="#tool-macagua" title="Herramientas">🔧</a> <a href="#security-macagua" title="Seguridad">🛡️</a> <a href="#question-macagua" title="Respondiendo preguntas">💬</a> <a href="#translation-macagua" title="Traducción">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Código">💻</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Pruebas">⚠️</a> <a href="#userTesting-macagua" title="Pruebas de usuario">📓</a> <a href="#projectManagement-macagua" title="Gestión de proyectos">📆</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/pulls?q=is%3Apr+reviewed-by%3Amacagua" title="Revisión de Pull Requests">👀</a> <a href="#ideas-macagua" title="Ideas, planificación y comentarios">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/humberto-hansen-92b73352/"><img src="https://instagram.fmrd1-1.fna.fbcdn.net/v/t51.2885-19/17881639_747899672054176_4890925133947994112_n.jpg?_nc_ht=instagram.fmrd1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=39h9kCktnDIAX_oAKBZ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDTMYuHMKnHrbd5GZckyn9aSBLLYLyafRJmzhP9ad1wTA&oe=648657F2&_nc_sid=f70a57?s=75" width="75px;" alt="Humberto R Hansen."/><br /><sub><b>Humberto R Hansen.</b></sub></a><br /><a href="#fundingFinding-humbertohansen" title="Búsqueda de fondos">🔍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Ahumbertohansen" title="Informes de errores">🐛</a> <a href="#maintenance-humbertohansen" title="Mantenimiento">🚧</a> <a href="#infra-humbertohansen" title="Infraestructura (Hosting, Build-Tools, etc.)">🚇</a> <a href="#security-humbertohansen" title="Seguridad">🛡️</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=humbertohansen" title="Documentación">📖</a> <a href="#tool-humbertohansen" title="Herramientas">🔧</a> <a href="#question-humbertohansen" title="Respondiendo preguntas">💬</a> <a href="#design-humbertohansen" title="Diseño">🎨</a> <a href="#translation-humbertohansen" title="Traducción">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=humbertohansen" title="Código">💻</a> <a href="#userTesting-humbertohansen" title="Pruebas de usuario">📓</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/pulls?q=is%3Apr+reviewed-by%3Ahumbertohansen" title="Revisión de Pull Requests">👀</a> <a href="#ideas-humbertohansen" title="Ideas, planificación y comentarios">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/alfadestroyer"><img src="https://avatars.githubusercontent.com/u/132786011?v=4?s=75" width="75px;" alt="Manuel Matos"/><br /><sub><b>Manuel Matos</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aalfadestroyer" title="Informes de errores">🐛</a> <a href="#design-alfadestroyer" title="Diseño">🎨</a> <a href="#translation-alfadestroyer" title="Traducción">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=alfadestroyer" title="Código">💻</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=alfadestroyer" title="Pruebas">⚠️</a> <a href="#userTesting-alfadestroyer" title="Pruebas de usuario">📓</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/JuanLP06"><img src="https://avatars.githubusercontent.com/u/10691487?v=4?s=75" width="75px;" alt="Juan Lopez"/><br /><sub><b>Juan Lopez</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3AJuanLP06" title="Informes de errores">🐛</a> <a href="#design-JuanLP06" title="Diseño">🎨</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=JuanLP06" title="Código">💻</a> <a href="#translation-JuanLP06" title="Traducción">🌍</a> <a href="#userTesting-JuanLP06" title="Pruebas de usuario">📓</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/ruben-dario-romero-chica-47906837/"><img src="https://avatars.githubusercontent.com/u/122922804?v=4?s=75" width="75px;" alt="Ruben Dario Romero Chica"/><br /><sub><b>Ruben Dario Romero Chica</b></sub></a><br /><a href="#business-scrumlatam" title="Desarrollo de negocios">💼</a> <a href="#mentoring-scrumlatam" title="Mentoría">🧑‍🏫</a> <a href="#eventOrganizing-scrumlatam" title="Organización de eventos">📋</a> <a href="#fundingFinding-scrumlatam" title="Búsqueda de fondos">🔍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Ascrumlatam" title="Informes de errores">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=scrumlatam" title="Documentación">📖</a> <a href="#content-scrumlatam" title="Contenido">🖋</a> <a href="#question-scrumlatam" title="Respondiendo preguntas">💬</a> <a href="#projectManagement-scrumlatam" title="Gestión de proyectos">📆</a> <a href="#ideas-scrumlatam" title="Ideas, planificación y comentarios">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/emilia-miranda-76242020/"><img src="https://avatars.githubusercontent.com/u/133285771?v=4?s=75" width="75px;" alt="Emilia Miranda"/><br /><sub><b>Emilia Miranda</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aemicmiranda" title="Informes de errores">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=emicmiranda" title="Documentación">📖</a> <a href="#content-emicmiranda" title="Contenido">🖋</a> <a href="#question-emicmiranda" title="Respondiendo preguntas">💬</a> <a href="#projectManagement-emicmiranda" title="Gestión de proyectos">📆</a> <a href="#ideas-emicmiranda" title="Ideas, planificación y comentarios">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/hiomara-apaza/"><img src="https://avatars.githubusercontent.com/u/133286537?v=4?s=75" width="75px;" alt="Vanessa Apaza"/><br /><sub><b>Vanessa Apaza</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3AHiomara" title="Informes de errores">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=Hiomara" title="Documentación">📖</a> <a href="#content-Hiomara" title="Contenido">🖋</a> <a href="#question-Hiomara" title="Respondiendo preguntas">💬</a> <a href="#projectManagement-Hiomara" title="Gestión de proyectos">📆</a> <a href="#ideas-Hiomara" title="Ideas, planificación y comentarios">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/lizbethmartelsalguero/"><img src="https://avatars.githubusercontent.com/u/134661241?v=4?s=75" width="75px;" alt="Lizbeth Martel"/><br /><sub><b>Lizbeth Martel</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Almartel0911" title="Informes de errores">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=lmartel0911" title="Documentación">📖</a> <a href="#content-lmartel0911" title="Contenido">🖋</a> <a href="#question-lmartel0911" title="Respondiendo preguntas">💬</a> <a href="#projectManagement-lmartel0911" title="Gestión de proyectos">📆</a> <a href="#ideas-lmartel0911" title="Ideas, planificación y comentarios">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/enny-infante-guevara-20585084/"><img src="https://avatars.githubusercontent.com/u/67449707?v=4?s=75" width="75px;" alt="Enny Infante"/><br /><sub><b>Enny Infante</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aennyin" title="Informes de errores">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=ennyin" title="Documentación">📖</a> <a href="#content-ennyin" title="Contenido">🖋</a> <a href="#question-ennyin" title="Respondiendo preguntas">💬</a> <a href="#projectManagement-ennyin" title="Gestión de proyectos">📆</a> <a href="#ideas-ennyin" title="Ideas, planificación y comentarios">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). ¡Contribuciones de cualquier tipo son bienvenidas!

Para ver solo los *colaboradores del código fuente*, consulte los [gráficos de los contribuyentes](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/graphs/contributors).

## Créditos

**Esto fue generado por [cookiecutter-plone-starter](https://github.com/collective/cookiecutter-plone-starter) el 11-05-2023 04:07:02**

## Licencia

Licenciado bajo la **GNU GENERAL PUBLIC LICENSE Version 2**, para obtener más detalles, consulta el archivo [LICENSE](LICENSE).
