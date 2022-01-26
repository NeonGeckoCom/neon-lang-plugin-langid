from ovos_plugin_manager.templates.language import LanguageDetector
from langid.langid import LanguageIdentifier, model


class LangIdPyDetector(LanguageDetector):
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

    def detect(self, text):
        return self.identifier.classify(text)[0]

    def detect_probs(self, text):
        l, p = self.identifier.classify(text)
        return {l: p}
