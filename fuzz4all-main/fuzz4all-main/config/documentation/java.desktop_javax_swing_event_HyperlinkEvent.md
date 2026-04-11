# Class HyperlinkEvent

**Source:** `java.desktop\javax\swing\event\HyperlinkEvent.html`

### Class Description

```java
public class
HyperlinkEvent

extends
EventObject
```

HyperlinkEvent is used to notify interested parties that
something has happened with respect to a hypertext link.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u)

Creates a new object representing a hypertext link event.
The other constructor is preferred, as it provides more
information if a URL could not be formed. This constructor
is primarily for backward compatibility.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- u

- the affected URL

---

#### public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- u

- the affected URL. This may be null if a valid URL
could not be created.
- desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.

---

#### public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- u

- the affected URL. This may be null if a valid URL
could not be created.
- desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
- sourceElement

- Element in the Document representing the
anchor

**Since:**
- 1.4

---

#### public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement,

InputEvent
inputEvent)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- u

- the affected URL. This may be null if a valid URL
could not be created.
- desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
- sourceElement

- Element in the Document representing the
anchor
- inputEvent

- InputEvent that triggered the hyperlink event

**Since:**
- 1.7

---

### Method Details

#### public
HyperlinkEvent.EventType
getEventType()

Gets the type of event.

**Returns:**
- the type

---

#### public
String
getDescription()

Get the description of the link as a string.
This may be useful if a URL can't be formed
from the description, in which case the associated
URL would be null.

**Returns:**
- the description of this link as a

String

---

#### public
URL
getURL()

Gets the URL that the link refers to.

**Returns:**
- the URL

---

#### public
Element
getSourceElement()

Returns the

Element

that corresponds to the source of the
event. This will typically be an

Element

representing
an anchor. If a constructor that is used that does not specify a source

Element

, or null was specified as the source

Element

, this will return null.

**Returns:**
- Element indicating source of event, or null

**Since:**
- 1.4

---

#### public
InputEvent
getInputEvent()

Returns the

InputEvent

that triggered the hyperlink event.
This will typically be a

MouseEvent

. If a constructor is used
that does not specify an

InputEvent

, or @{code null}
was specified as the

InputEvent

, this returns

null

.

**Returns:**
- InputEvent that triggered the hyperlink event, or null

**Since:**
- 1.7

---

### Additional Sections

#### Class HyperlinkEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.HyperlinkEvent

java.util.EventObject

- javax.swing.event.HyperlinkEvent

javax.swing.event.HyperlinkEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** HTMLFrameHyperlinkEvent

```java
public class
HyperlinkEvent

extends
EventObject
```

HyperlinkEvent is used to notify interested parties that
something has happened with respect to a hypertext link.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

HyperlinkEvent

extends

EventObject

HyperlinkEvent is used to notify interested parties that
something has happened with respect to a hypertext link.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

HyperlinkEvent.EventType

Defines the ENTERED, EXITED, and ACTIVATED event types, along
with their string representations, returned by toString().

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement,

InputEvent

inputEvent)

Creates a new object representing a hypertext link event.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

()

Get the description of the link as a string.

HyperlinkEvent.EventType

getEventType

()

Gets the type of event.

InputEvent

getInputEvent

()

Returns the

InputEvent

that triggered the hyperlink event.

Element

getSourceElement

()

Returns the

Element

that corresponds to the source of the
event.

URL

getURL

()

Gets the URL that the link refers to.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

static class

HyperlinkEvent.EventType

Defines the ENTERED, EXITED, and ACTIVATED event types, along
with their string representations, returned by toString().

---

#### Nested Class Summary

Defines the ENTERED, EXITED, and ACTIVATED event types, along
with their string representations, returned by toString().

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement)

Creates a new object representing a hypertext link event.

HyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement,

InputEvent

inputEvent)

Creates a new object representing a hypertext link event.

---

#### Constructor Summary

Creates a new object representing a hypertext link event.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

()

Get the description of the link as a string.

HyperlinkEvent.EventType

getEventType

()

Gets the type of event.

InputEvent

getInputEvent

()

Returns the

InputEvent

that triggered the hyperlink event.

Element

getSourceElement

()

Returns the

Element

that corresponds to the source of the
event.

URL

getURL

()

Gets the URL that the link refers to.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Get the description of the link as a string.

Gets the type of event.

Returns the

InputEvent

that triggered the hyperlink event.

Returns the

Element

that corresponds to the source of the
event.

Gets the URL that the link refers to.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u)
```

Creates a new object representing a hypertext link event.
The other constructor is preferred, as it provides more
information if a URL could not be formed. This constructor
is primarily for backward compatibility.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Since:** 1.4

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement,

InputEvent
inputEvent)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- getEventType

```java
public
HyperlinkEvent.EventType
getEventType()
```

Gets the type of event.

**Returns:** the type

- getDescription

```java
public
String
getDescription()
```

Get the description of the link as a string.
This may be useful if a URL can't be formed
from the description, in which case the associated
URL would be null.

**Returns:** the description of this link as a

String

- getURL

```java
public
URL
getURL()
```

Gets the URL that the link refers to.

**Returns:** the URL

- getSourceElement

```java
public
Element
getSourceElement()
```

Returns the

Element

that corresponds to the source of the
event. This will typically be an

Element

representing
an anchor. If a constructor that is used that does not specify a source

Element

, or null was specified as the source

Element

, this will return null.

**Returns:** Element indicating source of event, or null
**Since:** 1.4

- getInputEvent

```java
public
InputEvent
getInputEvent()
```

Returns the

InputEvent

that triggered the hyperlink event.
This will typically be a

MouseEvent

. If a constructor is used
that does not specify an

InputEvent

, or @{code null}
was specified as the

InputEvent

, this returns

null

.

**Returns:** InputEvent that triggered the hyperlink event, or null
**Since:** 1.7

Constructor Detail

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u)
```

