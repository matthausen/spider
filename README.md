# Spider

![spider](./logo.pgn)

Spider is an unofficial Amazon GraphQL API which allows the user to browse the Amazon catalogue.

It use scraping to fetch information from the official website and serve its content over an API.

It currently scrapes Amazon only but could fetch more information from other retailers in the near future.


## Table of contents
* [Technologies](#technologies)
* [How to use](#how-to-use)
* [Contribute](#contribute)
* [License](#license)


## Technologies

The stack includes:

* python
* flask
* graphene
* graphql


## How to use:

To run download the repo and install its dependencies

```pip3 install requirements.txt```

Later start the GraphQL server:

```python3 app.py```

The server starts on port :5000 and the GraphiQL interface is available at:

http://127.0.0.1:5000/graphql

## Contribute

Everyone is welcome to contribute to the source code.
Simply clone the project and branch off from `master`.

Also pull requests must have master as the destination branch


## License:

MIT: https://rem.mit-license.org