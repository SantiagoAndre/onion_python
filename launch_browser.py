from selenium import webdriver


def set_proxy(ip, port):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', ip)
    profile.set_preference('network.proxy.socks_port', port)
    profile.set_preference('network.proxy.socks_version', 5)
    profile.set_preference('network.proxy.socks_remote_dns', True)
    profile.update_preferences()
    return profile
if __name__ == '__main__':
	ipTor='127.0.0.1'
	SOCKSPort = 9050 #of file  tor_port
	proxy=set_proxy(ipTor, SOCKSPort)
	driver = webdriver.Firefox(firefox_profile=proxy)
	driver.get('http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page')
