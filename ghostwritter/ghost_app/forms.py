from django import forms

class GeneralConfigForm(forms.Form):
    post_status = forms.ChoiceField(
        choices=[
            ('publish', 'Publié'),
            ('draft', 'Brouillon'),
            ('pending', 'En attente'),
            ('private', 'Privé'),
        ],
        label="Statut des articles",
        initial='publish' # Default value
    )
    search_language = forms.CharField(
        label="Langue de recherche",
        initial='fr' # Default value
    )
    num_results = forms.IntegerField(
        label="Nombre de résultats de recherche",
        initial=3, # Default value
        min_value=1 # Validation: minimum value
    )
    generation_mode = forms.ChoiceField(
        choices=[
            ('search', 'Recherche'),
            ('direct', 'Direct'),
        ],
        label="Mode de génération",
        initial='search' # Default value
    )
    search_domain = forms.CharField(
        label="Domaine de recherche",
        initial='com' # Default value
    )


class OpenAIConfigForm(forms.Form):
    openai_api_key = forms.CharField(
        label="API Key",
        widget=forms.Textarea(attrs={'rows': 2}) # Textarea widget for API key
    )
    openai_model = forms.CharField(
        label="Modèle",
        initial='gpt-4o' # Default value
    )


class WordPressConfigForm(forms.Form):
    wordpress_username = forms.CharField(label="Nom d'utilisateur")
    wordpress_password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput # PasswordInput widget for security
    )


class SiteKeywordForm(forms.Form):
    url = forms.CharField(
        label="URL du Site",
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}) # URL input type and placeholder
    )
    keyword = forms.CharField(label="Mot-clé",  widget=forms.TextInput(attrs={'placeholder': 'Mot-clé principal'})) # Placeholder