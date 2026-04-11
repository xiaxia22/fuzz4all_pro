# Class PrintJobAdapter

**Source:** `java.desktop\javax\print\event\PrintJobAdapter.html`

### Class Description

```java
public abstract class
PrintJobAdapter

extends
Object

implements
PrintJobListener
```

An abstract adapter class for receiving print job events. The methods in this
class are empty. This class exists as a convenience for creating listener
objects. Extend this class to create a

PrintJobEvent

listener and
override the methods for the events of interest. Unlike the

ComponentListener

interface, this
abstract interface provides empty methods so that you only need to define the
methods you need, rather than all of the methods.

**All Implemented Interfaces:** PrintJobListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintJobAdapter()

*No description found.*

---

### Method Details

#### public void printDataTransferCompleted​(
PrintJobEvent
pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event.

**Specified by:**
- printDataTransferCompleted

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

#### public void printJobCompleted​(
PrintJobEvent
pje)

Called to notify the client that the job completed successfully.

**Specified by:**
- printJobCompleted

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

#### public void printJobFailed​(
PrintJobEvent
pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Specified by:**
- printJobFailed

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

#### public void printJobCanceled​(
PrintJobEvent
pje)

Called to notify the client that the job was canceled by user or program.

**Specified by:**
- printJobCanceled

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

#### public void printJobNoMoreEvents​(
PrintJobEvent
pje)

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Specified by:**
- printJobNoMoreEvents

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

#### public void printJobRequiresAttention​(
PrintJobEvent
pje)

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

**Specified by:**
- printJobRequiresAttention

in interface

PrintJobListener

**Parameters:**
- pje

- the event being notified

---

### Additional Sections

#### Class PrintJobAdapter

java.lang.Object

- javax.print.event.PrintJobAdapter

javax.print.event.PrintJobAdapter

**All Implemented Interfaces:** PrintJobListener

```java
public abstract class
PrintJobAdapter

extends
Object

implements
PrintJobListener
```

An abstract adapter class for receiving print job events. The methods in this
class are empty. This class exists as a convenience for creating listener
objects. Extend this class to create a

PrintJobEvent

listener and
override the methods for the events of interest. Unlike the

ComponentListener

interface, this
abstract interface provides empty methods so that you only need to define the
methods you need, rather than all of the methods.

public abstract class

PrintJobAdapter

extends

Object

implements

PrintJobListener

An abstract adapter class for receiving print job events. The methods in this
class are empty. This class exists as a convenience for creating listener
objects. Extend this class to create a

PrintJobEvent

listener and
override the methods for the events of interest. Unlike the

ComponentListener

interface, this
abstract interface provides empty methods so that you only need to define the
methods you need, rather than all of the methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrintJobAdapter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

printDataTransferCompleted

​(

PrintJobEvent

pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data.

void

printJobCanceled

​(

PrintJobEvent

pje)

Called to notify the client that the job was canceled by user or program.

void

printJobCompleted

​(

PrintJobEvent

pje)

Called to notify the client that the job completed successfully.

void

printJobFailed

​(

PrintJobEvent

pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

void

printJobNoMoreEvents

​(

PrintJobEvent

pje)

Called to notify the client that no more events will be delivered.

void

printJobRequiresAttention

​(

PrintJobEvent

pje)

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

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

PrintJobAdapter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

printDataTransferCompleted

​(

PrintJobEvent

pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data.

void

printJobCanceled

​(

PrintJobEvent

pje)

Called to notify the client that the job was canceled by user or program.

void

printJobCompleted

​(

PrintJobEvent

pje)

Called to notify the client that the job completed successfully.

void

printJobFailed

​(

PrintJobEvent

pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

void

printJobNoMoreEvents

​(

PrintJobEvent

pje)

Called to notify the client that no more events will be delivered.

void

printJobRequiresAttention

​(

PrintJobEvent

pje)

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

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

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data.

Called to notify the client that the job was canceled by user or program.

Called to notify the client that the job completed successfully.

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

Called to notify the client that no more events will be delivered.

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

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

- PrintJobAdapter

```java
public PrintJobAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- printDataTransferCompleted

```java
public void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event.

**Specified by:** printDataTransferCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobCompleted

```java
public void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Specified by:** printJobCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobFailed

```java
public void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Specified by:** printJobFailed

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobCanceled

```java
public void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by user or program.

**Specified by:** printJobCanceled

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobNoMoreEvents

```java
public void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Specified by:** printJobNoMoreEvents

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobRequiresAttention

```java
public void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

**Specified by:** printJobRequiresAttention

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

Constructor Detail

- PrintJobAdapter

```java
public PrintJobAdapter()
```

---

#### Constructor Detail

PrintJobAdapter

```java
public PrintJobAdapter()
```

---

#### PrintJobAdapter

public PrintJobAdapter()

Method Detail

- printDataTransferCompleted

```java
public void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event.

**Specified by:** printDataTransferCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobCompleted

```java
public void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Specified by:** printJobCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobFailed

```java
public void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Specified by:** printJobFailed

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobCanceled

```java
public void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by user or program.

**Specified by:** printJobCanceled

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobNoMoreEvents

```java
public void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Specified by:** printJobNoMoreEvents

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

- printJobRequiresAttention

```java
public void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

**Specified by:** printJobRequiresAttention

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### Method Detail

printDataTransferCompleted

```java
public void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event.

**Specified by:** printDataTransferCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printDataTransferCompleted

public void printDataTransferCompleted​(

PrintJobEvent

pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event.

printJobCompleted

```java
public void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Specified by:** printJobCompleted

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printJobCompleted

public void printJobCompleted​(

PrintJobEvent

pje)

Called to notify the client that the job completed successfully.

printJobFailed

```java
public void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Specified by:** printJobFailed

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printJobFailed

public void printJobFailed​(

PrintJobEvent

pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

printJobCanceled

```java
public void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by user or program.

**Specified by:** printJobCanceled

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printJobCanceled

public void printJobCanceled​(

PrintJobEvent

pje)

Called to notify the client that the job was canceled by user or program.

printJobNoMoreEvents

```java
public void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Specified by:** printJobNoMoreEvents

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printJobNoMoreEvents

public void printJobNoMoreEvents​(

PrintJobEvent

pje)

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

printJobRequiresAttention

```java
public void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

**Specified by:** printJobRequiresAttention

in interface

PrintJobListener
**Parameters:** pje

- the event being notified

---

#### printJobRequiresAttention

public void printJobRequiresAttention​(

PrintJobEvent

pje)

Called to notify the client that some possibly user rectifiable problem
occurs (eg printer out of paper).

---

