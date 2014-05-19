from django.contrib import admin
from rolls.models import SlowRoll
from django import forms


class FormatedTextInput(forms.Textarea):
    pass

class SlowRollForm(forms.ModelForm):
    class Meta:
        model = SlowRoll
        widgets = {"description" : FormatedTextInput(attrs={'class': 'redactor'})}

    #@property
    #def media(self):
    #    css = {'all': ('vendor/redactor/redactor/redactor.css', ) }
    #    js = ['vendor/jquery-2.0.3.min.js', 'vendor/redactor/redactor/redactor.js', 'vendor/redactor/init_redactor.js', ] 
    #    return forms.Media(js=js, css=css)

class SlowRollAdmin(admin.ModelAdmin):
    form=SlowRollForm
    class Media:
        css = {'all': ('vendor/redactor/redactor/redactor.css', ) }
        js = ('vendor/jquery-2.0.3.min.js', 'vendor/redactor/redactor/redactor.js', 'vendor/redactor/init_redactor.js', )

admin.site.register(SlowRoll, SlowRollAdmin)
