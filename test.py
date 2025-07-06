import requests
from amocrm.v2 import tokens

# Устанавливаем дефолтный менеджер токенов (не возвращает объект)
tokens.default_token_manager(
    client_id="c01ffeea-9bbd-4efe-83fd-ae25ae3335c9",
    client_secret="U1ROdUISrn1zxva95gZNHVFTqyvo9AB4PqsbMqQAsaTb6QvvHBjFNvtGLI5Zwh9T",
    subdomain="vbr07",
    redirect_url="https://dompluse.com/",
)

# Получаем установленный менеджер из внутреннего поля
token_manager = tokens.default_token_manager

# Получаем токен
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImRjNWUxMzMyNTc1MmVlMDdhMGI3NDkzOTdkODVkN2RiNzI4Y2IzNzI2OThkODgxMGJjNjU5YWQzNzNiMDE0ZjMwOTZlMDA2M2Y0MTA5NWNmIn0.eyJhdWQiOiJjMDFmZmVlYS05YmJkLTRlZmUtODNmZC1hZTI1YWUzMzM1YzkiLCJqdGkiOiJkYzVlMTMzMjU3NTJlZTA3YTBiNzQ5Mzk3ZDg1ZDdkYjcyOGNiMzcyNjk4ZDg4MTBiYzY1OWFkMzczYjAxNGYzMDk2ZTAwNjNmNDEwOTVjZiIsImlhdCI6MTc1MTY2NDIyMSwibmJmIjoxNzUxNjY0MjIxLCJleHAiOjE3NTE3NTA2MjEsInN1YiI6IjExMDAwMjk4IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxNzI4NTE4LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYjYxNDgzZDEtYmNmYy00MzRkLWExYjItNjQwNWYzZThlZjgwIiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.TuZzwZ2gzYhl3Eo-QM-edtlxc52plK2RXOqWKRRDARMy8zhBsnC1mMf733mLV_Z2WQrEPtALFVMobpzQY3i3VKNEm5YFopIiBnlFWEL_EeTSqnTEXVkX3l_xfXu87_9-p0E-BLp5Wit5ayGps2K33LOVcmyzFYYu2GOtmUAnQrXOS8QDKhAiWyisv93kdc4Ngp8N3VLe2_PE-Gr9y8gFm5oNCEhdyNI5sQGTwlCP1qk9zx95HUUakcOU8xzDltcLWrlqoA4kOMuYKLjztwBNi0P32Opa9pyDQliYN0_dRPRY4VqtSr2HfjDexzyQvBi21bopX1GmtsAnqgiSllHnoA"


headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

url = f"https://{token_manager.subdomain}.amocrm.ru/api/v4/leads/custom_fields"

response = requests.get(url, headers=headers)
response.raise_for_status()

custom_fields = response.json()['_embedded']['custom_fields']

print("Все кастомные поля сделок:")
for field in custom_fields:
    print(f"- {field['name']} (id: {field['id']}), required: {field.get('required', False)}")

