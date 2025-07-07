#!/usr/bin/env bash
# este escrip simula un analizador de codigo
# que puede fallar o tene exito dependiendo de los argumentos
echo "esto es una prueba"
case "$1" in
    "--fail")
        echo "hubo un error al analizaz, fallo al analizar"
        exit 1
        ;;
    "--success")
        echo "no hay error, el analizis es exitoso"
        exit 0
        ;;
    *)
        echo "analisis completado"
        exit 0
        ;;
esac