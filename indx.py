# # Tic Tac Toe o'yini

# # O'yin maydoni (bo'sh ro'yxat)
# board = [" " for _ in range(9)]  # 3x3 ta bo'sh joy (0-8 indexlari)
# current_player = "X"  # Dastlabki o'yinchi

# # O'yin maydonini chiqarish
# def print_board():
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")
#     print()

# # O'yin tugadi yoki yo'qligini tekshirish
# def check_winner():
#     winning_combinations = [
#         [0, 1, 2],  # 1. qator
#         [3, 4, 5],  # 2. qator
#         [6, 7, 8],  # 3. qator
#         [0, 3, 6],  # 1. ustun
#         [1, 4, 7],  # 2. ustun
#         [2, 5, 8],  # 3. ustun
#         [0, 4, 8],  # diagonal
#         [2, 4, 6]   # diagonal
#     ]
    
#     for combination in winning_combinations:
#         if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
#             return board[combination[0]]  # X yoki O g'olib bo'ladi
#     return None

# # O'yin davomida o'yinchidan navbatdagi harakatni olish
# def get_move():
#     while True:
#         try:
#             move = int(input(f"O'yinchi {current_player}, 1 dan 9 gacha sonni kiriting: ")) - 1
#             if board[move] == " ":
#                 return move
#             else:
#                 print("Bu joy band. Iltimos, boshqa joyni tanlang.")
#         except (ValueError, IndexError):
#             print("Noto'g'ri kiritish. Iltimos, 1 dan 9 gacha raqam kiriting.")

# # O'yinni boshlash
# def start_game():
#     global current_player
#     print("Tic Tac Toe o'yini boshlanmoqda!")
#     print_board()

#     for turn in range(9):  # 9 ta harakat bo'ladi (3x3 ta maydon)
#         move = get_move()
#         board[move] = current_player
#         print_board()

#         winner = check_winner()
#         if winner:
#             print(f"Tabriklayman! O'yinchi {winner} g'olib bo'ldi!")
#             break

#         # Navbatdagi o'yinchiga o'tish
#         current_player = "O" if current_player == "X" else "X"
#     else:
#         print("O'yin durang bilan yakunlandi!")

# # O'yinni boshlash
# start_game()
# Sample workflow for building and deploying an Astro site to GitHub Pages
#
# To get started with Astro see: https://docs.astro.build/en/getting-started/
#
