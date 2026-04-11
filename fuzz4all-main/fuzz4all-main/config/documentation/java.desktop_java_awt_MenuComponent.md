# Class MenuComponent

**Source:** `java.desktop\java\awt\MenuComponent.html`

### Class Description

```java
public abstract class
MenuComponent

extends
Object

implements
Serializable
```

The abstract class

MenuComponent

is the superclass
of all menu-related components. In this respect, the class

MenuComponent

is analogous to the abstract superclass

Component

for AWT components.

Menu components receive and process AWT events, just as components do,
through the method

processEvent

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MenuComponent()
throws
HeadlessException

Creates a

MenuComponent

.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public
String
getName()

Gets the name of the menu component.

**Returns:**
- the name of the menu component

**See Also:**
- setName(java.lang.String)

**Since:**
- 1.1

---

#### public void setName​(
String
name)

Sets the name of the component to the specified string.

**Parameters:**
- name

- the name of the menu component

**See Also:**
- getName()

**Since:**
- 1.1

---

#### public
MenuContainer
getParent()

Returns the parent container for this menu component.

**Returns:**
- the menu component containing this menu component,
or

null

if this menu component
is the outermost component, the menu bar itself

---

#### public
Font
getFont()

Gets the font used for this menu component.

**Returns:**
- the font used in this menu component, if there is one;

null

otherwise

**See Also:**
- setFont(java.awt.Font)

---

#### public void setFont​(
Font
f)

Sets the font to be used for this menu component to the specified
font. This font is also used by all subcomponents of this menu
component, unless those subcomponents specify a different font.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

**Parameters:**
- f

- the font to be set

**See Also:**
- getFont()

,

Font.getAttributes()

,

TextAttribute

---

#### public void removeNotify()

Removes the menu component's peer. The peer allows us to modify the
appearance of the menu component without changing the functionality of
the menu component.

---

#### @Deprecated

public boolean postEvent​(
Event
evt)

Posts the specified event to the menu.
This method is part of the Java 1.0 event system
and it is maintained only for backwards compatibility.
Its use is discouraged, and it may not be supported
in the future.

**Parameters:**
- evt

- the event which is to take place

**Returns:**
- unconditionally returns false

---

#### public final void dispatchEvent​(
AWTEvent
e)

Delivers an event to this component or one of its sub components.

**Parameters:**
- e

- the event

---

#### protected void processEvent​(
AWTEvent
e)

Processes events occurring on this menu component.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the event

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns a string representing the state of this

MenuComponent

. This method is intended to be used
only for debugging purposes, and the content and format of the
returned string may vary between implementations. The returned
string may be empty but may not be

null

.

**Returns:**
- the parameter string of this menu component

---

#### public
String
toString()

Returns a representation of this menu component as a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this menu component

---

#### protected final
Object
getTreeLock()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:**
- this component's locking object

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with
this

MenuComponent

.

The method implemented by this base class returns

null

.
Classes that extend

MenuComponent

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:**
- the

AccessibleContext

of this

MenuComponent

**Since:**
- 1.3

---

### Additional Sections

#### Class MenuComponent

java.lang.Object

- java.awt.MenuComponent

java.awt.MenuComponent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** MenuBar

,

MenuItem

```java
public abstract class
MenuComponent

extends
Object

implements
Serializable
```

The abstract class

MenuComponent

is the superclass
of all menu-related components. In this respect, the class

MenuComponent

is analogous to the abstract superclass

Component

for AWT components.

Menu components receive and process AWT events, just as components do,
through the method

processEvent

.

**Since:** 1.0
**See Also:** Serialized Form

public abstract class

MenuComponent

extends

Object

implements

Serializable

The abstract class

MenuComponent

is the superclass
of all menu-related components. In this respect, the class

MenuComponent

is analogous to the abstract superclass

Component

for AWT components.

Menu components receive and process AWT events, just as components do,
through the method

processEvent

.

Menu components receive and process AWT events, just as components do,
through the method

processEvent

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

MenuComponent.AccessibleAWTMenuComponent

Inner class of

MenuComponent

used to provide
default support for accessibility.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MenuComponent

()

Creates a

MenuComponent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

dispatchEvent

​(

AWTEvent

e)

Delivers an event to this component or one of its sub components.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with
this

MenuComponent

.

Font

getFont

()

Gets the font used for this menu component.

String

getName

()

Gets the name of the menu component.

MenuContainer

getParent

()

Returns the parent container for this menu component.

protected

Object

getTreeLock

()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

protected

String

paramString

()

Returns a string representing the state of this

MenuComponent

.

boolean

postEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

protected void

processEvent

​(

AWTEvent

e)

Processes events occurring on this menu component.

void

removeNotify

()

Removes the menu component's peer.

void

setFont

​(

Font

f)

Sets the font to be used for this menu component to the specified
font.

void

setName

​(

String

name)

