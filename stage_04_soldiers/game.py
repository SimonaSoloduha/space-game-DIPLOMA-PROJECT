# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from astrobox.space_field import SpaceField
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.reaper import ReaperDrone
from stage_04_soldiers.devastator import DevastatorDrone
from kiseliova import SimonDrone, SimonScene
from vader import VaderDrone

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SimonScene(
        field=(1200, 800),
        speed=5,
        asteroids_count=7,
        can_fight=True,
    )

    team_4 = [DevastatorDrone() for _ in range(NUMBER_OF_DRONES)]
    # team_1 = [VaderDrone() for _ in range(NUMBER_OF_DRONES)]
    team_2 = [ReaperDrone() for _ in range(NUMBER_OF_DRONES)]
    team_3 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    my_team = [SimonDrone() for _ in range(NUMBER_OF_DRONES)]

    scene.go()

# зачёт!
