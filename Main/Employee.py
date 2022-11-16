class Employee:
    id_: int
    firstname: str
    lastname: str
    rate: float
    hours: float
    reg: float
    ot: float
    gross: float
    fed: float
    state: float
    fica: float
    net: float

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def set_id(self, id_):
        self.id_ = id_

    def get_id(self):
        return self.id_

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_rate(self, rate):
        self.rate = rate

    def get_rate(self):
        return self.rate

    def set_hours(self, hours):
        self.hours = hours

    def get_hours(self):
        return self.hours

    def set_reg(self, rate, hours):
        if hours >= 40:
            self.reg = round(40 * rate, 2)
        else:
            self.reg = round(rate * hours, 2)

    def get_reg(self):
        return self.reg

    def set_ot(self, rate, hours):
        if hours > 40:
            self.ot = round((hours - 40) * rate * 1.5, 2)
        else:
            self.ot = 0

    def get_ot(self):
        return self.ot

    def set_gross(self, rate, hours):
        if hours > 40:
            reg = 40 * rate
            ot = (hours - 40) * rate * 1.5
            self.gross = round(reg + ot, 2)
        else:
            self.gross = round(rate * hours, 2)

    def get_gross(self):
        return self.gross

    def set_fed(self, rate, hours):
        if hours > 40:
            reg = 40 * rate
            ot = (hours - 40) * rate * 1.5
            self.fed = round((reg + ot) * 0.1, 2)
        else:
            self.fed = round((rate * hours) * 0.1, 2)

    def get_fed(self):
        return self.fed

    def set_state(self, rate, hours):
        if hours > 40:
            reg = 40 * rate
            ot = (hours - 40) * rate * 1.5
            self.state = round((reg + ot) * 0.06, 2)
        else:
            self.state = round((rate * hours) * 0.06, 2)

    def get_state(self):
        return self.state

    def set_fica(self, rate, hours):
        if hours > 40:
            reg = 40 * rate
            ot = (hours - 40) * rate * 1.5
            self.fica = round((reg + ot) * 0.03, 2)
        else:
            self.fica = round((rate * hours) * 0.03, 2)

    def get_fica(self):
        return self.fica

    def set_net(self, rate, hours):
        if hours > 40:
            reg = 40 * rate
            ot = (hours - 40) * rate * 1.5
            tax = (reg + ot) * 0.19
            self.net = round((reg + ot) - tax, 2)
        else:
            reg = rate * hours
            tax = reg * 0.19
            self.net = round(reg - tax, 2)

    def get_net(self):
        return self.net

    def __str__(self):
        fullname = self.get_firstname() + " " + self.get_lastname()

        return (
            "{:>15} {:>15.0f} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f}".format
            (fullname, self.get_hours(), self.get_rate(), self.get_reg(), self.get_ot(),
             self.get_gross(), self.get_fed(), self.get_state(), self.fica, self.net))
