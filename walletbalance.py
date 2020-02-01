#!/usr/bin/env python3
"""This plugin for c-lightning emulates `lncli walletbalance` command of LND.

Computes and displays the wallet's current balance summary.

Active the plugin with:
`lightningd --plugin=PATH_TO_PLUGIN/walletbalance.py`

Call the plugin with:
`lightning-cli walletbalance`

Author: Kristaps Kaupe (https://github.com/kristapsk)
"""

from lightning import LightningRpc, Plugin
from os.path import join

rpc = None
plugin = Plugin(autopatch=True)


@plugin.method("walletbalance")
def walletbalance(plugin=None):
    """Compute and display the wallet's current balance."""
    confirmed_balance = 0
    unconfirmed_balance = 0
    outputs = rpc.listfunds()["outputs"]
    for output in outputs:
        if output["status"] == "confirmed":
            confirmed_balance += output["value"]
        elif output["status"] == "unconfirmed":
            unconfirmed_balance += output["value"]
    return {
        "total_balance": str(confirmed_balance + unconfirmed_balance),
        "confirmed_balance": str(confirmed_balance),
        "unconfirmed_balance": str(unconfirmed_balance)
    }


@plugin.init()
def init(options, configuration, plugin):
    global rpc
    plugin.log("walletbalance init")
    path = join(configuration["lightning-dir"], configuration["rpc-file"])
    rpc = LightningRpc(path)


plugin.run()
