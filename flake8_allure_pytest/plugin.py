import ast

from flake8_plugin_utils import Plugin, Visitor, Error


__version__ = '0.1.0'

_T_CLASS_DECORATORS = ['feature', 'story']
_T_METHOD_DECORATORS = ['description']


class MissingTestClassTagError(Error):
    code = 'AL001'
    message = "class '{name}' should have {tags} tags"


class MissingTestMethodTagError(Error):
    code = 'AL002'
    message = "method '{name}' should have 'description' tag"


def is_test_class(node):
    return node.name.startswith('Test')


def is_test_method(node):
    return node.name.startswith('test_')


class FlakeAllurePytestVisitor(Visitor):

    def _check_node_decorators(self, node, decorators):
        required_decorators = set(decorators)

        for decorator in node.decorator_list:
            if isinstance(decorator.func, ast.Name):
                required_decorators.discard(decorator.func.id)
            if isinstance(decorator.func, ast.Attribute):
                required_decorators.discard(decorator.func.attr)

        if required_decorators:
            if isinstance(node, ast.ClassDef):
                self.error_from_node(
                    MissingTestClassTagError, node, name=node.name, tags=str(required_decorators)[1:-1]
                )
            elif isinstance(node, ast.FunctionDef):
                self.error_from_node(
                    MissingTestMethodTagError, node, name=node.name
                )

    def visit_ClassDef(self, node) -> None:
        if is_test_class(node):
            self._check_node_decorators(node, decorators=_T_CLASS_DECORATORS)

            for method in node.body:
                if is_test_method(method):
                    self._check_node_decorators(method, decorators=_T_METHOD_DECORATORS)


class AllurePytestPlugin(Plugin):
    name = 'flake8_allure_pytest'
    version = __version__
    visitors = [FlakeAllurePytestVisitor]
