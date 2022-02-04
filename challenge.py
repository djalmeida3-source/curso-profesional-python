from __future__ import division


def make_division_by(n):
    def division(m):
        return m/n
    return division

def run():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)
    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))
    print(division_by_3(division_by_5(200)))

if __name__ == "__main__":
    run()