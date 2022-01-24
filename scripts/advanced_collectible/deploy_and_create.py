from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)

from brownie import AdvancedCollectible, network, config


def deploy_and_create():
    account = get_account()

    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    print ("deployed advanced collectible",advanced_collectible.address)

def main():
    deploy_and_create()