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

print("프롬프트 관리 프로그램")
print(f"등록된 프롬프트: {len(prompts)}개")