# import src.uiipythonapi as uii
import uiipythonapi as uii

api = uii.Client("token here")
packageList, err = api.read_package_list("debian", "10", "x86_64")
print("Number of known packages for Debian 10: " + str(len(packageList)))


def dhcp_network(domain: str = "", ipnet: str = "", gateway: str = "", dns: str = "", nointernet: bool = False):
    return {
        "dhcp": True,
        # "domain": domain,
        # "ipnet": ipnet,
        # "gateway": gateway,
        # "dns": dns,
        "nointernet": False,
    }


def static_network(domain: str = "", ipnet: str = "", gateway: str = "", dns: str = "", nointernet: bool = False):
    return {
        "dhcp": False,
        "domain": domain,
        "ipnet": ipnet,
        "gateway": gateway,
        "dns": dns,
        "nointernet": nointernet,
    }


err = api.build("debian10.iso", "debian", "10", "x86_64", "horst", [dhcp_network()])
print("Errors: " + str(err))
