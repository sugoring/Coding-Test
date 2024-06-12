def solution(record):
    answer = []  # 최종 결과를 저장할 리스트
    trace = []  # Enter와 Leave 기록을 저장할 리스트
    Map = {}  # 사용자 ID와 닉네임을 매핑할 딕셔너리

    for i in range(len(record)):
        temp = record[i].split(' ')  # 기록을 공백 기준으로 분리
        
        if temp[0] == 'Enter':  # 사용자가 입장한 경우
            Map[temp[1]] = temp[2]  # 사용자 ID와 닉네임을 저장
            trace.append([temp[0], temp[1]])  # 입장 기록 추가
        elif temp[0] == 'Leave':  # 사용자가 퇴장한 경우
            trace.append([temp[0], temp[1]])  # 퇴장 기록 추가
        else:  # 사용자가 닉네임을 변경한 경우
            Map[temp[1]] = temp[2]  # 사용자 ID와 새로운 닉네임을 저장

    for i in range(len(trace)):
        if trace[i][0] == 'Enter':  # 입장 기록을 처리할 때
            result = Map[trace[i][1]] + "님이 들어왔습니다."  # 입장 메시지 생성
            answer.append(result)  # 결과 리스트에 추가
        else:  # 퇴장 기록을 처리할 때
            result = Map[trace[i][1]] + "님이 나갔습니다."  # 퇴장 메시지 생성
            answer.append(result)  # 결과 리스트에 추가

    return answer  # 최종 결과 반환
