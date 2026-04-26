import socket

def scan_port(ip, port):
    # একটি সকেট তৈরি করছি
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # ১ সেকেন্ডের মধ্যে রেসপন্স না পেলে টাইমআউট হবে
    
    # পোর্টটি ওপেন আছে কি না তা চেক করছি
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    s.close()

# আপনার পিসির বা লোকাল নেটওয়ার্কের আইপি এখানে দিন
target_ip = "127.0.0.1" 
scan_port(target_ip, 80)
