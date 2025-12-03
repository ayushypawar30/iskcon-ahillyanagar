import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'backend'))
from app import app
import json

def test_endpoint():
    print("Testing /api/orders/ORD-1764684942089")
    with app.test_client() as client:
        try:
            response = client.get('/api/orders/ORD-1764684942089')
            print(f"Status: {response.status_code}")
            print(f"Data: {response.data.decode()}")
        except Exception as e:
            print(f"CRASH: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_endpoint()
