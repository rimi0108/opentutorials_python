
user_id = 'hye1111'
user_passwd = 'rim2222'

id = input('아이디를 입력하세요 : ')
passwd = input('비밀번호를 입력하세요 : ')

if id == user_id and passwd == user_passwd:
    print(id + '님 환영합니다.')
elif id != user_id and passwd == user_passwd:
    print('아이디가 일치하지 않습니다.')
elif id == user_id and passwd != user_passwd:
    print('비밀번호가 일치하지 않습니다.')
elif id != user_id and passwd != user_passwd:
    print('아이디와 비밀번호가 일치하지 않습니다.')



