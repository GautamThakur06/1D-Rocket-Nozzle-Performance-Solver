import numpy as np
from scipy.optimize import fsolve


# INPUT PARAMETERS
Pc = 3.1e6        # Chamber pressure (Pa) - absolute
Tc = 3000         # Chamber temperature (K)
gamma = 1.4
R = 287
Ae_At = 5.76       # Area ratio (change later)
At = 6.86e-5       # Throat area (m^2)
Pa = 101325       # Ambient pressure (Pa)

# AREA-MACH RELATION


def area_mach(M):
    return (1/M)*((2/(gamma+1)*(1+(gamma-1)/2*M**2))**((gamma+1)/(2*(gamma-1))))

def solve_exit_mach():
    func = lambda M: area_mach(M) - Ae_At
    Me = fsolve(func, 2.5)[0]   # Supersonic initial guess
    return Me


# PERFORMANCE CALCULATIONS


Me = solve_exit_mach()

Te = Tc / (1 + (gamma-1)/2 * Me**2)
Pe = Pc * (1 + (gamma-1)/2 * Me**2)**(-gamma/(gamma-1))

ae = np.sqrt(gamma * R * Te)
Ve = Me * ae

mdot = At * Pc * np.sqrt(gamma/(R*Tc)) * \
       ((2/(gamma+1))**((gamma+1)/(2*(gamma-1))))

Ae = Ae_At * At

F = mdot * Ve + (Pe - Pa) * Ae

Cf = F / (Pc * At)
Isp = F / (mdot * 9.81)
if abs(Pe - Pa) < 2000:
    regime = "Ideally Expanded"
elif Pe > Pa:
    regime = "Underexpanded"
else:
    regime = "Overexpanded"
    
import matplotlib.pyplot as plt

ratios = np.linspace(2, 12, 30)
thrust_values = []

for ratio in ratios:
    Ae_At_temp = ratio
    
    func = lambda M: (1/M)*((2/(gamma+1)*(1+(gamma-1)/2*M**2))**((gamma+1)/(2*(gamma-1)))) - Ae_At_temp
    Me_temp = fsolve(func, 2.5)[0]
    
    Te_temp = Tc / (1 + (gamma-1)/2 * Me_temp**2)
    Pe_temp = Pc * (1 + (gamma-1)/2 * Me_temp**2)**(-gamma/(gamma-1))
    ae_temp = np.sqrt(gamma * R * Te_temp)
    Ve_temp = Me_temp * ae_temp
    
    Ae_temp = ratio * At
    F_temp = mdot * Ve_temp + (Pe_temp - Pa) * Ae_temp
    
    thrust_values.append(F_temp)


print("===== Rocket Performance Results =====")
print(f"Exit Mach: {Me:.4f}")
print(f"Exit Temperature (K): {Te:.2f}")
print(f"Exit Pressure (Pa): {Pe:.2f}")
print(f"Exit Velocity (m/s): {Ve:.2f}")
print(f"Mass Flow Rate (kg/s): {mdot:.4f}")
print(f"Thrust (N): {F:.2f}")
print(f"Thrust Coefficient (Cf): {Cf:.4f}")
print(f"Specific Impulse (s): {Isp:.2f}")
print(f"Expansion Regime: {regime}")
plt.plot(ratios, thrust_values)
plt.xlabel("Area Ratio (Ae/At)")
plt.ylabel("Thrust (N)")
plt.title("Thrust vs Area Ratio")
plt.grid(True)
plt.show()
