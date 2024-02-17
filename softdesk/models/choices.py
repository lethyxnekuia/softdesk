from django.utils.translation import gettext as _


class TagChoice:
    BUG = 'Bug'
    FEATURE = 'Feature'
    TASK = 'Task'

    @classmethod
    def get_as_choices(cls):
        return [
            (cls.BUG, _(cls.BUG)),
            (cls.FEATURE, _(cls.FEATURE)),
            (cls.TASK, _(cls.TASK)),
        ]


class PriorityChoice:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    @classmethod
    def get_as_choices(cls):
        return [
            (cls.HIGH, _(cls.HIGH)),
            (cls.MEDIUM, _(cls.MEDIUM)),
            (cls.LOW, _(cls.LOW)),
        ]


class StatusChoice:
    IN_PROGRESS = 'In Progress'
    TO_DO = 'To Do'
    FINISHED = 'Finished'

    @classmethod
    def get_as_choices(cls):
        return [
            (cls.IN_PROGRESS, _(cls.IN_PROGRESS)),
            (cls.TO_DO, _(cls.TO_DO)),
            (cls.FINISHED, _(cls.FINISHED)),
        ]


class ProjectTypeChoice:
    BACK = 'back-end'
    FRONT = 'front-end'
    IOS = 'ios'
    ANDROID = 'android'

    @classmethod
    def get_as_choices(cls):
        return [
            (cls.BACK, _(cls.BACK)),
            (cls.FRONT, _(cls.FRONT)),
            (cls.IOS, _(cls.IOS)),
            (cls.ANDROID, _(cls.ANDROID)),
        ]
