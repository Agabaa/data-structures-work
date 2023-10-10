def sum_even_and_odd_numbers(start, end):
    even_sum = sum(num for num in range(start, end + 1) if num % 2 == 0)
    odd_sum = sum(num for num in range(start, end + 1) if num % 2 != 0)
    return even_sum, odd_sum

start_range = 1
end_range = 10
even_sum, odd_sum = sum_even_and_odd_numbers(start_range, end_range)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")