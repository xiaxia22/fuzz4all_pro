# Class PropertyEditorSupport

**Source:** `java.desktop\java\beans\PropertyEditorSupport.html`

### Class Description

```java
public class
PropertyEditorSupport

extends
Object

implements
PropertyEditor
```

This is a support class to help build property editors.

It can be used either as a base class or as a delegate.

**All Implemented Interfaces:** PropertyEditor

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyEditorSupport()

Constructs a

PropertyEditorSupport

object.

**Since:**
- 1.5

---

#### public PropertyEditorSupport​(
Object
source)

Constructs a

PropertyEditorSupport

object.

**Parameters:**
- source

- the source used for event firing

**Since:**
- 1.5

---

### Method Details

#### public
Object
getSource()

Returns the bean that is used as the
source of events. If the source has not
been explicitly set then this instance of

PropertyEditorSupport

is returned.

**Returns:**
- the source object or this instance

**Since:**
- 1.5

---

#### public void setSource​(
Object
source)

Sets the source bean.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

**Parameters:**
- source

- source object to be used for events

**Since:**
- 1.5

---

#### public void setValue​(
Object
value)

Set (or change) the object that is to be edited.

**Specified by:**
- setValue

in interface

PropertyEditor

**Parameters:**
- value

- The new target object to be edited. Note that this
object should not be modified by the PropertyEditor, rather
the PropertyEditor should create a new object to hold any
modified value.

---

#### public
Object
getValue()

Gets the value of the property.

**Specified by:**
- getValue

in interface

PropertyEditor

**Returns:**
- The value of the property.

---

#### public boolean isPaintable()

Determines whether the class will honor the paintValue method.

**Specified by:**
- isPaintable

in interface

PropertyEditor

**Returns:**
- True if the class will honor the paintValue method.

---

#### public void paintValue​(
Graphics
gfx,

Rectangle
box)

Paint a representation of the value into a given area of screen
real estate. Note that the propertyEditor is responsible for doing
its own clipping so that it fits into the given rectangle.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

**Specified by:**
- paintValue

in interface

PropertyEditor

**Parameters:**
- gfx

- Graphics object to paint into.
- box

- Rectangle within graphics object into which we should paint.

---

#### public
String
getJavaInitializationString()

This method is intended for use when generating Java code to set
the value of the property. It should return a fragment of Java code
that can be used to initialize a variable with the current property
value.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

**Specified by:**
- getJavaInitializationString

in interface

PropertyEditor

**Returns:**
- A fragment of Java code representing an initializer for the
current value.

---

#### public
String
getAsText()

Gets the property value as a string suitable for presentation
to a human to edit.

**Specified by:**
- getAsText

in interface

PropertyEditor

**Returns:**
- The property value as a string suitable for presentation
to a human to edit.

Returns null if the value can't be expressed as a string.

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

---

#### public void setAsText​(
String
text)
throws
IllegalArgumentException

Sets the property value by parsing a given String. May raise
java.lang.IllegalArgumentException if either the String is
badly formatted or if this kind of property can't be expressed
as text.

**Specified by:**
- setAsText

in interface

PropertyEditor

**Parameters:**
- text

- The string to be parsed.

**Throws:**
- IllegalArgumentException

---

#### public
String
[] getTags()

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values. This can
be used to represent (for example) enum values. If a PropertyEditor
supports tags, then it should support the use of setAsText with
a tag value as a way of setting the value.

**Specified by:**
- getTags

in interface

PropertyEditor

**Returns:**
- The tag values for this property. May be null if this
property cannot be represented as a tagged value.

---

#### public
Component
getCustomEditor()

A PropertyEditor may chose to make available a full custom Component
that edits its property value. It is the responsibility of the
PropertyEditor to hook itself up to its editor Component itself and
to report property value changes by firing a PropertyChange event.

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

**Specified by:**
- getCustomEditor

in interface

PropertyEditor

**Returns:**
- A java.awt.Component that will allow a human to directly
edit the current property value. May be null if this is
not supported.

---

#### public boolean supportsCustomEditor()

Determines whether the propertyEditor can provide a custom editor.

**Specified by:**
- supportsCustomEditor

in interface

PropertyEditor

**Returns:**
- True if the propertyEditor can provide a custom editor.

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a listener for the value change.
When the property editor changes its value
it should fire a

