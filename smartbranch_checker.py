EXPECTED_VLANS = {
    10: ("EMPLOYEE", "192.168.10.0/24", "192.168.10.1"),
    20: ("GUEST", "192.168.20.0/24", "192.168.20.1"),
    30: ("SERVER", "192.168.30.0/24", "192.168.30.1"),
    99: ("MANAGEMENT", "192.168.99.0/24", "192.168.99.1"),
}

DEVICES = {
    "SERVER1": "192.168.30.10",
    "MGMT-PC": "192.168.99.10",
    "GUEST-LAP1": "192.168.20.11",
    "GUEST-LAP2": "192.168.20.12",
    "EMP-PC1": "192.168.10.11",
    "EMP-PC2": "192.168.10.12",
    "EMP-PC3": "192.168.10.13",
    "EMP-PC4": "192.168.10.14",
    "EMP-PC5": "192.168.10.15",
    "EMP-PC6": "192.168.10.16",
    "EMP-PC7": "192.168.10.17",
    "EMP-PC8": "192.168.10.18",
}

def check_vlans():
    print("\n--- VLAN VALIDATION ---")
    ok = True
    for vlan, (name, subnet, gateway) in EXPECTED_VLANS.items():
        if name:
            print(f"[PASS] VLAN {vlan} - {name}")
        else:
            print(f"[FAIL] VLAN {vlan} has no name")
            ok = False
    return ok

def check_gateways():
    print("\n--- GATEWAY VALIDATION ---")
    ok = True
    for vlan, (_, _, gateway) in EXPECTED_VLANS.items():
        if gateway == f"192.168.{vlan}.1":
            print(f"[PASS] VLAN {vlan} Gateway: {gateway}")
        else:
            print(f"[FAIL] VLAN {vlan} Gateway: {gateway}")
            ok = False
    return ok

def check_subnets():
    print("\n--- SUBNET VALIDATION ---")
    ok = True
    for vlan, (_, subnet, _) in EXPECTED_VLANS.items():
        expected = f"192.168.{vlan}.0/24"
        if subnet == expected:
            print(f"[PASS] VLAN {vlan} Subnet: {subnet}")
        else:
            print(f"[FAIL] VLAN {vlan} Subnet: {subnet}")
            ok = False
    return ok

def check_duplicate_ips():
    print("\n--- IP ADDRESS VALIDATION ---")
    seen = {}
    ok = True
    for device, ip in DEVICES.items():
        if ip in seen:
            print(f"[FAIL] Duplicate IP {ip}: {seen[ip]} and {device}")
            ok = False
        else:
            seen[ip] = device
    if ok:
        print("[PASS] No duplicate IP addresses found.")
    return ok

def main():
    print("=" * 45)
    print(" SmartBranch 360 Network Checker")
    print("=" * 45)
    results = [check_vlans(), check_gateways(), check_subnets(), check_duplicate_ips()]
    print("\n" + "=" * 45)
    print(" RESULT: NETWORK PLAN VALID" if all(results)
          else " RESULT: CONFIGURATION PROBLEMS FOUND")
    print("=" * 45)

if __name__ == "__main__":
    main()
