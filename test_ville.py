from task_tdd import search_word
import pytest


@pytest.mark.parametrize("choix", ['P'])
def test_town_name_is_under_two_caracters(choix):
    assert search_word(choix) == 'nothing to show'


@pytest.mark.parametrize("choix", ['Va'])
def test_town_name_is_up_two_caracters(choix):
    assert search_word(choix) == ['Valence']


@pytest.mark.parametrize("choix", ['NN'])
def test_town_name_is_insensible(choix):
    assert search_word(choix) == ['Vienne']


@pytest.mark.parametrize("choix", ['*'])
def test_town_name_return_all_towns(choix):
    assert search_word(choix) == [['Paris', 'Budapest', 'Skopje', 'Rotterdam', 'Valence', 'Vancouver', 'Amsterdam', 'Vienne', 'Sydney', 'New York', 'Londres', 'Bangkok', 'Hong Kong', 'Dubaï', 'Rome', 'Istanbul']]