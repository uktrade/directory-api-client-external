# directory-api-client-external
Export Directory external API client.

## Build status

[![CircleCI](https://circleci.com/gh/uktrade/directory-api-client-external/tree/master.svg?style=svg)](https://circleci.com/gh/uktrade/directory-api-client-external/tree/master)

## Coverage

[![codecov](https://codecov.io/gh/uktrade/directory-api-client-external/branch/master/graph/badge.svg)](https://codecov.io/gh/uktrade/directory-api-client-external)

## Requirements

## Installation

```shell
pip install -e git+https://git@github.com/uktrade/directory-api-client-external.git@0.0.1#egg=directory-api-client-external
```

## Usage

```python
from directory_api_external.client import DirectoryAPIClient

directory_client = DirectoryAPIClient(
    base_url="https://find-a-buyer.export.great.gov.uk/api",
    api_key=api_key
)
```

## Development

    $ git clone https://github.com/uktrade/directory-api-client-external
    $ cd directory-ui
    $ make
