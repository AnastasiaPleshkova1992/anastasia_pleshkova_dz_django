from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Form for adding a new product."""
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_name(self):
        """Check that the product name is not banned."""
        cleaned_data = self.cleaned_data['product_name']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать в названии слово "{word}"')
        return cleaned_data

    def clean_product_description(self):
        """Check that the product description is not banned."""
        cleaned_data = self.cleaned_data['product_description']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать в описании слово "{word}"')
        return cleaned_data
