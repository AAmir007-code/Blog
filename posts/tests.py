from django.test import TestCase
from .models import PostModel
from django.contrib.auth.models import User
# Create your tests here.

class PostsTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='test_user',email='test@gmail.com')
        author_all = User.objects.get(username='test_user')
        PostModel.objects.create(title='TestTitle',body='first body',author=author_all)
        PostModel.objects.create(title='TestTitle2',author=author_all)

    def test_objects_titles(self):
        obj1 = PostModel.objects.get(title='TestTitle')
        obj2 = PostModel.objects.get(title='TestTitle2')
        self.assertEqual(str(obj1),'TestTitle')
        self.assertEqual(str(obj2), 'TestTitle2')
        self.assertEqual(obj1.get_author(),obj2.get_author())

    def test_templates(self):
        request = self.client.get('/')
        self.assertTemplateUsed(request,'posts/home.html')
        obj1 = PostModel.objects.get(title='TestTitle')
        request_url = '/post/'+str(obj1.id)
        request =self.client.get(request_url)
        self.assertTemplateUsed(request,'posts/detail.html')




