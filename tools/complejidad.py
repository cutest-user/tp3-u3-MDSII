"""Complejidad ciclomatica por funcion (McCabe) usando solo la libreria estandar."""
import ast
import sys

NODOS = (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With, ast.IfExp,
         ast.comprehension)


def complejidad(func):
    c = 1
    for n in ast.walk(func):
        if isinstance(n, NODOS):
            c += 1
        elif isinstance(n, ast.BoolOp):
            c += len(n.values) - 1
    return c


def main(rutas):
    for ruta in rutas:
        arbol = ast.parse(open(ruta, encoding="utf-8").read())
        for n in ast.walk(arbol):
            if isinstance(n, ast.FunctionDef):
                print(f"{ruta}:{n.lineno} {n.name} CC={complejidad(n)}")


if __name__ == "__main__":
    main(sys.argv[1:])
