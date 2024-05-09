def calculate_max_bananas():
    total_bananas = 3000
    max_carry = 1000
    distance = 1000

    # Calculate distances for each segment
    x = 200  # Distance from Source to IP1
    y = 333  # Distance from IP1 to IP2
    z = distance - x - y  # Distance from IP2 to Destination

    # Calculate bananas at each point after each segment
    bananas_after_IP1 = total_bananas - 5 * x  # 5 trips for first segment
    bananas_after_IP2 = bananas_after_IP1 - 3 * y  # 3 trips for second segment
    bananas_after_IP2 = bananas_after_IP2 - 1  # Leaving 1 banana at IP2
    bananas_at_destination = bananas_after_IP2 - z  # 1 trip for last segment

    return bananas_at_destination

# Calculate and print the maximum number of bananas that can be transferred
max_bananas_transferred = calculate_max_bananas()
print("Maximum bananas that can be transferred:", max_bananas_transferred)
