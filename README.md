# Custom DatalistField Wtffield

## Overview

The DatalistField is a powerful custom field in the Flask web app forms, utilizing the native HTML <datalist> element. It enhances the functionality of datalists in web forms by incorporating two custom components: the DataListWidget and the CustomOptionWidget. Through these components, it provides advanced features for auto-suggestions, filtering, and customization options, resulting in a seamless and intuitive user experience.

When integrated with Flask's WTForms library, the DatalistField can be easily used as a custom field within the web application's forms. This allows developers to leverage its enhanced capabilities and make data entry and selection a more efficient process for users. By combining Flask, WTForms, and the DatalistField, developers can create dynamic and interactive web forms with improved user interaction and overall user experience.

## Features

- **Filtering:** The DatalistField supports filtering options, enabling users to narrow down the list of available items by typing specific keywords.

- **Easy Integration:** The component is designed for easy integration into existing web applications. It inherits from the **SelectField** component.

- **Auto-suggestions**: As the user types into the input field, the component provides real-time suggestions based on the predefined list of items. This feature helps users quickly find and select the desired item.

- **CustomOptionWidget:** The CustomOptionWidget allows developers to customize the options displayed in the datalist. This enables the addition of custom styles, icons, or other elements to enhance the user interface.

## Installation

```shell
git clone git@github.com:omarelkashef/DatalistField.git
```

## How to Use

```python
from DatalistField.py import DatalistField

class Form(FlaskForm):
    field = DatalistField()

if request.method == "GET":
    form = Form()
    form.field.choices = [("", "")] + [
            (choice.name, str(choice.id)) for choice in choices
            ]

```




  
