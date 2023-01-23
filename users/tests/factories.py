import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: 'First_%d' % n)
    last_name = factory.Sequence(lambda n: 'Last_%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'password')
    email = factory.Sequence(lambda n: 'user_%d@example.com' % n)

    class Meta:
        model = User
