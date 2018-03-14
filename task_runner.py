import fire
from subprocess import call


class TaskRunner(object):
    """A task runner class."""

    def integration_test(self):
        exit_code = call(['behave', 'tests/integration'])
        if exit_code is not 0:
            exit(exit_code)

    def build(self):
        print('Building...')
        self.integration_test()


if __name__ == '__main__':
    fire.Fire(TaskRunner)