PropertyChangeEvent

on all registered

PropertyChangeListener

s,
specifying the

null

value for the property name.
If the source property is set,
it should be used as the source of the event.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

**Specified by:**
- addPropertyChangeListener

in interface

PropertyEditor

**Parameters:**
- listener

- the

PropertyChangeListener

to add

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a listener for the value change.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

**Specified by:**
- removePropertyChangeListener

in interface

PropertyEditor

**Parameters:**
- listener

- the

PropertyChangeListener

to remove

---

#### public void firePropertyChange()

Report that we have been modified to any interested listeners.

---

### Additional Sections

#### Class PropertyEditorSupport

java.lang.Object

- java.beans.PropertyEditorSupport

java.beans.PropertyEditorSupport

**All Implemented Interfaces:** PropertyEditor

```java
public class
PropertyEditorSupport

extends
Object

implements
PropertyEditor
```

This is a support class to help build property editors.

It can be used either as a base class or as a delegate.

**Since:** 1.1

public class

PropertyEditorSupport

extends

Object

implements

PropertyEditor

This is a support class to help build property editors.

It can be used either as a base class or as a delegate.

It can be used either as a base class or as a delegate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyEditorSupport

()

Constructs a

PropertyEditorSupport

object.

PropertyEditorSupport

​(

Object

source)

Constructs a

PropertyEditorSupport

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a listener for the value change.

void

firePropertyChange

()

Report that we have been modified to any interested listeners.

String

getAsText

()

Gets the property value as a string suitable for presentation
to a human to edit.

Component

getCustomEditor

()

A PropertyEditor may chose to make available a full custom Component
that edits its property value.

String

getJavaInitializationString

()

This method is intended for use when generating Java code to set
the value of the property.

Object

getSource

()

Returns the bean that is used as the
source of events.

String

[]

getTags

()

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values.

Object

getValue

()

Gets the value of the property.

boolean

isPaintable

()

Determines whether the class will honor the paintValue method.

void

paintValue

​(

Graphics

gfx,

Rectangle

box)

Paint a representation of the value into a given area of screen
real estate.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a listener for the value change.

void

setAsText

​(

String

text)

Sets the property value by parsing a given String.

void

setSource

​(

Object

source)

Sets the source bean.

void

setValue

​(

Object

value)

Set (or change) the object that is to be edited.

boolean

supportsCustomEditor

()

Determines whether the propertyEditor can provide a custom editor.

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

Constructor Summary

Constructors

Constructor

Description

PropertyEditorSupport

()

Constructs a

PropertyEditorSupport

object.

PropertyEditorSupport

​(

Object

source)

Constructs a

PropertyEditorSupport

object.

---

#### Constructor Summary

Constructs a

PropertyEditorSupport

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a listener for the value change.

void

firePropertyChange

()

Report that we have been modified to any interested listeners.

String

getAsText

()

Gets the property value as a string suitable for presentation
to a human to edit.

Component

getCustomEditor

()

A PropertyEditor may chose to make available a full custom Component
that edits its property value.

String

getJavaInitializationString

()

This method is intended for use when generating Java code to set
the value of the property.

Object

getSource

()

Returns the bean that is used as the
source of events.

String

[]

getTags

()

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values.

Object

getValue

()

Gets the value of the property.

boolean

isPaintable

()

Determines whether the class will honor the paintValue method.

void

paintValue

​(

Graphics

gfx,

Rectangle

box)

Paint a representation of the value into a given area of screen
real estate.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a listener for the value change.

void

setAsText

​(

String

text)

Sets the property value by parsing a given String.

void

setSource

​(

Object

source)

Sets the source bean.

void

setValue

​(

Object

value)

Set (or change) the object that is to be edited.

boolean

supportsCustomEditor

()

Determines whether the propertyEditor can provide a custom editor.

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

Adds a listener for the value change.

Report that we have been modified to any interested listeners.

Gets the property value as a string suitable for presentation
to a human to edit.

A PropertyEditor may chose to make available a full custom Component
that edits its property value.

This method is intended for use when generating Java code to set
the value of the property.

Returns the bean that is used as the
source of events.

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values.

Gets the value of the property.

Determines whether the class will honor the paintValue method.

Paint a representation of the value into a given area of screen
real estate.

Removes a listener for the value change.

