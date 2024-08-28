from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=None, videos=None, current_user: User = None):
        if videos is None:
            videos = []
        if users is None:
            users = []
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def __str__(self):
        return self.current_user.nickname

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                print('Успешная авторизация!')
                return True
            else:
                return False

    def register(self, nickname: str, password: str, age: int):
        if nickname in [user.nickname for user in self.users]:
            print(f'Пользователь {nickname} уже существует!')
        else:
            self.users.append(User(nickname, password, age))
            print('Успешная регистрация!')
            self.current_user = self.users[-1]
            print('Вы авторизованы!')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if isinstance(arg, Video) and arg.title not in [video.title for video in self.videos]:
                self.videos.append(arg)
                print('Видео добавлено!')

    def get_videos(self, keyword: str):
        print([video.title for video in self.videos if keyword.lower() in video.title.lower()])

    def watch_video(self, title: str):
        for video in self.videos:
            if video.title == title:
                if self.current_user:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу!')
                    else:
                        for i in range(video.duration):
                            sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=' ')
                            if video.time_now == video.duration:
                                print('Конец видео!')
                                video.time_now = 0
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео!')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')