# Chaos Platform Authentication Service

[![Version](https://img.shields.io/pypi/v/chaosplatform-scheduler.svg)](https://img.shields.io/pypi/v/chaosplatform-scheduler.svg)
[![License](https://img.shields.io/pypi/l/chaosplatform-scheduler.svg)](https://img.shields.io/pypi/l/chaosplatform-scheduler.svg)
[![StackOverflow](https://img.shields.io/badge/StackOverflow-ChaosPlatform-blue.svg)](https://stackoverflow.com/questions/tagged/chaosplatform+or+chaostoolkit)

[![Build Status](https://travis-ci.org/chaostoolkit/chaosplatform-scheduler.svg?branch=master)](https://travis-ci.org/chaostoolkit/chaosplatform-scheduler)
[![Python versions](https://img.shields.io/pypi/pyversions/chaosplatform-scheduler.svg)](https://www.python.org/)

This is the default scheduler service of the [Chaos Platform][chaosplatform].

[chaosplatform]: https://chaosplatform.org/

## Purpose

* Provide a gRPC api to schedule/cancel experiment executions

## Content

* [Install]
* [Configure]
* [Run]

[install]: ./docs/install.md
[configure]: ./docs/settings.md
[run]: ./docs/run.md

## Contribute

Contributors to this project are welcome as this is an open-source effort that
seeks [discussions][join] and continuous improvement.

[join]: https://join.chaostoolkit.org/

From a code perspective, if you wish to contribute, you will need to run a 
Python 3.5+ environment. Then, fork this repository and submit a PR. The
project cares for code readability and checks the code style to match best
practices defined in [PEP8][pep8]. Please also make sure you provide tests
whenever you submit a PR so we keep the code reliable.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

The Chaos Platform projects require all contributors must sign a
[Developer Certificate of Origin][dco] on each commit they would like to merge
into the master branch of the repository. Please, make sure you can abide by
the rules of the DCO before submitting a PR.

[dco]: https://github.com/probot/dco#how-it-works