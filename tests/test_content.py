from collections import Counter

from platina_witcher3 import guide_data, gwent_catalog, progress, trophies


def test_base_game_trophy_list_is_complete_and_unique():
    ids = [item["id"] for item in trophies.TROPHIES]
    assert len(ids) == 53
    assert len(ids) == len(set(ids))
    assert Counter(item["tier"] for item in trophies.TROPHIES) == {
        "bronze": 42,
        "prata": 8,
        "ouro": 2,
        "platina": 1,
    }
    assert {item["id"] for item in trophies.TROPHIES if item["tier"] == "prata"} == {
        "king_is_dead", "ran_gauntlet", "butcher", "brawler", "overkill",
        "even_odds", "pest_control", "armed_dangerous",
    }


def test_every_content_id_and_progress_key_is_unique():
    for collection in (
        guide_data.TASKS, guide_data.GWENT_TASKS,
        guide_data.GATES, guide_data.CONTRACTS,
    ):
        ids = [item["id"] for item in collection]
        assert len(ids) == len(set(ids))
    keys = progress.all_keys()
    assert len(keys) == len(set(keys))
    assert len(guide_data.CONTRACTS) == 25
    assert Counter(item["region"] for item in guide_data.CONTRACTS) == {
        "velen": 11, "novigrad": 8, "skellige": 6,
    }


def test_gwent_vendors_and_missable_rewards_are_auditable():
    assert len(gwent_catalog.VENDORS) == 18
    assert sum(len(item["cards"]) for item in gwent_catalog.VENDORS) == 76
    assert len({item["id"] for item in gwent_catalog.VENDORS}) == 18
    assert all(item["cards"] for item in gwent_catalog.VENDORS)
    assert "gwent:following_thread_nekker" in next(
        gate["required"] for gate in guide_data.GATES
        if gate["id"] == "isle_of_mists_checkpoint"
    )
    assert "task:vegelbud_races" in next(
        gate["required"] for gate in guide_data.GATES
        if gate["id"] == "vegelbud_ball_checkpoint"
    )


def test_relations_point_to_existing_content():
    phases = {item["id"] for item in guide_data.PHASES}
    regions = {item["id"] for item in guide_data.REGIONS}
    trophy_ids = {item["id"] for item in trophies.TROPHIES}

    for task in guide_data.TASKS:
        assert task["region"] in regions
        assert task["phase"] in phases
        assert task.get("deadline", task["phase"]) in phases
        assert set(task.get("trophies", [])) <= trophy_ids

    for item in guide_data.GWENT_TASKS:
        assert item["region"] in regions

    for item in guide_data.CONTRACTS:
        assert item["region"] in regions

    for gate in guide_data.GATES:
        assert gate["phase"] in phases
        assert all(guide_data.item_by_key(key) is not None for key in gate["required"])


def test_spoiler_copy_does_not_use_em_dashes():
    user_facing = [guide_data.INTRO, guide_data.FOOTER, *trophies.TROPHY_TIPS.values()]
    for collection in (
        guide_data.PHASES,
        guide_data.TASKS,
        guide_data.GWENT_TASKS,
        guide_data.GATES,
        guide_data.BUILDS,
    ):
        for item in collection:
            for value in item.values():
                if isinstance(value, str):
                    user_facing.append(value)
                elif isinstance(value, list):
                    user_facing.extend(value)
    assert all("—" not in text and "–" not in text for text in user_facing)