Sets the property value by parsing a given String.

Sets the source bean.

Set (or change) the object that is to be edited.

Determines whether the propertyEditor can provide a custom editor.

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

- PropertyEditorSupport

```java
public PropertyEditorSupport()
```

Constructs a

PropertyEditorSupport

object.

**Since:** 1.5

- PropertyEditorSupport

```java
public PropertyEditorSupport​(
Object
source)
```

Constructs a

PropertyEditorSupport

object.

**Parameters:** source

- the source used for event firing
**Since:** 1.5

============ METHOD DETAIL ==========

- Method Detail

- getSource

```java
public
Object
getSource()
```

Returns the bean that is used as the
source of events. If the source has not
been explicitly set then this instance of

PropertyEditorSupport

is returned.

**Returns:** the source object or this instance
**Since:** 1.5

- setSource

```java
public void setSource​(
Object
source)
```

Sets the source bean.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

**Parameters:** source

- source object to be used for events
**Since:** 1.5

- setValue

```java
public void setValue​(
Object
value)
```

Set (or change) the object that is to be edited.

**Specified by:** setValue

in interface

PropertyEditor
**Parameters:** value

- The new target object to be edited. Note that this
object should not be modified by the PropertyEditor, rather
the PropertyEditor should create a new object to hold any
modified value.

- getValue

```java
public
Object
getValue()
```

Gets the value of the property.

**Specified by:** getValue

in interface

PropertyEditor
**Returns:** The value of the property.

- isPaintable

```java
public boolean isPaintable()
```

Determines whether the class will honor the paintValue method.

**Specified by:** isPaintable

in interface

PropertyEditor
**Returns:** True if the class will honor the paintValue method.

- paintValue

```java
public void paintValue​(
Graphics
gfx,

Rectangle
box)
```

Paint a representation of the value into a given area of screen
real estate. Note that the propertyEditor is responsible for doing
its own clipping so that it fits into the given rectangle.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

**Specified by:** paintValue

in interface

PropertyEditor
**Parameters:** gfx

- Graphics object to paint into.
**Parameters:** box

- Rectangle within graphics object into which we should paint.

- getJavaInitializationString

```java
public
String
getJavaInitializationString()
```

This method is intended for use when generating Java code to set
the value of the property. It should return a fragment of Java code
that can be used to initialize a variable with the current property
value.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

**Specified by:** getJavaInitializationString

in interface

PropertyEditor
**Returns:** A fragment of Java code representing an initializer for the
current value.

- getAsText

```java
public
String
getAsText()
```

Gets the property value as a string suitable for presentation
to a human to edit.

**Specified by:** getAsText

in interface

PropertyEditor
**Returns:** The property value as a string suitable for presentation
to a human to edit.

Returns null if the value can't be expressed as a string.

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

- setAsText

```java
public void setAsText​(
String
text)
throws
IllegalArgumentException
```

Sets the property value by parsing a given String. May raise
java.lang.IllegalArgumentException if either the String is
badly formatted or if this kind of property can't be expressed
as text.

**Specified by:** setAsText

in interface

PropertyEditor
**Parameters:** text

- The string to be parsed.
**Throws:** IllegalArgumentException

- getTags

```java
public
String
[] getTags()
```

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values. This can
be used to represent (for example) enum values. If a PropertyEditor
supports tags, then it should support the use of setAsText with
a tag value as a way of setting the value.

**Specified by:** getTags

in interface

PropertyEditor
**Returns:** The tag values for this property. May be null if this
property cannot be represented as a tagged value.

- getCustomEditor

```java
public
Component
getCustomEditor()
```

A PropertyEditor may chose to make available a full custom Component
that edits its property value. It is the responsibility of the
PropertyEditor to hook itself up to its editor Component itself and
to report property value changes by firing a PropertyChange event.

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

**Specified by:** getCustomEditor

in interface

PropertyEditor
**Returns:** A java.awt.Component that will allow a human to directly
edit the current property value. May be null if this is
not supported.

- supportsCustomEditor

```java
public boolean supportsCustomEditor()
```

Determines whether the propertyEditor can provide a custom editor.

**Specified by:** supportsCustomEditor

in interface

PropertyEditor
**Returns:** True if the propertyEditor can provide a custom editor.

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a listener for the value change.
When the property editor changes its value
it should fire a

