#!/bin/bash
cd "$(dirname "$0")"

cd ../frontend
npm run build

cd ..
rm -rf backend/web
cp -r frontend/build backend/web

