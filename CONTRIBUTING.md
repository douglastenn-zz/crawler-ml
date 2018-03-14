Contributing
============

Contributions are welcome!

**Please carefully read this page to make the code review process go as smoothly as possible and to maximize the likelihood of your contribution being merged.**

## Bug Reports

For bug reports or requests [submit an issue]().

## Pull Requests

The preferred way to contribute is to fork the
[main repository]() on Github.

1. Fork the [main repository]().  Click on the 'Fork' button near the title of the project. 

2. Clone this copy to your local disk:

        $ git clone crawler_ml.git
        $ cd crawler_ml

3. Create a branch to hold your changes and start making changes. Don't work in the `master` branch!

        $ git checkout -b my-feature

4. Work on this copy on your computer using Git to do the version control. When you're done editing, run the following to record your changes in Git:

        $ git add modified_files
        $ git commit

5. Push your changes to Github with:

        $ git push -u origin my-feature

6. Finally, go to the web page of your fork of the `crawler_ml` repo and click 'Pull Request' to send your changes for review.

### Github Pull Requests Docs

If you are not familiar with pull requests, review the [pull request docs](https://help.github.com/articles/about-pull-requests/).

## Logging

For write logs, you need to import the module [**logger_handler**](./crawler_ml/logger_handler.py).

```
from crawler_ml.logger_handler import logger

# Error 
logger.error('Error Message')

# INFO
logger.info('Info Message')

# Warning
logger.warning('Warning Message')
```

## Tests

### Unit tests

Make sure the unit tests are working.
And if do you implement another feature, you need to make a unit test with [`unittest`](https://docs.python.org/3/library/unittest.html) and [`nose`](http://nose.readthedocs.io/en/latest/).

We encourage you to develop using the TDD methodology `<3`

### Integration tests

Make sure the integration tests are working.
And if do you implement another feature, you need to make a integration test with [`behave`](http://pythonhosted.org/behave/).

### Creating a integration test

The integration tests are located on folder `tests/integration`.

Create the `feature_file` on `tests/integration` and the `test_file` on `tests/integration/steps`.

Please follow the [`behave`](http://pythonhosted.org/behave/) specification.

## Thanks for contribute :)