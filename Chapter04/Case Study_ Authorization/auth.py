import hashlib

class User:
    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""
        self.username = username
        # self.passord =

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        has_string = self.username + password
        hash_string = has_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