PropertyChangeEvent

on all registered

PropertyChangeListener

s,
specifying the

null

value for the property name.
If the source property is set,
it should be used as the source of the event.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

**Specified by:** addPropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to add

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a listener for the value change.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

**Specified by:** removePropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to remove

- firePropertyChange

```java
public void firePropertyChange()
```

Report that we have been modified to any interested listeners.

Constructor Detail

- PropertyEditorSupport

```java
public PropertyEditorSupport()
```

Constructs a

PropertyEditorSupport

object.

**Since:** 1.5

- PropertyEditorSupport

```java
public PropertyEditorSupport​(
Object
source)
```

Constructs a

PropertyEditorSupport

object.

**Parameters:** source

- the source used for event firing
**Since:** 1.5

---

#### Constructor Detail

PropertyEditorSupport

```java
public PropertyEditorSupport()
```

Constructs a

PropertyEditorSupport

object.

**Since:** 1.5

---

#### PropertyEditorSupport

public PropertyEditorSupport()

Constructs a

PropertyEditorSupport

object.

PropertyEditorSupport

```java
public PropertyEditorSupport​(
Object
source)
```

Constructs a

PropertyEditorSupport

object.

**Parameters:** source

- the source used for event firing
**Since:** 1.5

---

#### PropertyEditorSupport

public PropertyEditorSupport​(

Object

source)

Constructs a

PropertyEditorSupport

object.

Method Detail

- getSource

```java
public
Object
getSource()
```

Returns the bean that is used as the
source of events. If the source has not
been explicitly set then this instance of

PropertyEditorSupport

is returned.

**Returns:** the source object or this instance
**Since:** 1.5

- setSource

```java
public void setSource​(
Object
source)
```

Sets the source bean.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

**Parameters:** source

- source object to be used for events
**Since:** 1.5

- setValue

```java
public void setValue​(
Object
value)
```

Set (or change) the object that is to be edited.

**Specified by:** setValue

in interface

PropertyEditor
**Parameters:** value

- The new target object to be edited. Note that this
object should not be modified by the PropertyEditor, rather
the PropertyEditor should create a new object to hold any
modified value.

- getValue

```java
public
Object
getValue()
```

Gets the value of the property.

**Specified by:** getValue

in interface

PropertyEditor
**Returns:** The value of the property.

- isPaintable

```java
public boolean isPaintable()
```

Determines whether the class will honor the paintValue method.

**Specified by:** isPaintable

in interface

PropertyEditor
**Returns:** True if the class will honor the paintValue method.

- paintValue

```java
public void paintValue​(
Graphics
gfx,

Rectangle
box)
```

Paint a representation of the value into a given area of screen
real estate. Note that the propertyEditor is responsible for doing
its own clipping so that it fits into the given rectangle.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

**Specified by:** paintValue

in interface

PropertyEditor
**Parameters:** gfx

- Graphics object to paint into.
**Parameters:** box

- Rectangle within graphics object into which we should paint.

- getJavaInitializationString

```java
public
String
getJavaInitializationString()
```

This method is intended for use when generating Java code to set
the value of the property. It should return a fragment of Java code
that can be used to initialize a variable with the current property
value.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

**Specified by:** getJavaInitializationString

in interface

PropertyEditor
**Returns:** A fragment of Java code representing an initializer for the
current value.

- getAsText

```java
public
String
getAsText()
```

Gets the property value as a string suitable for presentation
to a human to edit.

**Specified by:** getAsText

in interface

PropertyEditor
**Returns:** The property value as a string suitable for presentation
to a human to edit.

Returns null if the value can't be expressed as a string.

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

- setAsText

```java
public void setAsText​(
String
text)
throws
IllegalArgumentException
```

Sets the property value by parsing a given String. May raise
java.lang.IllegalArgumentException if either the String is
badly formatted or if this kind of property can't be expressed
as text.

**Specified by:** setAsText

in interface

PropertyEditor
**Parameters:** text

- The string to be parsed.
**Throws:** IllegalArgumentException

- getTags

```java
public
String
[] getTags()
```

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values. This can
be used to represent (for example) enum values. If a PropertyEditor
supports tags, then it should support the use of setAsText with
a tag value as a way of setting the value.

**Specified by:** getTags

in interface

