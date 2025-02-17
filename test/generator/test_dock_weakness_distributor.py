import dataclasses
from randovania.generator.generator import generate_and_validate_description
from randovania.interface_common.preset_editor import PresetEditor
from randovania.layout.base.dock_rando_configuration import DockRandoMode

from randovania.layout.generator_parameters import GeneratorParameters
from randovania.layout.preset import Preset


async def test_dock_weakness_distribute(default_blank_preset):
    _editor = PresetEditor(default_blank_preset.fork())
    with _editor as editor:
        editor.dock_rando_configuration = dataclasses.replace(
            editor.dock_rando_configuration,
            mode=DockRandoMode.TWO_WAY
        )
        preset = editor.create_custom_preset_with()
    
    gen_params = GeneratorParameters(5000, False, [preset])
    description = await generate_and_validate_description(gen_params, None, False)

    assert description.all_patches[0].dock_weakness
