To run:

Assumes windows for chime. For mac, please replace winsound with an equivalent library.

1. Install python (3.6 or greater) locally
1. Run `pip install requests` in a command prompt
1. Copy check_stock.py to whatever folder you'd like to use in the command prompt
1. Update the zip code in check_stock.py
1. Run `python check_stock.py <name_of_item>`, where `<name_of_item>` is `ps5`, `ps5-digital`, `xbox-series-x`, `xbox-series-s`, or `dualsense`

To check other items, add the tcin number to the mapping in the check stock file. You can find the number easily by going to the product page in
the store website, and checking the URL.

I added dualsense so you can test and fiddle with the chime settings to get something you like.
