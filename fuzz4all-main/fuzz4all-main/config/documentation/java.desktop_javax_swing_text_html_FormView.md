# Class FormView

**Source:** `java.desktop\javax\swing\text\html\FormView.html`

### Class Description

```java
public class
FormView

extends
ComponentView

implements
ActionListener
```

Component decorator that implements the view interface
for form elements, <input>, <textarea>,
and <select>. The model for the component is stored
as an attribute of the element (using StyleConstants.ModelAttribute),
and is used to build the component of the view. The type
of the model is assumed to of the type that would be set by

HTMLDocument.HTMLReader.FormAction

. If there are
multiple views mapped over the document, they will share the
embedded component models.

The following table shows what components get built
by this view.

Shows what components get built by this view

Element Type

Component built

input, type button

JButton

input, type checkbox

JCheckBox

input, type image

JButton

input, type password

JPasswordField

input, type radio

JRadioButton

input, type reset

JButton

input, type submit

JButton

input, type text

JTextField

select, size > 1 or multiple attribute defined

JList in a JScrollPane

select, size unspecified or 1

JComboBox

textarea

JTextArea in a JScrollPane

input, type file

JTextField

**All Implemented Interfaces:** ActionListener

,

EventListener

,

SwingConstants

---

### Field Details

#### @Deprecated

public static final
String
SUBMIT

If a value attribute is not specified for a FORM input element
of type "submit", then this default string is used.

---

#### @Deprecated

public static final
String
RESET

If a value attribute is not specified for a FORM input element
of type "reset", then this default string is used.

---

### Constructor Details

#### public FormView​(
Element
elem)

Creates a new FormView object.

**Parameters:**
- elem

- the element to decorate

---

### Method Details

#### protected
Component
createComponent()

Create the component. This is basically a
big switch statement based upon the tag type
and html attributes of the associated element.

**Overrides:**
- createComponent

in class

ComponentView

**Returns:**
- the component that is associated with
this view

---

#### public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. For certain components, the maximum and preferred span are the
same. For others this will return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:**
- getMaximumSpan

in class

ComponentView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public void actionPerformed​(
ActionEvent
evt)

Responsible for processing the ActionEvent.
If the element associated with the FormView,
has a type of "submit", "reset", "text" or "password"
then the action is processed. In the case of a "submit"
the form is submitted. In the case of a "reset"
the form is reset to its original state.
In the case of "text" or "password", if the
element is the last one of type "text" or "password",
the form is submitted. Otherwise, focus is transferred
to the next component in the form.

**Specified by:**
- actionPerformed

in interface

ActionListener

**Parameters:**
- evt

- the ActionEvent.

---

#### protected void submitData​(
String
data)

This method is responsible for submitting the form data.
A thread is forked to undertake the submission.

**Parameters:**
- data

- data to submit

---

#### protected void imageSubmit​(
String
imageData)

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

**Parameters:**
- imageData

- the mouse click coordinates.

---

### Additional Sections

#### Class FormView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.ComponentView
- - javax.swing.text.html.FormView

javax.swing.text.View

- javax.swing.text.ComponentView
- - javax.swing.text.html.FormView

javax.swing.text.ComponentView

- javax.swing.text.html.FormView

javax.swing.text.html.FormView

**All Implemented Interfaces:** ActionListener

,

EventListener

,

SwingConstants

```java
public class
FormView

extends
ComponentView

implements
ActionListener
```

Component decorator that implements the view interface
for form elements, <input>, <textarea>,
and <select>. The model for the component is stored
as an attribute of the element (using StyleConstants.ModelAttribute),
and is used to build the component of the view. The type
of the model is assumed to of the type that would be set by

HTMLDocument.HTMLReader.FormAction

. If there are
multiple views mapped over the document, they will share the
embedded component models.

The following table shows what components get built
by this view.

Shows what components get built by this view

Element Type

Component built

input, type button

JButton

input, type checkbox

JCheckBox

input, type image

JButton

input, type password

JPasswordField

input, type radio

JRadioButton

input, type reset

JButton

input, type submit

JButton

input, type text

JTextField

select, size > 1 or multiple attribute defined

JList in a JScrollPane

select, size unspecified or 1

JComboBox

textarea

JTextArea in a JScrollPane

input, type file

JTextField

public class

FormView

extends

ComponentView

implements

ActionListener

Component decorator that implements the view interface
for form elements, <input>, <textarea>,
and <select>. The model for the component is stored
as an attribute of the element (using StyleConstants.ModelAttribute),
and is used to build the component of the view. The type
of the model is assumed to of the type that would be set by

HTMLDocument.HTMLReader.FormAction

