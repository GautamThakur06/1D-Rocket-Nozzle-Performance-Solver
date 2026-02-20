1D Isentropic Rocket Nozzle Performance Solver

Overview

This project presents an analytical 1D compressible flow solver developed in Python to evaluate the performance of a converging–diverging rocket nozzle under steady, isentropic conditions.

The solver predicts exit flow properties and evaluates thrust performance across varying area ratios.

⸻

Objectives
	•	Compute exit Mach number using the area–Mach relation
	•	Evaluate exit temperature and pressure
	•	Calculate mass flow rate
	•	Determine thrust and thrust coefficient
	•	Compute specific impulse (Isp)
	•	Classify expansion regime (underexpanded / overexpanded / ideally expanded)
	•	Analyze thrust variation with area ratio

⸻

Governing Relations

The solver is based on classical compressible flow equations:

Area–Mach Relation

Solved numerically using scipy.optimize.fsolve.

Isentropic Temperature & Pressure Relations

Thrust Equation

F = ṁVe + (Pe − Pa)Ae

⸻

Assumptions
	•	One-dimensional flow
	•	Steady flow
	•	Isentropic process
	•	Ideal gas behavior
	•	Constant specific heat ratio

⸻

Results

The solver generates thrust variation across different exit-to-throat area ratios
![Thrust vs Area Ratio](results/thrust_vs_area_ratio.png)
