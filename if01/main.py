#!/usr/bin/env python
# -*- coding: utf-8 -*-


def equacao_tem_raizes(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Não ha raízes reais")
    else:
        print("Há raízes reais")
