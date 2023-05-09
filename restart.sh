function killemall(){
    sudo ps aux | grep -e $1 | grep -v grep | awk '{print $2}' | xargs kill -9
}

export DJANGO_PORT=8080
alias run='python manage.py runserver'
alias rr='killemall manage.py;reset;run $DJANGO_PORT'
