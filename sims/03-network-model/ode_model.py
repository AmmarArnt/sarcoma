#!/usr/bin/env python3
"""Continuous ODE complement to the Boolean model — threshold / dose-response behaviour
the Boolean model cannot show. QUALITATIVE, illustrative parameters (clearly not fitted).

Core axis: ERK -| CIC -| ETV(+fusion) -> CCND/proliferation, with ERK->DUSP-|ERK feedback.
Demonstrates: (i) fusion-ON makes the proliferation index robust to MEK inhibition
(upstream bypass); (ii) fusion-OFF makes it MEK-sensitive; (iii) BRD4 inhibition lowers
output with a threshold but cannot zero it while the fusion term persists.
"""
from __future__ import annotations
import os, numpy as np
from scipy.integrate import odeint

HERE = os.path.dirname(os.path.abspath(__file__))

# illustrative rate constants (NOT fitted to data)
P = dict(kE=2.0, kdE=1.0, kfb=3.0, kdu=2.0, kddu=1.0,
         kci=1.5, kdci=3.0, ket=2.0, kdet=1.0, kcy=1.5, kdcy=1.0, alpha=1.0)


def rhs(y, t, IGF, Fusion, MEKi, BRD4i, p):
    E, Du, Ci, Et, Cy = y
    BRD4 = 1.0 - BRD4i
    drive_in = p["kE"] * IGF * (1 - MEKi)
    dE = drive_in * (1 - E) - p["kdE"] * E - p["kfb"] * Du * E
    dDu = p["kdu"] * E * (1 - Du) - p["kddu"] * Du
    dCi = p["kci"] * (1 - Ci) - p["kdci"] * E * Ci
    derep = Fusion + p["alpha"] * (1 - Ci)          # fusion = constitutive; (1-Ci) = ERK-driven de-repression
    dEt = p["ket"] * derep * BRD4 * (1 - Et) - p["kdet"] * Et
    dCy = p["kcy"] * Et * (1 - Cy) - p["kdcy"] * Cy
    return [dE, dDu, dCi, dEt, dCy]


def steady(IGF, Fusion, MEKi, BRD4i):
    y0 = [0.1, 0.1, 0.5, 0.1, 0.1]
    t = np.linspace(0, 50, 2000)
    sol = odeint(rhs, y0, t, args=(IGF, Fusion, MEKi, BRD4i, P))
    return sol[-1, 4]  # steady-state proliferation index Cy


def sweep(name, Fusion, var):
    grid = np.linspace(0, 1, 11)
    out = []
    for x in grid:
        if var == "MEKi":
            cy = steady(IGF=1.0, Fusion=Fusion, MEKi=x, BRD4i=0.0)
        else:
            cy = steady(IGF=1.0, Fusion=Fusion, MEKi=0.0, BRD4i=x)
        out.append((round(x, 1), round(cy, 3)))
    return out


def main():
    print("Steady-state proliferation index (Cy), illustrative ODE model\n")
    base_on = steady(1.0, 1.0, 0.0, 0.0)
    base_off = steady(1.0, 0.0, 0.0, 0.0)
    print(f"  Fusion ON, no drug:  Cy={base_on:.3f}")
    print(f"  Fusion OFF, no drug: Cy={base_off:.3f}")

    rows = ["variable,fusion,inhibition,Cy"]
    print("\n--- MEK inhibition dose-response ---")
    for fus, lab in [(1.0, "ON"), (0.0, "OFF")]:
        s = sweep("MEKi", fus, "MEKi")
        print(f"  Fusion {lab}: " + " ".join(f"{x}:{cy}" for x, cy in s))
        for x, cy in s: rows.append(f"MEKi,{lab},{x},{cy}")
    print("    -> Fusion ON is largely MEKi-insensitive (upstream bypass); Fusion OFF is MEKi-sensitive.")

    print("\n--- BRD4 inhibition dose-response ---")
    for fus, lab in [(1.0, "ON"), (0.0, "OFF")]:
        s = sweep("BRD4i", fus, "BRD4i")
        print(f"  Fusion {lab}: " + " ".join(f"{x}:{cy}" for x, cy in s))
        for x, cy in s: rows.append(f"BRD4i,{lab},{x},{cy}")
    print("    -> BRD4i lowers output with a threshold; while fusion term persists it cannot fully zero Cy at <100% inhibition.")

    with open(os.path.join(HERE, "ode_dose_response.csv"), "w") as fh:
        fh.write("\n".join(rows) + "\n")
    print("\n[done] wrote ode_dose_response.csv")


if __name__ == "__main__":
    main()
