num_book={}
while True:
    func=input('원하시는 기능을 입력하세요.\n기능1 : 연락처 추가\n기능2 : 연락처 전체 보기\n기능3 : 연락처 검색\n기능4 : 연락처 수정\n기능5 : 연락처 삭제\n기능6 : 프로그램 종료\n')
    if func == '1':
        print('')
        name=input('추가할 이름: ')
        num=input('추가할 연락처: ')
        #num_book[name]=num
        num_book.setdefault(name,num)
        print('')
    elif func == '2':
        print('')
        print(num_book)
        print('')
    elif func == '3':
        print('')
        search=input('조회할 이름: ')
        print(num_book.get(search,'없는 연락처입니다.'))
        print('')
    elif func == '4':
        print('')
        modify=input('수정할 이름: ')
        if modify in num_book:
            num_book[modify]=input('수정할 번호: ')
            print(num_book)
        else:
            print('없는 전화번호입니다.')
        print('')
    elif func == '5':
        print('')
        delete=input('삭제할 이름: ')
        if delete in num_book:
            del num_book[delete]
            print(num_book)
        else:
            print('없는 전화번호입니다.')
        print('')
    elif func == '6':
        print('')
        print('프로그램을 종료합니다.')
        print('')
        break
    else:
        print('')
        print('다시 입력해주세요.')
        print('')