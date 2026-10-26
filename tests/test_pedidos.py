import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import legacy  # noqa: E402
import pedidos  # noqa: E402

CASOS = [
    (
        [{"categoria": "libros", "precio": 100, "cantidad": 2}],
        "premium",
        "AR",
        "PROMO10",
    ),
    (
        [{"categoria": "electro", "precio": 500, "cantidad": 1}],
        "regular",
        "UY",
        "PROMO20",
    ),
    ([{"categoria": "ropa", "precio": 80, "cantidad": 3}], "regular", "CL", ""),
    ([{"categoria": "ropa", "precio": 80, "cantidad": 3}], "premium", "BR", None),
    ([{"categoria": "juguetes", "precio": 40, "cantidad": 5}], "premium", "XX", "OTRO"),
    ([{"categoria": "libros", "precio": 10, "cantidad": 1}], "nuevo", "AR", "PROMO10"),
    ([], "regular", "AR", ""),
]


class TestPedidos(unittest.TestCase):
    def test_valor_conocido(self):
        items = [{"categoria": "libros", "precio": 100, "cantidad": 2}]
        self.assertEqual(
            pedidos.calcular_total(items, "premium", "AR", "PROMO10"), 185.13
        )

    def test_sin_items(self):
        self.assertEqual(pedidos.calcular_total([], "regular", "AR", ""), 0)

    def test_pais_desconocido_sin_impuesto(self):
        items = [{"categoria": "ropa", "precio": 100, "cantidad": 1}]
        self.assertEqual(pedidos.calcular_total(items, "regular", "XX", ""), 92)

    def test_cupon_invalido_se_ignora(self):
        items = [{"categoria": "electro", "precio": 100, "cantidad": 1}]
        self.assertEqual(pedidos.calcular_total(items, "nuevo", "XX", "FALSO"), 100)

    def test_equivalencia_con_legacy(self):
        for args in CASOS:
            with self.subTest(args=args):
                self.assertEqual(
                    pedidos.calcular_total(*args), legacy.calcular_total(*args)
                )


if __name__ == "__main__":
    unittest.main()