Creates a new object representing a hypertext link event.
The other constructor is preferred, as it provides more
information if a URL could not be formed. This constructor
is primarily for backward compatibility.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Since:** 1.4

- HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement,

InputEvent
inputEvent)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Since:** 1.7

---

#### Constructor Detail

HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u)
```

Creates a new object representing a hypertext link event.
The other constructor is preferred, as it provides more
information if a URL could not be formed. This constructor
is primarily for backward compatibility.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL

---

#### HyperlinkEvent

public HyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u)

Creates a new object representing a hypertext link event.
The other constructor is preferred, as it provides more
information if a URL could not be formed. This constructor
is primarily for backward compatibility.

HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.

---

#### HyperlinkEvent

public HyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc)

Creates a new object representing a hypertext link event.

HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Since:** 1.4

---

#### HyperlinkEvent

public HyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement)

Creates a new object representing a hypertext link event.

HyperlinkEvent

```java
public HyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
u,

String
desc,

Element
sourceElement,

InputEvent
inputEvent)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** u

- the affected URL. This may be null if a valid URL
could not be created.
**Parameters:** desc

- the description of the link. This may be useful
when attempting to form a URL resulted in a MalformedURLException.
The description provides the text used when attempting to form the
URL.
**Parameters:** sourceElement

- Element in the Document representing the
anchor
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Since:** 1.7

---

#### HyperlinkEvent

public HyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

u,

String

desc,

Element

sourceElement,

InputEvent

inputEvent)

Creates a new object representing a hypertext link event.

Method Detail

- getEventType

```java
public
HyperlinkEvent.EventType
getEventType()
```

Gets the type of event.

**Returns:** the type

- getDescription

```java
public
String
getDescription()
```

Get the description of the link as a string.
This may be useful if a URL can't be formed
from the description, in which case the associated
URL would be null.

**Returns:** the description of this link as a

String

- getURL

```java
public
URL
getURL()
```

Gets the URL that the link refers to.

**Returns:** the URL

- getSourceElement

```java
public
Element
getSourceElement()
```

Returns the

Element

that corresponds to the source of the
event. This will typically be an

Element

representing
an anchor. If a constructor that is used that does not specify a source

Element

, or null was specified as the source

Element

, this will return null.

**Returns:** Element indicating source of event, or null
**Since:** 1.4

- getInputEvent

```java
public
InputEvent
getInputEvent()
```

Returns the

InputEvent

that triggered the hyperlink event.
This will typically be a

MouseEvent

. If a constructor is used
that does not specify an

InputEvent

, or @{code null}
was specified as the

InputEvent

, this returns

null

.

**Returns:** InputEvent that triggered the hyperlink event, or null
**Since:** 1.7

---

#### Method Detail

getEventType

```java
public
HyperlinkEvent.EventType
getEventType()
```

Gets the type of event.

**Returns:** the type

---

#### getEventType

public

HyperlinkEvent.EventType

getEventType()

Gets the type of event.

getDescription

```java
public
String
getDescription()
```

Get the description of the link as a string.
This may be useful if a URL can't be formed
from the description, in which case the associated
URL would be null.

**Returns:** the description of this link as a

String

---

#### getDescription

public

String

getDescription()

Get the description of the link as a string.
This may be useful if a URL can't be formed
from the description, in which case the associated
URL would be null.

getURL

```java
public
URL
getURL()
```

Gets the URL that the link refers to.

**Returns:** the URL

---

#### getURL

public

URL

getURL()

Gets the URL that the link refers to.

getSourceElement

```java
public
Element
getSourceElement()
```

Returns the

Element

that corresponds to the source of the
event. This will typically be an

Element

representing
an anchor. If a constructor that is used that does not specify a source

Element

, or null was specified as the source

Element

, this will return null.

**Returns:** Element indicating source of event, or null
**Since:** 1.4

---

#### getSourceElement

public

Element

getSourceElement()

Returns the

Element

that corresponds to the source of the
event. This will typically be an

Element

representing
an anchor. If a constructor that is used that does not specify a source

Element

, or null was specified as the source

Element

, this will return null.

getInputEvent

```java
public
InputEvent
getInputEvent()
```

Returns the

InputEvent

that triggered the hyperlink event.
This will typically be a

MouseEvent

. If a constructor is used
that does not specify an

InputEvent

, or @{code null}
was specified as the

InputEvent

, this returns

null

.

**Returns:** InputEvent that triggered the hyperlink event, or null
**Since:** 1.7

---

#### getInputEvent

public

InputEvent

getInputEvent()

Returns the

InputEvent

that triggered the hyperlink event.
This will typically be a

MouseEvent

. If a constructor is used
that does not specify an

InputEvent

, or @{code null}
was specified as the

InputEvent

, this returns

null

.

---

