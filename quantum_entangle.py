import qutip as qt
import numpy as np

phase = 1.33022
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 047 Entangled Density Matrix (core: 'sacrifices what I say or people 
Like my piece of shit brother does my wishes not to torment he with his s decisions . Or dark does buying Bitcoin or the girl dies not payinge 92% as her pimp'):")
print(rho)
