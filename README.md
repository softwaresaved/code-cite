# The Code and Data Citation Counter

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1209311.svg)](https://doi.org/10.5281/zenodo.1209311) [![Join the chat at https://gitter.im/code-cite/Lobby](https://badges.gitter.im/code-cite/Lobby.svg)](https://gitter.im/code-cite/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

***Allow researchers and policy makers to see how the presence and quality of links to data and software in publications are changing over time so that they can identify emergent behaviour.***

This project started at [Springer Nature Hackday](https://www.springernature.com/gb/researchers/campaigns/sn-hack-day) in November 2017 and continued at the [Collaborations Workshop Hackday](https://www.software.ac.uk/cw18/) in March 2018.

The goal is to analyse a corpus of papers for citation links into repositories which may hold research data and/or software.

We are highly motivated to support the much needed culture change regarding the recognition of open data and code sharing in the scientific community. Being able to measure the number of papers that cite their code and data in the academic literature is important to show **evidence of the increasing recognition** of research software and its developers. 

### What does the code cite counter do?

The code-cite counter searches a corpus of literature (eg: [Europe Pubmed Central](https://europepmc.org)) for particular terms (such as `github.com`, `doi.org/10.5281/zenodo` or `doi.org/10.6084/m9.figshare`) and show how their prevalence is increasing over time.

We also provide measures of stability and quality for this code by resolving links found in papers and evaluating metadata such as the existence of a `README` or `LICENSE` file.

Finally, we provide (the beginnings of) a [web interface](https://codecite.herokuapp.com/) so that users can run their own search queries from the published literature, and from specific journals of interest. You can see the source code in its (separate) [github repository](https://github.com/softwaresaved/code-cite-app).


### Contributing

We would love for you to join us on this journey!

Check out the [contributing guidelines](CONTRIBUTING.md) or our [list of issues](https://github.com/softwaresaved/code-cite/issues) to see how you can help.

### Contributors

Thank you to everyone who has contributed so far!

| [<img src="https://avatars.githubusercontent.com/andreww?s=460&v=4" width="100px;"/><br /><sub><b>Andrew Walker</b></sub>](https://github.com/andreww)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=andreww) 🤔 | [<img src="https://avatars.githubusercontent.com/longr?s=460&v=4" width="100px;"/><br /><sub><b>Robin Long</b></sub>](https://github.com/longr)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=longr) 🤔 | [<img src="https://avatars.githubusercontent.com/npscience?s=460&v=4" width="100px;"/><br /><sub><b>Naomi Penfold</b></sub>](https://github.com/npscience)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=npscience) [📖](https://github.com/softwaresaved/code-cite/commits?author=npscience) 🤔 | [<img src="https://avatars.githubusercontent.com/npch?s=460&v=4" width="100px;"/><br /><sub><b>Neil Chue Hong</b></sub>](https://github.com/npch)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=npch) 🤔 | [<img src="https://avatars.githubusercontent.com/martintoreilly?s=460&v=4" width="100px;"/><br /><sub><b>Martin O'Reilly</b></sub>](https://github.com/martintoreilly)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=martintoreilly) 🤔 |
| :---: | :---: | :---: | :---: | :---: |
| [<img src="https://avatars.githubusercontent.com/astruck?s=460&v=4" width="100px;"/><br /><sub><b>Alexander Struck</b></sub>](https://github.com/astruck)<br /> [📖](https://github.com/softwaresaved/code-cite/commits?author=astruck) 🤔 | [<img src="https://avatars.githubusercontent.com/ivyleavedtoadflax?s=460&v=4" width="100px;"/><br /><sub><b>Matthew Upson</b></sub>](https://github.com/ivyleavedtoadflax)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=ivyleavedtoadflax) 🤔 🎨 | [<img src="https://avatars.githubusercontent.com/islast?s=460&v=4" width="100px;"/><br/><sub><b>Isla Staden</b></sub>](https://github.com/islast)<br /> [💻](https://github.com/softwaresaved/code-cite/commits?author=islast) 🤔 💬 | [<img src="https://avatars.githubusercontent.com/kirstiejane?s=460&v=4" width="100px;"/><br /><sub><b>Kirstie Whitaker</b></sub>](https://github.com/kirstiejane)<br /> [📖](https://github.com/softwaresaved/code-cite/commits?author=kirstiejane) 🤔 [📢]() | [<img src="https://avatars.githubusercontent.com/shoaibsufi?s=460&v=4" width="100px;"/><br /><sub><b>Shoaib Sufi</b></sub>](https://github.com/shoaibsufi)<br /> [📖](https://github.com/softwaresaved/code-cite/commits?author=shoaibsufi) 🤔 [📢]() |


This project follows the [all-contributors][all-contributors] specification and this [emoji key][emojis] explains the different contributions. The order was determined by reverse numerical order of authors' [ORCIDs](https://orcid.org/).

### Community

The project was inspired by [Yo Yehudi's](https://github.com/yochannah) [Code is Science](https://github.com/yochannah/code-is-science/) project and seeks to complement the work by that community by providing some numbers associated with the prevalence of code citations in the published literature.

Our efforts also complement published work by Park et al (2017, doi:[10.1007/s11192-017-2240-2](https://doi.org/10.1007/s11192-017-2240-2)).

### Licence and citations

The Code and Data Citation Counter is licensed under a MIT license and archived on [Zenodo][zenodo-concept].

If you would like to cite the concept, please use this doi: [10.5281/zenodo.1209095][zenodo-concept].

If you would like to reference a specific version of the software, please use the doi associated with that version. The doi is available in the release notes, and can also be found at the [link][zenodo-concept] above. The most recent release is version 0.2 which has doi: [10.5281/zenodo.1209311](zenodo-v0.2).

There are also two files containing reference information (in [`cff`](CITATION.cff) and [`codemeta`](codemeta.json) formats) within the repository which should contain all the information you need to cite this repository.

### Secrets

Some scripts may require the use of secrets you don't want to be stored in this public
Github repository (e.g. web service API keys). You can create a "secrets" folder
in the top level of this repository to store these. This "secrets" folder and
all comments will be ignored by Git.


[emojis]: https://github.com/kentcdodds/all-contributors#emoji-key
[all-contributors]: https://github.com/kentcdodds/all-contributors
[zenodo-concept]: https://doi.org/10.5281/zenodo.1209095
[zenodo-v0.2]: https://doi.org/10.5281/zenodo.1209311
