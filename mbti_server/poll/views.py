from django.shortcuts import render,redirect
from .models import Question

def survey(request):
    if request.method == 'POST':
        responses = {key: request.POST[key] for key in request.POST if key.startswith('response_')}
        # 응답 처리 로직을 추가할 수 있습니다.
        return redirect('result')  # 응답 후 리디렉션할 페이지

    questions = [
        {'category': 'EI', 'text': '당신은 주말에 사람들과 함께 보내는 시간을 즐기나요?'},
        {'category': 'EI', 'text': '혼자 조용히 보내는 시간을 선호하나요?'},
        {'category': 'EI', 'text': '새로운 사람들과 쉽게 친구가 되나요?'},
        {'category': 'EI', 'text': '소수의 깊은 관계를 선호하나요?'},
        {'category': 'EI', 'text': '에너지를 얻기 위해 사람들과 어울리나요?'},
        {'category': 'EI', 'text': '혼자만의 시간이 필요하나요?'},
        {'category': 'EI', 'text': '파티나 모임에서 주도적으로 대화를 이끌어 가나요?'},
        {'category': 'EI', 'text': '파티나 모임에서 주로 경청하는 편인가요?'},
        {'category': 'EI', 'text': '외출을 자주 계획하고 실행하나요?'},
        {'category': 'EI', 'text': '집에서 시간을 보내는 것을 외출하는 것보다 더 좋아하나요?'},
        {'category': 'EI', 'text': '즉흥적인 활동을 즐기나요?'},
        {'category': 'EI', 'text': '계획된 활동을 선호하나요?'},

        {'category': 'SN', 'text': '당신은 현재의 사실과 세부 사항에 집중하나요?'},
        {'category': 'SN', 'text': '미래의 가능성과 큰 그림을 중시하나요?'},
        {'category': 'SN', 'text': '실질적이고 구체적인 정보를 선호하나요?'},
        {'category': 'SN', 'text': '아이디어와 개념을 더 중시하나요?'},
        {'category': 'SN', 'text': '경험에 기반한 결정을 내리나요?'},
        {'category': 'SN', 'text': '상상력과 직관에 기반한 결정을 내리나요?'},
        {'category': 'SN', 'text': '일상적인 세부 사항에 주의를 기울이나요?'},
        {'category': 'SN', 'text': '가능성에 더 주의를 기울이나요?'},
        {'category': 'SN', 'text': '눈에 보이는 현실을 믿나요?'},
        {'category': 'SN', 'text': '보이지 않는 가능성을 더 믿나요?'},
        {'category': 'SN', 'text': '구체적이고 현실적인 목표를 설정하나요?'},
        {'category': 'SN', 'text': '이상적이고 추상적인 목표를 설정하나요?'},

        {'category': 'TF', 'text': '당신은 결정을 내릴 때 논리와 분석을 중시하나요?'},
        {'category': 'TF', 'text': '사람들의 감정과 관계를 중시하나요?'},
        {'category': 'TF', 'text': '공정성과 객관성을 중요하게 생각하나요?'},
        {'category': 'TF', 'text': '조화와 공감을 중요하게 생각하나요?'},
        {'category': 'TF', 'text': '비판적이고 논리적인 사고를 자주 하나요?'},
        {'category': 'TF', 'text': '감정적이고 관계 중심의 사고를 자주 하나요?'},
        {'category': 'TF', 'text': '문제를 해결할 때 원칙과 기준에 따라 결정하나요?'},
        {'category': 'TF', 'text': '상황과 사람들에 따라 유연하게 결정하나요?'},
        {'category': 'TF', 'text': '갈등 상황에서 논리적이고 객관적인 접근을 하나요?'},
        {'category': 'TF', 'text': '감정적이고 인간적인 접근을 하나요?'},
        {'category': 'TF', 'text': '의사결정 시 사실과 데이터를 중요시하나요?'},
        {'category': 'TF', 'text': '사람들의 의견과 감정을 중요시하나요?'},

        {'category': 'JP', 'text': '당신은 계획을 세우고 그에 따라 행동하는 것을 좋아하나요?'},
        {'category': 'JP', 'text': '즉흥적으로 상황에 맞게 행동하는 것을 좋아하나요?'},
        {'category': 'JP', 'text': '마감일을 지키기 위해 계획을 세우나요?'},
        {'category': 'JP', 'text': '마감일에 가까워질 때까지 기다렸다가 일을 처리하나요?'},
        {'category': 'JP', 'text': '체계적이고 조직적으로 일을 처리하나요?'},
        {'category': 'JP', 'text': '유연하고 자율적으로 일을 처리하나요?'},
        {'category': 'JP', 'text': '결정을 빨리 내리고 실행에 옮기나요?'},
        {'category': 'JP', 'text': '가능한 모든 옵션을 고려한 후에 결정을 내리나요?'},
        {'category': 'JP', 'text': '일을 시작하기 전에 계획을 철저히 세우나요?'},
        {'category': 'JP', 'text': '일을 하면서 계획을 세워나가나요?'},
        {'category': 'JP', 'text': '미리 계획된 일정에 따라 움직이는 것을 좋아하나요?'},
        {'category': 'JP', 'text': '상황에 따라 유연하게 대처하는 것을 좋아하나요?'},
    ]
    categories = {
        'EI': '외향형 (E) vs. 내향형 (I)',
        'SN': '감각형 (S) vs. 직관형 (N)',
        'TF': '사고형 (T) vs. 감정형 (F)',
        'JP': '판단형 (J) vs. 인식형 (P)'
    }
    context = {
        'questions': questions,
        'categories': categories
    }
    return render(request, 'poll/polls.html', context)

# result page
def result(request):
    return render(request, "poll/result.html")