import requests

url = 'http://localhost:5000/api/donations'
data = {
    'donorName': 'Test User',
    'amount': '500',
    'email': 'test@example.com',
    'phone': '1234567890',
    'address': 'Test Address',
    'scheme': 'Test Scheme'
}
# We need to send a file for 'screenshot' as the backend expects it keys 'screenshot' in request.files
# But if it's missing, my code in app.py says:
# if 'screenshot' in request.files: ... else: ...
# So standard JSON/form might fall through to the else?
# Wait, if I send multipart without file, it might go to 'else' but request.json will be None?
# Let's test providing a dummy file.

files = {'screenshot': ('test.txt', b'dummy content')}

try:
    response = requests.post(url, data=data, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
