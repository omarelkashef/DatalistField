# Custom DatalistField Wtffield

## Overview

The Custom DatalistField Wtffield is a powerful custom web component that enhances the functionality of datalists in web forms. It extends the native HTML `<datalist>` element by incorporating two custom components: the **DataListWidget** and the **CustomOptionWidget**. These components provide advanced features for auto-suggestions, filtering, and customization options, offering a seamless and intuitive user experience.

![Custom DatalistField Wtffield](https://example.com/path/to/image.png)

## Features

- **Filtering:** The DatalistField supports filtering options, enabling users to narrow down the list of available items by typing specific keywords.

- **Easy Integration:** The component is designed for easy integration into existing web applications. It inherits from the **SelectField** component, ensuring compatibility with the native HTML `<select>` element.

- **Auto-suggestions**: As the user types into the input field, the component provides real-time suggestions based on the predefined list of items. This feature helps users quickly find and select the desired item.

- **Customization**: Developers can easily customize the look and feel of the Custom Datalist Wtffield to match the overall design of their web application. CSS classes and styles can be modified to achieve the desired appearance.

- **CustomOptionWidget:** The CustomOptionWidget allows developers to customize the options displayed in the datalist. This enables the addition of custom styles, icons, or other elements to enhance the user interface.

## Installation

`git clone git@github.com:omarelkashef/DatalistField.git`

## How to Use

```
from DatalistField.py import DatalistField

class Form(FlaskForm):
    field = DatalistField()

if request.method == "GET":
    form = Form()
    form.field.choices = [("", "")] + [
            (choice.name, str(choice.id)) for choice in choices
            ]

```




  
