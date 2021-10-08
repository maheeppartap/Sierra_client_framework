import os
import string
from abc import ABC

import meraki
import meraki_v0

from AP_Handler import APHandler
from AP_Handler import security_options


class MR45(APHandler, ABC):
    """
       Each device can have the following attributes updated:
       - networkId (string)
       - number (string)
       - name (string): The name of the SSID
       - enabled (boolean): Whether or not the SSID is enabled
       - authMode (string): The association control method for the SSID ('open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius' or 'ipsk-without-radius')
       - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
       - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
       - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
       - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only')
       - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth' or 'Sponsored guest'). This attribute is not supported for template children.
       - radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
       - radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
       - radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
       - radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
       - radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
       - radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
       - radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
       - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a concentrator' or 'VPN')
       - useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
       - concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
       - vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
       - defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
       - apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
       - walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
       - walledGardenRanges (string): Specify your walled garden by entering space-separated addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. 192.168.1.1/24 192.168.37.10/32 www.yahoo.com *.google.com). Meraki's splash page is automatically included in your walled garden.
       - radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
       - minBitrate (number): The minimum bitrate in Mbps. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
       - bandSelection (string): The client-serving radio frequencies. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
       - perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
       - perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
       - lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
       - visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
       - availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
       - availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
       """

    def __init__(self, Serial: str = None):
        super().__init__()
        # assert Serial is not None, "Serial of device cannot be None!"
        # self.serial = Serial

        # api_key, make sure it's an environment variable
        self.api_key = os.environ.get("MERAKI_API_KEY")

        # self.list_of_devices = self.get_list_of_devices(API_KEY=self.api_key)

    def update_device(self, network_id: str = None, number: int = None, API_KEY: str = None,
                      suppress_logging: bool = False,
                      **kwargs):
        """
         Sends an update to merak cloud to update device. The update will consist of items specified in **kwargs.
         **kwargs should be made up of the above list of items ONLY
        :param network_id: What network the device is on
        :param number: What index that device was on the list of get_list_devices() call
        :param API_KEY: API Key the network is connected to
        :param suppress_logging:Not recommended, but the meraki's logging directory change feature is broken. So if you
        don't want to debug, use this
        :return:
        """
        assert self.api_key is not None, f'''API_KEY cannot be empty'''

        print("kawargs are: ", kwargs)
        legacy_dashboard = meraki_v0.DashboardAPI(self.api_key, suppress_logging=suppress_logging)
        legacy_dashboard.ssids.updateNetworkSsid(networkId=network_id,
                                                 number=number,
                                                 **kwargs
                                                 )

    def _change_security(self, sec: security_options):
        sec_options = {
            # todo: make a dictionary here for all security types. Look into how the original API worked for help
        }

    def _change_ssid(self, SSID: string):
        raise NotImplementedError()

    @staticmethod
    def _verify_config(config: dict) -> bool:
        # todo: check if device exists. The device's name will be highest level in the dictionary tree
        #  call get_list_devices to check if device exists
        print("verifying: ", config)
        return True

    def _unpack_data(self, raw_data: dict):
        print(f'Unpacking: {raw_data}')
        api_data = {}
        for field in raw_data.keys():
            if field == "SSID":
                api_data['name'] = raw_data.get(field)
            if field == "security":
                api_data['wpaEncryptionMode'] = raw_data.get(field)
            if field == "key":
                api_data['psk'] = raw_data.get(field)
            if field == "bitrate":
                api_data['bitrate'] = raw_data.get(field)
        return api_data

    def _create_config(self, raw_data: dict):
        api_conforming_data = self._unpack_data(raw_data)
        self.update_device(network_id=raw_data['networkID'],
                           number=0,
                           API_KEY=os.environ.get("MERAKI_API_KEY"),
                           **api_conforming_data
                           )

    @staticmethod
    def get_list_of_devices(organization: str = None,
                            API_KEY=os.environ.get("MERAKI_API_KEY"),
                            network: str = None,
                            suppress_logging: bool = False):
        """
        Will return list of devices in organization's network
        :param organization: What organization to look for in case more than one is handled with API key. Ignored if
        only one organization
        :param network: What network to look for devices on, cannot be None
        :param API_KEY: Used to get all organizations
        :param suppress_logging: Not recommended, but the meraki's logging directory change feature is broken. So if you don't want to debug, use this
        :return: List of Devices
        """
        assert API_KEY is not None, "API_key param cannot be empty"
        assert network is not None, "Network param cannot be empty"

        dashboard = meraki.DashboardAPI(api_key=API_KEY, suppress_logging=suppress_logging)

        list_orgs = dashboard.organizations.getOrganizations()
        assert list_orgs is not None, "No organizations are tied to your API key."

        curr_org_id = None
        if len(list_orgs) == 1:
            curr_org_id = list_orgs[0]['id']
        else:
            assert organization is not None, "Multiple organizations are tied to your API key, pass in the organization"
            for orgs in list_orgs:
                if orgs['name'] == organization:
                    curr_org_id = orgs['id']
                    break
            assert curr_org_id is not None, f'''Could not find given organization:"{organization}"'''

        list_networks = dashboard.organizations.getOrganizationNetworks(curr_org_id)
        assert len(list_networks) > 1, "No networks in organization"

        curr_network_id = None
        if len(list_networks) == 1:
            curr_network_id = list_networks[0]['id']
        else:
            assert network is not None, f'''Multiple networks found in organization_id:"{curr_org_id}"'''
            for net in list_networks:
                if net['name'] == network:
                    curr_network_id = net['id']
        assert curr_network_id is not None, f'''Could not find network:"{network}"'''

        list_devices = dashboard.networks.getNetworkDevices(curr_network_id)
        # assert list_devices is not None, f'''No devices on current network_id: "{curr_network_id}"'''
        print(list_devices)
        return list_devices
