# Class AccessibleHyperlink

**Source:** `java.desktop\javax\accessibility\AccessibleHyperlink.html`

### Class Description

```java
public abstract class
AccessibleHyperlink

extends
Object

implements
AccessibleAction
```

Encapsulation of a link, or set of links (e.g. client side imagemap) in a
Hypertext document

**All Implemented Interfaces:** AccessibleAction

---

### Field Details

*No entries found.*

### Constructor Details

#### public AccessibleHyperlink()

*No description found.*

---

### Method Details

#### public abstract boolean isValid()

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

**Returns:**
- a flag indicating whether this link is still valid with respect
to the

AccessibleHypertext

it belongs to

---

#### public abstract int getAccessibleActionCount()

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap). In general, links will
have only one

AccessibleAction

in them.

**Specified by:**
- getAccessibleActionCount

in interface

AccessibleAction

**Returns:**
- the zero-based number of actions in this object

---

#### public abstract boolean doAccessibleAction​(int i)

Performs the specified action on the object.

**Specified by:**
- doAccessibleAction

in interface

AccessibleAction

**Parameters:**
- i

- zero-based index of actions

**Returns:**
- true

if the action was performed; otherwise

false

**See Also:**
- getAccessibleActionCount()

---

#### public abstract
String
getAccessibleActionDescription​(int i)

Returns a string description of this particular link action. This should
be a text string associated with anchoring text, this should be the
anchor text. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

**Specified by:**
- getAccessibleActionDescription

in interface

AccessibleAction

**Parameters:**
- i

- zero-based index of the actions

**Returns:**
- a string description of the action

**See Also:**
- getAccessibleActionCount()

---

#### public abstract
Object
getAccessibleActionObject​(int i)

Returns an object that represents the link action, as appropriate for
that link. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return a java.net.URL("http://www.sun.com/access.html");

**Parameters:**
- i

- zero-based index of the actions

**Returns:**
- an object representing the hypertext link itself

**See Also:**
- getAccessibleActionCount()

---

#### public abstract
Object
getAccessibleActionAnchor​(int i)

Returns an object that represents the link anchor, as appropriate for
that link. E.g. from HTML: <a
href="http://www.sun.com/access">Accessibility</a> this method
would return a

String

containing the text: "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

**Parameters:**
- i

- zero-based index of the actions

**Returns:**
- an object representing the hypertext anchor

**See Also:**
- getAccessibleActionCount()

---

#### public abstract int getStartIndex()

Gets the index with the hypertext document at which this link begins.

**Returns:**
- index of start of link

---

#### public abstract int getEndIndex()

Gets the index with the hypertext document at which this link ends.

**Returns:**
- index of end of link

---

### Additional Sections

#### Class AccessibleHyperlink

java.lang.Object

- javax.accessibility.AccessibleHyperlink

javax.accessibility.AccessibleHyperlink

**All Implemented Interfaces:** AccessibleAction

**Direct Known Subclasses:** JEditorPane.JEditorPaneAccessibleHypertextSupport.HTMLLink

```java
public abstract class
AccessibleHyperlink

extends
Object

implements
AccessibleAction
```

Encapsulation of a link, or set of links (e.g. client side imagemap) in a
Hypertext document

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleText

,

AccessibleContext.getAccessibleText()

public abstract class

AccessibleHyperlink

extends

Object

implements

AccessibleAction

Encapsulation of a link, or set of links (e.g. client side imagemap) in a
Hypertext document

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.accessibility.

AccessibleAction

CLICK

,

DECREMENT

,

INCREMENT

,

TOGGLE_EXPAND

,

TOGGLE_POPUP

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleHyperlink

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

doAccessibleAction

​(int i)

Performs the specified action on the object.

abstract

Object

getAccessibleActionAnchor

​(int i)

Returns an object that represents the link anchor, as appropriate for
that link.

abstract int

getAccessibleActionCount

()

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap).

abstract

String

getAccessibleActionDescription

​(int i)

Returns a string description of this particular link action.

abstract

Object

getAccessibleActionObject

​(int i)

Returns an object that represents the link action, as appropriate for
that link.

abstract int

getEndIndex

()

Gets the index with the hypertext document at which this link ends.

abstract int

getStartIndex

()

Gets the index with the hypertext document at which this link begins.

abstract boolean

isValid

()

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

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

- Fields declared in interface javax.accessibility.

AccessibleAction

CLICK

,

DECREMENT

,

INCREMENT

,

TOGGLE_EXPAND

,

TOGGLE_POPUP

---

#### Field Summary

Fields declared in interface javax.accessibility.

AccessibleAction

CLICK

,

DECREMENT