Sets the name of the component to the specified string.

String

toString

()

Returns a representation of this menu component as a string.

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

MenuComponent.AccessibleAWTMenuComponent

Inner class of

MenuComponent

used to provide
default support for accessibility.

---

#### Nested Class Summary

Inner class of

MenuComponent

used to provide
default support for accessibility.

Constructor Summary

Constructors

Constructor

Description

MenuComponent

()

Creates a

MenuComponent

.

---

#### Constructor Summary

Creates a

MenuComponent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

dispatchEvent

​(

AWTEvent

e)

Delivers an event to this component or one of its sub components.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with
this

MenuComponent

.

Font

getFont

()

Gets the font used for this menu component.

String

getName

()

Gets the name of the menu component.

MenuContainer

getParent

()

Returns the parent container for this menu component.

protected

Object

getTreeLock

()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

protected

String

paramString

()

Returns a string representing the state of this

MenuComponent

.

boolean

postEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

protected void

processEvent

​(

AWTEvent

e)

Processes events occurring on this menu component.

void

removeNotify

()

Removes the menu component's peer.

void

setFont

​(

Font

f)

Sets the font to be used for this menu component to the specified
font.

void

setName

​(

String

name)

Sets the name of the component to the specified string.

String

toString

()

Returns a representation of this menu component as a string.

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

wait

,

wait

,

wait

---

#### Method Summary

Delivers an event to this component or one of its sub components.

Gets the

AccessibleContext

associated with
this

MenuComponent

.

Gets the font used for this menu component.

Gets the name of the menu component.

Returns the parent container for this menu component.

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

Returns a string representing the state of this

MenuComponent

.

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

Processes events occurring on this menu component.

Removes the menu component's peer.

Sets the font to be used for this menu component to the specified
font.

Sets the name of the component to the specified string.

Returns a representation of this menu component as a string.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MenuComponent

```java
public MenuComponent()
throws
HeadlessException
```

Creates a

MenuComponent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the menu component.

**Returns:** the name of the menu component
**Since:** 1.1
**See Also:** setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the name of the menu component
**Since:** 1.1
**See Also:** getName()

- getParent

```java
public
MenuContainer
getParent()
```

Returns the parent container for this menu component.

**Returns:** the menu component containing this menu component,
or

null

if this menu component
is the outermost component, the menu bar itself

- getFont

```java
public
Font
getFont()
```

Gets the font used for this menu component.

**Returns:** the font used in this menu component, if there is one;

null

otherwise
**See Also:** setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font to be used for this menu component to the specified
font. This font is also used by all subcomponents of this menu
component, unless those subcomponents specify a different font.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

**Parameters:** f

- the font to be set
**See Also:** getFont()

,

Font.getAttributes()

,

TextAttribute

- removeNotify

```java
public void removeNotify()
```

Removes the menu component's peer. The peer allows us to modify the
appearance of the menu component without changing the functionality of
the menu component.

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

Posts the specified event to the menu.
This method is part of the Java 1.0 event system
and it is maintained only for backwards compatibility.
Its use is discouraged, and it may not be supported
in the future.

**Parameters:** evt

- the event which is to take place
**Returns:** unconditionally returns false

- dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Delivers an event to this component or one of its sub components.

**Parameters:** e

- the event

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this menu component.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

MenuComponent

. This method is intended to be used
only for debugging purposes, and the content and format of the
returned string may vary between implementations. The returned
string may be empty but may not be

null

.

**Returns:** the parameter string of this menu component

- toString

```java
public
String
toString()
```

Returns a representation of this menu component as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this menu component

- getTreeLock

```java
protected final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with
this

MenuComponent

.

The method implemented by this base class returns

null

.
Classes that extend

MenuComponent

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

MenuComponent
**Since:** 1.3

Constructor Detail

- MenuComponent

```java
public MenuComponent()
throws
HeadlessException
```

Creates a

MenuComponent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

MenuComponent

```java
public MenuComponent()
throws
HeadlessException
```

Creates a

MenuComponent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### MenuComponent

public MenuComponent()
throws

HeadlessException

Creates a

MenuComponent

.

Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the menu component.

**Returns:** the name of the menu component
**Since:** 1.1
**See Also:** setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the name of the menu component
**Since:** 1.1
**See Also:** getName()

- getParent

```java
public
MenuContainer
getParent()
```

Returns the parent container for this menu component.

**Returns:** the menu component containing this menu component,
or

null

if this menu component
is the outermost component, the menu bar itself

- getFont

```java
public
Font
getFont()
```

Gets the font used for this menu component.

**Returns:** the font used in this menu component, if there is one;

null

otherwise
**See Also:** setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font to be used for this menu component to the specified
font. This font is also used by all subcomponents of this menu
component, unless those subcomponents specify a different font.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

**Parameters:** f

- the font to be set
**See Also:** getFont()

,

Font.getAttributes()

,

TextAttribute

- removeNotify

```java
public void removeNotify()
```

Removes the menu component's peer. The peer allows us to modify the
appearance of the menu component without changing the functionality of
the menu component.

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

Posts the specified event to the menu.
This method is part of the Java 1.0 event system
and it is maintained only for backwards compatibility.
Its use is discouraged, and it may not be supported
in the future.

**Parameters:** evt

- the event which is to take place
**Returns:** unconditionally returns false

- dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Delivers an event to this component or one of its sub components.

**Parameters:** e

- the event

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this menu component.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

MenuComponent

. This method is intended to be used
only for debugging purposes, and the content and format of the
returned string may vary between implementations. The returned
string may be empty but may not be

null

.

**Returns:** the parameter string of this menu component

- toString

```java
public
String
toString()
```

Returns a representation of this menu component as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this menu component

- getTreeLock

```java
protected final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with
this

