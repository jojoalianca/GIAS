from django import forms
from django.core.validators import FileExtensionValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import PDFUpload
from .models import *
# from custom.models import *

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['title', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Hanya file PDF yang diperbolehkan.")
        return file
class DateInput(forms.DateInput):
    input_type = 'date'

class FunsionarioForm(forms.ModelForm):
    data_entrada = forms.DateField(label='data_entrada', widget=DateInput())
    class Meta:
        model = Funsionario
        fields = [
            'nome', 'sexu', 'cargo','regime','grau','level','background','scalaun','diresaun', 
            'departamentu', 'endereco', 'telefone', 'data_entrada', 
            'image', 'status', 'status_profisaun'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-5 mb-0'),
                Column('sexu', css_class='form-group col-md-2 mb-0'),
                Column('cargo', css_class='form-group col-md-5 mb-0'),
            ),
            Row(
                
                Column('regime', css_class='form-group col-md-1 mb-0'),
                Column('grau', css_class='form-group col-md-1 mb-0'),
                Column('level', css_class='form-group col-md-1 mb-0'),
                Column('background', css_class='form-group col-md-3 mb-0'),
                Column('scalaun', css_class='form-group col-md-3 mb-0'),
                Column('diresaun', css_class='form-group col-md-3 mb-0'),
               
                css_class='form-row'
            ),
            Row(
                
                Column('departamentu', css_class='form-group col-md-4 mb-0'),
                Column('endereco', css_class='form-group col-md-4 mb-0'),
                Column('telefone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('data_entrada', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-4 mb-0'),
                Column('status_profisaun', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
            ),
            
            HTML(""" <center> <img id='output' width='200' /> </center> """),
            HTML(
                """ <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML(
                """  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )

    # Validasi Telefone
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            # Hanya menerima angka dan panjang minimal 10 karakter
            if not telefone.isdigit():
                raise forms.ValidationError(" Numeru Telefone Tenke Hakerek Ho Numeru.")
            if len(telefone) < 8:
                raise forms.ValidationError("Numeru telefone tenke iha mais ou menus 8 digito.")
        return telefone

    # Validasi Email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Mengecek apakah email valid dengan menggunakan regex atau is_valid_email()
            if '@' not in email:
                raise forms.ValidationError("Email La Validu. Komfirma iha Sinal '@'.")
            if len(email) >50:
                raise forms.ValidationError("Email terlalu naruk. Maksimal 15 karakter.")
        return email

class ArquivuForm(forms.ModelForm):
    data_Arquivu = forms.DateField(label='data_Arquivu', widget=DateInput())
    documento_pdf = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]  # Validasi hanya PDF
    )
    class Meta:
        model = ArquivuRelatoriu
        fields = ['no_carta','data_Arquivu','departamento','titulo','hato_o_ba','documento_pdf']   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                
                Column('no_carta', css_class='form-group col-md-4 mb-0'),
                Column('data_Arquivu', css_class='form-group col-md-4 mb-0'),
                Column('departamento', css_class='form-group col-md-4 mb-0'),
                Column('titulo', css_class='form-group col-md-4 mb-0'),
                Column('hato_o_ba', css_class='form-group col-md-4 mb-0'),
                Column('documento_pdf', css_class='form-group col-md-4 mb-0'),
            ),
            HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )

class EntradaForm(forms.ModelForm):
    data_entrada = forms.DateField(label='data_entrada', widget=DateInput())
    data_dok = forms.DateField(label='data_dok', widget=DateInput())
    dokumen = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]  # Validasi hanya PDF
    )
    class Meta:
        model = KartaEntrada
        fields = ['remetente','destinatário','no_karta','data_entrada','data_dok','no_referensia','assunto','hato_o_ba',\
        'husi','dokumen','despaixa']   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                
                Column('remetente', css_class='form-group col-md-4 mb-0'),
                Column('destinatário', css_class='form-group col-md-4 mb-0'),
                Column('no_karta', css_class='form-group col-md-4 mb-0'),
                Column('data_entrada', css_class='form-group col-md-4 mb-0'),
                Column('data_dok', css_class='form-group col-md-4 mb-0'),
                Column('no_referensia', css_class='form-group col-md-4 mb-0'),
                Column('assunto', css_class='form-group col-md-4 mb-0'),
                Column('hato_o_ba', css_class='form-group col-md-4 mb-0'),
                Column('husi', css_class='form-group col-md-4 mb-0'),
            ),
            HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )

class KartaEntradaForm(forms.ModelForm):
    class Meta:
        model = KartaEntrada
        fields = ['despaixa', 'dokumen'] 

class ClienteRaiPointForm(forms.ModelForm):
    class Meta:
        model = ClienteRaiPoint
        fields = ['latitude', 'longitude', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                
                Column('latitude', css_class='form-group col-md-4 mb-0'),
                Column('longitude', css_class='form-group col-md-4 mb-0'),
                
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
            ),
            
            HTML(""" <center> <img id='output' width='200' /> </center> """),
            HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )