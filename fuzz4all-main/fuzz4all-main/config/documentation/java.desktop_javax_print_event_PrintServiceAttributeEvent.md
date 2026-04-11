# Class PrintServiceAttributeEvent

**Source:** `java.desktop\javax\print\event\PrintServiceAttributeEvent.html`

### Class Description

```java
public class
PrintServiceAttributeEvent

extends
PrintEvent
```

Class

PrintServiceAttributeEvent

encapsulates an event a Print
Service instance reports to let the client know of changes in the print
service state.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintServiceAttributeEvent​(
PrintService
source,

PrintServiceAttributeSet
attributes)

Constructs a

PrintServiceAttributeEvent

object.

**Parameters:**
- source

- the print job generating this event
- attributes

- the attribute changes being reported

**Throws:**
- IllegalArgumentException

- if

source

is

null

---

### Method Details

#### public
PrintService
getPrintService()

Returns the print service.

**Returns:**
- PrintService

object

---

#### public
PrintServiceAttributeSet
getAttributes()

Determine the printing service attributes that changed and their new
values.

**Returns:**
- attributes containing the new values for the service attributes
that changed. The returned set may be unmodifiable.

---

### Additional Sections

#### Class PrintServiceAttributeEvent

java.lang.Object

- java.util.EventObject
- - javax.print.event.PrintEvent
- - javax.print.event.PrintServiceAttributeEvent

java.util.EventObject

- javax.print.event.PrintEvent
- - javax.print.event.PrintServiceAttributeEvent

javax.print.event.PrintEvent

- javax.print.event.PrintServiceAttributeEvent

javax.print.event.PrintServiceAttributeEvent

**All Implemented Interfaces:** Serializable

```java
public class
PrintServiceAttributeEvent

extends
PrintEvent
```

Class

PrintServiceAttributeEvent

encapsulates an event a Print
Service instance reports to let the client know of changes in the print
service state.

**See Also:** Serialized Form

public class

PrintServiceAttributeEvent

extends

PrintEvent

Class

PrintServiceAttributeEvent

encapsulates an event a Print
Service instance reports to let the client know of changes in the print
service state.

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

PrintServiceAttributeEvent

​(

PrintService

source,

PrintServiceAttributeSet

attributes)

Constructs a

PrintServiceAttributeEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrintServiceAttributeSet

getAttributes

()

Determine the printing service attributes that changed and their new
values.

PrintService

getPrintService

()

Returns the print service.

- Methods declared in class javax.print.event.

PrintEvent

toString

- Methods declared in class java.util.

EventObject

getSource

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

PrintServiceAttributeEvent

​(

PrintService

source,

PrintServiceAttributeSet

attributes)

Constructs a

PrintServiceAttributeEvent

object.

---

#### Constructor Summary

Constructs a

PrintServiceAttributeEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrintServiceAttributeSet

getAttributes

()

Determine the printing service attributes that changed and their new
values.

PrintService

getPrintService

()

Returns the print service.

- Methods declared in class javax.print.event.

PrintEvent

toString

- Methods declared in class java.util.

EventObject

getSource

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

Determine the printing service attributes that changed and their new
values.

Returns the print service.

Methods declared in class javax.print.event.

PrintEvent

toString

---

#### Methods declared in class javax.print.event. PrintEvent

Methods declared in class java.util.

EventObject

getSource

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

- PrintServiceAttributeEvent

```java
public PrintServiceAttributeEvent​(
PrintService
source,

PrintServiceAttributeSet
attributes)
```

Constructs a

PrintServiceAttributeEvent

object.

**Parameters:** source

- the print job generating this event
**Parameters:** attributes

- the attribute changes being reported
**Throws:** IllegalArgumentException

- if

source

is

null

============ METHOD DETAIL ==========

- Method Detail

- getPrintService

```java
public
PrintService
getPrintService()
```

Returns the print service.

**Returns:** PrintService

object

- getAttributes

```java
public
PrintServiceAttributeSet
getAttributes()
```

Determine the printing service attributes that changed and their new
values.

**Returns:** attributes containing the new values for the service attributes
that changed. The returned set may be unmodifiable.

Constructor Detail

- PrintServiceAttributeEvent

```java
public PrintServiceAttributeEvent​(
PrintService
source,

PrintServiceAttributeSet
attributes)
```

Constructs a

PrintServiceAttributeEvent

object.

**Parameters:** source

- the print job generating this event
**Parameters:** attributes

- the attribute changes being reported
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### Constructor Detail

PrintServiceAttributeEvent

```java
public PrintServiceAttributeEvent​(
PrintService
source,

PrintServiceAttributeSet
attributes)
```

Constructs a

PrintServiceAttributeEvent

object.

**Parameters:** source

- the print job generating this event
**Parameters:** attributes

- the attribute changes being reported
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### PrintServiceAttributeEvent

public PrintServiceAttributeEvent​(

PrintService

source,

PrintServiceAttributeSet

attributes)

Constructs a

PrintServiceAttributeEvent

object.

Method Detail

- getPrintService

```java
public
PrintService
getPrintService()
```

Returns the print service.

**Returns:** PrintService

object

- getAttributes

```java
public
PrintServiceAttributeSet
getAttributes()
```

Determine the printing service attributes that changed and their new
values.

**Returns:** attributes containing the new values for the service attributes
that changed. The returned set may be unmodifiable.

---

#### Method Detail

getPrintService

```java
public
PrintService
getPrintService()
```

Returns the print service.

**Returns:** PrintService

object

---

#### getPrintService

public

PrintService

getPrintService()

Returns the print service.

getAttributes

```java
public
PrintServiceAttributeSet
getAttributes()
```

Determine the printing service attributes that changed and their new
values.

**Returns:** attributes containing the new values for the service attributes
that changed. The returned set may be unmodifiable.

---

#### getAttributes

public

PrintServiceAttributeSet

getAttributes()

Determine the printing service attributes that changed and their new
values.

---

