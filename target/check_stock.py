# Replace "00000" with your zip code on line 16
# Adjust chime settings to taste; test with dualsense
# Run with command:
# python check_stock.py ps5
# python check_stock.py ps5-digital
# python check_stock.py xbox-series-x
# python check_stock.py xbox-series-s
# python check_stock.py dualsense

import datetime
import requests
import sys
import time
import winsound

YOUR_ZIP_CODE = 00000
TCINs = {
    "ps5": 81114595,
    "ps5-digital": 81114596,
    "xbox-series-x": 80790841,
    "xbox-series-s": 80790842,
    "dualsense": 81114477 # Use to test the chime / zip, it's almost always in stock
}

FREQUENCY = 500
CHIME_DURATION = 200
CHIME_GAP = 200
CHIME_COUNT = 5

LOCATIONS_LINK = "https://api.target.com/fulfillment_aggregator/v1/fiats/{tcin}?key=ff457966e64d5e877fdbad070f276d18ecec4a01&nearby={zip}&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test"

def makeReq(tcin):
    r = requests.get(LOCATIONS_LINK.format(tcin=tcin, zip=YOUR_ZIP_CODE))
    return r.text

def checkAvailability(tcin):
    while True:
        data = makeReq(tcin)
        print(datetime.datetime.now())
        if 'IN_STOCK' in data:
            doChime()
            break
        time.sleep(0.5)
    
def isInStock(store):
    if store['order_pickup']['availability_status'] != "OUT_OF_STOCK":
        print(store)
        return True
    elif store['order_pickup']['reason_code'] != "OUT_OF_STOCK":
        print(store)
        return True
    elif store['in_store_only']['availability_status'] != "OUT_OF_STOCK":
        print(store)
        return True
    elif store['ship_to_store']['availability_status'] != "UNAVAILABLE":
        print(store)
        return True
    return False



def doChime():
    for i in range(CHIME_COUNT):
        winsound.Beep(FREQUENCY, CHIME_DURATION)
        time.sleep(float(CHIME_GAP) / 1000.0)

if __name__ == '__main__':
    console = sys.argv[1] if len(sys.argv) > 1 else "ps5"
    tcin = TCINs[console]
    checkAvailability(tcin)
    print("Caught stock for %s" % console)