. If there are
multiple views mapped over the document, they will share the
embedded component models.

The following table shows what components get built
by this view.

Shows what components get built by this view

Element Type

Component built

input, type button

JButton

input, type checkbox

JCheckBox

input, type image

JButton

input, type password

JPasswordField

input, type radio

JRadioButton

input, type reset

JButton

input, type submit

JButton

input, type text

JTextField

select, size > 1 or multiple attribute defined

JList in a JScrollPane

select, size unspecified or 1

JComboBox

textarea

JTextArea in a JScrollPane

input, type file

JTextField

The following table shows what components get built
by this view.

Shows what components get built by this view

Element Type

Component built

input, type button

JButton

input, type checkbox

JCheckBox

input, type image

JButton

input, type password

JPasswordField

input, type radio

JRadioButton

input, type reset

JButton

input, type submit

JButton

input, type text

JTextField

select, size > 1 or multiple attribute defined

JList in a JScrollPane

select, size unspecified or 1

JComboBox

textarea

JTextArea in a JScrollPane

input, type file

JTextField

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

FormView.MouseEventListener

MouseEventListener class to handle form submissions when
an input with type equal to image is clicked on.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

RESET

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

static

String

SUBMIT

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FormView

​(

Element

elem)

Creates a new FormView object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

evt)

Responsible for processing the ActionEvent.

protected

Component

createComponent

()

Create the component.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

protected void

imageSubmit

​(

String

imageData)

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

protected void

submitData

​(

String

data)

This method is responsible for submitting the form data.

- Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMinimumSpan

,

getPreferredSpan

,

modelToView

,

paint

,

setParent

,

viewToModel

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

FormView.MouseEventListener

MouseEventListener class to handle form submissions when
an input with type equal to image is clicked on.

---

#### Nested Class Summary

MouseEventListener class to handle form submissions when
an input with type equal to image is clicked on.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

RESET

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

static

String

SUBMIT

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

---

#### Fields declared in class javax.swing.text. View

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

FormView

​(

Element

elem)

Creates a new FormView object.

---

#### Constructor Summary

Creates a new FormView object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

evt)

Responsible for processing the ActionEvent.

protected

Component

createComponent

()

Create the component.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

protected void

imageSubmit

​(

String

imageData)

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

protected void

submitData

​(

String

data)

This method is responsible for submitting the form data.

- Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMinimumSpan

,

getPreferredSpan

,

modelToView

,

paint

,

setParent

,

viewToModel

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Responsible for processing the ActionEvent.

Create the component.

Determines the maximum span for this view along an
axis.

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

This method is responsible for submitting the form data.

Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMinimumSpan

,

getPreferredSpan

,

modelToView

,

paint

,

setParent

,

viewToModel

---

#### Methods declared in class javax.swing.text. ComponentView

Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

---

#### Methods declared in class javax.swing.text. View

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- SUBMIT

```java
@Deprecated

public static final
String
SUBMIT
```

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

If a value attribute is not specified for a FORM input element
of type "submit", then this default string is used.

- RESET

```java
@Deprecated

public static final
String
RESET
```

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

If a value attribute is not specified for a FORM input element
of type "reset", then this default string is used.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FormView

```java
public FormView​(
Element
elem)
```

Creates a new FormView object.

**Parameters:** elem

- the element to decorate

============ METHOD DETAIL ==========

- Method Detail

- createComponent

```java
protected
Component
createComponent()
```

Create the component. This is basically a
big switch statement based upon the tag type
and html attributes of the associated element.

**Overrides:** createComponent

in class

ComponentView
**Returns:** the component that is associated with
this view

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. For certain components, the maximum and preferred span are the
same. For others this will return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

ComponentView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
evt)
```

Responsible for processing the ActionEvent.
If the element associated with the FormView,
has a type of "submit", "reset", "text" or "password"
then the action is processed. In the case of a "submit"
the form is submitted. In the case of a "reset"
the form is reset to its original state.
In the case of "text" or "password", if the
element is the last one of type "text" or "password",
the form is submitted. Otherwise, focus is transferred
to the next component in the form.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** evt

- the ActionEvent.

- submitData

```java
protected void submitData​(
String
data)
```

This method is responsible for submitting the form data.
A thread is forked to undertake the submission.

**Parameters:** data

- data to submit

- imageSubmit

```java
protected void imageSubmit​(
String
imageData)
```

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

**Parameters:** imageData

- the mouse click coordinates.

Field Detail

- SUBMIT

```java
@Deprecated

public static final
String
SUBMIT
```

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

If a value attribute is not specified for a FORM input element
of type "submit", then this default string is used.

- RESET

```java
@Deprecated

