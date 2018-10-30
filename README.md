# directory-api-client-external

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]

**Export Directory external API client.**

---

## Installation

```sh
    $ pip install directory-api-external
```

The api client expects the following settings:

| Setting                                       | Notes                                                       |
| --------------------------------------------- | ----------------------------------------------------------- |
| DIRECTORY_API_CLIENT_EXTERNAL_BASE_URL        |                                                             |
| DIRECTORY_API_CLIENT_EXTERNAL_API_KEY         | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_API_CLIENT_EXTERNAL_SENDER_ID       | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_API_CLIENT_EXTERNAL_DEFAULT_TIMEOUT |                                                             |

Once that is done the API client can be used:

```py
from directory_api_external.client import api_client
```


## Development

    $ git clone https://github.com/uktrade/directory-api-client-external
    $ cd directory-api-client-external

## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |


Then run the following command:

    make publish


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-api-client-external/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-api-client-external

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-api-client-external/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-api-client-external/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-api-client-external/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-api-client-external

[pypi-image]: https://badge.fury.io/py/directory-api-external.svg
[pypi]: https://badge.fury.io/py/directory-api-external
