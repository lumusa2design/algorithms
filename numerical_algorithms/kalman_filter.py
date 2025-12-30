import numpy as np
class kalman1D:
    def __init__(self, state:float, variance:float, noise:float, sense_noise:float):
        self.state = state
        self.variance = variance
        self.noise = noise
        self.sense_noise = sense_noise
    
    def step(self, measure:float) -> float:
        measure= np.array(measure)

        state_pred = self.state
        variance_pred = self.variance + self.noise

        innovaiton = float(measure ) - state_pred
        innovaiton_var = variance_pred + self.sense_noise
        kalmans_gain = variance_pred / innovaiton_var

        self.state = state_pred + kalmans_gain * innovaiton
        self.variance = (1 - kalmans_gain) * variance_pred
        return self.state
    

if __name__ == "__main__":
    kf = kalman1D(state=0.0, variance=1.0, noise=0.1, sense_noise=0.5)
    measurements = [1.0, 2.0, 3.0, 2.5, 3.5]
    for measure in measurements:
        estimate = kf.step(measure)
        print(f"Measurement: {measure}, Estimate: {estimate}")
