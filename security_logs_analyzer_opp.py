class User:

    def __init__(self, username, ip_address, failed_login):
        self.username = username
        self.ip_address = ip_address
        self.failed_login = failed_login

    def show_info(self):
        print("=" * 30)
        print("Username   :", self.username)
        print("IP Address :", self.ip_address)
        print("Attempt    :", self.failed_login)
        print("=" * 30)


class ThreatAnalyzer:

    def calculateScore(self, user):
        return user.failed_login * 10

    def threatLevel(self, user):

        if user.failed_login >= 10:
            return "Critical"

        elif user.failed_login >= 5:
            return "High"

        elif user.failed_login >= 3:
            return "Medium"

        return "Low"


class SecurityReport:

    def generate(self, user, analyzer):

        print("=" * 30)
        print("SECURITY REPORT")
        print("=" * 30)

        print(f"Username   : {user.username}")
        print(f"IP Address : {user.ip_address}")
        print(f"Attempts   : {user.failed_login}")

        print()

        print(
            f"Risk Score : {analyzer.calculateScore(user)}"
        )

        print(
            f"Threat Level : {analyzer.threatLevel(user)}"
        )


user1 = User(
    "admin",
    "192.168.12.2",
    7
)

user2 = User(
    "student",
    "192.168.2.1",
    10
)

analyzer = ThreatAnalyzer()

report = SecurityReport()

report.generate(user1, analyzer)