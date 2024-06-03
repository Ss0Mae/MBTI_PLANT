# poll/views.py
from django.shortcuts import render, redirect


def survey(request):
    questions = {
        'EI': [
            {'number': 'q1', 'question': '당신은 주말에 사람들과 함께 보내는 시간을 즐기나요?'},
            {'number': 'q2', 'question': '혼자 조용히 보내는 시간을 선호하나요?'},
            {'number': 'q3', 'question': '새로운 사람들과 쉽게 친구가 되나요?'},
            {'number': 'q4', 'question': '소수의 깊은 관계를 선호하나요?'},
            {'number': 'q5', 'question': '에너지를 얻기 위해 사람들과 어울리나요?'},
            {'number': 'q6', 'question': '혼자만의 시간이 필요하나요?'},
            {'number': 'q7', 'question': '파티나 모임에서 주도적으로 대화를 이끌어 가나요?'},
            {'number': 'q8', 'question': '파티나 모임에서 주로 경청하는 편인가요?'},
            {'number': 'q9', 'question': '외출을 자주 계획하고 실행하나요?'},
            {'number': 'q10', 'question': '집에서 시간을 보내는 것을 외출하는 것보다 더 좋아하나요?'},
            {'number': 'q11', 'question': '즉흥적인 활동을 즐기나요?'},
            {'number': 'q12', 'question': '계획된 활동을 선호하나요?'}
        ],
        'SN': [
            {'number': 'q13', 'question': '당신은 현재의 사실과 세부 사항에 집중하나요?'},
            {'number': 'q14', 'question': '미래의 가능성과 큰 그림을 중시하나요?'},
            {'number': 'q15', 'question': '실질적이고 구체적인 정보를 선호하나요?'},
            {'number': 'q16', 'question': '아이디어와 개념을 더 중시하나요?'},
            {'number': 'q17', 'question': '경험에 기반한 결정을 내리나요?'},
            {'number': 'q18', 'question': '상상력과 직관에 기반한 결정을 내리나요?'},
            {'number': 'q19', 'question': '일상적인 세부 사항에 주의를 기울이나요?'},
            {'number': 'q20', 'question': '가능성에 더 주의를 기울이나요?'},
            {'number': 'q21', 'question': '눈에 보이는 현실을 믿나요?'},
            {'number': 'q22', 'question': '보이지 않는 가능성을 더 믿나요?'},
            {'number': 'q23', 'question': '구체적이고 현실적인 목표를 설정하나요?'},
            {'number': 'q24', 'question': '이상적이고 추상적인 목표를 설정하나요?'}
        ],
        'TF': [
            {'number': 'q25', 'question': '당신은 결정을 내릴 때 논리와 분석을 중시하나요?'},
            {'number': 'q26', 'question': '사람들의 감정과 관계를 중시하나요?'},
            {'number': 'q27', 'question': '공정성과 객관성을 중요하게 생각하나요?'},
            {'number': 'q28', 'question': '조화와 공감을 중요하게 생각하나요?'},
            {'number': 'q29', 'question': '비판적이고 논리적인 사고를 자주 하나요?'},
            {'number': 'q30', 'question': '감정적이고 관계 중심의 사고를 자주 하나요?'},
            {'number': 'q31', 'question': '문제를 해결할 때 원칙과 기준에 따라 결정하나요?'},
            {'number': 'q32', 'question': '상황과 사람들에 따라 유연하게 결정하나요?'},
            {'number': 'q33', 'question': '갈등 상황에서 논리적이고 객관적인 접근을 하나요?'},
            {'number': 'q34', 'question': '감정적이고 인간적인 접근을 하나요?'},
            {'number': 'q35', 'question': '의사결정 시 사실과 데이터를 중요시하나요?'},
            {'number': 'q36', 'question': '사람들의 의견과 감정을 중요시하나요?'}
        ],
        'JP': [
            {'number': 'q37', 'question': '당신은 계획을 세우고 그에 따라 행동하는 것을 좋아하나요?'},
            {'number': 'q38', 'question': '즉흥적으로 상황에 맞게 행동하는 것을 좋아하나요?'},
            {'number': 'q39', 'question': '마감일을 지키기 위해 계획을 세우나요?'},
            {'number': 'q40', 'question': '마감일에 가까워질 때까지 기다렸다가 일을 처리하나요?'},
            {'number': 'q41', 'question': '체계적이고 조직적으로 일을 처리하나요?'},
            {'number': 'q42', 'question': '유연하고 자율적으로 일을 처리하나요?'},
            {'number': 'q43', 'question': '결정을 빨리 내리고 실행에 옮기나요?'},
            {'number': 'q44', 'question': '가능한 모든 옵션을 고려한 후에 결정을 내리나요?'},
            {'number': 'q45', 'question': '일을 시작하기 전에 계획을 철저히 세우나요?'},
            {'number': 'q46', 'question': '일을 하면서 계획을 세워나가나요?'},
            {'number': 'q47', 'question': '미리 계획된 일정에 따라 움직이는 것을 좋아하나요?'},
            {'number': 'q48', 'question': '상황에 따라 유연하게 대처하는 것을 좋아하나요?'}
        ]
    }

    context = {
        'questions': questions,
    }
    return render(request, 'poll/polls.html', context)


def result(request):
    if request.method == 'POST':
        responses = {key: request.POST[key] for key in request.POST if key.startswith('q')}
        mbti = calculateMbti(responses)

        # mbti = 'ESTJ'
        if mbti == 'ESTJ':
            return render(request, 'poll/estj.html')
        elif mbti == 'ESTP':
            return render(request, 'poll/estp.html')
        elif mbti == 'ESFJ':
            return render(request, 'poll/esfj.html')
        elif mbti == 'ESFP':
            return render(request, 'poll/esfp.html')
        elif mbti == 'ENTJ':
            return render(request, 'poll/entj.html')
        elif mbti == 'ENTP':
            return render(request, 'poll/entp.html')
        elif mbti == 'ENFJ':
            return render(request, 'poll/enfj.html')
        elif mbti == 'ENFP':
            return render(request, 'poll/enfp.html')
        elif mbti == 'ISTJ':
            return render(request, 'poll/istj.html')
        elif mbti == 'ISTP':
            return render(request, 'poll/istp.html')
        elif mbti == 'ISFJ':
            return render(request, 'poll/isfj.html')
        elif mbti == 'ISFP':
            return render(request, 'poll/isfp.html')
        elif mbti == 'INTJ':
            return render(request, 'poll/intj.html')
        elif mbti == 'INTP':
            return render(request, 'poll/intp.html')
        elif mbti == 'INFJ':
            return render(request, 'poll/infj.html')
        elif mbti == 'INFP':
            return render(request, 'poll/infp.html')

    return render(request, 'poll/result.html')  # get 방식 요청 응답


def calculateMbti(responses):
    # ToDo: 승현님 작업 : responses 바탕으로 mbti 산출하기, (calculate 브랜치 생성 후 작업 요망)
    # input : {'key' : 'value'} 각 질문 번호에 대한 응답이 담겨 있는 딕셔너리 형태, ex) {'q1' : 'yes'}
    # output : 'ESTJ' 등의 MBTI를 나타내는 문자열 return
    mbti = ''
    # E/I (q1 ~ q12)

    # S/N (q13 ~ q24)

    # T/F (q25 ~ q36)

    # J/P (q37 ~ q48)
    return mbti
