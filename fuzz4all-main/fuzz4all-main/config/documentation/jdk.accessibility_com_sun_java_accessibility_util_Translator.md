# Class Translator

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\Translator.html`

### Class Description

```java
public class
Translator

extends
AccessibleContext

implements
Accessible
,
AccessibleComponent
```

The

Translator

class provides a translation to interface

Accessible

for objects that do not implement interface

Accessible

. Assistive
technologies can use the

getAccessible

class method of

Translator

to obtain an object that implements interface

Accessible

.
If the object passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

An example of how an assistive technology might use the

Translator

class is as follows:

```java
Accessible accessible = Translator.getAccessible(someObj);
// obtain information from the 'accessible' object.
```

Note: This implementation is missing many things and is not a recommended way
to implement accessibility features for a toolkit. Instead of relying upon this
code, a toolkit's components should implement interface

Accessible

directly.

**All Implemented Interfaces:** Accessible

,

AccessibleComponent

---

### Field Details

#### protected
Object
source

The source object needing translating.

---

### Constructor Details

#### public Translator()

Create a new

Translator

. You must call the

setSource

method to set the object to be translated after calling this constructor.

---

#### public Translator​(
Object
o)

Create a new

Translator

with the source object o.

**Parameters:**
- o

- the Component that does not implement interface

Accessible

---

### Method Details

#### protected static
Class
<?> getTranslatorClass​(
Class
<?> c)

Find a translator for this class. If one doesn't exist for this
class explicitly, try its superclass and so on.

**Parameters:**
- c

- a Class

**Returns:**
- the

Translator

Class for the Class passed in

---

#### public static
Accessible
getAccessible​(
Object
o)

Obtain an object that implements interface

Accessible

. If the object
passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

**Parameters:**
- o

- an Object; if a null is passed in a null is returned

**Returns:**
- an

Object

, possibly the

Object

passed in, that
implements the

Accessible

interface for the

Object

which was passed in

---

#### public
Object
getSource()

Get the source

Object

of the

Translator

.

**Returns:**
- the source

Object

of the

Translator

---

#### public void setSource​(
Object
o)

Set the source object of the

Translator

.

**Parameters:**
- o

- the Component that does not implement interface Accessible

---

#### public boolean equals​(
Object
o)

Returns true if this object is the same as the one passed in.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the

Object

to check against

**Returns:**
- true if this is the same object

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return hashcode.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- hashcode

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
AccessibleContext
getAccessibleContext()

Returns this object.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Returns:**
- the

AccessibleContext

associated with this object

---

#### public
String
getAccessibleName()

Get the accessible name of this object.

**Overrides:**
- getAccessibleName

in class

AccessibleContext

**Returns:**
- the localized name of the object; can be null if this object
does not have a name

**See Also:**
- AccessibleContext.setAccessibleName(java.lang.String)

---

#### public void setAccessibleName​(
String
s)

Set the name of this object.

**Overrides:**
- setAccessibleName

in class

AccessibleContext

**Parameters:**
- s

- the new localized name of the object

**See Also:**
- AccessibleContext.getAccessibleName()

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
String
getAccessibleDescription()

Get the accessible description of this object.

**Overrides:**
- getAccessibleDescription

in class

AccessibleContext

**Returns:**
- the description of the object; can be null if this object does
not have a description

**See Also:**
- AccessibleContext.setAccessibleDescription(java.lang.String)

---

#### public void setAccessibleDescription​(
String
s)

Set the accessible description of this object.

**Overrides:**
- setAccessibleDescription

in class

AccessibleContext

**Parameters:**
- s

- the new localized description of the object

**See Also:**
- AccessibleContext.setAccessibleName(java.lang.String)

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
AccessibleRole
getAccessibleRole()

Get the role of this object.

**Specified by:**
- getAccessibleRole

in class

AccessibleContext

**Returns:**
- an instance of AccessibleRole describing the role of the object

**See Also:**
- AccessibleRole

---

#### public
AccessibleStateSet
getAccessibleStateSet()

Get the state of this object, given an already populated state.
This method is intended for use by subclasses so they don't have
to check for everything.

**Specified by:**
- getAccessibleStateSet

in class

AccessibleContext

**Returns:**
- an instance of

AccessibleStateSet

containing the current state of the object

**See Also:**
- AccessibleStateSet

,

AccessibleState

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
Accessible
getAccessibleParent()

Get the accessible parent of this object.

**Overrides:**
- getAccessibleParent

in class

AccessibleContext

**Returns:**
- the accessible parent of this object; can be null if this
object does not have an accessible parent

---

#### public int getAccessibleIndexInParent()

Get the index of this object in its accessible parent.

**Specified by:**
- getAccessibleIndexInParent

in class

AccessibleContext

**Returns:**
- -1 of this object does not have an accessible parent; otherwise,
the index of the child in its accessible parent

**See Also:**
- AccessibleContext.getAccessibleParent()

,

AccessibleContext.getAccessibleChildrenCount()

,

AccessibleContext.getAccessibleChild(int)

---

#### public int getAccessibleChildrenCount()

Returns the number of accessible children in the object.

**Specified by:**
- getAccessibleChildrenCount

in class

AccessibleContext

**Returns:**
- the number of accessible children in the object

---

#### public
Accessible
getAccessibleChild​(int i)

Return the nth accessible child of the object.

**Specified by:**
- getAccessibleChild

in class

AccessibleContext

**Parameters:**
- i

- zero-based index of child

**Returns:**
- the nth accessible child of the object

**See Also:**
- AccessibleContext.getAccessibleChildrenCount()

---

#### public
Locale
getLocale()
throws
IllegalComponentStateException

Gets the

Locale

of the component. If the component does not have a
locale, the locale of its parent is returned.

**Specified by:**
- getLocale

in class

AccessibleContext

**Returns:**
- the

Locale

of the object

**Throws:**
- IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
l)

Add a

PropertyChangeListener

to the listener list. The listener
is registered for all properties.

**Overrides:**
- addPropertyChangeListener

in class

AccessibleContext

**Parameters:**
- l

- The PropertyChangeListener to be added

**See Also:**
- AccessibleContext.ACCESSIBLE_NAME_PROPERTY

,

AccessibleContext.ACCESSIBLE_DESCRIPTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_STATE_PROPERTY

,

AccessibleContext.ACCESSIBLE_VALUE_PROPERTY

,

AccessibleContext.ACCESSIBLE_SELECTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_TEXT_PROPERTY

,

AccessibleContext.ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
l)

Remove the

PropertyChangeListener

from the listener list.

**Overrides:**
- removePropertyChangeListener

in class

AccessibleContext

**Parameters:**
- l

- The PropertyChangeListener to be removed

---

#### public
Color
getBackground()

Get the background

Color

of this object.

**Specified by:**
- getBackground

in interface

AccessibleComponent

**Returns:**
- if supported, the background

Color

of the object;
otherwise, null

**See Also:**
- AccessibleComponent.setBackground(java.awt.Color)

---

#### public void setBackground​(
Color
c)

Set the background

Color

of this object.

**Specified by:**
- setBackground

in interface

AccessibleComponent

**Parameters:**
- c

- the new

Color

for the background

**See Also:**
- AccessibleComponent.setBackground(java.awt.Color)

---

#### public
Color
getForeground()

Get the foreground

Color

of this object.

**Specified by:**
- getForeground

in interface

AccessibleComponent

**Returns:**
- if supported, the foreground

Color

of the object; otherwise, null

**See Also:**
- AccessibleComponent.setForeground(java.awt.Color)

---

#### public void setForeground​(
Color
c)

Set the foreground

Color

of this object.

**Specified by:**
- setForeground

in interface

AccessibleComponent

**Parameters:**
- c

- the new

Color

for the foreground

**See Also:**
- AccessibleComponent.getForeground()

---

#### public
Cursor
getCursor()

Get the

Cursor

of this object.

**Specified by:**
- getCursor

in interface

AccessibleComponent

**Returns:**
- if supported, the Cursor of the object; otherwise, null

**See Also:**
- AccessibleComponent.setCursor(java.awt.Cursor)

---

#### public void setCursor​(
Cursor
c)

Set the

Cursor

of this object.

**Specified by:**
- setCursor

in interface

AccessibleComponent

**Parameters:**
- c

- the new

Cursor

for the object

**See Also:**
- AccessibleComponent.getCursor()

---

#### public
Font
getFont()

Get the

Font

of this object.

**Specified by:**
- getFont

in interface

AccessibleComponent

**Returns:**
- if supported, the

Font

for the object; otherwise, null

**See Also:**
- AccessibleComponent.setFont(java.awt.Font)

---

#### public void setFont​(
Font
f)

Set the

Font

of this object.

**Specified by:**
- setFont

in interface

AccessibleComponent

**Parameters:**
- f

- the new

Font

for the object

**See Also:**
- AccessibleComponent.getFont()

---

#### public
FontMetrics
getFontMetrics​(
Font
f)

Get the

FontMetrics

of this object.

**Specified by:**
- getFontMetrics

in interface

AccessibleComponent

**Parameters:**
- f

- the

Font

**Returns:**
- if supported, the

FontMetrics

the object; otherwise, null

**See Also:**
- getFont()

---

#### public boolean isEnabled()

Determine if the object is enabled.

**Specified by:**
- isEnabled

in interface

AccessibleComponent

**Returns:**
- true if object is enabled; otherwise, false

**See Also:**
- AccessibleComponent.setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

---

#### public void setEnabled​(boolean b)

Set the enabled state of the object.

**Specified by:**
- setEnabled

in interface

AccessibleComponent

**Parameters:**
- b

- if true, enables this object; otherwise, disables it

**See Also:**
- AccessibleComponent.isEnabled()

---

#### public boolean isVisible()

Determine if the object is visible.

**Specified by:**
- isVisible

in interface

AccessibleComponent

**Returns:**
- true if object is visible; otherwise, false

**See Also:**
- AccessibleComponent.setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

---

#### public void setVisible​(boolean b)

Set the visible state of the object.

**Specified by:**
- setVisible

in interface

AccessibleComponent

**Parameters:**
- b

- if true, shows this object; otherwise, hides it

**See Also:**
- AccessibleComponent.isVisible()

---

#### public boolean isShowing()

Determine if the object is showing. This is determined by checking
the visibility of the object and ancestors of the object.

**Specified by:**
- isShowing

in interface

AccessibleComponent

**Returns:**
- true if object is showing; otherwise, false

---

#### public boolean contains​(
Point
p)

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

**Specified by:**
- contains

in interface

AccessibleComponent

**Parameters:**
- p

- the

Point

relative to the coordinate system of the object

**Returns:**
- true if object contains

Point

; otherwise false

**See Also:**
- AccessibleComponent.getBounds()

---

#### public
Point
getLocationOnScreen()

Returns the location of the object on the screen.

**Specified by:**
- getLocationOnScreen

in interface

AccessibleComponent

**Returns:**
- location of object on screen; can be null if this object
is not on the screen

**See Also:**
- AccessibleComponent.getBounds()

,

AccessibleComponent.getLocation()

---

#### public
Point
getLocation()

Returns the location of the object relative to parent.

**Specified by:**
- getLocation

in interface

AccessibleComponent

**Returns:**
- location of object relative to parent; can be null if
this object or its parent are not on the screen

**See Also:**
- AccessibleComponent.getBounds()

,

AccessibleComponent.getLocationOnScreen()

---

#### public void setLocation​(
Point
p)

Sets the location of the object relative to parent.

**Specified by:**
- setLocation

in interface

AccessibleComponent

**Parameters:**
- p

- the new position for the top-left corner

**See Also:**
- AccessibleComponent.getLocation()

---

#### public
Rectangle
getBounds()

Returns the current bounds of this object.

**Specified by:**
- getBounds

in interface

AccessibleComponent

**Returns:**
- current bounds of object; can be null if this object
is not on the screen

**See Also:**
- AccessibleComponent.contains(java.awt.Point)

---

#### public void setBounds​(
Rectangle
r)

Sets the current bounds of this object.

**Specified by:**
- setBounds

in interface

AccessibleComponent

**Parameters:**
- r

- rectangle indicating this component's bounds

**See Also:**
- AccessibleComponent.getBounds()

---

#### public
Dimension
getSize()

Returns the current size of this object.

**Specified by:**
- getSize

in interface

AccessibleComponent

**Returns:**
- current size of object; can be null if this object is
not on the screen

**See Also:**
- AccessibleComponent.setSize(java.awt.Dimension)

---

#### public void setSize​(
Dimension
d)

Sets the current size of this object.

**Specified by:**
- setSize

in interface

AccessibleComponent

**Parameters:**
- d

- The dimension specifying the new size of the object

**See Also:**
- AccessibleComponent.getSize()

---

#### public
Accessible
getAccessibleAt​(
Point
p)

Returns the accessible child contained at the local coordinate
Point, if one exists.

**Specified by:**
- getAccessibleAt

in interface

AccessibleComponent

**Parameters:**
- p

- The point relative to the coordinate system of this object

**Returns:**
- the Accessible at the specified location, if it exists

---

#### public boolean isFocusTraversable()

Returns whether this object can accept focus or not.

**Specified by:**
- isFocusTraversable

in interface

AccessibleComponent

**Returns:**
- true if object can accept focus; otherwise false

**See Also:**
- AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

---

#### public void requestFocus()

Requests focus for this object.

**Specified by:**
- requestFocus

in interface

AccessibleComponent

**See Also:**
- AccessibleComponent.isFocusTraversable()

---

#### public void addFocusListener​(
FocusListener
l)

Adds the specified

FocusListener

to receive focus events from
this component.

**Specified by:**
- addFocusListener

in interface

AccessibleComponent

**Parameters:**
- l

- the focus listener

**See Also:**
- AccessibleComponent.removeFocusListener(java.awt.event.FocusListener)

---

#### public void removeFocusListener​(
FocusListener
l)

Removes the specified focus listener so it no longer receives focus
events from this component.

**Specified by:**
- removeFocusListener

in interface

AccessibleComponent

**Parameters:**
- l

- the focus listener; this method performs no function, nor does it
throw an exception if the listener specified was not previously added
to this component; if listener is null, no exception is thrown and no
action is performed.

**See Also:**
- AccessibleComponent.addFocusListener(java.awt.event.FocusListener)

---

### Additional Sections

#### Class Translator

java.lang.Object

- javax.accessibility.AccessibleContext
- - com.sun.java.accessibility.util.Translator

javax.accessibility.AccessibleContext

- com.sun.java.accessibility.util.Translator

com.sun.java.accessibility.util.Translator

**All Implemented Interfaces:** Accessible

,

AccessibleComponent

```java
public class
Translator

