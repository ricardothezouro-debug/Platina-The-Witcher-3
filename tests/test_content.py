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


def test_skill_tree_links_point_to_real_skills_without_cycles():
    from platina_witcher3 import skill_tree

    assert len(skill_tree.SKILLS) == 80
    for name, (tree, links) in skill_tree.SKILLS.items():
        assert tree in skill_tree.TREE_ORDER
        for link in links:
            assert link in skill_tree.SKILLS, f"{name} -> {link}"
    # unlock_order de tudo terminaria em recursao infinita se houvesse ciclo
    everything = skill_tree.unlock_order(list(skill_tree.SKILLS))
    assert sorted(everything) == sorted(skill_tree.SKILLS)


def test_builds_equip_twelve_real_skills_and_path_respects_links():
    from platina_witcher3 import skill_tree

    for build in guide_data.BUILDS:
        assert len(build["equip"]) == 12, build["id"]
        assert len(set(build["equip"])) == 12, build["id"]
        assert build["confidence"] in {"confirmado", "fonte única", "inconsistente"}
        path = skill_tree.unlock_order(build["equip"])
        assert set(build["equip"]) <= set(path)
        position = {name: index for index, name in enumerate(path)}
        for name in path:
            for link in skill_tree.links_of(name):
                assert position[link] < position[name], f"{build['id']}: {link} antes de {name}"


def test_power_stones_split_by_region_add_up_to_24():
    from platina_witcher3.walkthroughs import power_stones_by_region

    stones = power_stones_by_region()
    assert {region: len(items) for region, items in stones.items()} == {
        "white_orchard": 6, "velen": 6, "novigrad": 2, "skellige": 9, "kaer_morhen": 1,
    }
    assert all(stone.get("image") for items in stones.values() for stone in items)
