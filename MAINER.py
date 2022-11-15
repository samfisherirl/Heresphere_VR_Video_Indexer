import input_json
import json
import selenium_deploy as S

lg = input_json.jhandler()

window = input_json.login(lg)
input_json.closer(window)

pw = S.Browser("https://www.eporner.com/login/", "")  # create object
pw.navigate()  # nav to above url to login
S.login(lg)  # use username and password to login
vr = S.Browser(lg[3], "video-")
# goto videos page
vr.navigate()
array = vr.getlinks()
# return individual video page links
val = S.buildclass(array)
# click download button to expand video dl links, then find highest resolution
S.writer(val)
# append video download links to url
S.driver.quit()
