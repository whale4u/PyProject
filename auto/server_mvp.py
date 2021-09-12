import requests

resp = requests.post("https://sctapi.ftqq.com/SCT74621TNgPAfL0cbFypVMIgwuUaRilK.send",
                     data={"text": "xray vuln alarm", "desp": "This is description!"})
# print(resp.text)
if "SUCCESS" in resp.text:
    print("OK")

# if resp.json()["errno"] != 0:
#     raise ValueError("push ftqq failed, %s" % resp.text)
# else:
#     print("OK!")