extends
AccessibleContext

implements
Accessible
,
AccessibleComponent
```

The

Translator

class provides a translation to interface

Accessible

for objects that do not implement interface

Accessible

. Assistive
technologies can use the

getAccessible

class method of

Translator

to obtain an object that implements interface

Accessible

.
If the object passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

An example of how an assistive technology might use the

Translator

class is as follows:

```java
Accessible accessible = Translator.getAccessible(someObj);
// obtain information from the 'accessible' object.
```

Note: This implementation is missing many things and is not a recommended way
to implement accessibility features for a toolkit. Instead of relying upon this
code, a toolkit's components should implement interface

Accessible

directly.

public class

Translator

extends

AccessibleContext

implements

Accessible

,

AccessibleComponent

The

Translator

class provides a translation to interface

Accessible

for objects that do not implement interface

Accessible

. Assistive
technologies can use the

getAccessible

class method of

Translator

to obtain an object that implements interface

Accessible

.
If the object passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

An example of how an assistive technology might use the

Translator

class is as follows:

```java
Accessible accessible = Translator.getAccessible(someObj);
// obtain information from the 'accessible' object.
```

Note: This implementation is missing many things and is not a recommended way
to implement accessibility features for a toolkit. Instead of relying upon this
code, a toolkit's components should implement interface

Accessible

directly.

An example of how an assistive technology might use the

Translator

class is as follows:

```java
Accessible accessible = Translator.getAccessible(someObj);
// obtain information from the 'accessible' object.
```

Note: This implementation is missing many things and is not a recommended way
to implement accessibility features for a toolkit. Instead of relying upon this
code, a toolkit's components should implement interface

Accessible

directly.

Accessible accessible = Translator.getAccessible(someObj);
// obtain information from the 'accessible' object.

Note: This implementation is missing many things and is not a recommended way
to implement accessibility features for a toolkit. Instead of relying upon this
code, a toolkit's components should implement interface

Accessible

directly.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

source

The source object needing translating.

- Fields declared in class javax.accessibility.

AccessibleContext

ACCESSIBLE_ACTION_PROPERTY

,

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

,

ACCESSIBLE_CARET_PROPERTY

,

ACCESSIBLE_CHILD_PROPERTY

,

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_HYPERTEXT_OFFSET

,

ACCESSIBLE_INVALIDATE_CHILDREN

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_TABLE_CAPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

,

ACCESSIBLE_TABLE_MODEL_CHANGED

,

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

,

ACCESSIBLE_TABLE_SUMMARY_CHANGED

,

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

,

accessibleDescription

,

accessibleName

,

accessibleParent

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Translator

()

Create a new

Translator

.

Translator

​(

Object

o)

Create a new

Translator

with the source object o.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addFocusListener

​(

FocusListener

l)

Adds the specified

FocusListener

to receive focus events from
this component.

void

addPropertyChangeListener

​(

PropertyChangeListener

l)

Add a

PropertyChangeListener

to the listener list.

boolean

contains

​(

Point

p)

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

boolean

equals

​(

Object

o)

Returns true if this object is the same as the one passed in.

static

Accessible

getAccessible

​(

Object

o)

Obtain an object that implements interface

Accessible

.

Accessible

getAccessibleAt

​(

Point

p)

Returns the accessible child contained at the local coordinate
Point, if one exists.

Accessible

getAccessibleChild

​(int i)

Return the nth accessible child of the object.

int

getAccessibleChildrenCount

()

Returns the number of accessible children in the object.

AccessibleContext

getAccessibleContext

()

Returns this object.

String

getAccessibleDescription

()

Get the accessible description of this object.

int

getAccessibleIndexInParent

()

Get the index of this object in its accessible parent.

String

getAccessibleName

()

Get the accessible name of this object.

Accessible

getAccessibleParent

()

Get the accessible parent of this object.

AccessibleRole

getAccessibleRole

()

Get the role of this object.

AccessibleStateSet

getAccessibleStateSet

()

Get the state of this object, given an already populated state.

Color

getBackground

()

Get the background

Color

of this object.

Rectangle

getBounds

()

Returns the current bounds of this object.

Cursor

getCursor

()

Get the

Cursor

of this object.

Font

getFont

()

Get the

Font

of this object.

FontMetrics

getFontMetrics

​(

Font

f)

Get the

FontMetrics

of this object.

Color

getForeground

()

Get the foreground

Color

of this object.

Locale

getLocale

()

Gets the

Locale

of the component.

Point

getLocation

()

Returns the location of the object relative to parent.

Point

getLocationOnScreen

()

Returns the location of the object on the screen.

Dimension

getSize

()

Returns the current size of this object.

Object

getSource

()

Get the source

Object

of the

Translator

.

protected static

Class

<?>

getTranslatorClass

​(

Class

<?> c)

Find a translator for this class.

int

hashCode

()

Return hashcode.

boolean

isEnabled

()

Determine if the object is enabled.

boolean

isFocusTraversable

()

Returns whether this object can accept focus or not.

boolean

isShowing

()

Determine if the object is showing.

boolean

isVisible

()

Determine if the object is visible.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

void

removePropertyChangeListener

​(

PropertyChangeListener

l)

Remove the

PropertyChangeListener

from the listener list.

void

requestFocus

()

Requests focus for this object.

void

setAccessibleDescription

​(

String

s)

Set the accessible description of this object.

void

setAccessibleName

​(

String

s)

Set the name of this object.

void

setBackground

​(

Color

c)

Set the background

Color

of this object.

void

setBounds

​(

Rectangle

r)

Sets the current bounds of this object.

void

setCursor

​(

Cursor

c)

Set the

Cursor

of this object.

void

setEnabled

​(boolean b)

Set the enabled state of the object.

void

setFont

​(

Font

f)

Set the

Font

of this object.

void

setForeground

​(

Color

c)

Set the foreground

Color

of this object.

void

setLocation

​(

Point

p)

Sets the location of the object relative to parent.

void

setSize

​(

Dimension

d)

Sets the current size of this object.

void

setSource

​(

Object

o)

Set the source object of the

Translator

.

void

setVisible

​(boolean b)

Set the visible state of the object.

- Methods declared in class javax.accessibility.

AccessibleContext

firePropertyChange

,

getAccessibleAction

,

getAccessibleComponent

,

getAccessibleEditableText

,

getAccessibleIcon

,

getAccessibleRelationSet

,

getAccessibleSelection

,

getAccessibleTable

,

getAccessibleText

,

getAccessibleValue

,

setAccessibleParent

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Fields

Modifier and Type

Field

Description

protected

Object

source

The source object needing translating.

- Fields declared in class javax.accessibility.

AccessibleContext

ACCESSIBLE_ACTION_PROPERTY

,

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

,

ACCESSIBLE_CARET_PROPERTY

,

ACCESSIBLE_CHILD_PROPERTY

,

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_HYPERTEXT_OFFSET

,

ACCESSIBLE_INVALIDATE_CHILDREN

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_TABLE_CAPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

,

ACCESSIBLE_TABLE_MODEL_CHANGED

,

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

,

ACCESSIBLE_TABLE_SUMMARY_CHANGED

,

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

,

accessibleDescription

,

accessibleName

,

accessibleParent

---

#### Field Summary

The source object needing translating.

Fields declared in class javax.accessibility.

AccessibleContext

ACCESSIBLE_ACTION_PROPERTY

,

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

,

ACCESSIBLE_CARET_PROPERTY

,

ACCESSIBLE_CHILD_PROPERTY

,

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_HYPERTEXT_OFFSET

,

ACCESSIBLE_INVALIDATE_CHILDREN

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_TABLE_CAPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

,

ACCESSIBLE_TABLE_MODEL_CHANGED

,

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

,

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

,

ACCESSIBLE_TABLE_SUMMARY_CHANGED

,

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

,

accessibleDescription

,

accessibleName

,

accessibleParent

---

#### Fields declared in class javax.accessibility. AccessibleContext

Constructor Summary

Constructors

Constructor

Description

Translator

()

Create a new

Translator

.

Translator

​(

Object

o)

Create a new

Translator

with the source object o.

---

#### Constructor Summary

Create a new

Translator

.

Create a new

Translator

with the source object o.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addFocusListener

​(

FocusListener

l)

Adds the specified

FocusListener

to receive focus events from
this component.

void

addPropertyChangeListener

​(

PropertyChangeListener

l)

Add a

PropertyChangeListener

to the listener list.

boolean

contains

​(

Point

p)

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

boolean

equals

​(

Object

o)

Returns true if this object is the same as the one passed in.

static

Accessible

getAccessible

​(

Object

o)

Obtain an object that implements interface

Accessible

.

Accessible

getAccessibleAt

​(

Point

p)

Returns the accessible child contained at the local coordinate
Point, if one exists.

Accessible

getAccessibleChild

​(int i)

Return the nth accessible child of the object.

int

getAccessibleChildrenCount

()

Returns the number of accessible children in the object.

AccessibleContext

getAccessibleContext

()

Returns this object.

String

getAccessibleDescription

()

Get the accessible description of this object.

int

getAccessibleIndexInParent

()

Get the index of this object in its accessible parent.

String

getAccessibleName

()

Get the accessible name of this object.

Accessible

getAccessibleParent

()

Get the accessible parent of this object.

AccessibleRole

getAccessibleRole

()

Get the role of this object.

AccessibleStateSet

getAccessibleStateSet

()

Get the state of this object, given an already populated state.

Color

getBackground

()

Get the background

Color

of this object.

Rectangle

getBounds

()

Returns the current bounds of this object.

Cursor

getCursor

()

Get the

Cursor

of this object.

Font

getFont

()

Get the

Font

of this object.

FontMetrics

getFontMetrics

​(

Font

f)

Get the

FontMetrics

of this object.

Color

getForeground

()

Get the foreground

Color

of this object.

Locale

getLocale

()

Gets the

Locale

of the component.

Point

getLocation

()

Returns the location of the object relative to parent.

Point

getLocationOnScreen

()

Returns the location of the object on the screen.

Dimension

getSize

()

Returns the current size of this object.

Object

getSource

()

Get the source

Object

of the

Translator

.

protected static

Class

<?>

getTranslatorClass

​(

Class

<?> c)

Find a translator for this class.

int

hashCode

()

Return hashcode.

boolean

isEnabled

()

Determine if the object is enabled.

boolean

isFocusTraversable

()

Returns whether this object can accept focus or not.

boolean

isShowing

()

Determine if the object is showing.

boolean

isVisible

()

Determine if the object is visible.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

void

removePropertyChangeListener

​(

PropertyChangeListener

l)

Remove the

PropertyChangeListener

from the listener list.

void

requestFocus

()

Requests focus for this object.

void

setAccessibleDescription

​(

String

s)

Set the accessible description of this object.

void

setAccessibleName

​(

String

s)

Set the name of this object.

void

setBackground

​(

Color

c)

Set the background

Color

of this object.

void

setBounds

​(

Rectangle

r)

Sets the current bounds of this object.

void

setCursor

​(

Cursor

c)

Set the

Cursor

of this object.

void

setEnabled

​(boolean b)

Set the enabled state of the object.

void

setFont

​(

Font

f)

Set the

Font

of this object.

void

setForeground

​(

Color

c)

Set the foreground

Color

of this object.

void

setLocation

​(

Point

p)

Sets the location of the object relative to parent.

void

setSize

​(

Dimension

d)

Sets the current size of this object.

void

setSource

​(

Object

o)

Set the source object of the

Translator

.

void

setVisible

​(boolean b)

Set the visible state of the object.

- Methods declared in class javax.accessibility.

AccessibleContext

firePropertyChange

,

getAccessibleAction

,

getAccessibleComponent

,

getAccessibleEditableText

,

getAccessibleIcon

,

getAccessibleRelationSet

,

getAccessibleSelection

,

getAccessibleTable

,

getAccessibleText

,

getAccessibleValue

,

setAccessibleParent

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Adds the specified

FocusListener

to receive focus events from
this component.

Add a

PropertyChangeListener

to the listener list.

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

Returns true if this object is the same as the one passed in.

Obtain an object that implements interface

Accessible

.

Returns the accessible child contained at the local coordinate
Point, if one exists.

Return the nth accessible child of the object.

Returns the number of accessible children in the object.

Returns this object.

Get the accessible description of this object.

Get the index of this object in its accessible parent.

Get the accessible name of this object.

Get the accessible parent of this object.

Get the role of this object.

Get the state of this object, given an already populated state.

Get the background

Color

of this object.

Returns the current bounds of this object.

Get the

Cursor

of this object.

Get the

Font

of this object.

Get the

FontMetrics

of this object.

Get the foreground

Color

of this object.

Gets the

Locale

of the component.

Returns the location of the object relative to parent.

Returns the location of the object on the screen.

Returns the current size of this object.

Get the source

Object

of the

Translator

.

Find a translator for this class.

Return hashcode.

Determine if the object is enabled.

Returns whether this object can accept focus or not.

Determine if the object is showing.

Determine if the object is visible.

Removes the specified focus listener so it no longer receives focus
events from this component.

Remove the

PropertyChangeListener

from the listener list.

Requests focus for this object.

Set the accessible description of this object.

Set the name of this object.

Set the background

Color

of this object.

Sets the current bounds of this object.

Set the

Cursor

of this object.

Set the enabled state of the object.

Set the

Font

of this object.

Set the foreground

Color

of this object.

Sets the location of the object relative to parent.

Sets the current size of this object.

Set the source object of the

Translator

.

Set the visible state of the object.

Methods declared in class javax.accessibility.

AccessibleContext

firePropertyChange

,

getAccessibleAction

,

getAccessibleComponent

,

getAccessibleEditableText

,

getAccessibleIcon

,

getAccessibleRelationSet

,

getAccessibleSelection

,

getAccessibleTable

,

getAccessibleText

,

getAccessibleValue

,

setAccessibleParent

---

#### Methods declared in class javax.accessibility. AccessibleContext

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- source

```java
protected
Object
source
```

The source object needing translating.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Translator

```java
public Translator()
```

Create a new

Translator

. You must call the

setSource

method to set the object to be translated after calling this constructor.

- Translator

```java
public Translator​(
Object
o)
```

Create a new

Translator

with the source object o.

**Parameters:** o

- the Component that does not implement interface

Accessible

============ METHOD DETAIL ==========

- Method Detail

- getTranslatorClass

```java
protected static
Class
<?> getTranslatorClass​(
Class
<?> c)
```

Find a translator for this class. If one doesn't exist for this
class explicitly, try its superclass and so on.

**Parameters:** c

- a Class
**Returns:** the

Translator

Class for the Class passed in

- getAccessible

```java
public static
Accessible
getAccessible​(
Object
o)
```

Obtain an object that implements interface

Accessible

. If the object
passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

**Parameters:** o

- an Object; if a null is passed in a null is returned
**Returns:** an

Object

, possibly the

Object

passed in, that
implements the

Accessible

interface for the

Object

which was passed in

- getSource

```java
public
Object
getSource()
```

Get the source

Object

of the

Translator

.

**Returns:** the source

Object

of the

Translator

- setSource

```java
public void setSource​(
Object
o)
```

Set the source object of the

Translator

.

**Parameters:** o

- the Component that does not implement interface Accessible

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object is the same as the one passed in.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to check against
**Returns:** true if this is the same object
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** hashcode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Returns this object.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

associated with this object

- getAccessibleName

```java
public
String
getAccessibleName()
```

Get the accessible name of this object.

**Overrides:** getAccessibleName

in class

AccessibleContext
**Returns:** the localized name of the object; can be null if this object
does not have a name
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

- setAccessibleName

```java
public void setAccessibleName​(
String
s)
```

Set the name of this object.

**Overrides:** setAccessibleName

in class

AccessibleContext
**Parameters:** s

- the new localized name of the object
**See Also:** AccessibleContext.getAccessibleName()

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Get the accessible description of this object.

**Overrides:** getAccessibleDescription

in class

AccessibleContext
**Returns:** the description of the object; can be null if this object does
not have a description
**See Also:** AccessibleContext.setAccessibleDescription(java.lang.String)

- setAccessibleDescription

```java
public void setAccessibleDescription​(
String
s)
```

Set the accessible description of this object.

**Overrides:** setAccessibleDescription

in class

AccessibleContext
**Parameters:** s

- the new localized description of the object
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleRole

```java
public
AccessibleRole
getAccessibleRole()
```

Get the role of this object.

**Specified by:** getAccessibleRole

in class

AccessibleContext
**Returns:** an instance of AccessibleRole describing the role of the object
**See Also:** AccessibleRole

- getAccessibleStateSet

```java
public
AccessibleStateSet
getAccessibleStateSet()
```

Get the state of this object, given an already populated state.
This method is intended for use by subclasses so they don't have
to check for everything.

**Specified by:** getAccessibleStateSet

in class

AccessibleContext
**Returns:** an instance of

AccessibleStateSet

containing the current state of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Get the accessible parent of this object.

**Overrides:** getAccessibleParent

in class

AccessibleContext
**Returns:** the accessible parent of this object; can be null if this
object does not have an accessible parent

- getAccessibleIndexInParent

```java
public int getAccessibleIndexInParent()
```

Get the index of this object in its accessible parent.

**Specified by:** getAccessibleIndexInParent

in class

AccessibleContext
**Returns:** -1 of this object does not have an accessible parent; otherwise,
the index of the child in its accessible parent
**See Also:** AccessibleContext.getAccessibleParent()

,

AccessibleContext.getAccessibleChildrenCount()

,

AccessibleContext.getAccessibleChild(int)

- getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount()
```

