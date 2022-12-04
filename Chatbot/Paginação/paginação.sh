#! /bin/bash
`echo Tamanho da paginação: >> paginação.txt`
`getconf PAGE_SIZE >> paginação.txt`
`echo Tamanho da memoria RAM em bytes: >> paginação.txt`
`echo $(getconf PAGE_SIZE)*$(getconf _PHYS_PAGES)|bc >> paginação.txt`
`echo Tamanho da memoria virtual: >> paginação.txt`
`echo $(getconf PAGE_SIZE)*$(getconf AVPHYS_PAGES)|bc >> paginação.txt`
