1)	virtualenv -> virtualenvWrapper 이용
    : 디렉토리 일일이 진입하여 가상환경 만들기(activate) 불편
(vitualenv : 격리된 파이썬 환경을 만들기 위한 도구)

1 – virtualenvwrapper 설치
 pip install virtualenv virtualenvwrapper

2 – 환경변수 설정
$ mkdir ~/.virtualenvs (가상환경 디렉토리 설정)
$ export WORKON_HOME=~/.virtualenvs
$ source /usr/local/bin/virtualenvwrapper.sh

3 – command로 virtualenvwrapper 이용
Virtualenvwrapper 라고 치면 주요 명령어 리스트 출력 
*command
mkvirtualenv [가상환경 이름] : 가상환경 생성
rmvirtualenv [가상환경 이름] : 가상환경 삭제
workon [가상환경 이름] : 가상환경 진입
setvirtualenvproject : 프로젝트 디렉토리에서 해당 command 입력 시, 디렉토리와 가상환경 맵핑
deactivate : 가상환경 빠져나오기

=> 기존 virtualenv : source $WORKON_HOME/설정프로파일 디렉토리/bin/activate
=> Virtualenvwrapper : mkvirtualenv [가상환경 이름]
---------------------------------------------------------

2)	py manage.py migrate / py manage.py makemigrations
마이그레이션(Migration) ~ git에서 버전 생성하는 것과 유사함

*command
py manage.py makemigrations : 마이그레이션 생성
py manage.py migrate : 마이그레이션 적용
py manage.py showmigrations : 마이그레이션 적용 여부 알려줌
py manage.py sqlmigrate [app_name] [migration_name] : 해당 마이그레이션 파일이 어떤 SQL 구문으로 실행되는지 보여줌

*주의사항 : 적용된 마이그레이션 파일, 즉 이미 py manage.py migrate 한 파일은 절대로 삭제하면 안됨 
            -> 각 마이그레이션은 이전 버전에 대해 의존성을 가지기 때문 
            -> 마이그레이션 파일을 삭제하려면 반드시 적용 해제하고 삭제할 것
                 => 이전 버전으로 되돌린 후 삭제하거나 (py manage.py migrate [app_name] [이전 버전])
                 => 초기화 한 후 삭제 (py manage.py migrate [app_name] zero)



===========================================
py -m django --version 명령어를 실행하면 현재 활성화된 Python 환경에서 Django의 버전을 확인
"no module" 오류=>Django가 현재 Python 환경에 설치되어 있지 않은 경우
해결방안.
-가상 환경을 활성화
-가상 환경에 Django를 설치
-py -m django --version 명령어를 실행하여 Django의 버전을 확인
-------
새로운 오류 no module named pip=>Python이 pip를 찾지 못하는 것
-Python이 설치된 경로로 이동한 다음, get-pip.py 스크립트를 다운로드-
-python get-pip.py 명령어를 실행하여 pip를 설치
-해결
코드에서 장고에 노란줄 => 해당 모듈이 Python 환경에서 찾을 수 없기 때문에 발생
발생원인:
1. 모듈이 설치되어 있지 않은 경우
2. 모듈의 이름이 잘못된 경우
3. 모듈의 경로가 잘못 설정된 경우
해결법 :필요한 모듈 설치=>pip install django 명령어를 실행하여 Django 모듈을 설치

Index html파일 큰따옴표




