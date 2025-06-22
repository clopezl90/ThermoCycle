from .equipment import Equipment

class MixingChamber(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.work = 0
        self.heat = 0

    def calculate(self):
        self.heat = self.enthalpy_balance
        #Mass flow rate definition
        mout=0
        for property in self.properties_in:
            mout = mout + property.mass_flow_rate
        #Enthalpy definition and for loop for calculation of energy with mass and enthalpy
        hout=0
        for property in self.properties_in:
            hout = hout + (property.mass_flow_rate * property.H)


        enthalpy = hout / mout


        prop_out = self.properties_out[0]
        prop_out.set_mass_flow_rate(mout)
        prop_out.set_enthalpy(enthalpy)




