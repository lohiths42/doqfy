from django.db import models
from cryptography.fernet import Fernet
import base64


class Snippet(models.Model):
    content = models.TextField()
    secret_key = models.CharField(max_length=50, blank=True)
    encrypted_content = models.BinaryField(blank=True)
    shareable_url = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Snippet {self.pk}"

    def encrypt_content(self):
        cipher_suite = Fernet(self.secret_key.encode())
        encrypted_content = cipher_suite.encrypt(self.content.encode())
        self.encrypted_content = encrypted_content
        self.content = ""

    def decrypt_content(self):
        cipher_suite = Fernet(self.secret_key.encode())
        decrypted_content = cipher_suite.decrypt(self.encrypted_content).decode()
        self.content = decrypted_content
