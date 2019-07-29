

class PIDController:
    def __init__(self, kp = 0.0, ki = 0.0, kd = 0.0, max_windup = 10):
        #TODO
        self.kp_ = float(kp)
        self.ki_ = float(ki)
        self.kd_ = float(kd)

        #Store relevant data
        self.last_time_stamp_ = 0.0
        self.set_point_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ = 0.0
        self.max_windup_ = float(max_windup)

        #Control effor history
        self.u_p = [0]
        self.u_i = [0]
        self.u_d = [0]
 
    def reset(self):
        #TODO
        self.kp_ = float(kp)
        self.ki_ = float(ki)
        self.kd_ = float(kd)

        #Store relevant data
        self.last_time_stamp_ = 0.0
        self.set_point_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ = 0.0
        self.max_windup_ = float(0)

        #Control effor history
        self.u_p = [0]
        self.u_i = [0]
        self.u_d = [0]

    def setTarget(self, target):
        #TODO
        self.set_point_ = float(target)

    def setKP(self, kp):
        #TODO
        self.kp_ = float(kp)

    def setKI(self, ki):
        #TODO
        self.ki_ = float(ki)

    def setKD(self, kd):
        #TODO
        self.kd_ = float(kd)

    def setMaxWindup(self, max_windup):
        #TODO
        self.max_windup_ = float(max_windup)

    def update(self, measured_value, timestamp):
        #TODO
        delta_time = timestamp - self.last_time_stamp_
        if delta_time == 0:
            return 0
        #else
        error = self.set_point_ = measured_value
        self.last_time_stamp_ = timestamp
        self.error_sum_ +=  error*delta_time
        delta_error = self.last_error_ - error
        self.last_error_ = error

        # Addressing windup
        if self.error_sum_ > self.max_windup_:
            self.error_sum_ = self.max_windup_
        elif self.error_sum_ < -self.max_windup_:
            self.error_sum_ = -self.max_windup_

        p = self.kp_ * error
        i = self.ki_ * self.error_sum_
        d = self.kd_ * (delta_error/delta_time)

        u = p + i + d # controller effort

        self.u_p.append(p)
        self.u_i.append(i)
        self.u_d.append(d)

        return u

