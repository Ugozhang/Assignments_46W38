import numpy as np

class GeneralWindTurbine:
    """
    A general trubine model 

    Params:
    ------
    rotor_diameter  (float)
    hub_height      (float)
    rated_power     (float)
    v_in            (float)
    v_rated         (float)
    v_out           (float)
    name            (str) (optional) : Name of turbine
    """

    def __init__(self, rotor_diameter, hub_height, rated_power,
                 v_in, v_rated, v_out, name=None):
        self.rotor_diameter = rotor_diameter
        self.hub_height = hub_height
        self.rated_power = rated_power
        self.v_in = v_in
        self.v_rated = v_rated
        self.v_out = v_out
        self.name = name if name is not None else "General Wind Turbine"

    def get_power(self, v):
        """
        Compute power output

        """

        # vectorize
        v = np.asarray(v)

        # Initialize the Power output vectors as 0, 
        # v < v_in, v > v_out would be default as 0.
        P = np.zeros_like(v, dtype=float)

        # Regions
        idx_in_to_rated = (v >= self.v_in) & (v < self.v_rated)
        idx_rated_to_out = (v >= self.v_rated) & (v < self.v_out)

        # Power
        P[idx_in_to_rated] = self.rated_power * (v[idx_in_to_rated] / self.v_rated) ** 3
        P[idx_rated_to_out] = self.rated_power

        return P
    
class WindTurbine(GeneralWindTurbine):
    """
    Compute Power output by power curve table and its interpolation

    Params:
    ------
    rotor_diameter  (float)
    hub_height      (float)
    rated_power     (float)
    v_in            (float)
    v_rated         (float)
    v_out           (float)
    name            (str) (optional) : Name of turbine
    power_curve_data (np.ndarray) : 2darray of ws-power relation
    """
    def __init__(self, rotor_diameter, hub_height, rated_power,
                 v_in, v_rated, v_out, power_curve_data, name=None):
        super().__init__(rotor_diameter, hub_height, rated_power,
                         v_in, v_rated, v_out, name)
        self.power_curve_data = np.asarray(power_curve_data, dtype=float)
    
    def get_power(self, v):
        """
        Overwrite super() power output with interp of power curve data
        """
        
        v = np.asarray(v, dtype=float)

        ws = self.power_curve_data[:, 0]
        pw = self.power_curve_data[:, 1]

        # interp left and right be 0.0
        P = np.interp(v, ws, pw, left = 0.0, right = 0.0)

        return P