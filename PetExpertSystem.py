def inputSpace():
    while True:
        Space = input("Nhap khong gian song (Nho/Rong): ")
        if Space == "Nho" or Space == "Rong":
            return Space
        print("Nhap khong hop le! Vui long nhap 'Nho' hoac 'Rong'.")

def inputTime():
    while True:
        Time = input("Nhap thoi gian ban co the cham soc (It/Nhieu): ")
        if Time == "It" or Time == "Nhieu":
            return Time
        print("Nhap khong hop le! Vui long nhap 'It' hoac 'Nhieu'.")

def inputHobby():
    while True:
        Hobby = input("Ban thich tuong tac voi thu cung hay chi thich ngam (Choi/Ngam)? ")
        if Hobby == "Choi" or Hobby == "Ngam":
            return Hobby
        print("Nhap khong hop le! Vui long nhap 'Choi' hoac 'Ngam'.")

# Ham he chuyen gia
def PetExpertSys(Space, Time, Hobby):
    suggestions = []
    # Khong gian nho, it thoi gian
    if Space == "Nho" and Time == "It":
        suggestions += ["Hamster", "Ca canh", "Chim nho"]
    # Khong gian nho, nhieu thoi gian
    elif Space == "Nho" and Time == "Nhieu":
        if Hobby == "Choi":
            suggestions += ["Meo", "Hamster", "Ca canh"]
        # So thich ngam thu cung
        else: 
            suggestions += ["Hamster", "Ca canh", "Chim nho"]
    # Khong gian rong, it thoi gian
    elif Space == "Rong" and Time == "It":
        if Hobby == "Choi":
            suggestions += ["Cho canh", "Meo"]
        # So thich ngam thu cung
        else: 
            suggestions += ["Cho canh", "Chim"]
    # Khong gian rong, nhieu thoi gian
    elif Space == "Rong" and Time == "Nhieu":
        suggestions += ["Cho lon", "Tho", "Chim"]
        if Hobby == "Choi":
            suggestions += ["Meo", "Tho", "Chim", "Ngua", "Soc canh", ]
        # So thich ngam thu cung
        else: 
            suggestions += ["Chim", "Ca canh", "Ga canh", "Hamster", "Rua canh"]

    result = ""
    for i in range(len(suggestions)):
        result += suggestions[i]
        if i != len(suggestions) - 1:
            result += ", "
    return result

def main():
    Space = inputSpace()
    Time = inputTime()
    Hobby = inputHobby()

    result = PetExpertSys(Space, Time, Hobby)
    print("Goi y cac loai thu cung phu hop voi ban: ", result)

if __name__ == "__main__":
    main()
