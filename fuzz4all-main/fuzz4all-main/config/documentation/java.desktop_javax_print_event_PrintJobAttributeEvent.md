# Class PrintJobAttributeEvent

**Source:** `java.desktop\javax\print\event\PrintJobAttributeEvent.html`

### Class Description

```java
public class
PrintJobAttributeEvent

extends
PrintEvent
```

Class

PrintJobAttributeEvent

encapsulates an event a

PrintService

reports to let the client know that one or more printing
attributes for a

PrintJob

have changed.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintJobAttributeEvent​(
DocPrintJob
source,

PrintJobAttributeSet
attributes)

Constructs a

PrintJobAttributeEvent

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
DocPrintJob
getPrintJob()

Determine the

PrintJob

to which this print job event pertains.

**Returns:**
- PrintJob

object

---

#### public
PrintJobAttributeSet
getAttributes()

Determine the printing attributes that changed and their new values.

**Returns:**
- attributes containing the new values for the print job attributes
that changed. The returned set may not be modifiable.

---

### Additional Sections

#### Class PrintJobAttributeEvent

java.lang.Object

- java.util.EventObject
- - javax.print.event.PrintEvent
- - javax.print.event.PrintJobAttributeEvent

java.util.EventObject

- javax.print.event.PrintEvent
- - javax.print.event.PrintJobAttributeEvent

javax.print.event.PrintEvent

- javax.print.event.PrintJobAttributeEvent

javax.print.event.PrintJobAttributeEvent

**All Implemented Interfaces:** Serializable

```java
public class
PrintJobAttributeEvent

extends
PrintEvent
```

Class

PrintJobAttributeEvent

encapsulates an event a

PrintService

reports to let the client know that one or more printing
attributes for a

PrintJob

have changed.

**See Also:** Serialized Form

public class

PrintJobAttributeEvent

extends

PrintEvent

Class

PrintJobAttributeEvent

encapsulates an event a

PrintService

reports to let the client know that one or more printing
attributes for a

PrintJob

have changed.

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

PrintJobAttributeEvent

​(

DocPrintJob

source,

PrintJobAttributeSet

attributes)

Constructs a

PrintJobAttributeEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrintJobAttributeSet

getAttributes

()

Determine the printing attributes that changed and their new values.

DocPrintJob

getPrintJob

()

Determine the

PrintJob

to which this print job event pertains.

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

PrintJobAttributeEvent

​(

DocPrintJob

source,

PrintJobAttributeSet

attributes)

Constructs a

PrintJobAttributeEvent

object.

---

#### Constructor Summary

Constructs a

PrintJobAttributeEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PrintJobAttributeSet

getAttributes

()

Determine the printing attributes that changed and their new values.

DocPrintJob

getPrintJob

()

Determine the

PrintJob

to which this print job event pertains.

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

Determine the printing attributes that changed and their new values.

Determine the

PrintJob

to which this print job event pertains.

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

- PrintJobAttributeEvent

```java
public PrintJobAttributeEvent​(
DocPrintJob
source,

PrintJobAttributeSet
attributes)
```

Constructs a

PrintJobAttributeEvent

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

- getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determine the

PrintJob

to which this print job event pertains.

**Returns:** PrintJob

object

- getAttributes

```java
public
PrintJobAttributeSet
getAttributes()
```

Determine the printing attributes that changed and their new values.

**Returns:** attributes containing the new values for the print job attributes
that changed. The returned set may not be modifiable.

Constructor Detail

- PrintJobAttributeEvent

```java
public PrintJobAttributeEvent​(
DocPrintJob
source,

PrintJobAttributeSet
attributes)
```

Constructs a

PrintJobAttributeEvent

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

PrintJobAttributeEvent

```java
public PrintJobAttributeEvent​(
DocPrintJob
source,

PrintJobAttributeSet
attributes)
```

Constructs a

PrintJobAttributeEvent

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

#### PrintJobAttributeEvent

public PrintJobAttributeEvent​(

DocPrintJob

source,

PrintJobAttributeSet

attributes)

Constructs a

PrintJobAttributeEvent

object.

Method Detail

- getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determine the

PrintJob

to which this print job event pertains.

**Returns:** PrintJob

object

- getAttributes

```java
public
PrintJobAttributeSet
getAttributes()
```

Determine the printing attributes that changed and their new values.

**Returns:** attributes containing the new values for the print job attributes
that changed. The returned set may not be modifiable.

---

#### Method Detail

getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determine the

PrintJob

to which this print job event pertains.

**Returns:** PrintJob

object

---

#### getPrintJob

public

DocPrintJob

getPrintJob()

Determine the

PrintJob

to which this print job event pertains.

getAttributes

```java
public
PrintJobAttributeSet
getAttributes()
```

Determine the printing attributes that changed and their new values.

**Returns:** attributes containing the new values for the print job attributes
that changed. The returned set may not be modifiable.

---

#### getAttributes

public

PrintJobAttributeSet

getAttributes()

Determine the printing attributes that changed and their new values.

---

