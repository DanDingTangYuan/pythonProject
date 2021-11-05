class Card:
    """a playing card."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]  # 牌面數字1-13
    SUITS = ["黑", "紅", "梅", "方"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):  # 重寫print()方法， 列印一張牌的資訊
        if self.is_face_up:
            rep = self.suit+self.rank
        else:
            rep = "XX"
        return rep

    def pic_order(self):  # 給每一張牌編上序號
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "J":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        if self.suit == "黑":
            suit = 1
        elif self.suit == "紅":
            suit = 2
        elif self.suit == "梅":
            suit = 3
        else:
            suit = 4
        return (suit-1)*13+FaceNum

    def flip(self):  # 翻牌方法
        self.is_face_up = not self.is_face_up


# Hand類
class Hand:
    """a hand of playing card."""

    def __init__(self):  # cards 列表變數儲存手中的牌
        self.cards = []

    def __str__(self):  # 重寫print（）方法，列印手中的牌。
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+"\t"
        else:
            rep = "無牌"
        return rep

    def clear(self):  # 清空手中的牌
        self.cards = []

    def add(self, card):  # 增加牌
        self.cards.append(card)

    def give(self, card, other_hand):  # 把一張牌給其他選手
        self.cards.remove(card)
        other_hand.add(card)

    # Poke類,Poke是Hand的子類。


class Poke(Hand):
    """a deck of playing cards."""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuf(self):  # 洗牌
        import random
        random.shuffle(self.cards)  # 打亂牌的順序

    def deal(self, hands, per_hand=13):  # 發牌，發給玩家，每人13張）
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)

                else:
                    print("不能繼續發牌了，牌已經發完了")


    # 主程式：
if __name__ == "__main__":
    print("this is a modle with classes for playing cards.")
    # 4個玩家
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    poke1.populate()  # 生成一副牌
    poke1.shuf()  # 洗牌
    poke1.deal(players, 13)  # 給玩家發牌，每人13張
    # 顯示4位牌手的牌
    n = 1
    for hand in players:
        print("牌手", n, end="")
        print(hand)
        n += 1
    input("\nPress the enter key to exit.")
    print(Card.SUITS)
