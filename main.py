"""Fetches California weather.

Makes an HTTP request to the National Weather Service API to fetch weather alerts for the state of California.
"""

from httpx import get as httpx_get
from time import time as time_time


NWS_CA_WEATHER = "https://api.weather.gov/alerts?area=CA"


def main():
	start = time_time()
	response = httpx_get("https://api.weather.gov/alerts?area=CA")
	response.json()
	end = time_time()
	print("Total time taken: ", (end - start), " s")


if __name__ == '__main__':
	main()
