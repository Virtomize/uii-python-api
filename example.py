""" Example for the usage of the UII python API package """
import uiipythonapi as uii

api = uii.Client("token here")
packageList, err = api.read_package_list("debian", "10", "x86_64")
print("Number of known packages for Debian 10: " + str(len(packageList)))


def dhcp_network():
    """ Example of how to define a dynamic network """
    return {
        "dhcp": True,
        "nointernet": False,
    }


def static_network(domain: str = "",
                   ip_net: str = "",
                   gateway: str = "",
                   dns: str = "",
                   no_internet: bool = False):
    """ Example of how to define a static network """
    return {
        "dhcp": False,
        "domain": domain,
        "ipnet": ip_net,
        "gateway": gateway,
        "dns": dns,
        "nointernet": no_internet,
    }


error = api.build("debian10.iso", "debian", "10", "x86_64", "horst", [dhcp_network()])
print("Errors: " + str(error))