PropertyEditor
**Returns:** The tag values for this property. May be null if this
property cannot be represented as a tagged value.

- getCustomEditor

```java
public
Component
getCustomEditor()
```

A PropertyEditor may chose to make available a full custom Component
that edits its property value. It is the responsibility of the
PropertyEditor to hook itself up to its editor Component itself and
to report property value changes by firing a PropertyChange event.

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

**Specified by:** getCustomEditor

in interface

PropertyEditor
**Returns:** A java.awt.Component that will allow a human to directly
edit the current property value. May be null if this is
not supported.

- supportsCustomEditor

```java
public boolean supportsCustomEditor()
```

Determines whether the propertyEditor can provide a custom editor.

**Specified by:** supportsCustomEditor

in interface

PropertyEditor
**Returns:** True if the propertyEditor can provide a custom editor.

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a listener for the value change.
When the property editor changes its value
it should fire a

PropertyChangeEvent

on all registered

PropertyChangeListener

s,
specifying the

null

value for the property name.
If the source property is set,
it should be used as the source of the event.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

**Specified by:** addPropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to add

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a listener for the value change.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

**Specified by:** removePropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to remove

- firePropertyChange

```java
public void firePropertyChange()
```

Report that we have been modified to any interested listeners.

---

#### Method Detail

getSource

```java
public
Object
getSource()
```

Returns the bean that is used as the
source of events. If the source has not
been explicitly set then this instance of

PropertyEditorSupport

is returned.

**Returns:** the source object or this instance
**Since:** 1.5

---

#### getSource

public

Object

getSource()

Returns the bean that is used as the
source of events. If the source has not
been explicitly set then this instance of

PropertyEditorSupport

is returned.

setSource

```java
public void setSource​(
Object
source)
```

Sets the source bean.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

**Parameters:** source

- source object to be used for events
**Since:** 1.5

---

#### setSource

public void setSource​(

Object

source)

Sets the source bean.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

The source bean is used as the source of events
for the property changes. This source should be used for information
purposes only and should not be modified by the PropertyEditor.

setValue

```java
public void setValue​(
Object
value)
```

Set (or change) the object that is to be edited.

**Specified by:** setValue

in interface

PropertyEditor
**Parameters:** value

- The new target object to be edited. Note that this
object should not be modified by the PropertyEditor, rather
the PropertyEditor should create a new object to hold any
modified value.

---

#### setValue

public void setValue​(

Object

value)

Set (or change) the object that is to be edited.

getValue

```java
public
Object
getValue()
```

Gets the value of the property.

**Specified by:** getValue

in interface

PropertyEditor
**Returns:** The value of the property.

---

#### getValue

public

Object

getValue()

Gets the value of the property.

isPaintable

```java
public boolean isPaintable()
```

Determines whether the class will honor the paintValue method.

**Specified by:** isPaintable

in interface

PropertyEditor
**Returns:** True if the class will honor the paintValue method.

---

#### isPaintable

public boolean isPaintable()

Determines whether the class will honor the paintValue method.

paintValue

```java
public void paintValue​(
Graphics
gfx,

Rectangle
box)
```

Paint a representation of the value into a given area of screen
real estate. Note that the propertyEditor is responsible for doing
its own clipping so that it fits into the given rectangle.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

**Specified by:** paintValue

in interface

PropertyEditor
**Parameters:** gfx

- Graphics object to paint into.
**Parameters:** box

- Rectangle within graphics object into which we should paint.

---

#### paintValue

public void paintValue​(

Graphics

gfx,

Rectangle

box)

Paint a representation of the value into a given area of screen
real estate. Note that the propertyEditor is responsible for doing
its own clipping so that it fits into the given rectangle.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

If the PropertyEditor doesn't honor paint requests (see isPaintable)
this method should be a silent noop.

getJavaInitializationString

```java
public
String
getJavaInitializationString()
```

This method is intended for use when generating Java code to set
the value of the property. It should return a fragment of Java code
that can be used to initialize a variable with the current property
value.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

**Specified by:** getJavaInitializationString

in interface

PropertyEditor
**Returns:** A fragment of Java code representing an initializer for the
current value.

---

#### getJavaInitializationString

public

String

getJavaInitializationString()

This method is intended for use when generating Java code to set
the value of the property. It should return a fragment of Java code
that can be used to initialize a variable with the current property
value.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

