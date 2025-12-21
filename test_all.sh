#!/bin/bash
set -e

for dir in */; do
  [ -d "$dir" ] || continue
  pushd "$dir"
  make test
  popd
done
