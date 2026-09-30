"""Chaves estáveis usadas pelo progresso do guia."""
from __future__ import annotations

from . import guide_data, gwent_catalog
from . import trophies


def trophy_key(trophy_id: str) -> str:
    return f"trophy:{trophy_id}"


def task_key(task_id: str) -> str:
    return f"task:{task_id}"


def gwent_key(item_id: str) -> str:
    return f"gwent:{item_id}"


def gate_key(gate_id: str) -> str:
    return f"gate:{gate_id}"


def contract_key(contract_id: str) -> str:
    return f"contract:{contract_id}"


def vendor_key(vendor_id: str) -> str:
    return f"vendor:{vendor_id}"


def trophy_keys() -> list[str]:
    return [trophy_key(item["id"]) for item in trophies.TROPHIES]


def task_keys() -> list[str]:
    return [task_key(item["id"]) for item in guide_data.TASKS]


def gwent_keys() -> list[str]:
    return [gwent_key(item["id"]) for item in guide_data.GWENT_TASKS]


def gate_keys() -> list[str]:
    return [gate_key(item["id"]) for item in guide_data.GATES]


def contract_keys() -> list[str]:
    return [contract_key(item["id"]) for item in guide_data.CONTRACTS]


def vendor_keys() -> list[str]:
    return [vendor_key(item["id"]) for item in gwent_catalog.VENDORS]


def all_keys() -> list[str]:
    return (
        trophy_keys() + task_keys() + gwent_keys() + gate_keys()
        + contract_keys() + vendor_keys()
    )
