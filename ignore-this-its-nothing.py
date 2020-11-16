from requests_html import HTMLSession

#base_url = ('https://www.walmart.com/ip/TSV-PS4-Controller-Dual-Shock-Skin-Grip-Anti-slip-Silicone-Cover-Protector-Case-for-Sony-PS4-PS4-Slim-PS4-Pro-Controller-8-Thumb-Grips/304160322')
base_url = ('https://www.walmart.com/ip/PlayStation-5-Console/363472942')
session = HTMLSession()
r = session.get(base_url)
#yo = r.html.find('.prod-ProductCTA')
yo = r.html.find('span')
print(yo)