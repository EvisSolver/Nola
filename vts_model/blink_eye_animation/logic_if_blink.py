from . import config_blink


async def logic_if():

    if config_blink.gradus >= 90:
        config_blink.t_speed *= -1

    elif config_blink.gradus <= 0:
        config_blink.t_speed *= -1

    config_blink.gradus += config_blink.t_speed