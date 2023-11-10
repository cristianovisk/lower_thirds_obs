import obsws_python as obs
import time

def hide_LowerThird(name, subtitle):
    cl = obs.ReqClient()
    with open('name.txt', 'w') as file:
        file.write(name)
    with open('subtitle.txt', 'w') as file:
        file.write(subtitle)

    cl.trigger_hot_key_by_key_sequence(keyId="OBS_KEY_PAGEDOWN", pressCtrl=False, pressAlt=False, pressShift=False, pressCmd=False)


def unhide_LowerThird(name, subtitle):
    cl = obs.ReqClient()
    with open('name.txt', 'w') as file:
        file.write(name)
    with open('subtitle.txt', 'w') as file:
        file.write(subtitle)
    
    time.sleep(2)

    cl.trigger_hot_key_by_key_sequence(keyId="OBS_KEY_PAGEUP", pressCtrl=False, pressAlt=False, pressShift=False, pressCmd=False)