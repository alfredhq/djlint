from .analyzers.context_processors import ContextProcessorsAnalyzer
from .analyzers.db_backends import DB_BackendsAnalyzer
from .analyzers.formtools import FormToolsAnalyzer
from .analyzers.generic_views import GenericViewsAnalyzer
from .analyzers.render_to_response import RenderToResponseAnalyzer
from .analyzers.syntax_error import SyntaxErrorAnalyzer
from .analyzers.template_loaders import TemplateLoadersAnalyzer

from .parsers import Parser


ANALYZERS = (
    ContextProcessorsAnalyzer,
    DB_BackendsAnalyzer,
    FormToolsAnalyzer,
    GenericViewsAnalyzer,
    RenderToResponseAnalyzer,
    SyntaxErrorAnalyzer,
    TemplateLoadersAnalyzer,
)


def analyze(path):
    parsed_code = Parser(path).parse()
    for analyzer in ANALYZERS:
        for result in analyzer(parsed_code, path).analyze():
            yield result
