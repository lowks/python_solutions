import codewars_test as test
from codewar_solutions import get_count

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Should count all vowels")
    def all_vowels():
        test.assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")
        
    @test.it("Should not count \"y\"")
    def only_y():
        test.assert_equals(get_count("y"), 0, f"Incorrect answer for \"y\"")        
        
    @test.it("Should return 0 when no vowels")
    def no_vowels():
        test.assert_equals(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")
        
    @test.it("Should return 0 for empty string")
    def no_vowels():
        test.assert_equals(get_count(""), 0, f"Incorrect answer for empty string")
        
    @test.it("Should return 5 for \"abracadabra\"")
    def test_abracadabra():    
        test.assert_equals(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")

    test.assert_equals(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
    test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
    test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])

    test.describe("Basic tests")
    test.assert_equals(group([3, 2, 6, 2, 1, 3]), [[3, 3], [2, 2], [6], [1]])
    test.assert_equals(group([3, 2, 6, 2]), [[3], [2, 2], [6]])
    test.assert_equals(group([]), [])
    test.assert_equals(group([1, 100, 4, 2, 4]), [[1], [100], [4, 4], [2]])
    test.assert_equals(group([-1, 1, -1]), [[-1, -1], [1]])