# Class HTMLFrameHyperlinkEvent

**Source:** `java.desktop\javax\swing\text\html\HTMLFrameHyperlinkEvent.html`

### Class Description

```java
public class
HTMLFrameHyperlinkEvent

extends
HyperlinkEvent
```

HTMLFrameHyperlinkEvent is used to notify interested
parties that link was activated in a frame.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
targetFrame)

Creates a new object representing a html frame
hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- targetURL

- the affected URL
- targetFrame

- the Frame to display the document in

---

#### public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

String
targetFrame)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- targetURL

- the affected URL
- desc

- a description
- targetFrame

- the Frame to display the document in

---

#### public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

Element
sourceElement,

String
targetFrame)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- targetURL

- the affected URL
- sourceElement

- the element that corresponds to the source
of the event
- targetFrame

- the Frame to display the document in

---

#### public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

String
targetFrame)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- targetURL

- the affected URL
- desc

- a description
- sourceElement

- the element that corresponds to the source
of the event
- targetFrame

- the Frame to display the document in

---

#### public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

InputEvent
inputEvent,

String
targetFrame)

Creates a new object representing a hypertext link event.

**Parameters:**
- source

- the object responsible for the event
- type

- the event type
- targetURL

- the affected URL
- desc

- a description
- sourceElement

- the element that corresponds to the source
of the event
- inputEvent

- InputEvent that triggered the hyperlink event
- targetFrame

- the Frame to display the document in

**Since:**
- 1.7

---

### Method Details

#### public
String
getTarget()

returns the target for the link.

**Returns:**
- the target for the link

---

### Additional Sections

#### Class HTMLFrameHyperlinkEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.HyperlinkEvent
- - javax.swing.text.html.HTMLFrameHyperlinkEvent

java.util.EventObject

- javax.swing.event.HyperlinkEvent
- - javax.swing.text.html.HTMLFrameHyperlinkEvent

javax.swing.event.HyperlinkEvent

- javax.swing.text.html.HTMLFrameHyperlinkEvent

javax.swing.text.html.HTMLFrameHyperlinkEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** FormSubmitEvent

```java
public class
HTMLFrameHyperlinkEvent

extends
HyperlinkEvent
```

HTMLFrameHyperlinkEvent is used to notify interested
parties that link was activated in a frame.

**See Also:** Serialized Form

public class

HTMLFrameHyperlinkEvent

extends

HyperlinkEvent

HTMLFrameHyperlinkEvent is used to notify interested
parties that link was activated in a frame.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.event.

HyperlinkEvent

HyperlinkEvent.EventType

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

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

targetFrame)

Creates a new object representing a html frame
hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

InputEvent

inputEvent,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

Element

sourceElement,

String

targetFrame)

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

getTarget

()

returns the target for the link.

- Methods declared in class javax.swing.event.

HyperlinkEvent

getDescription

,

getEventType

,

getInputEvent

,

getSourceElement

,

getURL

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

- Nested classes/interfaces declared in class javax.swing.event.

HyperlinkEvent

HyperlinkEvent.EventType

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.event.

HyperlinkEvent

HyperlinkEvent.EventType

---

#### Nested classes/interfaces declared in class javax.swing.event. HyperlinkEvent

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

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

targetFrame)

Creates a new object representing a html frame
hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

InputEvent

inputEvent,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

Element

sourceElement,

String

targetFrame)

Creates a new object representing a hypertext link event.

---

#### Constructor Summary

Creates a new object representing a html frame
hypertext link event.

Creates a new object representing a hypertext link event.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getTarget

()

returns the target for the link.

- Methods declared in class javax.swing.event.

HyperlinkEvent

getDescription

,

getEventType

,

getInputEvent

,

getSourceElement

,

getURL

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

returns the target for the link.

Methods declared in class javax.swing.event.

HyperlinkEvent

getDescription

,

getEventType

,

getInputEvent

,

getSourceElement

,

getURL

---

#### Methods declared in class javax.swing.event. HyperlinkEvent

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

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
targetFrame)
```

Creates a new object representing a html frame
hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

InputEvent
inputEvent,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Parameters:** targetFrame

- the Frame to display the document in
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
public
String
getTarget()
```

returns the target for the link.

**Returns:** the target for the link

Constructor Detail

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
targetFrame)
```

Creates a new object representing a html frame
hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

- HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

InputEvent
inputEvent,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Parameters:** targetFrame

- the Frame to display the document in
**Since:** 1.7

---

#### Constructor Detail

HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
targetFrame)
```

Creates a new object representing a html frame
hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** targetFrame

- the Frame to display the document in

---

#### HTMLFrameHyperlinkEvent

public HTMLFrameHyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

targetFrame)

Creates a new object representing a html frame
hypertext link event.

HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** targetFrame

- the Frame to display the document in

---

#### HTMLFrameHyperlinkEvent

public HTMLFrameHyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

---

#### HTMLFrameHyperlinkEvent

public HTMLFrameHyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

Element

sourceElement,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** targetFrame

- the Frame to display the document in

---

#### HTMLFrameHyperlinkEvent

public HTMLFrameHyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

String

targetFrame)

Creates a new object representing a hypertext link event.

HTMLFrameHyperlinkEvent

```java
public HTMLFrameHyperlinkEvent​(
Object
source,

HyperlinkEvent.EventType
type,

URL
targetURL,

String
desc,

Element
sourceElement,

InputEvent
inputEvent,

String
targetFrame)
```

Creates a new object representing a hypertext link event.

**Parameters:** source

- the object responsible for the event
**Parameters:** type

- the event type
**Parameters:** targetURL

- the affected URL
**Parameters:** desc

- a description
**Parameters:** sourceElement

- the element that corresponds to the source
of the event
**Parameters:** inputEvent

- InputEvent that triggered the hyperlink event
**Parameters:** targetFrame

- the Frame to display the document in
**Since:** 1.7

---

#### HTMLFrameHyperlinkEvent

public HTMLFrameHyperlinkEvent​(

Object

source,

HyperlinkEvent.EventType

type,

URL

targetURL,

String

desc,

Element

sourceElement,

InputEvent

inputEvent,

String

targetFrame)

Creates a new object representing a hypertext link event.

Method Detail

- getTarget

```java
public
String
getTarget()
```

returns the target for the link.

**Returns:** the target for the link

---

#### Method Detail

getTarget

```java
public
String
getTarget()
```

returns the target for the link.

**Returns:** the target for the link

---

#### getTarget

public

String

getTarget()

returns the target for the link.

---

