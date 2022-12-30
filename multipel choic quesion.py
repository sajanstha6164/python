class question_answer:
    def __init__(self,que,ans):
        self.que=que
        self.ans=ans

question_array=[
    "1.what is 2+3?\n(a)1\n(b)2\n(c)5\n",
    "2.what is 2*3?\n(a)6\n(b)3\n(c)5\n",
    "3.what is 3-2?\n(a)1\n(b)2\n(c)5\n"
]
answer_sheet=[
    question_answer(question_array[0],"c"),
    question_answer(question_array[1],"a"),
    question_answer(question_array[2],"a")

]
score=0
for question in answer_sheet:
    answer=input(question.que)
    print("\n")
    if answer==question.ans:
        score=score+1

print("Your score is "+str(score))

