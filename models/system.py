#Entrada dos valores: fsw, ΔV, Vdc, Vin, potencia

class Values:
    def __init__(self):
        self._fsw = None
        self._delta_i = None
        self._bus_voltage = None
        self._input_voltage = None
        self._power = None
    
    @property
    def fsw(self):
        return self._fsw
    
    @fsw.setter
    def fsw(self, value):
        if value <= 0:
            raise ValueError("Only positive values")
        self._fsw = value


    @property
    def delta_i(self):
        return self._delta_i
    
    @delta_i.setter
    def delta_i(self, value):
        if value <= 0:
            raise ValueError("Only positive values")
        
        self._delta_i = value


    @property
    def bus_voltage(self):
        return self._bus_voltage
    
    @bus_voltage.setter
    def bus_voltage(self, value):
        if value <= 0:
            raise ValueError("Only positive values")

        self._bus_voltage = value
    

    @property
    def input_voltage(self):
        return self._input_voltage
    
    @input_voltage.setter
    def input_voltage(self, value):
        if value <= 0:
            raise ValueError("Only positive values")
        
        self._input_voltage = value
    

    @property
    def power(self):
        return self._power    
    
    @power.setter
    def power(self, value):
        if value <= 0:
            raise ValueError("Only positive values")
        
        self._power = value
