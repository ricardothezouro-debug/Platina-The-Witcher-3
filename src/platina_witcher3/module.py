"""Adaptador do guia para o Streamer Sidekick."""
from dataclasses import dataclass

from . import guide_data
from . import progress
from .storage import load_progress

MODULE_ID = guide_data.GUIDE_ID


@dataclass(frozen=True)
class ModuleInfo:
    module_id: str
    title: str
    subtitle: str
    status: str
    accent: str


def module_info():
    state = load_progress()
    done = set(state.get("done", []))
    keys = progress.trophy_keys()
    completed = sum(1 for key in keys if key in done)
    data = dict(
        module_id=guide_data.GUIDE_ID,
        title=guide_data.GAME_NAME,
        subtitle=guide_data.GAME_SUBTITLE,
        status=f"{completed}/{len(keys)} troféus",
        accent=guide_data.ACCENT,
    )
    try:
        from streamer_sidekick.core.modules import ModuleInfo as SidekickModuleInfo

        return SidekickModuleInfo(**data)
    except Exception:
        return ModuleInfo(**data)


def help_text() -> str:
    from .paths import guide_dir_label

    return (
        "Guia do jogo base de The Witcher 3: Wild Hunt no PS5 Remastered.\n\n"
        "A campanha começa na Marcha da Morte e não pode ter a dificuldade "
        "reduzida. Marque a fase atual da história para o painel avisar o que "
        "precisa ser resolvido antes de cada ponto crítico.\n\n"
        "A ordem de exploração é livre. Situações que podem fechar troféus ou "
        "cartas aparecem com a tag PERDÍVEL. Informações narrativas ficam "
        "recolhidas em SPOILER.\n\n"
        f"O progresso é salvo em {guide_dir_label()} e sobrevive a atualizações."
    )


def build_page(config=None):
    from .page import GuidePage

    return GuidePage()
