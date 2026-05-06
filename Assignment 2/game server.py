from collections import deque


class GameServerQueue:
    def __init__(self, num_player_team: int) -> None:
        self._num_player_team = num_player_team
        self._player_queue = deque()

    def fill_queue_with_names(self) -> None:
        count = int(input("Wie viele Spieler möchten Sie hinzufügen? "))
        for _ in range(count):
            name = input("Spielername: ")
            self._player_queue.append(name)
        print(f"Warteschlange: {list(self._player_queue)}")

    def build_teams(self) -> None:
        team_number = 1
        while len(self._player_queue) >= self._num_player_team:
            team = []
            for _ in range(self._num_player_team):
                team.append(self._player_queue.popleft())
            print(f"Team {team_number}: {team}")
            team_number += 1
        if self._player_queue:
            print(f"Verbleibende Spieler in der Schlange: {list(self._player_queue)}")


if __name__ == "__main__":
    queue = GameServerQueue(num_player_team=2)
    queue.fill_queue_with_names()
    queue.build_teams()
