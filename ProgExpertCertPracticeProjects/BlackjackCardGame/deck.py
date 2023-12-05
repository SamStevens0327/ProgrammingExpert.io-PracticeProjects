numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]
royals = ["T", "J", "Q", "K"]
ace = ["A"]
ranks = numbers + royals + ace
suits = ["\u2666", "\u2665", "\u2663", "\u2660"]

# cards = []
# for i in range(len(suits)):
#     for j in range(len(ranks)):
#         cards.append(ranks[j] + suits[i])


# for i in range(len(suits)):
#     for j in range(len(ranks)):
#         if ranks[j] in numbers:
#             val = int(ranks[j])
#         elif ranks[j] in royals:
#             val = 10
#         elif ranks[j] in ace:
#             val = 11
        
#         cards.update(f"{ranks[j]}{suits[i]}", val)


# good old brute force method
cards = {
    "2\u2666": 2, "2\u2665": 2, "2\u2663": 2, "2\u2660": 2,
    "3\u2666": 3, "3\u2665": 3, "3\u2663": 3, "3\u2660": 3,
    "4\u2666": 4, "4\u2665": 4, "4\u2663": 4, "4\u2660": 4,
    "5\u2666": 5, "5\u2665": 5, "5\u2663": 5, "5\u2660": 5,
    "5\u2666": 5, "5\u2665": 5, "5\u2663": 5, "5\u2660": 5,
    "7\u2666": 7, "7\u2665": 7, "7\u2663": 7, "7\u2660": 7,
    "8\u2666": 8, "8\u2665": 8, "8\u2663": 8, "8\u2660": 8,
    "9\u2666": 9, "9\u2665": 9, "9\u2663": 9, "9\u2660": 9,
    "T\u2666": 10, "T\u2665": 10, "T\u2663": 10, "T\u2660": 10,
    "J\u2666": 10, "J\u2665": 10, "J\u2663": 10, "J\u2660": 10,
    "Q\u2666": 10, "Q\u2665": 10, "Q\u2663": 10, "Q\u2660": 10,
    "K\u2666": 10, "K\u2665": 10, "K\u2663": 10, "K\u2660": 10,
    "A\u2666": 11, "A\u2665": 11, "A\u2663": 11, "A\u2660": 11, 
}