Returns the number of accessible children in the object.

**Specified by:** getAccessibleChildrenCount

in class

AccessibleContext
**Returns:** the number of accessible children in the object

- getAccessibleChild

```java
public
Accessible
getAccessibleChild​(int i)
```

Return the nth accessible child of the object.

**Specified by:** getAccessibleChild

in class

AccessibleContext
**Parameters:** i

- zero-based index of child
**Returns:** the nth accessible child of the object
**See Also:** AccessibleContext.getAccessibleChildrenCount()

- getLocale

```java
public
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the

Locale

of the component. If the component does not have a
locale, the locale of its parent is returned.

**Specified by:** getLocale

in class

AccessibleContext
**Returns:** the

Locale

of the object
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Add a

PropertyChangeListener

to the listener list. The listener
is registered for all properties.

**Overrides:** addPropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be added
**See Also:** AccessibleContext.ACCESSIBLE_NAME_PROPERTY

,

AccessibleContext.ACCESSIBLE_DESCRIPTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_STATE_PROPERTY

,

AccessibleContext.ACCESSIBLE_VALUE_PROPERTY

,

AccessibleContext.ACCESSIBLE_SELECTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_TEXT_PROPERTY

,

AccessibleContext.ACCESSIBLE_VISIBLE_DATA_PROPERTY

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Remove the

PropertyChangeListener

from the listener list.

**Overrides:** removePropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be removed

- getBackground

```java
public
Color
getBackground()
```

Get the background

Color

of this object.

**Specified by:** getBackground

in interface

AccessibleComponent
**Returns:** if supported, the background

Color

of the object;
otherwise, null
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

- setBackground

```java
public void setBackground​(
Color
c)
```

Set the background

Color

of this object.

**Specified by:** setBackground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the background
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

- getForeground

```java
public
Color
getForeground()
```

Get the foreground

Color

of this object.

**Specified by:** getForeground

in interface

AccessibleComponent
**Returns:** if supported, the foreground

Color

of the object; otherwise, null
**See Also:** AccessibleComponent.setForeground(java.awt.Color)

- setForeground

```java
public void setForeground​(
Color
c)
```

Set the foreground

Color

of this object.

**Specified by:** setForeground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the foreground
**See Also:** AccessibleComponent.getForeground()

- getCursor

```java
public
Cursor
getCursor()
```

Get the

Cursor

of this object.

**Specified by:** getCursor

in interface

AccessibleComponent
**Returns:** if supported, the Cursor of the object; otherwise, null
**See Also:** AccessibleComponent.setCursor(java.awt.Cursor)

- setCursor

```java
public void setCursor​(
Cursor
c)
```

Set the

Cursor

of this object.

**Specified by:** setCursor

in interface

AccessibleComponent
**Parameters:** c

- the new

Cursor

for the object
**See Also:** AccessibleComponent.getCursor()

- getFont

```java
public
Font
getFont()
```

Get the

Font

of this object.

**Specified by:** getFont

in interface

AccessibleComponent
**Returns:** if supported, the

Font

for the object; otherwise, null
**See Also:** AccessibleComponent.setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Set the

Font

of this object.

**Specified by:** setFont

in interface

AccessibleComponent
**Parameters:** f

- the new

Font

for the object
**See Also:** AccessibleComponent.getFont()

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Get the

FontMetrics

of this object.

**Specified by:** getFontMetrics

in interface

AccessibleComponent
**Parameters:** f

- the

Font
**Returns:** if supported, the

FontMetrics

the object; otherwise, null
**See Also:** getFont()

- isEnabled

```java
public boolean isEnabled()
```

Determine if the object is enabled.

**Specified by:** isEnabled

in interface

AccessibleComponent
**Returns:** true if object is enabled; otherwise, false
**See Also:** AccessibleComponent.setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

- setEnabled

```java
public void setEnabled​(boolean b)
```

Set the enabled state of the object.

**Specified by:** setEnabled

in interface

AccessibleComponent
**Parameters:** b

- if true, enables this object; otherwise, disables it
**See Also:** AccessibleComponent.isEnabled()

- isVisible

```java
public boolean isVisible()
```

Determine if the object is visible.

**Specified by:** isVisible

in interface

AccessibleComponent
**Returns:** true if object is visible; otherwise, false
**See Also:** AccessibleComponent.setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

- setVisible

```java
public void setVisible​(boolean b)
```

Set the visible state of the object.

**Specified by:** setVisible

in interface

AccessibleComponent
**Parameters:** b

- if true, shows this object; otherwise, hides it
**See Also:** AccessibleComponent.isVisible()

- isShowing

```java
public boolean isShowing()
```

Determine if the object is showing. This is determined by checking
the visibility of the object and ancestors of the object.

**Specified by:** isShowing

in interface

AccessibleComponent
**Returns:** true if object is showing; otherwise, false

- contains

```java
public boolean contains​(
Point
p)
```

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

**Specified by:** contains

in interface

AccessibleComponent
**Parameters:** p

- the

Point

relative to the coordinate system of the object
**Returns:** true if object contains

Point

; otherwise false
**See Also:** AccessibleComponent.getBounds()

- getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Specified by:** getLocationOnScreen

in interface

AccessibleComponent
**Returns:** location of object on screen; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocation()

- getLocation

```java
public
Point
getLocation()
```

Returns the location of the object relative to parent.

**Specified by:** getLocation

in interface

AccessibleComponent
**Returns:** location of object relative to parent; can be null if
this object or its parent are not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocationOnScreen()

- setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the object relative to parent.

**Specified by:** setLocation

in interface

AccessibleComponent
**Parameters:** p

- the new position for the top-left corner
**See Also:** AccessibleComponent.getLocation()

- getBounds

```java
public
Rectangle
getBounds()
```

Returns the current bounds of this object.

**Specified by:** getBounds

in interface

AccessibleComponent
**Returns:** current bounds of object; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.contains(java.awt.Point)

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Sets the current bounds of this object.

**Specified by:** setBounds

in interface

AccessibleComponent
**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** AccessibleComponent.getBounds()

- getSize

```java
public
Dimension
getSize()
```

Returns the current size of this object.

**Specified by:** getSize

in interface

AccessibleComponent
**Returns:** current size of object; can be null if this object is
not on the screen
**See Also:** AccessibleComponent.setSize(java.awt.Dimension)

- setSize

```java
public void setSize​(
Dimension
d)
```

Sets the current size of this object.

**Specified by:** setSize

in interface

AccessibleComponent
**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** AccessibleComponent.getSize()

- getAccessibleAt

```java
public
Accessible
getAccessibleAt​(
Point
p)
```

Returns the accessible child contained at the local coordinate
Point, if one exists.

**Specified by:** getAccessibleAt

in interface

AccessibleComponent
**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the Accessible at the specified location, if it exists

- isFocusTraversable

```java
public boolean isFocusTraversable()
```

Returns whether this object can accept focus or not.

**Specified by:** isFocusTraversable

in interface

AccessibleComponent
**Returns:** true if object can accept focus; otherwise false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

- requestFocus

```java
public void requestFocus()
```

Requests focus for this object.

**Specified by:** requestFocus

in interface

AccessibleComponent
**See Also:** AccessibleComponent.isFocusTraversable()

- addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified

FocusListener

to receive focus events from
this component.

**Specified by:** addFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener
**See Also:** AccessibleComponent.removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Specified by:** removeFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener; this method performs no function, nor does it
throw an exception if the listener specified was not previously added
to this component; if listener is null, no exception is thrown and no
action is performed.
**See Also:** AccessibleComponent.addFocusListener(java.awt.event.FocusListener)

Field Detail

- source

```java
protected
Object
source
```

The source object needing translating.

---

#### Field Detail

source

```java
protected
Object
source
```

The source object needing translating.

---

#### source

protected

Object

source

The source object needing translating.

Constructor Detail

- Translator

```java
public Translator()
```

Create a new

Translator

. You must call the

setSource

method to set the object to be translated after calling this constructor.

- Translator

```java
public Translator​(
Object
o)
```

Create a new

Translator

with the source object o.

**Parameters:** o

- the Component that does not implement interface

Accessible

---

#### Constructor Detail

Translator

```java
public Translator()
```

Create a new

Translator

. You must call the

setSource

method to set the object to be translated after calling this constructor.

---

#### Translator

public Translator()

Create a new

Translator

. You must call the

setSource

method to set the object to be translated after calling this constructor.

Translator

```java
public Translator​(
Object
o)
```

Create a new

Translator

with the source object o.

**Parameters:** o

- the Component that does not implement interface

Accessible

---

#### Translator

public Translator​(

Object

o)

Create a new

Translator

with the source object o.

Method Detail

- getTranslatorClass

```java
protected static
Class
<?> getTranslatorClass​(
Class
<?> c)
```

Find a translator for this class. If one doesn't exist for this
class explicitly, try its superclass and so on.

**Parameters:** c

- a Class
**Returns:** the

Translator

Class for the Class passed in

- getAccessible

```java
public static
Accessible
getAccessible​(
Object
o)
```

Obtain an object that implements interface

Accessible

. If the object
passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

**Parameters:** o

- an Object; if a null is passed in a null is returned
**Returns:** an

Object

, possibly the

Object

passed in, that
implements the

Accessible

interface for the

Object

which was passed in

- getSource

```java
public
Object
getSource()
```

Get the source

Object

of the

Translator

.

**Returns:** the source

Object

of the

Translator

- setSource

```java
public void setSource​(
Object
o)
```

Set the source object of the

Translator

.

**Parameters:** o

- the Component that does not implement interface Accessible

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object is the same as the one passed in.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to check against
**Returns:** true if this is the same object
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** hashcode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Returns this object.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

associated with this object

- getAccessibleName

```java
public
String
getAccessibleName()
```

Get the accessible name of this object.

**Overrides:** getAccessibleName

in class

AccessibleContext
**Returns:** the localized name of the object; can be null if this object
does not have a name
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

- setAccessibleName

```java
public void setAccessibleName​(
String
s)
```

Set the name of this object.

**Overrides:** setAccessibleName

in class

AccessibleContext
**Parameters:** s

- the new localized name of the object
**See Also:** AccessibleContext.getAccessibleName()

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Get the accessible description of this object.

**Overrides:** getAccessibleDescription

in class

AccessibleContext
**Returns:** the description of the object; can be null if this object does
not have a description
**See Also:** AccessibleContext.setAccessibleDescription(java.lang.String)

- setAccessibleDescription

```java
public void setAccessibleDescription​(
String
s)
```

Set the accessible description of this object.

**Overrides:** setAccessibleDescription

in class

AccessibleContext
**Parameters:** s

- the new localized description of the object
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleRole

```java
public
AccessibleRole
getAccessibleRole()
```

Get the role of this object.

**Specified by:** getAccessibleRole

in class

AccessibleContext
**Returns:** an instance of AccessibleRole describing the role of the object
**See Also:** AccessibleRole

- getAccessibleStateSet

```java
public
AccessibleStateSet
getAccessibleStateSet()
```

Get the state of this object, given an already populated state.
This method is intended for use by subclasses so they don't have
to check for everything.

**Specified by:** getAccessibleStateSet

in class

AccessibleContext
**Returns:** an instance of

AccessibleStateSet

containing the current state of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Get the accessible parent of this object.

**Overrides:** getAccessibleParent

in class

AccessibleContext
**Returns:** the accessible parent of this object; can be null if this
object does not have an accessible parent

- getAccessibleIndexInParent

```java
public int getAccessibleIndexInParent()
```

Get the index of this object in its accessible parent.

**Specified by:** getAccessibleIndexInParent

in class

AccessibleContext
**Returns:** -1 of this object does not have an accessible parent; otherwise,
the index of the child in its accessible parent
**See Also:** AccessibleContext.getAccessibleParent()

,

AccessibleContext.getAccessibleChildrenCount()

,

AccessibleContext.getAccessibleChild(int)

- getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount()
```

