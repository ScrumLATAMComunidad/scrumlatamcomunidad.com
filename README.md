# SCRUM LATAM Comunidad Website

The [Scrum Latam Comunidad](https://www.scrumlatamcomunidad.com/)
Website repository.

[![Built with Cookiecutter Plone Starter](https://img.shields.io/badge/built%20with-Cookiecutter%20Plone%20Starter-0083be.svg?logo=cookiecutter)](https://github.com/collective/cookiecutter-plone-starter/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Backend Tests](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml)
[![Frontend Tests](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml)
[![All Contributors](https://img.shields.io/github/all-contributors/ScrumLATAMComunidad/scrumlatamcomunidad.com?color=ee8449&style=flat-square)](#contributors)


A new SCRUM LATAM Comunidad Website using Plone 6 and Volto
technologies.

## Quick start

### Development Setup

-   Python 3.9, 3.10, 3.11
-   Node 16
-   yarn
-   Docker

### Install

Install the requirements dependencies, executing the following command:

```shell
sudo apt install build-essential python3-dev python3-venv git tree curl
```

Download and install [Node Version Manager -
NVM](https://github.com/nvm-sh/nvm/blob/master/README.md), executing the
following command:

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

Setting the `nvm` script into console environments to use it, executing
the following command:

```shell
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" \
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

To reflect the `nvm` script changes in the terminal environments to use
it, executing the following command:

```shell
source ~/.bashrc && exit
```

Launch the terminal again and continues with execute the next commands.

Install [Node 16 Version](https://nodejs.org/en/blog/release/v16.16.0):

Download and install Node 16 Version, executing the following command:

```shell
nvm install 16
```

Enable the Node 16 Version to use it, executing the following command:

```shell
nvm use 16
```

Install [yarn](https://yarnpkg.com/) tool, executing the following
command:

```shell
npm install --global yarn
```

Clone and install the git repository, executing the following command:

```shell
git clone git@github.com:ScrumLATAMComunidad/scrumlatamcomunidad.com.git scrumlatamcomunidad-com && cd $_
```

Install the dev stack, executing the following command:

```shell
make install
```

### Start

Open two consoles to run each of the following commands in each of them:

Start the Backend (<http://localhost:8080/>)

```shell
make start-backend
```

Start the Frontend (<http://localhost:3000/>)

```shell
make start-frontend
```

### Help

For more details information about tasks available for command `make`,
executing the following command:

```shell
make help
```

## Structure

This monorepo is composed by two distinct codebases: api and frontend.

-   **backend**: API (Backend) Plone installation using `pip` (not
    *buildout*). Includes a policy package named `slc_sitioweb`. More
    details information at
    [backend/src/slc\_sitioweb/README.md](backend/src/slc_sitioweb/README.md)
    file.
-   **devops**: Devops Deployments scripts por this monorepo. More
    details information at [devops/README.md](devops/README.md) file.
-   **frontend**: React (Volto) package named frontend. More details
    information at [frontend/README.md](frontend/README.md) file.

### Reasoning

-   Repo contains all codebase needed to run the site (excluding
    existing addons for Plone and React).
-   Github Workflows are triggered based on changes on each codebase
    (see `.github/workflows`)
-   Easier to create Docker images for each codebase
-   Showcase Plone installation/setup without buildout

## Linters and Formatting

There are some hooks to run lint checks on the code. If you want to
automatically format them, you can run

`make format`

in the root folder or especifically in each backend or frontend folders.

Linters commands are available in each backend and frontend folder.

## Acceptance tests

There are `Makefile` commands in place:

`build-test-acceptance-server`: Build Acceptance Backend Server Docker
image that it's being used afterwards. Must be run before running the
tests, if the backend code has changed.

`start-test-acceptance-server`: Start server fixture in docker (previous
build required)

`start-test-acceptance-frontend`: Start the Core Acceptance Frontend
Fixture in dev mode

`test-acceptance`: Start Core Cypress Acceptance Tests in dev mode

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

For see only the *source code contributors* checkout the [contributors graphs](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/graphs/contributors).

## Credits

**This was generated by [cookiecutter-plone-starter](https://github.com/collective/cookiecutter-plone-starter) on 2023-05-11 04:07:02**
