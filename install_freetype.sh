#!/bin/bash
wget -O freetype-2.4.0.tar.gz https://download.savannah.gnu.org/releases/freetype/freetype-2.4.0.tar.gz
tar -zxf freetype-2.4.0.tar.gz
cd freetype-2.4.0
./configure
make
make install