,

INCREMENT

,

TOGGLE_EXPAND

,

TOGGLE_POPUP

---

#### Fields declared in interface javax.accessibility. AccessibleAction

Constructor Summary

Constructors

Constructor

Description

AccessibleHyperlink

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

doAccessibleAction

​(int i)

Performs the specified action on the object.

abstract

Object

getAccessibleActionAnchor

​(int i)

Returns an object that represents the link anchor, as appropriate for
that link.

abstract int

getAccessibleActionCount

()

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap).

abstract

String

getAccessibleActionDescription

​(int i)

Returns a string description of this particular link action.

abstract

Object

getAccessibleActionObject

​(int i)

Returns an object that represents the link action, as appropriate for
that link.

abstract int

getEndIndex

()

Gets the index with the hypertext document at which this link ends.

abstract int

getStartIndex

()

Gets the index with the hypertext document at which this link begins.

abstract boolean

isValid

()

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

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

Performs the specified action on the object.

Returns an object that represents the link anchor, as appropriate for
that link.

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap).

Returns a string description of this particular link action.

Returns an object that represents the link action, as appropriate for
that link.

Gets the index with the hypertext document at which this link ends.

Gets the index with the hypertext document at which this link begins.

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

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

- AccessibleHyperlink

```java
public AccessibleHyperlink()
```

============ METHOD DETAIL ==========

- Method Detail

- isValid

```java
public abstract boolean isValid()
```

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

**Returns:** a flag indicating whether this link is still valid with respect
to the

AccessibleHypertext

it belongs to

- getAccessibleActionCount

```java
public abstract int getAccessibleActionCount()
```

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap). In general, links will
have only one

AccessibleAction

in them.

**Specified by:** getAccessibleActionCount

in interface

AccessibleAction
**Returns:** the zero-based number of actions in this object

- doAccessibleAction

```java
public abstract boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Specified by:** doAccessibleAction

in interface

AccessibleAction
**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

- getAccessibleActionDescription

```java
public abstract
String
getAccessibleActionDescription​(int i)
```

Returns a string description of this particular link action. This should
be a text string associated with anchoring text, this should be the
anchor text. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

**Specified by:** getAccessibleActionDescription

in interface

AccessibleAction
**Parameters:** i

- zero-based index of the actions
**Returns:** a string description of the action
**See Also:** getAccessibleActionCount()

- getAccessibleActionObject

```java
public abstract
Object
getAccessibleActionObject​(int i)
```

Returns an object that represents the link action, as appropriate for
that link. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return a java.net.URL("http://www.sun.com/access.html");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext link itself
**See Also:** getAccessibleActionCount()

- getAccessibleActionAnchor

```java
public abstract
Object
getAccessibleActionAnchor​(int i)
```

Returns an object that represents the link anchor, as appropriate for
that link. E.g. from HTML: <a
href="http://www.sun.com/access">Accessibility</a> this method
would return a

String

containing the text: "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext anchor
**See Also:** getAccessibleActionCount()

- getStartIndex

```java
public abstract int getStartIndex()
```

Gets the index with the hypertext document at which this link begins.

**Returns:** index of start of link

- getEndIndex

```java
public abstract int getEndIndex()
```

Gets the index with the hypertext document at which this link ends.

**Returns:** index of end of link

Constructor Detail

- AccessibleHyperlink

```java
public AccessibleHyperlink()
```

---

#### Constructor Detail

AccessibleHyperlink

```java
public AccessibleHyperlink()
```

---

#### AccessibleHyperlink

public AccessibleHyperlink()

Method Detail

- isValid

```java
public abstract boolean isValid()
```

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

**Returns:** a flag indicating whether this link is still valid with respect
to the

AccessibleHypertext

it belongs to

- getAccessibleActionCount

```java
public abstract int getAccessibleActionCount()
```

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap). In general, links will
have only one

AccessibleAction

in them.

**Specified by:** getAccessibleActionCount

in interface

AccessibleAction
**Returns:** the zero-based number of actions in this object

- doAccessibleAction

```java
public abstract boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Specified by:** doAccessibleAction

in interface

AccessibleAction
**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

- getAccessibleActionDescription

```java
public abstract
String
getAccessibleActionDescription​(int i)
```

Returns a string description of this particular link action. This should
be a text string associated with anchoring text, this should be the
anchor text. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

**Specified by:** getAccessibleActionDescription

in interface

AccessibleAction
**Parameters:** i

- zero-based index of the actions
**Returns:** a string description of the action
**See Also:** getAccessibleActionCount()

- getAccessibleActionObject

```java
public abstract
Object
getAccessibleActionObject​(int i)
```