Returns the number of accessible children in the object.

**Specified by:** getAccessibleChildrenCount

in class

AccessibleContext
**Returns:** the number of accessible children in the object

- getAccessibleChild

```java
public
Accessible
getAccessibleChild​(int i)
```

Return the nth accessible child of the object.

**Specified by:** getAccessibleChild

in class

AccessibleContext
**Parameters:** i

- zero-based index of child
**Returns:** the nth accessible child of the object
**See Also:** AccessibleContext.getAccessibleChildrenCount()

- getLocale

```java
public
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the

Locale

of the component. If the component does not have a
locale, the locale of its parent is returned.

**Specified by:** getLocale

in class

AccessibleContext
**Returns:** the

Locale

of the object
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Add a

PropertyChangeListener

to the listener list. The listener
is registered for all properties.

**Overrides:** addPropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be added
**See Also:** AccessibleContext.ACCESSIBLE_NAME_PROPERTY

,

AccessibleContext.ACCESSIBLE_DESCRIPTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_STATE_PROPERTY

,

AccessibleContext.ACCESSIBLE_VALUE_PROPERTY

,

AccessibleContext.ACCESSIBLE_SELECTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_TEXT_PROPERTY

,

AccessibleContext.ACCESSIBLE_VISIBLE_DATA_PROPERTY

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Remove the

PropertyChangeListener

from the listener list.

**Overrides:** removePropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be removed

- getBackground

```java
public
Color
getBackground()
```

Get the background

Color

of this object.

**Specified by:** getBackground

in interface

AccessibleComponent
**Returns:** if supported, the background

Color

of the object;
otherwise, null
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

- setBackground

```java
public void setBackground​(
Color
c)
```

Set the background

Color

of this object.

**Specified by:** setBackground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the background
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

- getForeground

```java
public
Color
getForeground()
```

Get the foreground

Color

of this object.

**Specified by:** getForeground

in interface

AccessibleComponent
**Returns:** if supported, the foreground

Color

of the object; otherwise, null
**See Also:** AccessibleComponent.setForeground(java.awt.Color)

- setForeground

```java
public void setForeground​(
Color
c)
```

Set the foreground

Color

of this object.

**Specified by:** setForeground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the foreground
**See Also:** AccessibleComponent.getForeground()

- getCursor

```java
public
Cursor
getCursor()
```

Get the

Cursor

of this object.

**Specified by:** getCursor

in interface

AccessibleComponent
**Returns:** if supported, the Cursor of the object; otherwise, null
**See Also:** AccessibleComponent.setCursor(java.awt.Cursor)

- setCursor

```java
public void setCursor​(
Cursor
c)
```

Set the

Cursor

of this object.

**Specified by:** setCursor

in interface

AccessibleComponent
**Parameters:** c

- the new

Cursor

for the object
**See Also:** AccessibleComponent.getCursor()

- getFont

```java
public
Font
getFont()
```

Get the

Font

of this object.

**Specified by:** getFont

in interface

AccessibleComponent
**Returns:** if supported, the

Font

for the object; otherwise, null
**See Also:** AccessibleComponent.setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Set the

Font

of this object.

**Specified by:** setFont

in interface

AccessibleComponent
**Parameters:** f

- the new

Font

for the object
**See Also:** AccessibleComponent.getFont()

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Get the

FontMetrics

of this object.

**Specified by:** getFontMetrics

in interface

AccessibleComponent
**Parameters:** f

- the

Font
**Returns:** if supported, the

FontMetrics

the object; otherwise, null
**See Also:** getFont()

- isEnabled

```java
public boolean isEnabled()
```

Determine if the object is enabled.

**Specified by:** isEnabled

in interface

AccessibleComponent
**Returns:** true if object is enabled; otherwise, false
**See Also:** AccessibleComponent.setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

- setEnabled

```java
public void setEnabled​(boolean b)
```

Set the enabled state of the object.

**Specified by:** setEnabled

in interface

AccessibleComponent
**Parameters:** b

- if true, enables this object; otherwise, disables it
**See Also:** AccessibleComponent.isEnabled()

- isVisible

```java
public boolean isVisible()
```

Determine if the object is visible.

**Specified by:** isVisible

in interface

AccessibleComponent
**Returns:** true if object is visible; otherwise, false
**See Also:** AccessibleComponent.setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

- setVisible

```java
public void setVisible​(boolean b)
```

Set the visible state of the object.

**Specified by:** setVisible

in interface

AccessibleComponent
**Parameters:** b

- if true, shows this object; otherwise, hides it
**See Also:** AccessibleComponent.isVisible()

- isShowing

```java
public boolean isShowing()
```

Determine if the object is showing. This is determined by checking
the visibility of the object and ancestors of the object.

**Specified by:** isShowing

in interface

AccessibleComponent
**Returns:** true if object is showing; otherwise, false

- contains

```java
public boolean contains​(
Point
p)
```

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

**Specified by:** contains

in interface

AccessibleComponent
**Parameters:** p

- the

Point

relative to the coordinate system of the object
**Returns:** true if object contains

Point

; otherwise false
**See Also:** AccessibleComponent.getBounds()

- getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Specified by:** getLocationOnScreen

in interface

AccessibleComponent
**Returns:** location of object on screen; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocation()

- getLocation

```java
public
Point
getLocation()
```

Returns the location of the object relative to parent.

**Specified by:** getLocation

in interface

AccessibleComponent
**Returns:** location of object relative to parent; can be null if
this object or its parent are not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocationOnScreen()

- setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the object relative to parent.

**Specified by:** setLocation

in interface

AccessibleComponent
**Parameters:** p

- the new position for the top-left corner
**See Also:** AccessibleComponent.getLocation()

- getBounds

```java
public
Rectangle
getBounds()
```

Returns the current bounds of this object.

**Specified by:** getBounds

in interface

AccessibleComponent
**Returns:** current bounds of object; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.contains(java.awt.Point)

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Sets the current bounds of this object.

**Specified by:** setBounds

in interface

AccessibleComponent
**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** AccessibleComponent.getBounds()

- getSize

```java
public
Dimension
getSize()
```

Returns the current size of this object.

**Specified by:** getSize

in interface

AccessibleComponent
**Returns:** current size of object; can be null if this object is
not on the screen
**See Also:** AccessibleComponent.setSize(java.awt.Dimension)

- setSize

```java
public void setSize​(
Dimension
d)
```

Sets the current size of this object.

**Specified by:** setSize

in interface

AccessibleComponent
**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** AccessibleComponent.getSize()

- getAccessibleAt

```java
public
Accessible
getAccessibleAt​(
Point
p)
```

Returns the accessible child contained at the local coordinate
Point, if one exists.

**Specified by:** getAccessibleAt

in interface

AccessibleComponent
**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the Accessible at the specified location, if it exists

- isFocusTraversable

```java
public boolean isFocusTraversable()
```

Returns whether this object can accept focus or not.

**Specified by:** isFocusTraversable

in interface

AccessibleComponent
**Returns:** true if object can accept focus; otherwise false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

- requestFocus

```java
public void requestFocus()
```

Requests focus for this object.

**Specified by:** requestFocus

in interface

AccessibleComponent
**See Also:** AccessibleComponent.isFocusTraversable()

- addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified

FocusListener

to receive focus events from
this component.

**Specified by:** addFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener
**See Also:** AccessibleComponent.removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Specified by:** removeFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener; this method performs no function, nor does it
throw an exception if the listener specified was not previously added
to this component; if listener is null, no exception is thrown and no
action is performed.
**See Also:** AccessibleComponent.addFocusListener(java.awt.event.FocusListener)

---

#### Method Detail

getTranslatorClass

```java
protected static
Class
<?> getTranslatorClass​(
Class
<?> c)
```

Find a translator for this class. If one doesn't exist for this
class explicitly, try its superclass and so on.

**Parameters:** c

- a Class
**Returns:** the

Translator

Class for the Class passed in

---

#### getTranslatorClass

protected static

Class

<?> getTranslatorClass​(

Class

<?> c)

Find a translator for this class. If one doesn't exist for this
class explicitly, try its superclass and so on.

getAccessible

```java
public static
Accessible
getAccessible​(
Object
o)
```

Obtain an object that implements interface

Accessible

. If the object
passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

**Parameters:** o

- an Object; if a null is passed in a null is returned
**Returns:** an

Object

, possibly the

Object

passed in, that
implements the

Accessible

interface for the

Object

which was passed in

---

#### getAccessible

public static

Accessible

getAccessible​(

Object

o)

Obtain an object that implements interface

Accessible

. If the object
passed in already implements interface

Accessible

,

getAccessible

merely returns the object.

getSource

```java
public
Object
getSource()
```

Get the source

Object

of the

Translator

.

**Returns:** the source

Object

of the

Translator

---

#### getSource

public

Object

getSource()

Get the source

Object

of the

Translator

.

setSource

```java
public void setSource​(
Object
o)
```

Set the source object of the

Translator

.

**Parameters:** o

- the Component that does not implement interface Accessible

---

#### setSource

public void setSource​(

Object

o)

Set the source object of the

Translator

.

equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object is the same as the one passed in.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to check against
**Returns:** true if this is the same object
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Returns true if this object is the same as the one passed in.

hashCode

```java
public int hashCode()
```

Return hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** hashcode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return hashcode.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Returns this object.

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

associated with this object

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Returns this object.

getAccessibleName

```java
public
String
getAccessibleName()
```

Get the accessible name of this object.

**Overrides:** getAccessibleName

in class

AccessibleContext
**Returns:** the localized name of the object; can be null if this object
does not have a name
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

---

#### getAccessibleName

public

String

getAccessibleName()

Get the accessible name of this object.

setAccessibleName

```java
public void setAccessibleName​(
String
s)
```

Set the name of this object.

**Overrides:** setAccessibleName

in class

AccessibleContext
**Parameters:** s

- the new localized name of the object
**See Also:** AccessibleContext.getAccessibleName()

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### setAccessibleName

public void setAccessibleName​(

String

s)

Set the name of this object.

getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Get the accessible description of this object.

**Overrides:** getAccessibleDescription

in class

AccessibleContext
**Returns:** the description of the object; can be null if this object does
not have a description
**See Also:** AccessibleContext.setAccessibleDescription(java.lang.String)

---

#### getAccessibleDescription

public

String

getAccessibleDescription()

Get the accessible description of this object.

setAccessibleDescription

```java
public void setAccessibleDescription​(
String
s)
```

Set the accessible description of this object.

**Overrides:** setAccessibleDescription

in class

AccessibleContext
**Parameters:** s

- the new localized description of the object
**See Also:** AccessibleContext.setAccessibleName(java.lang.String)

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### setAccessibleDescription

public void setAccessibleDescription​(

String

s)

Set the accessible description of this object.

getAccessibleRole

```java
public
AccessibleRole
getAccessibleRole()
```

Get the role of this object.

**Specified by:** getAccessibleRole

in class

AccessibleContext
**Returns:** an instance of AccessibleRole describing the role of the object
**See Also:** AccessibleRole

---

#### getAccessibleRole

public

AccessibleRole

getAccessibleRole()

Get the role of this object.

getAccessibleStateSet

```java
public
AccessibleStateSet
getAccessibleStateSet()
```

Get the state of this object, given an already populated state.
This method is intended for use by subclasses so they don't have
to check for everything.

**Specified by:** getAccessibleStateSet

in class

AccessibleContext
**Returns:** an instance of

AccessibleStateSet

containing the current state of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

AccessibleContext.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### getAccessibleStateSet

public

AccessibleStateSet

getAccessibleStateSet()

Get the state of this object, given an already populated state.
This method is intended for use by subclasses so they don't have
to check for everything.

getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Get the accessible parent of this object.

**Overrides:** getAccessibleParent

in class

AccessibleContext
**Returns:** the accessible parent of this object; can be null if this
object does not have an accessible parent

---

#### getAccessibleParent

public

Accessible

getAccessibleParent()

Get the accessible parent of this object.

getAccessibleIndexInParent

```java
public int getAccessibleIndexInParent()
```

Get the index of this object in its accessible parent.

**Specified by:** getAccessibleIndexInParent

in class

AccessibleContext
**Returns:** -1 of this object does not have an accessible parent; otherwise,
the index of the child in its accessible parent
**See Also:** AccessibleContext.getAccessibleParent()

,

AccessibleContext.getAccessibleChildrenCount()

,

AccessibleContext.getAccessibleChild(int)

---

#### getAccessibleIndexInParent

public int getAccessibleIndexInParent()

Get the index of this object in its accessible parent.

getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount()
```

