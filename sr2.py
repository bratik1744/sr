from pprint import pprint
from time import sleep
import requests

def f(n, s):
        for i in range(0, 10000):
                a = requests.post(f"https://edu.sirius.online/noo-back/v66.3/course/1289/learn/12491/{n}/solve", headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
                        "Accept": "application/json",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJQUzUxMiJ9.eyJmaXJzdE5hbWUiOiLQlNCw0L3QuNC40LsiLCJlbWFpbCI6InN0dWt1bmRhbmlpbEBnbWFpbC5jb20iLCJwYXJlbnRDb2RlIjoiS2FwOGd6d1hnVndrIiwiaWQiOiIxMDAxMjAwNzAxMTEwMzExOTYiLCJsYXN0TmFtZSI6ItCh0YLRg9C60YPQvSIsImlhdCI6MS42ODYzODIxMTI0NDAzNjY5NjdlOSwibWlkZGxlTmFtZSI6ItCQ0LvQtdC60YHQsNC90LTRgNC-0LLQuNGHIiwicm9sZXMiOlsibm9vUlciXSwiZXhwIjoxLjY4Njk4NjkxMjQ0MDM2Njk2N2U5fQ.rzRDGdlhAJA_awy2PBdqbpejoa9Mx3vRxm7ScasIfkO1xZyvys4qX6T91EAJJWGrkhnXmJrUYnJ8moEIe0AZrk5OM-klnyDadpEsq9S0RpNapbG-EyAXPlWUVAhOfnts0-qhFYRfTt0ymoAcrnE2_zQCq2TmKD3XmqW_KgjRcprUUTDMaZYAdvtVcnFbvbeY7zpBultRaUeZ4ocw56ioYyutaOSYQlJo5Kqj87VRc-5MNaMtLuNoHRKoyb43aE3IG-vFq1xvNfv2iGHqm2UK6PhL4VMeKpuyoOW-8h5vUOGgp8_kYI7M0Y31VsOPlAEGHAjH7heopwvwOLjWZXudUA",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin"}, json=[{"solution":[str(i/s)]}]).json()
                pprint(f"{n} - {i} - {a['verdict']}")
                if a['verdict'] != "wrong":
                        break

fil = open("in.txt", "r")
for i in fil.readlines():
        n, s = map(int, i.rstrip().split())
        f(n, s)