Returns an object that represents the link action, as appropriate for
that link. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return a java.net.URL("http://www.sun.com/access.html");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext link itself
**See Also:** getAccessibleActionCount()

- getAccessibleActionAnchor

```java
public abstract
Object
getAccessibleActionAnchor​(int i)
```

Returns an object that represents the link anchor, as appropriate for
that link. E.g. from HTML: <a
href="http://www.sun.com/access">Accessibility</a> this method
would return a

String

containing the text: "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext anchor
**See Also:** getAccessibleActionCount()

- getStartIndex

```java
public abstract int getStartIndex()
```

Gets the index with the hypertext document at which this link begins.

**Returns:** index of start of link

- getEndIndex

```java
public abstract int getEndIndex()
```

Gets the index with the hypertext document at which this link ends.

**Returns:** index of end of link

---

#### Method Detail

isValid

```java
public abstract boolean isValid()
```

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

**Returns:** a flag indicating whether this link is still valid with respect
to the

AccessibleHypertext

it belongs to

---

#### isValid

public abstract boolean isValid()

Since the document a link is associated with may have changed, this
method returns whether or not this Link is still valid (with respect to
the document it references).

getAccessibleActionCount

```java
public abstract int getAccessibleActionCount()
```

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap). In general, links will
have only one

AccessibleAction

in them.

**Specified by:** getAccessibleActionCount

in interface

AccessibleAction
**Returns:** the zero-based number of actions in this object

---

#### getAccessibleActionCount

public abstract int getAccessibleActionCount()

Returns the number of accessible actions available in this Link If there
are more than one, the first one is NOT considered the "default" action
of this LINK object (e.g. in an HTML imagemap). In general, links will
have only one

AccessibleAction

in them.

doAccessibleAction

```java
public abstract boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Specified by:** doAccessibleAction

in interface

AccessibleAction
**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

---

#### doAccessibleAction

public abstract boolean doAccessibleAction​(int i)

Performs the specified action on the object.

getAccessibleActionDescription

```java
public abstract
String
getAccessibleActionDescription​(int i)
```

Returns a string description of this particular link action. This should
be a text string associated with anchoring text, this should be the
anchor text. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

**Specified by:** getAccessibleActionDescription

in interface

AccessibleAction
**Parameters:** i

- zero-based index of the actions
**Returns:** a string description of the action
**See Also:** getAccessibleActionCount()

---

#### getAccessibleActionDescription

public abstract

String

getAccessibleActionDescription​(int i)

Returns a string description of this particular link action. This should
be a text string associated with anchoring text, this should be the
anchor text. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this method would return "top hat"

getAccessibleActionObject

```java
public abstract
Object
getAccessibleActionObject​(int i)
```

Returns an object that represents the link action, as appropriate for
that link. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return a java.net.URL("http://www.sun.com/access.html");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext link itself
**See Also:** getAccessibleActionCount()

---

#### getAccessibleActionObject

public abstract

Object

getAccessibleActionObject​(int i)

Returns an object that represents the link action, as appropriate for
that link. E.g. from HTML: <a
HREF="http://www.sun.com/access">Accessibility</a> this method
would return a java.net.URL("http://www.sun.com/access.html");

getAccessibleActionAnchor

```java
public abstract
Object
getAccessibleActionAnchor​(int i)
```

Returns an object that represents the link anchor, as appropriate for
that link. E.g. from HTML: <a
href="http://www.sun.com/access">Accessibility</a> this method
would return a

String

containing the text: "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

**Parameters:** i

- zero-based index of the actions
**Returns:** an object representing the hypertext anchor
**See Also:** getAccessibleActionCount()

---

#### getAccessibleActionAnchor

public abstract

Object

getAccessibleActionAnchor​(int i)

Returns an object that represents the link anchor, as appropriate for
that link. E.g. from HTML: <a
href="http://www.sun.com/access">Accessibility</a> this method
would return a

String

containing the text: "Accessibility".

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

Similarly, from this HTML: <a HREF="#top"><img src="top-hat.gif"
alt="top hat"></a> this might return the object
ImageIcon("top-hat.gif", "top hat");

getStartIndex

```java
public abstract int getStartIndex()
```

Gets the index with the hypertext document at which this link begins.

**Returns:** index of start of link

---

#### getStartIndex

public abstract int getStartIndex()

Gets the index with the hypertext document at which this link begins.

getEndIndex

```java
public abstract int getEndIndex()
```

Gets the index with the hypertext document at which this link ends.

**Returns:** index of end of link

---

#### getEndIndex

public abstract int getEndIndex()

Gets the index with the hypertext document at which this link ends.

---

