def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject:score})
    else:
      subject_score.update({student:{subject:score}})
    return subject_score        

def calc_average_score(subject_score):
    dict = {}
    for i in subject_score:
        result = sum(subject_score[i].values())/len(subject_score[i])
        dict.update({i : f'{result:.2f}'})
    
    return dict
    
    