from src.thermoProperty import ThermoProperty
from src.connector import Connector
from src.equipment.turbine import Turbine
from src.equipment.heater import Heater
from src.equipment.condenser import Condenser
from src.equipment.pump import Pump
from src.equipment.mixingchamber import MixingChamber
from src.equipment.aaa import Aaa
from src.thermoCycle import ThermoCycle

fluid = "Water"
water_mass_flow_rate = 1.0  # kg/s

#Here, I assumed that turbine delivers half of flow rate to heat exchanger and to condenser. So more after, mass
#conservation has to be mantained

prop_1 = ThermoProperty("point_1", fluid)
prop_1.set_mass_flow_rate(water_mass_flow_rate/2)
prop_1.set_pressure(20e3)
prop_1.set_temperature(35)

prop_2 = ThermoProperty("point_2", fluid)
prop_2.set_mass_flow_rate(water_mass_flow_rate/2)
prop_2.set_pressure(3e6)
prop_2.set_temperature(35)

prop_3 = ThermoProperty("point_3", fluid)
prop_3.set_mass_flow_rate(water_mass_flow_rate/2)
prop_3.set_pressure(3e6)
prop_3.set_temperature(120)

prop_4 = ThermoProperty("point_4", fluid)
prop_4.set_mass_flow_rate(water_mass_flow_rate/2)
prop_4.set_pressure(6e6)
prop_4.set_temperature(120)

prop_5 = ThermoProperty("point_5", fluid)
prop_5.set_mass_flow_rate(water_mass_flow_rate)
prop_5.set_pressure(6e6)
prop_5.set_temperature(180)

prop_6 = ThermoProperty("point_6", fluid)
prop_6.set_mass_flow_rate(water_mass_flow_rate)
prop_6.set_pressure(6e6)
prop_6.set_temperature(400)

prop_7 = ThermoProperty("point_7", fluid)
prop_7.set_mass_flow_rate(water_mass_flow_rate/2)
prop_7.set_pressure(20e5)
prop_7.set_temperature(180)

prop_8 = ThermoProperty("point_8", fluid)
prop_8.set_mass_flow_rate(water_mass_flow_rate/2)
prop_8.set_pressure(2e5)
prop_8.set_temperature(45)

prop_9 = ThermoProperty("point_9", fluid)
prop_9.set_mass_flow_rate(water_mass_flow_rate/2)
prop_9.set_pressure(3e6)
prop_9.set_temperature(85)

pipe_1 = Connector("pipe_1")  # AAA to pump 2
pipe_1.set_properties_in(prop_3)
pipe_1.set_properties_out(prop_3)

pipe_2 = Connector("pipe_2")  # pump 2 to mixer
pipe_2.set_properties_in(prop_4)
pipe_2.set_properties_out(prop_4)

pipe_3 = Connector("pipe_3")  # condenser to pump 1
pipe_3.set_properties_in(prop_1)
pipe_3.set_properties_out(prop_1)

pipe_4 = Connector("pipe_4")  # pump1 to heat exc.
pipe_4.set_properties_in(prop_2)
pipe_4.set_properties_out(prop_2)

pipe_5 = Connector("pipe_5")  # mixing chamber to heater
pipe_5.set_properties_in(prop_5)
pipe_5.set_properties_out(prop_5)

pipe_6 = Connector("pipe_6")  # heater to turbine
pipe_6.set_properties_in(prop_6)
pipe_6.set_properties_out(prop_6)

pipe_7 = Connector("pipe_7")  # turbine to heat exc
pipe_7.set_properties_in(prop_7)
pipe_7.set_properties_out(prop_7)

pipe_8 = Connector("pipe_8")  # turbine to condenser
pipe_8.set_properties_in(prop_8)
pipe_8.set_properties_out(prop_8)

pipe_9 = Connector("pipe_9")  # heat exc to mixer
pipe_9.set_properties_in(prop_9)
pipe_9.set_properties_out(prop_9)


heater = Heater("heater")
turbine = Turbine("turbine")
condenser = Condenser("condenser")
#new pump is added using the same class
pump = Pump("pump")
pump2 = Pump("pump2")
#chamber and heat exchanger created
mixingchamber = MixingChamber("mixingchamber")
aaa = Aaa("aaa")

heater.add_connectors_in(pipe_5)
heater.add_connectors_out(pipe_6)

turbine.add_connectors_in(pipe_6)
turbine.add_connectors_out(pipe_7)
turbine.add_connectors_out(pipe_8)

condenser.add_connectors_in(pipe_8)
condenser.add_connectors_out(pipe_1)

pump.add_connectors_in(pipe_1)
pump.add_connectors_out(pipe_2)

pump2.add_connectors_in(pipe_3)
pump2.add_connectors_out(pipe_4)

mixingchamber.add_connectors_in(pipe_4)
mixingchamber.add_connectors_in(pipe_9)
mixingchamber.add_connectors_out(pipe_5)

aaa.add_connectors_in(pipe_2)
aaa.add_connectors_in(pipe_7)
aaa.add_connectors_out(pipe_3)
aaa.add_connectors_out(pipe_9)

rankine_power_cycle = ThermoCycle()
rankine_power_cycle.add_equipment(pump)
rankine_power_cycle.add_equipment(pump2)
rankine_power_cycle.add_equipment(heater)
rankine_power_cycle.add_equipment(turbine)
rankine_power_cycle.add_equipment(condenser)
rankine_power_cycle.add_equipment(mixingchamber)
rankine_power_cycle.add_equipment(aaa)

rankine_power_cycle.initialize()
rankine_power_cycle.calculate()
rankine_power_cycle.calculate_efficiency()
rankine_power_cycle.draw("app_aula.png")
