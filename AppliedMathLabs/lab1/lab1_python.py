"""        Lab #1 - Python         """

from typing import List


def sum_even_numbers(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

    """
    Examples:
         sum_even_numbers([1, 2, 3, 4, 5]) == 6
    (כי 2 + 4 = 6)

        sum_even_numbers([10, 15, 20]) == 30
    (כי 10 + 20 = 30)
    """
    # כתוב את הקוד שלך כאן
    pass


def find_unique_words(text: str) -> List[str]:
    """
    Example:
        find_unique_words("Hello world hello Python") == ["hello", "python", "world"]
    """
    # כתוב את הקוד שלך כאן
    unique_words = set()
    for word in text.split():
        unique_words.add(word.lower())
    return sorted(unique_words)

    pass


def count_occurrences(items: list, item_to_count) -> dict:
    """
    Examples:
        count_occurrences([1, 2, 1, 3, 1, 2], 1) == {1: 3}

        count_occurrences(["a", "b", "c", "a"], "a") == {"a": 2}
    """
    # כתוב את הקוד שלך כאן
    count = 0
    for item in items:
        if item == item_to_count:
            count += 1
    return {item_to_count: count}

    pass


def is_prime(number: int) -> bool:
    """
    Examples:
        is_prime(7) == True

        is_prime(10) == False

        is_prime(1) == False
    """
    # כתוב את הקוד שלך כאן
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    pass


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Example:
        merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4}
    """
    # כתוב את הקוד שלך כאן
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
    pass


if __name__ == '__main__':
    '''                 Running Examples        '''
    print("--- משימה 1 ---")
    print(f"sum_even_numbers([1, 2, 3, 4, 5]) -> {sum_even_numbers([1, 2, 3, 4, 5])}")

    print("\n--- משימה 2 ---")
    print(f"find_unique_words('Hello world hello Python') -> {find_unique_words('Hello world hello Python')}")

    print("\n--- משימה 3 ---")
    print(f"count_occurrences([1, 2, 1, 3, 1, 2], 1) -> {count_occurrences([1, 2, 1, 3, 1, 2], 1)}")

    print("\n--- משימה 4 ---")
    print(f"is_prime(7) -> {is_prime(7)}")
    print(f"is_prime(10) -> {is_prime(10)}")

    print("\n--- משימה 5 ---")
    print(f"merge_dictionaries({{'a': 1, 'b': 2}}, {{'b': 3, 'c': 4}}) -> {merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}")
