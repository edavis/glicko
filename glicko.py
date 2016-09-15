#!/usr/bin/env python

from math import log, sqrt, pi

q = round(log(10.0) / 400.0, 7)

def g(RD):
    _ = 1.0 / sqrt(1.0 + 3.0 * q ** 2.0 * (RD ** 2.0) / pi ** 2.0)
    return round(_, 4)

def E(r, rj, RDj):
    _ = 1.0 / (1.0 + pow(10.0, -g(RDj) * (r - rj) / 400.0))
    return round(_, 3)

def d2(r, matches):
    _ = (q ** 2.0 * sum((g(RDj) ** 2.0) * (E(r, rj, RDj)) * (1 - E(r, rj, RDj)) for (rj, RDj, sj) in matches)) ** -1.0
    return round(_, 2)

def outcome(a, b):
    (ri, RDi) = a; (rj, RDj) = b
    _ = 1.0 / (1.0 + 10.0 ** (-g(sqrt(RDi ** 2.0 + RDj ** 2.0)) * (ri - rj) / 400.0))
    return round(_, 3)

def glicko(r, RD, matches):
    r_new = r + q / (1.0 / RD ** 2.0 + 1.0 / d2(r, matches)) * sum(g(RDj) * (sj - E(r, rj, RDj)) for (rj, RDj, sj) in matches)
    RD_new = sqrt((1.0 / RD ** 2.0 + 1.0 / d2(r, matches)) ** -1.0)
    return (round(r_new, 0), round(RD_new, 1))
