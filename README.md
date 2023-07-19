# SCRUM LATAM Comunidad Web portal

The [SCRUM LATAM Comunidad](https://www.scrumlatamcomunidad.com/)
Web portal repository.

[Spanish](README_es.md)

[![Built with Cookiecutter Plone Starter](https://img.shields.io/badge/built%20with-Cookiecutter%20Plone%20Starter-0083be.svg?logo=cookiecutter)](https://github.com/collective/cookiecutter-plone-starter/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Backend Tests](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/backend.yml)
[![Frontend Tests](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml/badge.svg)](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/actions/workflows/frontend.yml)
[![All Contributors](https://img.shields.io/github/all-contributors/ScrumLATAMComunidad/scrumlatamcomunidad.com?color=ee8449&style=flat-square)](#contributors)

A new SCRUM LATAM Comunidad Web portal using Plone 6 and Volto
technologies.

## Quick start

### Development Setup

- Python 3.9, 3.10, 3.11
- Node 16
- yarn
- Docker

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
    *buildout*). Includes a policy package named `slc_web`. More
    details information at
    [backend/src/slc\_web/README.md](backend/src/slc_web/README.md)
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

## Analytics summary

![Alt](https://repobeats.axiom.co/api/embed/af3ecafec830363436b35fc00afdb198a0821001.svg "Repobeats analytics image")

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/leonardojcaballerog"><img src="https://avatars.githubusercontent.com/u/185395?v=4?s=75" width="75px;" alt="Leonardo J. Caballero G."/><br /><sub><b>Leonardo J. Caballero G.</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Amacagua" title="Bug reports">🐛</a> <a href="#maintenance-macagua" title="Maintenance">🚧</a> <a href="#infra-macagua" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Documentation">📖</a> <a href="#tool-macagua" title="Tools">🔧</a> <a href="#security-macagua" title="Security">🛡️</a> <a href="#question-macagua" title="Answering Questions">💬</a> <a href="#translation-macagua" title="Translation">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Code">💻</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=macagua" title="Tests">⚠️</a> <a href="#userTesting-macagua" title="User Testing">📓</a> <a href="#projectManagement-macagua" title="Project Management">📆</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/pulls?q=is%3Apr+reviewed-by%3Amacagua" title="Reviewed Pull Requests">👀</a> <a href="#ideas-macagua" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/humberto-hansen-92b73352/"><img src="https://instagram.fmrd1-1.fna.fbcdn.net/v/t51.2885-19/17881639_747899672054176_4890925133947994112_n.jpg?_nc_ht=instagram.fmrd1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=39h9kCktnDIAX_oAKBZ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDTMYuHMKnHrbd5GZckyn9aSBLLYLyafRJmzhP9ad1wTA&oe=648657F2&_nc_sid=f70a57?s=75" width="75px;" alt="Humberto R Hansen."/><br /><sub><b>Humberto R Hansen.</b></sub></a><br /><a href="#fundingFinding-humbertohansen" title="Funding Finding">🔍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Ahumbertohansen" title="Bug reports">🐛</a> <a href="#maintenance-humbertohansen" title="Maintenance">🚧</a> <a href="#infra-humbertohansen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#security-humbertohansen" title="Security">🛡️</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=humbertohansen" title="Documentation">📖</a> <a href="#tool-humbertohansen" title="Tools">🔧</a> <a href="#question-humbertohansen" title="Answering Questions">💬</a> <a href="#design-humbertohansen" title="Design">🎨</a> <a href="#translation-humbertohansen" title="Translation">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=humbertohansen" title="Code">💻</a> <a href="#userTesting-humbertohansen" title="User Testing">📓</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/pulls?q=is%3Apr+reviewed-by%3Ahumbertohansen" title="Reviewed Pull Requests">👀</a> <a href="#ideas-humbertohansen" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/alfadestroyer"><img src="https://avatars.githubusercontent.com/u/132786011?v=4?s=75" width="75px;" alt="Manuel Matos"/><br /><sub><b>Manuel Matos</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aalfadestroyer" title="Bug reports">🐛</a> <a href="#design-alfadestroyer" title="Design">🎨</a> <a href="#translation-alfadestroyer" title="Translation">🌍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=alfadestroyer" title="Code">💻</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=alfadestroyer" title="Tests">⚠️</a> <a href="#userTesting-alfadestroyer" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/JuanLP06"><img src="https://avatars.githubusercontent.com/u/10691487?v=4?s=75" width="75px;" alt="Juan Lopez"/><br /><sub><b>Juan Lopez</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3AJuanLP06" title="Bug reports">🐛</a> <a href="#design-JuanLP06" title="Design">🎨</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=JuanLP06" title="Code">💻</a> <a href="#translation-JuanLP06" title="Translation">🌍</a> <a href="#userTesting-JuanLP06" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/ruben-dario-romero-chica-47906837/"><img src="https://avatars.githubusercontent.com/u/122922804?v=4?s=75" width="75px;" alt="Ruben Dario Romero Chica"/><br /><sub><b>Ruben Dario Romero Chica</b></sub></a><br /><a href="#business-scrumlatam" title="Business development">💼</a> <a href="#mentoring-scrumlatam" title="Mentoring">🧑‍🏫</a> <a href="#eventOrganizing-scrumlatam" title="Event Organizing">📋</a> <a href="#fundingFinding-scrumlatam" title="Funding Finding">🔍</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Ascrumlatam" title="Bug reports">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=scrumlatam" title="Documentation">📖</a> <a href="#content-scrumlatam" title="Content">🖋</a> <a href="#question-scrumlatam" title="Answering Questions">💬</a> <a href="#projectManagement-scrumlatam" title="Project Management">📆</a> <a href="#ideas-scrumlatam" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/emilia-miranda-76242020/"><img src="https://avatars.githubusercontent.com/u/133285771?v=4?s=75" width="75px;" alt="Emilia Miranda"/><br /><sub><b>Emilia Miranda</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aemicmiranda" title="Bug reports">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=emicmiranda" title="Documentation">📖</a> <a href="#content-emicmiranda" title="Content">🖋</a> <a href="#question-emicmiranda" title="Answering Questions">💬</a> <a href="#projectManagement-emicmiranda" title="Project Management">📆</a> <a href="#ideas-emicmiranda" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/hiomara-apaza/"><img src="https://avatars.githubusercontent.com/u/133286537?v=4?s=75" width="75px;" alt="Vanessa Apaza"/><br /><sub><b>Vanessa Apaza</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3AHiomara" title="Bug reports">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=Hiomara" title="Documentation">📖</a> <a href="#content-Hiomara" title="Content">🖋</a> <a href="#question-Hiomara" title="Answering Questions">💬</a> <a href="#projectManagement-Hiomara" title="Project Management">📆</a> <a href="#ideas-Hiomara" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/lizbethmartelsalguero/"><img src="https://avatars.githubusercontent.com/u/134661241?v=4?s=75" width="75px;" alt="Lizbeth Martel"/><br /><sub><b>Lizbeth Martel</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Almartel0911" title="Bug reports">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=lmartel0911" title="Documentation">📖</a> <a href="#content-lmartel0911" title="Content">🖋</a> <a href="#question-lmartel0911" title="Answering Questions">💬</a> <a href="#projectManagement-lmartel0911" title="Project Management">📆</a> <a href="#ideas-lmartel0911" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/enny-infante-guevara-20585084/"><img src="https://avatars.githubusercontent.com/u/67449707?v=4?s=75" width="75px;" alt="Enny Infante"/><br /><sub><b>Enny Infante</b></sub></a><br /><a href="https://github.com/macagua/scrumlatamcomunidad.com/issues?q=author%3Aennyin" title="Bug reports">🐛</a> <a href="https://github.com/macagua/scrumlatamcomunidad.com/commits?author=ennyin" title="Documentation">📖</a> <a href="#content-ennyin" title="Content">🖋</a> <a href="#question-ennyin" title="Answering Questions">💬</a> <a href="#projectManagement-ennyin" title="Project Management">📆</a> <a href="#ideas-ennyin" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

For see only the *source code contributors* checkout the [contributors graphs](https://github.com/ScrumLATAMComunidad/scrumlatamcomunidad.com/graphs/contributors).

## Credits

**This was generated by [cookiecutter-plone-starter](https://github.com/collective/cookiecutter-plone-starter) on 2023-05-11 04:07:02**

## License

Licensing by **GNU GENERAL PUBLIC LICENSE Version 2**, for more details checkout [LICENSE](LICENSE) file.
