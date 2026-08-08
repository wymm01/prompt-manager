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


def add_prompt():
    print("\n===== 프롬프트 추가 =====")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비어 있을 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비어 있을 수 없습니다.")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리를 선택하세요.")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    print(f"{len(categories) + 1}. 직접 입력")

    while True:
        category_choice = input("선택: ").strip()

        if category_choice.isdigit():
            number = int(category_choice)

            if 1 <= number <= len(categories):
                category = categories[number - 1]
                break

            if number == len(categories) + 1:
                category = input("카테고리 입력: ").strip()

                if category:
                    break

        print("올바른 카테고리를 선택해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_list():
    print("\n===== 프롬프트 목록 =====")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        favorite = " ⭐" if prompt["favorite"] else ""

        print(
            f"{i}. {prompt['title']} "
            f"[{prompt['category']}]{favorite}"
        )


def show_by_category():
    print("\n===== 카테고리별 조회 =====")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = input("카테고리를 선택하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 입력입니다.")
        return

    number = int(choice)

    if number < 1 or number > len(categories):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[number - 1]

    found = False

    print(f"\n===== {selected_category} 프롬프트 =====")

    for i, prompt in enumerate(prompts, 1):
        if prompt["category"] == selected_category:
            favorite = " ⭐" if prompt["favorite"] else ""
            print(
                f"{i}. {prompt['title']}"
                f"{favorite}"
            )
            found = True

    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            print("프롬프트 검색 기능은 준비 중입니다.")

        elif choice == "5":
            print("프롬프트 상세 보기 기능은 준비 중입니다.")

        elif choice == "6":
            print("즐겨찾기 기능은 준비 중입니다.")

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()