"""
weather_demo.py
Fetch hourly temperature from Open‑Meteo and print the first timestamp + temp.
Works with 'requests' if installed; otherwise falls back to urllib.
"""
import json
import sys

URL = "https://api.open-meteo.com/v1/forecast?latitude=35.4689&longitude=-97.52&hourly=temperature_2m"

def fetch_with_urllib(url):
    from urllib.request import urlopen
    with urlopen(url) as resp:
        return resp.read().decode("utf-8")

def fetch_with_requests(url):
    import requests
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text

def main():
    # Try requests first; if missing, fall back.
    try:
        text = fetch_with_requests(URL)
    except Exception:
        text = fetch_with_urllib(URL)
    data = json.loads(text)

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    if not times or not temps:
        print("No hourly data returned.")
        sys.exit(1)
    print(f"First reading: {times[0]} -> {temps[0]} °C")
    # Bonus: print current (nearest) reading by comparing to current hour.
    # (Simplified: we just print the first 5 readings)
    print("Next few readings:")
    for t, temp in list(zip(times, temps))[:5]:
        print(f"  {t}  {temp} °C")

if __name__ == "__main__":
    main()