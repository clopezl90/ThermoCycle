from .equipment import Equipment

class Aaa(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.work = 0
        self.heat = 0

    def calculate(self):
        self.heat = self.enthalpy_balance
        #This divice has 2 inlet and 2 outlet. Setting them according to the cycle:

        property2 = self.properties_in[0]
        property7 = self.properties_in[1]

        property3 = self.properties_out[0]
        property9 = self.properties_out[1]

        #Setting mass flow rates and enthalpies.

        m2 = property2.mass_flow_rate
        h2 = property2.H

        m7 = property7.mass_flow_rate
        h7 = property7.H
        h9 = property9.H

        #Here, I assumed that point 9 is defined and p3 is the one to be calculated.
        h3 = h2 + (m7 / m2) * (h7 - h9)

        property3.set_mass_flow_rate(m2)
        property3.set_enthalpy(h3)