public static final
String
RESET
```

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

If a value attribute is not specified for a FORM input element
of type "reset", then this default string is used.

---

#### Field Detail

SUBMIT

```java
@Deprecated

public static final
String
SUBMIT
```

Deprecated.

As of 1.3, value now comes from UIManager property
FormView.submitButtonText

If a value attribute is not specified for a FORM input element
of type "submit", then this default string is used.

---

#### SUBMIT

@Deprecated

public static final

String

SUBMIT

If a value attribute is not specified for a FORM input element
of type "submit", then this default string is used.

RESET

```java
@Deprecated

public static final
String
RESET
```

Deprecated.

As of 1.3, value comes from UIManager UIManager property
FormView.resetButtonText

If a value attribute is not specified for a FORM input element
of type "reset", then this default string is used.

---

#### RESET

@Deprecated

public static final

String

RESET

If a value attribute is not specified for a FORM input element
of type "reset", then this default string is used.

Constructor Detail

- FormView

```java
public FormView​(
Element
elem)
```

Creates a new FormView object.

**Parameters:** elem

- the element to decorate

---

#### Constructor Detail

FormView

```java
public FormView​(
Element
elem)
```

Creates a new FormView object.

**Parameters:** elem

- the element to decorate

---

#### FormView

public FormView​(

Element

elem)

Creates a new FormView object.

Method Detail

- createComponent

```java
protected
Component
createComponent()
```

Create the component. This is basically a
big switch statement based upon the tag type
and html attributes of the associated element.

**Overrides:** createComponent

in class

ComponentView
**Returns:** the component that is associated with
this view

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. For certain components, the maximum and preferred span are the
same. For others this will return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

ComponentView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
evt)
```

Responsible for processing the ActionEvent.
If the element associated with the FormView,
has a type of "submit", "reset", "text" or "password"
then the action is processed. In the case of a "submit"
the form is submitted. In the case of a "reset"
the form is reset to its original state.
In the case of "text" or "password", if the
element is the last one of type "text" or "password",
the form is submitted. Otherwise, focus is transferred
to the next component in the form.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** evt

- the ActionEvent.

- submitData

```java
protected void submitData​(
String
data)
```

This method is responsible for submitting the form data.
A thread is forked to undertake the submission.

**Parameters:** data

- data to submit

- imageSubmit

```java
protected void imageSubmit​(
String
imageData)
```

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

**Parameters:** imageData

- the mouse click coordinates.

---

#### Method Detail

createComponent

```java
protected
Component
createComponent()
```

Create the component. This is basically a
big switch statement based upon the tag type
and html attributes of the associated element.

**Overrides:** createComponent

in class

ComponentView
**Returns:** the component that is associated with
this view

---

#### createComponent

protected

Component

createComponent()

Create the component. This is basically a
big switch statement based upon the tag type
and html attributes of the associated element.

getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. For certain components, the maximum and preferred span are the
same. For others this will return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

ComponentView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getMaximumSpan

public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. For certain components, the maximum and preferred span are the
same. For others this will return the value
returned by Component.getMaximumSize along the
axis of interest.

actionPerformed

```java
public void actionPerformed​(
ActionEvent
evt)
```

Responsible for processing the ActionEvent.
If the element associated with the FormView,
has a type of "submit", "reset", "text" or "password"
then the action is processed. In the case of a "submit"
the form is submitted. In the case of a "reset"
the form is reset to its original state.
In the case of "text" or "password", if the
element is the last one of type "text" or "password",
the form is submitted. Otherwise, focus is transferred
to the next component in the form.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** evt

- the ActionEvent.

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

evt)

Responsible for processing the ActionEvent.
If the element associated with the FormView,
has a type of "submit", "reset", "text" or "password"
then the action is processed. In the case of a "submit"
the form is submitted. In the case of a "reset"
the form is reset to its original state.
In the case of "text" or "password", if the
element is the last one of type "text" or "password",
the form is submitted. Otherwise, focus is transferred
to the next component in the form.

submitData

```java
protected void submitData​(
String
data)
```

This method is responsible for submitting the form data.
A thread is forked to undertake the submission.

**Parameters:** data

- data to submit

---

#### submitData

protected void submitData​(

String

data)

This method is responsible for submitting the form data.
A thread is forked to undertake the submission.

imageSubmit

```java
protected void imageSubmit​(
String
imageData)
```

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

**Parameters:** imageData

- the mouse click coordinates.

---

#### imageSubmit

protected void imageSubmit​(

String

imageData)

This method is called to submit a form in response
to a click on an image -- an <INPUT> form
element of type "image".

---

