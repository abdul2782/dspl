#!/bin/env python3
# Copyright 2018 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from absl import app
from absl import flags
from dspl2 import (Dspl2JsonLdExpander, Dspl2RdfExpander, LocalFileGetter,
                   FrameGraph, LoadGraph, ValidateDspl2)
import sys


FLAGS = flags.FLAGS
flags.DEFINE_boolean('rdf', False, 'Process the JSON-LD as RDF.')


def main(args):
  if len(args) != 2:
    print(f'Usage: {args[0]} [DSPL file]', file=sys.stderr)
    exit(1)
  getter = LocalFileGetter(args[1])
  if flags.FLAGS.rdf:
    graph = Dspl2RdfExpander(getter).Expand()
    dspl = FrameGraph(getter.graph)
  else:
    dspl = Dspl2JsonLdExpander(getter).Expand()
  warnings = ValidateDspl2(dspl, getter)
  for warning in warnings:
    print(warning)


if __name__ == '__main__':
  app.run(main)
