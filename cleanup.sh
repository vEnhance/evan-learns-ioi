#!/usr/bin/env bash
# Cleans up Rust generated stuff
set -euxo pipefail

find . -path '*/target/*' -delete
find . -type d -name target -delete
