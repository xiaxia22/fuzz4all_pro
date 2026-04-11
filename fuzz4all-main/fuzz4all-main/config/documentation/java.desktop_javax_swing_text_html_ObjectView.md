# Class ObjectView

**Source:** `java.desktop\javax\swing\text\html\ObjectView.html`

### Class Description

```java
public class
ObjectView

extends
ComponentView
```

Component decorator that implements the view interface
for <object> elements.

This view will try to load the class specified by the

classid

attribute. If possible, the Classloader
used to load the associated Document is used.
This would typically be the same as the ClassLoader
used to load the EditorKit. If the document's
ClassLoader is null,

Class.forName

is used.

If the class can successfully be loaded, an attempt will
be made to create an instance of it by calling

Class.newInstance

. An attempt will be made
to narrow the instance to type

java.awt.Component

to display the object.

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public ObjectView​(
Element
elem)

Creates a new ObjectView object.

**Parameters:**
- elem

- the element to decorate

---

### Method Details

#### protected
Component
createComponent()

Create the component. The classid is used
as a specification of the classname, which
we try to load.

**Overrides:**
- createComponent

in class

ComponentView

**Returns:**
- the component that is associated with
this view

---

### Additional Sections

#### Class ObjectView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.ComponentView
- - javax.swing.text.html.ObjectView

javax.swing.text.View

- javax.swing.text.ComponentView
- - javax.swing.text.html.ObjectView

javax.swing.text.ComponentView

- javax.swing.text.html.ObjectView

javax.swing.text.html.ObjectView

**All Implemented Interfaces:** SwingConstants

```java
public class
ObjectView

extends
ComponentView
```

Component decorator that implements the view interface
for <object> elements.

This view will try to load the class specified by the

classid

attribute. If possible, the Classloader
used to load the associated Document is used.
This would typically be the same as the ClassLoader
used to load the EditorKit. If the document's
ClassLoader is null,

Class.forName

is used.

If the class can successfully be loaded, an attempt will
be made to create an instance of it by calling

Class.newInstance

. An attempt will be made
to narrow the instance to type

java.awt.Component

to display the object.

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

public class

ObjectView

extends

ComponentView

Component decorator that implements the view interface
for <object> elements.

This view will try to load the class specified by the

classid

attribute. If possible, the Classloader
used to load the associated Document is used.
This would typically be the same as the ClassLoader
used to load the EditorKit. If the document's
ClassLoader is null,

Class.forName

is used.

If the class can successfully be loaded, an attempt will
be made to create an instance of it by calling

Class.newInstance

. An attempt will be made
to narrow the instance to type

java.awt.Component

to display the object.

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

This view will try to load the class specified by the

classid

attribute. If possible, the Classloader
used to load the associated Document is used.
This would typically be the same as the ClassLoader
used to load the EditorKit. If the document's
ClassLoader is null,

Class.forName

is used.

If the class can successfully be loaded, an attempt will
be made to create an instance of it by calling

Class.newInstance

. An attempt will be made
to narrow the instance to type

java.awt.Component

to display the object.

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

If the class can successfully be loaded, an attempt will
be made to create an instance of it by calling

Class.newInstance

. An attempt will be made
to narrow the instance to type

java.awt.Component

to display the object.

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

This view can also manage a set of parameters with limitations.
The parameters to the <object> element are expected to
be present on the associated elements attribute set as simple
strings. Each bean property will be queried as a key on
the AttributeSet, with the expectation that a non-null value
(of type String) will be present if there was a parameter
specification for the property. Reflection is used to
set the parameter. Currently, this is limited to a very
simple single parameter of type String.

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

A simple example HTML invocation is:

```java
<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>
```

<object classid="javax.swing.JLabel">
<param name="text" value="sample text">
</object>

=========== FIELD SUMMARY ===========

- Field Summary

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

ObjectView

​(

Element

elem)

Creates a new ObjectView object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Component

createComponent

()

Create the component.

- Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMaximumSpan

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

Field Summary

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

ObjectView

​(

Element

elem)

Creates a new ObjectView object.

---

#### Constructor Summary

Creates a new ObjectView object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Component

createComponent

()

Create the component.

- Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMaximumSpan

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

Create the component.

Methods declared in class javax.swing.text.

ComponentView

getAlignment

,

getComponent

,

getMaximumSpan

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ObjectView

```java
public ObjectView​(
Element
elem)
```

Creates a new ObjectView object.

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

Create the component. The classid is used
as a specification of the classname, which
we try to load.

**Overrides:** createComponent

in class

ComponentView
**Returns:** the component that is associated with
this view

Constructor Detail

- ObjectView

```java
public ObjectView​(
Element
elem)
```

Creates a new ObjectView object.

**Parameters:** elem

- the element to decorate

---

#### Constructor Detail

ObjectView

```java
public ObjectView​(
Element
elem)
```

Creates a new ObjectView object.

**Parameters:** elem

- the element to decorate

---

#### ObjectView

public ObjectView​(

Element

elem)

Creates a new ObjectView object.

Method Detail

- createComponent

```java
protected
Component
createComponent()
```

Create the component. The classid is used
as a specification of the classname, which
we try to load.

**Overrides:** createComponent

in class

ComponentView
**Returns:** the component that is associated with
this view

---

#### Method Detail

createComponent

```java
protected
Component
createComponent()
```

Create the component. The classid is used
as a specification of the classname, which
we try to load.

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

Create the component. The classid is used
as a specification of the classname, which
we try to load.

---

