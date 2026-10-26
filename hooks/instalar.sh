#!/bin/sh
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "hook instalado en .git/hooks/pre-commit"
