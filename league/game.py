from league.base_game import BaseGame


class LeagueOfNoobsGame(BaseGame):
    def create(self) -> None:
        from league.title_view import TitleView
        LeagueOfNoobsGame.set_current_view(TitleView())
