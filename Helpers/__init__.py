import AP_Handler.derived_AP.ciscoMR45


def __AP__(name):
    """
    This is a bridge between YAML dictionary and the Object

    :arg name: A string, such as "lexus" or "cisco"
    :return: A reference to the derived AP.
    """
    # todo: Add more devices here as we go
    derived_ap_dict = {
        "cisco": AP_Handler.derived_AP.ciscoMR45.MR45,
        "lexus": None,
        "steps": None,
    }

    return derived_ap_dict[name]
