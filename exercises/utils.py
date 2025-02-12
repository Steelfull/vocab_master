# exercises/utils.py
def calculate_difficulty(user):
    success_rate = Exercise.objects.filter(
        user=user,
        items__is_correct=True
    ).count() / ExerciseItem.objects.filter(
        exercise__user=user
    ).count()
    
    if success_rate > 0.8:
        return {'level': 'advanced', 'cases': ['akkusativ', 'dativ']}
    elif success_rate > 0.5:
        return {'level': 'intermediate', 'cases': ['nominativ', 'akkusativ']}
    else:
        return {'level': 'basic', 'cases': ['nominativ']}