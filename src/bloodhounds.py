from solidity_checks import (
    check_outdated_versions,
    check_pragma_experimental,
    check_send_transfer,
    check_low_level_call,
    check_tx_origin,
    check_visibility_specifiers,
    check_storage_initialization
)

check_structures = {
    "initial": [
        {"name": "Outdated Versions", "func": check_outdated_versions},
        {"name": "Pragma Experimental", "func": check_pragma_experimental},
        {"name": "Send/Transfer", "func": check_send_transfer},
        {"name": "Low-Level Call", "func": check_low_level_call},
        {"name": "Tx.Origin", "func": check_tx_origin},
        {"name": "Visibility Specifiers", "func": check_visibility_specifiers}
    ],
    "rareskills" :   [
        {"name": "Storage initialization", "func": check_storage_initialization}
    ]

}
