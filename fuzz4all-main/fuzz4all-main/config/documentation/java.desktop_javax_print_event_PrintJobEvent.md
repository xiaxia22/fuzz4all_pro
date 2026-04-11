# Class PrintJobEvent

**Source:** `java.desktop\javax\print\event\PrintJobEvent.html`

### Class Description

```java
public class
PrintJobEvent

extends
PrintEvent
```

Class

PrintJobEvent

encapsulates common events a print job reports to
let a listener know of progress in the processing of the

DocPrintJob

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int JOB_CANCELED

The job was canceled by the

PrintService

.

**See Also:**
- Constant Field Values

---

#### public static final int JOB_COMPLETE

The document is completely printed.

**See Also:**
- Constant Field Values

---

#### public static final int JOB_FAILED

The print service reports that the job cannot be completed. The
application must resubmit the job.

**See Also:**
- Constant Field Values

---

#### public static final int REQUIRES_ATTENTION

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue. One
example of an event that can generate this message is when the printer
runs out of paper.

**See Also:**
- Constant Field Values

---

#### public static final int NO_MORE_EVENTS

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete. This message indicates the print
job has no further information or communication with the print service.
This message should always be delivered if a terminal event
(completed/failed/canceled) is not delivered. For example, if messages
such as

JOB_COMPLETE

have NOT been received before receiving this
message, the only inference that should be drawn is that the print
service does not support delivering such an event.

**See Also:**
- Constant Field Values

---

#### public static final int DATA_TRANSFER_COMPLETE

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service. The client may free
data resources.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public PrintJobEvent​(
DocPrintJob
source,
int reason)

Constructs a

PrintJobEvent

object.

**Parameters:**
- source

- a

DocPrintJob

object
- reason

- an int specifying the reason

**Throws:**
- IllegalArgumentException

- if

source

is

null

---

### Method Details

#### public int getPrintEventType()

Gets the reason for this event.

**Returns:**
- reason int

---

#### public
DocPrintJob
getPrintJob()

Determines the

DocPrintJob

to which this print job event
pertains.

**Returns:**
- the

DocPrintJob

object that represents the print job that
reports the events encapsulated by this

PrintJobEvent

---

### Additional Sections

#### Class PrintJobEvent

java.lang.Object

- java.util.EventObject
- - javax.print.event.PrintEvent
- - javax.print.event.PrintJobEvent

java.util.EventObject

- javax.print.event.PrintEvent
- - javax.print.event.PrintJobEvent

javax.print.event.PrintEvent

- javax.print.event.PrintJobEvent

javax.print.event.PrintJobEvent

**All Implemented Interfaces:** Serializable

```java
public class
PrintJobEvent

extends
PrintEvent
```

Class

PrintJobEvent

encapsulates common events a print job reports to
let a listener know of progress in the processing of the

DocPrintJob

.

**See Also:** Serialized Form

public class

PrintJobEvent

extends

PrintEvent

Class

PrintJobEvent

encapsulates common events a print job reports to
let a listener know of progress in the processing of the

DocPrintJob

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DATA_TRANSFER_COMPLETE

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service.

static int

JOB_CANCELED

The job was canceled by the

PrintService

.

static int

JOB_COMPLETE

The document is completely printed.

static int

JOB_FAILED

The print service reports that the job cannot be completed.

static int

NO_MORE_EVENTS

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete.

static int

REQUIRES_ATTENTION

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrintJobEvent

​(

DocPrintJob

source,
int reason)

Constructs a

PrintJobEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getPrintEventType

()

Gets the reason for this event.

DocPrintJob

getPrintJob

()

Determines the

DocPrintJob

to which this print job event
pertains.

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

Fields

Modifier and Type

Field

Description

static int

DATA_TRANSFER_COMPLETE

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service.

static int

JOB_CANCELED

The job was canceled by the

PrintService

.

static int

JOB_COMPLETE

The document is completely printed.

static int

JOB_FAILED

The print service reports that the job cannot be completed.

static int

NO_MORE_EVENTS

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete.

