with open('file_task6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    my_dict = {}
    for i in lines:
        subject, lecture, practise, labor = i.split()
        lecture = lecture.replace('—', '0(')
        practise = practise.replace('—', '0(')
        labor = labor.replace('—', '0(')
        lecture = lecture.split('(')
        practise = practise.split('(')
        labor = labor.split('(')
        lecture[0] = int(lecture[0])
        practise[0] = int(practise[0])
        labor[0] = int(labor[0])
        hours = lecture[0] + practise[0] + labor[0]
        my_dict[subject] = hours
    print(my_dict)
