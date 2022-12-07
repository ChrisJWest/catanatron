import random

from catanatron.models.player import Player
from catanatron.models.actions import ActionType


WEIGHTS_BY_ACTION_TYPE = {
    ActionType.BUILD_CITY: 10000,
    ActionType.BUILD_SETTLEMENT: 1000,
    ActionType.BUY_DEVELOPMENT_CARD: 100,
}

WEIGHTS_BY_ACTION_TYPE_2 = {
    ActionType.BUILD_CITY: 10000,
    ActionType.BUILD_SETTLEMENT: 1000,
    ActionType.BUY_DEVELOPMENT_CARD: 100,
    ActionType.BUILD_ROAD: 100,
    ActionType.PLAY_KNIGHT_CARD: 2,
    ActionType.PLAY_YEAR_OF_PLENTY: 2,
    ActionType.PLAY_MONOPOLY: 2,
    ActionType.PLAY_MONOPOLY: 2,
}


class WeightedRandomPlayer(Player):
    """
    Player that decides at random, but skews distribution
    to actions that are likely better (cities > settlements > dev cards).
    """

    def decide(self, game, playable_actions):
        bloated_actions = []
        for action in playable_actions:
            weight = WEIGHTS_BY_ACTION_TYPE.get(action.action_type, 1)
            bloated_actions.extend([action] * weight)

        index = random.randrange(0, len(bloated_actions))
        return bloated_actions[index]
    
class WeightedRandomPlayer2(Player):
    """
    Player that decides at random, but skews distribution
    to actions that are likely better (cities > settlements > dev cards).
    """

    def decide(self, game, playable_actions):
        bloated_actions = []
        for action in playable_actions:
            weight = WEIGHTS_BY_ACTION_TYPE_2.get(action.action_type, 1)
            bloated_actions.extend([action] * weight)

        index = random.randrange(0, len(bloated_actions))
        return bloated_actions[index]