static int

REQUIRES_ATTENTION

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service.

The job was canceled by the

PrintService

.

The document is completely printed.

The print service reports that the job cannot be completed.

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete.

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

PrintJobEvent

​(

DocPrintJob

source,
int reason)

Constructs a

PrintJobEvent

object.

---

#### Constructor Summary

Constructs a

PrintJobEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getPrintEventType

()

Gets the reason for this event.

DocPrintJob

getPrintJob

()

Determines the

DocPrintJob

to which this print job event
pertains.

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

Gets the reason for this event.

Determines the

DocPrintJob

to which this print job event
pertains.

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

============ FIELD DETAIL ===========

- Field Detail

- JOB_CANCELED

```java
public static final int JOB_CANCELED
```

The job was canceled by the

PrintService

.

**See Also:** Constant Field Values

- JOB_COMPLETE

```java
public static final int JOB_COMPLETE
```

The document is completely printed.

**See Also:** Constant Field Values

- JOB_FAILED

```java
public static final int JOB_FAILED
```

The print service reports that the job cannot be completed. The
application must resubmit the job.

**See Also:** Constant Field Values

- REQUIRES_ATTENTION

```java
public static final int REQUIRES_ATTENTION
```

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue. One
example of an event that can generate this message is when the printer
runs out of paper.

**See Also:** Constant Field Values

- NO_MORE_EVENTS

```java
public static final int NO_MORE_EVENTS
```

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete. This message indicates the print
job has no further information or communication with the print service.
This message should always be delivered if a terminal event
(completed/failed/canceled) is not delivered. For example, if messages
such as

JOB_COMPLETE

have NOT been received before receiving this
message, the only inference that should be drawn is that the print
service does not support delivering such an event.

**See Also:** Constant Field Values

- DATA_TRANSFER_COMPLETE

```java
public static final int DATA_TRANSFER_COMPLETE
```

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service. The client may free
data resources.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrintJobEvent

```java
public PrintJobEvent​(
DocPrintJob
source,
int reason)
```

Constructs a

PrintJobEvent

object.

**Parameters:** source

- a

DocPrintJob

object
**Parameters:** reason

- an int specifying the reason
**Throws:** IllegalArgumentException

- if

source

is

null

============ METHOD DETAIL ==========

- Method Detail

- getPrintEventType

```java
public int getPrintEventType()
```

Gets the reason for this event.

**Returns:** reason int

- getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determines the

DocPrintJob

to which this print job event
pertains.

**Returns:** the

DocPrintJob

object that represents the print job that
reports the events encapsulated by this

PrintJobEvent

Field Detail

- JOB_CANCELED

```java
public static final int JOB_CANCELED
```

The job was canceled by the

PrintService

.

**See Also:** Constant Field Values

- JOB_COMPLETE

```java
public static final int JOB_COMPLETE
```

The document is completely printed.

**See Also:** Constant Field Values

- JOB_FAILED

```java
public static final int JOB_FAILED
```

The print service reports that the job cannot be completed. The
application must resubmit the job.

**See Also:** Constant Field Values

- REQUIRES_ATTENTION

```java
public static final int REQUIRES_ATTENTION
```

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue. One
example of an event that can generate this message is when the printer
runs out of paper.

**See Also:** Constant Field Values

- NO_MORE_EVENTS

```java
public static final int NO_MORE_EVENTS
```

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete. This message indicates the print
job has no further information or communication with the print service.
This message should always be delivered if a terminal event
(completed/failed/canceled) is not delivered. For example, if messages
such as

JOB_COMPLETE

have NOT been received before receiving this
message, the only inference that should be drawn is that the print
service does not support delivering such an event.

**See Also:** Constant Field Values

- DATA_TRANSFER_COMPLETE

```java
public static final int DATA_TRANSFER_COMPLETE
```

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service. The client may free
data resources.

**See Also:** Constant Field Values

---

#### Field Detail

JOB_CANCELED

```java
public static final int JOB_CANCELED
```

The job was canceled by the

PrintService

.

