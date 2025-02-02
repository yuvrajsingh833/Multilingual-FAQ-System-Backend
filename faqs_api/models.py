from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from deep_translator import GoogleTranslator

class FAQ(models.Model):
    question = models.TextField(null=True)
    answer = RichTextField()

    async def get_translation(self, lang='en', field='question'):
        cached_key = f'faq_{self.id}_{field}_{lang}'
        cached_translation = cache.get(cached_key)

        if cached_translation:
            return cached_translation
        
        text_to_translate = self.answer if field == 'answer' else self.question

        try:
            translation_result =GoogleTranslator(source='auto', target=lang).translate(text_to_translate)
            
        except Exception as e:
            print(f"Translation failed: {e}")
            return text_to_translate

        cache.set(cached_key, translation_result, timeout=3600)
        return translation_result

    def __str__(self):
        return self.question
