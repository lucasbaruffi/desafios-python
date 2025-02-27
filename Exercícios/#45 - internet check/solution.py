# apenas para testar a internet

# pip install speedtest-cli

import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f"Download Speed in Mbps: {down_speed}")

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f"Upload Speed in Mbps: {up_speed}")

    ping = test.results.ping
    print(f"Ping: {ping}")
Speed_Test()