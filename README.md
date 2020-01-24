# lightning-walletbalance

[![tippin.me](https://badgen.net/badge/%E2%9A%A1%EF%B8%8Ftippin.me/@kristapsk/F0918E)](https://tippin.me/@kristapsk)

walletbalance plugin for c-lightning

This plugin for c-lightning emulates `lncli walletbalance` command of LND.

Computes and displays the wallet's current balance summary.

Active the plugin with:
`lightningd --plugin=PATH_TO_PLUGIN/walletbalance.py`

Call the plugin with:
`lightning-cli walletbalance`
