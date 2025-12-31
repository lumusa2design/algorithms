import numpy as np

class kalman1D_velocity:
    def __init__(self, time_interval: float, position=(0.0, 0.0), variance=1.0, noise=1.0, sense_noise=1.0):
        self.time_interval = float(time_interval)

        self.transition_matrix = np.array([[1.0, self.time_interval],
                                           [0.0, 1.0]], dtype=float)

        self.observation_matrix = np.array([[1.0, 0.0]], dtype=float)

        time_interval = self.time_interval
        self.noise_variance = float(noise) * np.array([[time_interval**4 / 4.0, time_interval**3 / 2.0],
                                                       [time_interval**3 / 2.0, time_interval**2]], dtype=float)

        self.sense_noise = np.array([[float(sense_noise)]], dtype=float)

        self.state = np.array([[float(position[0])],
                               [float(position[1])]], dtype=float)

        self.variance = np.eye(2, dtype=float) * float(variance)
        self.identity_matrix = np.eye(2, dtype=float)

    def step(self, measure: float):
        measure = np.array([[float(measure)]], dtype=float)

        state_pred = self.transition_matrix @ self.state
        variance_pred = self.transition_matrix @ self.variance @ self.transition_matrix.T + self.noise_variance

        innovation = measure - (self.observation_matrix @ state_pred)
        innovation_var = self.observation_matrix @ variance_pred @ self.observation_matrix.T + self.sense_noise
        kalman_gain = variance_pred @ self.observation_matrix.T @ np.linalg.inv(innovation_var)

        self.state = state_pred + kalman_gain @ innovation
        self.variance = (self.identity_matrix - kalman_gain @ self.observation_matrix) @ variance_pred

        return self.state


if __name__ == "__main__":
    dt = 1/30
    measurements = [100, 102, 105, 103, 110, 111, 109, 112]

    kf = kalman1D_velocity(time_interval=dt, position=(measurements[0], 0.0), variance=10.0, noise=5.0, sense_noise=9.0)

    for z in measurements:
        state_hat = kf.step(z)
        print(f"z={z:6.2f} -> poŝ={state_hat[0,0]:7.3f}   vel̂={state_hat[1,0]:7.3f}")
