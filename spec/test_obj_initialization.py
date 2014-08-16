from model.game import *
import unittest
from sqlalchemy import inspect
import datetime

class TestObjectInitialization(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        make_tables()

    @classmethod
    def tearDownClass(self):
        meta_data.drop_all(engine)

    def test_thing(self):
        assert 2*3 == 6
        s = Summoner()

    def test_when_game_is_made(self):
        session = SessionMaker()
        def add_a_game():
            game = Game(
                game_mode   = 'CLASSIC',
                game_type   = 'MATCHED_GAME',
                game_id     = 100100100101,
                create_date = datetime.datetime.now(),
            )
            session.add(game)
            session.commit()
            return game

        def query_for_game():
            return session.query(Game).filter_by(game_id=100100100101).first()
        
        expected = add_a_game()
        observed = query_for_game()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_game_stats_is_made(self):
        session = SessionMaker()
        def add_a_game_stats():
            game_stats = GameStats(
                summoner_name = 'Bjerson',
                champion = 'Garen',
                spell1 = 'Ignite',
                spell2 = 'Flash',
                item0 =  'Bork',
                blue = True,
                won = True,
            )
            session.add(game_stats)
            session.commit()
            return game_stats

        def query_for_game_stats():
            return session.query(GameStats).filter_by(summoner_name='Bjerson').first()

        expected = add_a_game_stats()
        observed = query_for_game_stats()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_summoner_is_made(self):
        session = SessionMaker()
        def add_a_summoner():
            summoner = Summoner()
            session.add(summoner)
            session.commit()
            return summoner

        def query_for_summoner():
            return session.query(Summoner).first()

        expected = add_a_summoner()
        observed = query_for_summoner()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)


    def test_when_summoner_name_is_made(self):
        session = SessionMaker()
        def add_a_summoner_name():
            summoner_name = SummonerName(name='seven_nation_gnarmy', region='na')
            session.add(summoner_name)
            session.commit()
            return summoner_name

        def query_for_summoner_name():
            return session.query(SummonerName).first()

        expected = add_a_summoner_name()
        observed = query_for_summoner_name()
        session.close()
        assert expected is observed, 'Observed:\t{0}\nExpected:\t{1}'.format(observed, expected)

    def test_when_they_work_together(self):
        pass    


if __name__ == '__main__':
    unittest.main()