Returns the number of accessible children in the object.

**Specified by:** getAccessibleChildrenCount

in class

AccessibleContext
**Returns:** the number of accessible children in the object

---

#### getAccessibleChildrenCount

public int getAccessibleChildrenCount()

Returns the number of accessible children in the object.

getAccessibleChild

```java
public
Accessible
getAccessibleChild​(int i)
```

Return the nth accessible child of the object.

**Specified by:** getAccessibleChild

in class

AccessibleContext
**Parameters:** i

- zero-based index of child
**Returns:** the nth accessible child of the object
**See Also:** AccessibleContext.getAccessibleChildrenCount()

---

#### getAccessibleChild

public

Accessible

getAccessibleChild​(int i)

Return the nth accessible child of the object.

getLocale

```java
public
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the

Locale

of the component. If the component does not have a
locale, the locale of its parent is returned.

**Specified by:** getLocale

in class

AccessibleContext
**Returns:** the

Locale

of the object
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

---

#### getLocale

public

Locale

getLocale()
throws

IllegalComponentStateException

Gets the

Locale

of the component. If the component does not have a
locale, the locale of its parent is returned.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Add a

PropertyChangeListener

to the listener list. The listener
is registered for all properties.

**Overrides:** addPropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be added
**See Also:** AccessibleContext.ACCESSIBLE_NAME_PROPERTY

,

AccessibleContext.ACCESSIBLE_DESCRIPTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_STATE_PROPERTY

,

AccessibleContext.ACCESSIBLE_VALUE_PROPERTY

,

AccessibleContext.ACCESSIBLE_SELECTION_PROPERTY

,

AccessibleContext.ACCESSIBLE_TEXT_PROPERTY

,

AccessibleContext.ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

l)

Add a

PropertyChangeListener

to the listener list. The listener
is registered for all properties.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Remove the

PropertyChangeListener

from the listener list.

**Overrides:** removePropertyChangeListener

in class

AccessibleContext
**Parameters:** l

- The PropertyChangeListener to be removed

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

l)

Remove the

PropertyChangeListener

from the listener list.

getBackground

```java
public
Color
getBackground()
```

Get the background

Color

of this object.

**Specified by:** getBackground

in interface

AccessibleComponent
**Returns:** if supported, the background

Color

of the object;
otherwise, null
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

---

#### getBackground

public

Color

getBackground()

Get the background

Color

of this object.

setBackground

```java
public void setBackground​(
Color
c)
```

Set the background

Color

of this object.

**Specified by:** setBackground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the background
**See Also:** AccessibleComponent.setBackground(java.awt.Color)

---

#### setBackground

public void setBackground​(

Color

c)

Set the background

Color

of this object.

getForeground

```java
public
Color
getForeground()
```

Get the foreground

Color

of this object.

**Specified by:** getForeground

in interface

AccessibleComponent
**Returns:** if supported, the foreground

Color

of the object; otherwise, null
**See Also:** AccessibleComponent.setForeground(java.awt.Color)

---

#### getForeground

public

Color

getForeground()

Get the foreground

Color

of this object.

setForeground

```java
public void setForeground​(
Color
c)
```

Set the foreground

Color

of this object.

**Specified by:** setForeground

in interface

AccessibleComponent
**Parameters:** c

- the new

Color

for the foreground
**See Also:** AccessibleComponent.getForeground()

---

#### setForeground

public void setForeground​(

Color

c)

Set the foreground

Color

of this object.

getCursor

```java
public
Cursor
getCursor()
```

Get the

Cursor

of this object.

**Specified by:** getCursor

in interface

AccessibleComponent
**Returns:** if supported, the Cursor of the object; otherwise, null
**See Also:** AccessibleComponent.setCursor(java.awt.Cursor)

---

#### getCursor

public

Cursor

getCursor()

Get the

Cursor

of this object.

setCursor

```java
public void setCursor​(
Cursor
c)
```

Set the

Cursor

of this object.

**Specified by:** setCursor

in interface

AccessibleComponent
**Parameters:** c

- the new

Cursor

for the object
**See Also:** AccessibleComponent.getCursor()

---

#### setCursor

public void setCursor​(

Cursor

c)

Set the

Cursor

of this object.

getFont

```java
public
Font
getFont()
```

Get the

Font

of this object.

**Specified by:** getFont

in interface

AccessibleComponent
**Returns:** if supported, the

Font

for the object; otherwise, null
**See Also:** AccessibleComponent.setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Get the

Font

of this object.

setFont

```java
public void setFont​(
Font
f)
```

Set the

Font

of this object.

**Specified by:** setFont

in interface

AccessibleComponent
**Parameters:** f

- the new

Font

for the object
**See Also:** AccessibleComponent.getFont()

---

#### setFont

public void setFont​(

Font

f)

Set the

Font

of this object.

getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Get the

FontMetrics

of this object.

**Specified by:** getFontMetrics

in interface

AccessibleComponent
**Parameters:** f

- the

Font
**Returns:** if supported, the

FontMetrics

the object; otherwise, null
**See Also:** getFont()

---

#### getFontMetrics

public

FontMetrics

getFontMetrics​(

Font

f)

Get the

FontMetrics

of this object.

isEnabled

```java
public boolean isEnabled()
```

Determine if the object is enabled.

**Specified by:** isEnabled

in interface

AccessibleComponent
**Returns:** true if object is enabled; otherwise, false
**See Also:** AccessibleComponent.setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

---

#### isEnabled

public boolean isEnabled()

Determine if the object is enabled.

setEnabled

```java
public void setEnabled​(boolean b)
```

Set the enabled state of the object.

**Specified by:** setEnabled

in interface

AccessibleComponent
**Parameters:** b

- if true, enables this object; otherwise, disables it
**See Also:** AccessibleComponent.isEnabled()

---

#### setEnabled

public void setEnabled​(boolean b)

Set the enabled state of the object.

isVisible

```java
public boolean isVisible()
```

Determine if the object is visible.

**Specified by:** isVisible

in interface

AccessibleComponent
**Returns:** true if object is visible; otherwise, false
**See Also:** AccessibleComponent.setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

---

#### isVisible

public boolean isVisible()

Determine if the object is visible.

setVisible

```java
public void setVisible​(boolean b)
```

Set the visible state of the object.

**Specified by:** setVisible

in interface

AccessibleComponent
**Parameters:** b

- if true, shows this object; otherwise, hides it
**See Also:** AccessibleComponent.isVisible()

---

#### setVisible

public void setVisible​(boolean b)

Set the visible state of the object.

isShowing

```java
public boolean isShowing()
```

Determine if the object is showing. This is determined by checking
the visibility of the object and ancestors of the object.

**Specified by:** isShowing

in interface

AccessibleComponent
**Returns:** true if object is showing; otherwise, false

---

#### isShowing

public boolean isShowing()

Determine if the object is showing. This is determined by checking
the visibility of the object and ancestors of the object.

contains

```java
public boolean contains​(
Point
p)
```

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

**Specified by:** contains

in interface

AccessibleComponent
**Parameters:** p

- the

Point

relative to the coordinate system of the object
**Returns:** true if object contains

Point

; otherwise false
**See Also:** AccessibleComponent.getBounds()

---

#### contains

public boolean contains​(

Point

p)

Checks whether the specified

Point

is within this
object's bounds, where the

Point

is relative to the coordinate
system of the object.

getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Specified by:** getLocationOnScreen

in interface

AccessibleComponent
**Returns:** location of object on screen; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocation()

---

#### getLocationOnScreen

public

Point

getLocationOnScreen()

Returns the location of the object on the screen.

getLocation

```java
public
Point
getLocation()
```

Returns the location of the object relative to parent.

**Specified by:** getLocation

in interface

AccessibleComponent
**Returns:** location of object relative to parent; can be null if
this object or its parent are not on the screen
**See Also:** AccessibleComponent.getBounds()

,

AccessibleComponent.getLocationOnScreen()

---

#### getLocation

public

Point

getLocation()

Returns the location of the object relative to parent.

setLocation

```java
public void setLocation​(
Point
p)
```

Sets the location of the object relative to parent.

**Specified by:** setLocation

in interface

AccessibleComponent
**Parameters:** p

- the new position for the top-left corner
**See Also:** AccessibleComponent.getLocation()

---

#### setLocation

public void setLocation​(

Point

p)

Sets the location of the object relative to parent.

getBounds

```java
public
Rectangle
getBounds()
```

Returns the current bounds of this object.

**Specified by:** getBounds

in interface

AccessibleComponent
**Returns:** current bounds of object; can be null if this object
is not on the screen
**See Also:** AccessibleComponent.contains(java.awt.Point)

---

#### getBounds

public

Rectangle

getBounds()

Returns the current bounds of this object.

setBounds

```java
public void setBounds​(
Rectangle
r)
```

Sets the current bounds of this object.

**Specified by:** setBounds

in interface

AccessibleComponent
**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** AccessibleComponent.getBounds()

---

#### setBounds

public void setBounds​(

Rectangle

r)

Sets the current bounds of this object.

getSize

```java
public
Dimension
getSize()
```

Returns the current size of this object.

**Specified by:** getSize

in interface

AccessibleComponent
**Returns:** current size of object; can be null if this object is
not on the screen
**See Also:** AccessibleComponent.setSize(java.awt.Dimension)

---

#### getSize

public

Dimension

getSize()

Returns the current size of this object.

setSize

```java
public void setSize​(
Dimension
d)
```

Sets the current size of this object.

**Specified by:** setSize

in interface

AccessibleComponent
**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** AccessibleComponent.getSize()

---

#### setSize

public void setSize​(

Dimension

d)

Sets the current size of this object.

getAccessibleAt

```java
public
Accessible
getAccessibleAt​(
Point
p)
```

Returns the accessible child contained at the local coordinate
Point, if one exists.

**Specified by:** getAccessibleAt

in interface

AccessibleComponent
**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the Accessible at the specified location, if it exists

---

#### getAccessibleAt

public

Accessible

getAccessibleAt​(

Point

p)

Returns the accessible child contained at the local coordinate
Point, if one exists.

isFocusTraversable

```java
public boolean isFocusTraversable()
```

Returns whether this object can accept focus or not.

**Specified by:** isFocusTraversable

in interface

AccessibleComponent
**Returns:** true if object can accept focus; otherwise false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

---

#### isFocusTraversable

public boolean isFocusTraversable()

Returns whether this object can accept focus or not.

requestFocus

```java
public void requestFocus()
```

Requests focus for this object.

**Specified by:** requestFocus

in interface

AccessibleComponent
**See Also:** AccessibleComponent.isFocusTraversable()

---

#### requestFocus

public void requestFocus()

Requests focus for this object.

addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified

FocusListener

to receive focus events from
this component.

**Specified by:** addFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener
**See Also:** AccessibleComponent.removeFocusListener(java.awt.event.FocusListener)

---

#### addFocusListener

public void addFocusListener​(

FocusListener

l)

Adds the specified

FocusListener

to receive focus events from
this component.

removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Specified by:** removeFocusListener

in interface

AccessibleComponent
**Parameters:** l

- the focus listener; this method performs no function, nor does it
throw an exception if the listener specified was not previously added
to this component; if listener is null, no exception is thrown and no
action is performed.
**See Also:** AccessibleComponent.addFocusListener(java.awt.event.FocusListener)

---

#### removeFocusListener

public void removeFocusListener​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

---

