# Class FormSubmitEvent

**Source:** `java.desktop\javax\swing\text\html\FormSubmitEvent.html`

### Class Description

```java
public class
FormSubmitEvent

extends
HTMLFrameHyperlinkEvent
```

FormSubmitEvent is used to notify interested
parties that a form was submitted.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
FormSubmitEvent.MethodType
getMethod()

Gets the form method type.

**Returns:**
- the form method type, either

Method.GET

or

Method.POST

.

---

#### public
String
getData()

Gets the form submission data.

**Returns:**
- the string representing the form submission data.

---

### Additional Sections

#### Class FormSubmitEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.HyperlinkEvent
- - javax.swing.text.html.HTMLFrameHyperlinkEvent
- - javax.swing.text.html.FormSubmitEvent

java.util.EventObject

- javax.swing.event.HyperlinkEvent
- - javax.swing.text.html.HTMLFrameHyperlinkEvent
- - javax.swing.text.html.FormSubmitEvent

javax.swing.event.HyperlinkEvent

- javax.swing.text.html.HTMLFrameHyperlinkEvent
- - javax.swing.text.html.FormSubmitEvent

javax.swing.text.html.HTMLFrameHyperlinkEvent

- javax.swing.text.html.FormSubmitEvent

javax.swing.text.html.FormSubmitEvent

**All Implemented Interfaces:** Serializable

```java
public class
FormSubmitEvent

extends
HTMLFrameHyperlinkEvent
```

FormSubmitEvent is used to notify interested
parties that a form was submitted.

**Since:** 1.5
**See Also:** Serialized Form

public class

FormSubmitEvent

extends

HTMLFrameHyperlinkEvent

FormSubmitEvent is used to notify interested
parties that a form was submitted.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

FormSubmitEvent.MethodType

Represents an HTML form method type.

- Nested classes/interfaces declared in class javax.swing.event.

HyperlinkEvent

HyperlinkEvent.EventType

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getData

()

Gets the form submission data.

FormSubmitEvent.MethodType

getMethod

()

Gets the form method type.

- Methods declared in class javax.swing.text.html.

HTMLFrameHyperlinkEvent

getTarget

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

Nested Classes

Modifier and Type

Class

Description

static class

FormSubmitEvent.MethodType

Represents an HTML form method type.

- Nested classes/interfaces declared in class javax.swing.event.

HyperlinkEvent

HyperlinkEvent.EventType

---

#### Nested Class Summary

Represents an HTML form method type.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getData

()

Gets the form submission data.

FormSubmitEvent.MethodType

getMethod

()

Gets the form method type.

- Methods declared in class javax.swing.text.html.

HTMLFrameHyperlinkEvent

getTarget

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

Gets the form submission data.

Gets the form method type.

Methods declared in class javax.swing.text.html.

HTMLFrameHyperlinkEvent

getTarget

---

#### Methods declared in class javax.swing.text.html. HTMLFrameHyperlinkEvent

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

============ METHOD DETAIL ==========

- Method Detail

- getMethod

```java
public
FormSubmitEvent.MethodType
getMethod()
```

Gets the form method type.

**Returns:** the form method type, either

Method.GET

or

Method.POST

.

- getData

```java
public
String
getData()
```

Gets the form submission data.

**Returns:** the string representing the form submission data.

Method Detail

- getMethod

```java
public
FormSubmitEvent.MethodType
getMethod()
```

Gets the form method type.

**Returns:** the form method type, either

Method.GET

or

Method.POST

.

- getData

```java
public
String
getData()
```

Gets the form submission data.

**Returns:** the string representing the form submission data.

---

#### Method Detail

getMethod

```java
public
FormSubmitEvent.MethodType
getMethod()
```

Gets the form method type.

**Returns:** the form method type, either

Method.GET

or

Method.POST

.

---

#### getMethod

public

FormSubmitEvent.MethodType

getMethod()

Gets the form method type.

getData

```java
public
String
getData()
```

Gets the form submission data.

**Returns:** the string representing the form submission data.

---

#### getData

public

String

getData()

Gets the form submission data.

---

