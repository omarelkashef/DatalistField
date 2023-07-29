from markupsafe import Markup, escape
from wtforms.fields import SelectField
from wtforms.widgets import Select
from wtforms.widgets.core import html_params

class DatalistWidget(Select):
    """
    A custom widget class that represents a Datalist input element.

    This widget is used in combination with the DatalistField to provide an autocomplete feature.

    :param multiple: If True, allows multiple selections; defaults to False.
    :type multiple: bool
    """

    def __init__(self, multiple=False):
        """
        Initialize the DatalistWidget.

        :param multiple: If True, allows multiple selections; defaults to False.
        :type multiple: bool
        """
        super().__init__(multiple)

    def __call__(self, field, **kwargs):
        """
        Render DatalistWidget.

        :param field: The form field for which to render the widget.
        :type field: wtforms.fields.core.Field
        :param kwargs: Additional attributes to apply to the widget.
        :returns: The rendered HTML markup of the DatalistWidget.
        :rtype: Markup
        """
        kwargs.setdefault("id", field.id)
        if "required" not in kwargs and "required" in getattr(field, "flags", []):
            kwargs["required"] = True
        params = html_params(name=field.name, **kwargs)
        html = [
            f'<input autocomplete=off list={kwargs["id"]} name={field.name}> \n <datalist {params} />'
        ]
        for val, label, selected in field.iter_choices():
            html.append(self.render_option(val, label, selected))
        html.append("</datalist>")
        return Markup("".join(html))

    @classmethod
    def render_option(cls, value, label, selected, **kwargs):
        """
        Render an option element.

        :param value: The value of the option.
        :param label: The label to display for the option.
        :param selected: True if the option is selected, False otherwise.
        :param kwargs: Additional attributes to apply to the option element.
        :returns: The rendered HTML markup of the option.
        :rtype: Markup
        """
        if value is True:
            # Handle the special case of a 'True' value.
            value = str(value)

        options = dict(kwargs, value=value)
        if selected:
            options["selected"] = True
        return Markup(f"<option {html_params(**options)}>{escape(label)}</option>")


class CustomOptionWidget(object):
    """
    A custom widget class that renders a custom option element for DatalistField.

    This widget is used by DatalistField to render individual options.
    """

    def __call__(self, field, **kwargs):
        """
        Render option widget.

        :param field: The form field for which to render the custom option widget.
        :type field: wtforms.fields.core.Field
        :param kwargs: Additional attributes to apply to the custom option widget.
        :returns: The rendered HTML markup of the custom option widget.
        :rtype: Markup
        """
        return DatalistField.render_option(
            field._value(), field.label.text, field.checked, **kwargs
        )


class DatalistField(SelectField):
    """
    A custom form field class that represents a Datalist input field.

    This field uses the DatalistWidget as the default widget for rendering.

    :ivar widget: The widget used to render the field; defaults to DatalistWidget.
    :vartype widget: DatalistWidget
    :ivar option_widget: The widget used to render individual options in the field; defaults to CustomOptionWidget.
    :vartype option_widget: CustomOptionWidget
    """

    widget = DatalistWidget()
    option_widget = CustomOptionWidget()