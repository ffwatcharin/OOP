def add_score(subject_score, subject, score):
    subject_score.update({subject : score})
    return subject_score


def calc_average_score(subject_score):
    return f'{sum(subject_score.values())/len(subject_score):.2f}'

    