Example results are "2", "new Color(127,127,34)", "Color.orange", etc.

getAsText

```java
public
String
getAsText()
```

Gets the property value as a string suitable for presentation
to a human to edit.

**Specified by:** getAsText

in interface

PropertyEditor
**Returns:** The property value as a string suitable for presentation
to a human to edit.

Returns null if the value can't be expressed as a string.

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

---

#### getAsText

public

String

getAsText()

Gets the property value as a string suitable for presentation
to a human to edit.

Returns null if the value can't be expressed as a string.

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

If a non-null value is returned, then the PropertyEditor should
be prepared to parse that string back in setAsText().

setAsText

```java
public void setAsText​(
String
text)
throws
IllegalArgumentException
```

Sets the property value by parsing a given String. May raise
java.lang.IllegalArgumentException if either the String is
badly formatted or if this kind of property can't be expressed
as text.

**Specified by:** setAsText

in interface

PropertyEditor
**Parameters:** text

- The string to be parsed.
**Throws:** IllegalArgumentException

---

#### setAsText

public void setAsText​(

String

text)
throws

IllegalArgumentException

Sets the property value by parsing a given String. May raise
java.lang.IllegalArgumentException if either the String is
badly formatted or if this kind of property can't be expressed
as text.

getTags

```java
public
String
[] getTags()
```

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values. This can
be used to represent (for example) enum values. If a PropertyEditor
supports tags, then it should support the use of setAsText with
a tag value as a way of setting the value.

**Specified by:** getTags

in interface

PropertyEditor
**Returns:** The tag values for this property. May be null if this
property cannot be represented as a tagged value.

---

#### getTags

public

String

[] getTags()

If the property value must be one of a set of known tagged values,
then this method should return an array of the tag values. This can
be used to represent (for example) enum values. If a PropertyEditor
supports tags, then it should support the use of setAsText with
a tag value as a way of setting the value.

getCustomEditor

```java
public
Component
getCustomEditor()
```

A PropertyEditor may chose to make available a full custom Component
that edits its property value. It is the responsibility of the
PropertyEditor to hook itself up to its editor Component itself and
to report property value changes by firing a PropertyChange event.

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

**Specified by:** getCustomEditor

in interface

PropertyEditor
**Returns:** A java.awt.Component that will allow a human to directly
edit the current property value. May be null if this is
not supported.

---

#### getCustomEditor

public

Component

getCustomEditor()

A PropertyEditor may chose to make available a full custom Component
that edits its property value. It is the responsibility of the
PropertyEditor to hook itself up to its editor Component itself and
to report property value changes by firing a PropertyChange event.

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

The higher-level code that calls getCustomEditor may either embed
the Component in some larger property sheet, or it may put it in
its own individual dialog, or ...

supportsCustomEditor

```java
public boolean supportsCustomEditor()
```

Determines whether the propertyEditor can provide a custom editor.

**Specified by:** supportsCustomEditor

in interface

PropertyEditor
**Returns:** True if the propertyEditor can provide a custom editor.

---

#### supportsCustomEditor

public boolean supportsCustomEditor()

Determines whether the propertyEditor can provide a custom editor.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a listener for the value change.
When the property editor changes its value
it should fire a

PropertyChangeEvent

on all registered

PropertyChangeListener

s,
specifying the

null

value for the property name.
If the source property is set,
it should be used as the source of the event.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

**Specified by:** addPropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to add

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a listener for the value change.
When the property editor changes its value
it should fire a

PropertyChangeEvent

on all registered

PropertyChangeListener

s,
specifying the

null

value for the property name.
If the source property is set,
it should be used as the source of the event.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

The same listener object may be added more than once,
and will be called as many times as it is added.
If

listener

is

null

,
no exception is thrown and no action is taken.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a listener for the value change.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

**Specified by:** removePropertyChangeListener

in interface

PropertyEditor
**Parameters:** listener

- the

PropertyChangeListener

to remove

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a listener for the value change.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

If the same listener was added more than once,
it will be notified one less time after being removed.
If

listener

is

null

, or was never added,
no exception is thrown and no action is taken.

firePropertyChange

```java
public void firePropertyChange()
```

Report that we have been modified to any interested listeners.

---

#### firePropertyChange

public void firePropertyChange()

Report that we have been modified to any interested listeners.

---