**See Also:** Constant Field Values

---

#### JOB_CANCELED

public static final int JOB_CANCELED

The job was canceled by the

PrintService

.

JOB_COMPLETE

```java
public static final int JOB_COMPLETE
```

The document is completely printed.

**See Also:** Constant Field Values

---

#### JOB_COMPLETE

public static final int JOB_COMPLETE

The document is completely printed.

JOB_FAILED

```java
public static final int JOB_FAILED
```

The print service reports that the job cannot be completed. The
application must resubmit the job.

**See Also:** Constant Field Values

---

#### JOB_FAILED

public static final int JOB_FAILED

The print service reports that the job cannot be completed. The
application must resubmit the job.

REQUIRES_ATTENTION

```java
public static final int REQUIRES_ATTENTION
```

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue. One
example of an event that can generate this message is when the printer
runs out of paper.

**See Also:** Constant Field Values

---

#### REQUIRES_ATTENTION

public static final int REQUIRES_ATTENTION

The print service indicates that a - possibly transient - problem may
require external intervention before the print service can continue. One
example of an event that can generate this message is when the printer
runs out of paper.

NO_MORE_EVENTS

```java
public static final int NO_MORE_EVENTS
```

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete. This message indicates the print
job has no further information or communication with the print service.
This message should always be delivered if a terminal event
(completed/failed/canceled) is not delivered. For example, if messages
such as

JOB_COMPLETE

have NOT been received before receiving this
message, the only inference that should be drawn is that the print
service does not support delivering such an event.

**See Also:** Constant Field Values

---

#### NO_MORE_EVENTS

public static final int NO_MORE_EVENTS

Not all print services may be capable of delivering interesting events,
or even telling when a job is complete. This message indicates the print
job has no further information or communication with the print service.
This message should always be delivered if a terminal event
(completed/failed/canceled) is not delivered. For example, if messages
such as

JOB_COMPLETE

have NOT been received before receiving this
message, the only inference that should be drawn is that the print
service does not support delivering such an event.

DATA_TRANSFER_COMPLETE

```java
public static final int DATA_TRANSFER_COMPLETE
```

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service. The client may free
data resources.

**See Also:** Constant Field Values

---

#### DATA_TRANSFER_COMPLETE

public static final int DATA_TRANSFER_COMPLETE

The job is not necessarily printed yet, but the data has been transferred
successfully from the client to the print service. The client may free
data resources.

Constructor Detail

- PrintJobEvent

```java
public PrintJobEvent​(
DocPrintJob
source,
int reason)
```

Constructs a

PrintJobEvent

object.

**Parameters:** source

- a

DocPrintJob

object
**Parameters:** reason

- an int specifying the reason
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### Constructor Detail

PrintJobEvent

```java
public PrintJobEvent​(
DocPrintJob
source,
int reason)
```

Constructs a

PrintJobEvent

object.

**Parameters:** source

- a

DocPrintJob

object
**Parameters:** reason

- an int specifying the reason
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### PrintJobEvent

public PrintJobEvent​(

DocPrintJob

source,
int reason)

Constructs a

PrintJobEvent

object.

Method Detail

- getPrintEventType

```java
public int getPrintEventType()
```

Gets the reason for this event.

**Returns:** reason int

- getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determines the

DocPrintJob

to which this print job event
pertains.

**Returns:** the

DocPrintJob

object that represents the print job that
reports the events encapsulated by this

PrintJobEvent

---

#### Method Detail

getPrintEventType

```java
public int getPrintEventType()
```

Gets the reason for this event.

**Returns:** reason int

---

#### getPrintEventType

public int getPrintEventType()

Gets the reason for this event.

getPrintJob

```java
public
DocPrintJob
getPrintJob()
```

Determines the

DocPrintJob

to which this print job event
pertains.

**Returns:** the

DocPrintJob

object that represents the print job that
reports the events encapsulated by this

PrintJobEvent

---

#### getPrintJob

public

DocPrintJob

getPrintJob()

Determines the

DocPrintJob

to which this print job event
pertains.

---

