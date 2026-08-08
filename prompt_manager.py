prompts = [
    {
        "title": "블로그 글 작성",
        "content": "친절하고 이해하기 쉬운 말투로 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "따뜻한 햇살이 비치는 카페에서 책을 읽는 사람의 모습을 그려줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무 자동화 아이디어",
        "content": "반복적인 업무를 자동화할 수 있는 방법을 단계별로 제안해줘.",
        "category": "자동화",
        "favorite": True
    }
]


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            print("프롬프트 추가 기능은 준비 중입니다.")
        elif choice == "2":
            print("프롬프트 목록 기능은 준비 중입니다.")
        elif choice == "3":
            print("카테고리별 조회 기능은 준비 중입니다.")
        elif choice == "4":
            print("검색 기능은 준비 중입니다.")
        elif choice == "5":
            print("상세 보기 기능은 준비 중입니다.")
        elif choice == "6":
            print("즐겨찾기 기능은 준비 중입니다.")
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()