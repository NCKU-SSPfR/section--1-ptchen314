from judge_code import game_over

def test_game_over_0():
    """Test when health is 0"""
    assert game_over(0) == True

def test_game_over_666():
    """Test when health is 666 (win condition)"""
    assert game_over(666) == True

def test_game_over_other():
    """Test when health is neither 0 nor 666"""
    assert game_over(3) == False
    assert game_over(1) == False
    assert game_over(100) == False
