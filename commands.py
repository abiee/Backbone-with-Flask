# -*- coding:utf-8 -*-

from flask.ext.script import Command, Option, prompt_bool

import os
import config

class Test(Command):
    "Run tests."

    start_discovery_dir = "tests"

    def get_options(self):
        return [
            Option('--start_discover', '-s', dest='start_discovery',
                help='Pattern to search for features',
                default=self.start_discovery_dir),
        ]

    def run(self, start_discovery):
        import nose

        if os.path.exists(start_discovery):
            argv = ["d", "--verbosity=2"]

            nose.run(argv=argv)
        else:
            print("Directory '%s' was not found in project root." % start_discovery)