MenuComponent

.

The method implemented by this base class returns

null

.
Classes that extend

MenuComponent

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

MenuComponent
**Since:** 1.3

---

#### Method Detail

getName

```java
public
String
getName()
```

Gets the name of the menu component.

**Returns:** the name of the menu component
**Since:** 1.1
**See Also:** setName(java.lang.String)

---

#### getName

public

String

getName()

Gets the name of the menu component.

setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the name of the menu component
**Since:** 1.1
**See Also:** getName()

---

#### setName

public void setName​(

String

name)

Sets the name of the component to the specified string.

getParent

```java
public
MenuContainer
getParent()
```

Returns the parent container for this menu component.

**Returns:** the menu component containing this menu component,
or

null

if this menu component
is the outermost component, the menu bar itself

---

#### getParent

public

MenuContainer

getParent()

Returns the parent container for this menu component.

getFont

```java
public
Font
getFont()
```

Gets the font used for this menu component.

**Returns:** the font used in this menu component, if there is one;

null

otherwise
**See Also:** setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Gets the font used for this menu component.

setFont

```java
public void setFont​(
Font
f)
```

Sets the font to be used for this menu component to the specified
font. This font is also used by all subcomponents of this menu
component, unless those subcomponents specify a different font.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

**Parameters:** f

- the font to be set
**See Also:** getFont()

,

Font.getAttributes()

,

TextAttribute

---

#### setFont

public void setFont​(

Font

f)

Sets the font to be used for this menu component to the specified
font. This font is also used by all subcomponents of this menu
component, unless those subcomponents specify a different font.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

Some platforms may not support setting of all font attributes
of a menu component; in such cases, calling

setFont

will have no effect on the unsupported font attributes of this
menu component. Unless subcomponents of this menu component
specify a different font, this font will be used by those
subcomponents if supported by the underlying platform.

removeNotify

```java
public void removeNotify()
```

Removes the menu component's peer. The peer allows us to modify the
appearance of the menu component without changing the functionality of
the menu component.

---

#### removeNotify

public void removeNotify()

Removes the menu component's peer. The peer allows us to modify the
appearance of the menu component without changing the functionality of
the menu component.

postEvent

```java
@Deprecated

public boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1, replaced by

dispatchEvent

.

Posts the specified event to the menu.
This method is part of the Java 1.0 event system
and it is maintained only for backwards compatibility.
Its use is discouraged, and it may not be supported
in the future.

**Parameters:** evt

- the event which is to take place
**Returns:** unconditionally returns false

---

#### postEvent

@Deprecated

public boolean postEvent​(

Event

evt)

Posts the specified event to the menu.
This method is part of the Java 1.0 event system
and it is maintained only for backwards compatibility.
Its use is discouraged, and it may not be supported
in the future.

dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Delivers an event to this component or one of its sub components.

**Parameters:** e

- the event

---

#### dispatchEvent

public final void dispatchEvent​(

AWTEvent

e)

Delivers an event to this component or one of its sub components.

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this menu component.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events occurring on this menu component.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

MenuComponent

. This method is intended to be used
only for debugging purposes, and the content and format of the
returned string may vary between implementations. The returned
string may be empty but may not be

null

.

**Returns:** the parameter string of this menu component

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

MenuComponent

. This method is intended to be used
only for debugging purposes, and the content and format of the
returned string may vary between implementations. The returned
string may be empty but may not be

null

.

toString

```java
public
String
toString()
```

Returns a representation of this menu component as a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this menu component

---

#### toString

public

String

toString()

Returns a representation of this menu component as a string.

getTreeLock

```java
protected final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

---

#### getTreeLock

protected final

Object

getTreeLock()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with
this

MenuComponent

.

The method implemented by this base class returns

null

.
Classes that extend

MenuComponent

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

MenuComponent
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with
this

MenuComponent

.

The method implemented by this base class returns

null

.
Classes that extend

MenuComponent

should implement this method to return the

AccessibleContext

associated with the subclass.

---

