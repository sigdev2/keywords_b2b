#!/usr/bin/env python
# -*- coding: utf-8 -*-

r''' Copyright 2018, SigDev

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. '''

import os
import codecs
import argparse
import sys
from .keywords_b2b import parse
from . import __version__, __copyright__, __name__ as __base_name__

class ArgumentParser(argparse.ArgumentParser):    
    def _get_action_from_name(self, name):
        container = self._actions
        if name is None:
            return None
        for action in container:
            if r'/'.join(action.option_strings) == name:
                return action
            elif action.metavar == name:
                return action
            elif action.dest == name:
                return action

    def error(self, message):
        exc = sys.exc_info()[1]
        if exc:
            exc.argument = self._get_action_from_name(exc.argument_name)
            raise exc
        super(ArgumentParser, self).error(message)

def check_encoding(enc):
    try:
        codecs.lookup(enc)
    except LookupError as e:
        raise argparse.ArgumentTypeError('\'%r\' incorect encoding: \'%r\'' % enc, str(e))

def main(a):
    vers = r'Version ' + __version__ + r', ' + __copyright__
    parser = ArgumentParser(add_help = True,
                                    prog = __base_name__,
                                    formatter_class = argparse.RawDescriptionHelpFormatter,
                                    description = r'Generate keywords combinations',
                                    epilog = vers)

    parser.add_argument(r'input', type=str, help=r'Keywords file')
    parser.add_argument(r'--encoding', r'-c', type=check_encoding, default=r'utf-8', help=r'Work files encoding')
    parser.add_argument(r'--version', r'-v', action=r'version', version=r'%(prog) ' +  __version__)

    args = parser.parse_args(a)
    
    encoding = args.encoding
    if encoding == None:
        encoding = r'utf-8'

    out = ''
    fn = args.input
    if not os.path.exists(fn):
        return 1

    with codecs.open(fn, r'r', encoding=encoding) as f:
        out = parse(f.read())
    with codecs.open(os.path.basename(fn) + r'.csv', r'w', encoding=r'cp1251') as f:
        f.write(out)
    
    return 0

if __name__ == r'__main__':
    sys.exit(main(sys.argv[1:]))
