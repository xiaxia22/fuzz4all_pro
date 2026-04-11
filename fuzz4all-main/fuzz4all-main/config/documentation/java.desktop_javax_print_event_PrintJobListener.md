# Interface PrintJobListener

**Source:** `java.desktop\javax\print\event\PrintJobListener.html`

### Class Description

```java
public interface
PrintJobListener
```

Implementations of this listener interface should be attached to a

DocPrintJob

to monitor the status of the
printer job. These callback methods may be invoked on the thread processing
the print job, or a service created notification thread. In either case the
client should not perform lengthy processing in these callbacks.

**All Known Implementing Classes:** PrintJobAdapter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void printDataTransferCompleted​(
PrintJobEvent
pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event. If this event is not
received the client should wait for a terminal event
(completed/canceled/failed) before freeing the resources.

**Parameters:**
- pje

- the job generating this event

---

#### void printJobCompleted​(
PrintJobEvent
pje)

Called to notify the client that the job completed successfully.

**Parameters:**
- pje

- the job generating this event

---

#### void printJobFailed​(
PrintJobEvent
pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Parameters:**
- pje

- the job generating this event

---

#### void printJobCanceled​(
PrintJobEvent
pje)

Called to notify the client that the job was canceled by a user or a
program.

**Parameters:**
- pje

- the job generating this event

---

#### void printJobNoMoreEvents​(
PrintJobEvent
pje)

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Parameters:**
- pje

- the job generating this event

---

#### void printJobRequiresAttention​(
PrintJobEvent
pje)

Called to notify the client that an error has occurred that the user
might be able to fix. One example of an error that can generate this
event is when the printer runs out of paper.

**Parameters:**
- pje

- the job generating this event

---

### Additional Sections

#### Interface PrintJobListener

**All Known Implementing Classes:** PrintJobAdapter

```java
public interface
PrintJobListener
```

Implementations of this listener interface should be attached to a

DocPrintJob

to monitor the status of the
printer job. These callback methods may be invoked on the thread processing
the print job, or a service created notification thread. In either case the
client should not perform lengthy processing in these callbacks.

public interface

PrintJobListener

Implementations of this listener interface should be attached to a

DocPrintJob

to monitor the status of the
printer job. These callback methods may be invoked on the thread processing
the print job, or a service created notification thread. In either case the
client should not perform lengthy processing in these callbacks.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

Called to notify the client that the job was canceled by a user or a
program.

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

Called to notify the client that an error has occurred that the user
might be able to fix.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

Called to notify the client that the job was canceled by a user or a
program.

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

Called to notify the client that an error has occurred that the user
might be able to fix.

---

#### Method Summary

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data.

Called to notify the client that the job was canceled by a user or a
program.

Called to notify the client that the job completed successfully.

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

Called to notify the client that no more events will be delivered.

Called to notify the client that an error has occurred that the user
might be able to fix.

============ METHOD DETAIL ==========

- Method Detail

- printDataTransferCompleted

```java
void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event. If this event is not
received the client should wait for a terminal event
(completed/canceled/failed) before freeing the resources.

**Parameters:** pje

- the job generating this event

- printJobCompleted

```java
void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Parameters:** pje

- the job generating this event

- printJobFailed

```java
void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Parameters:** pje

- the job generating this event

- printJobCanceled

```java
void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by a user or a
program.

**Parameters:** pje

- the job generating this event

- printJobNoMoreEvents

```java
void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Parameters:** pje

- the job generating this event

- printJobRequiresAttention

```java
void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that an error has occurred that the user
might be able to fix. One example of an error that can generate this
event is when the printer runs out of paper.

**Parameters:** pje

- the job generating this event

Method Detail

- printDataTransferCompleted

```java
void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event. If this event is not
received the client should wait for a terminal event
(completed/canceled/failed) before freeing the resources.

**Parameters:** pje

- the job generating this event

- printJobCompleted

```java
void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Parameters:** pje

- the job generating this event

- printJobFailed

```java
void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Parameters:** pje

- the job generating this event

- printJobCanceled

```java
void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by a user or a
program.

**Parameters:** pje

- the job generating this event

- printJobNoMoreEvents

```java
void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Parameters:** pje

- the job generating this event

- printJobRequiresAttention

```java
void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that an error has occurred that the user
might be able to fix. One example of an error that can generate this
event is when the printer runs out of paper.

**Parameters:** pje

- the job generating this event

---

#### Method Detail

printDataTransferCompleted

```java
void printDataTransferCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event. If this event is not
received the client should wait for a terminal event
(completed/canceled/failed) before freeing the resources.

**Parameters:** pje

- the job generating this event

---

#### printDataTransferCompleted

void printDataTransferCompleted​(

PrintJobEvent

pje)

Called to notify the client that data has been successfully transferred
to the print service, and the client may free local resources allocated
for that data. The client should not assume that the data has been
completely printed after receiving this event. If this event is not
received the client should wait for a terminal event
(completed/canceled/failed) before freeing the resources.

printJobCompleted

```java
void printJobCompleted​(
PrintJobEvent
pje)
```

Called to notify the client that the job completed successfully.

**Parameters:** pje

- the job generating this event

---

#### printJobCompleted

void printJobCompleted​(

PrintJobEvent

pje)

Called to notify the client that the job completed successfully.

printJobFailed

```java
void printJobFailed​(
PrintJobEvent
pje)
```

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

**Parameters:** pje

- the job generating this event

---

#### printJobFailed

void printJobFailed​(

PrintJobEvent

pje)

Called to notify the client that the job failed to complete successfully
and will have to be resubmitted.

printJobCanceled

```java
void printJobCanceled​(
PrintJobEvent
pje)
```

Called to notify the client that the job was canceled by a user or a
program.

**Parameters:** pje

- the job generating this event

---

#### printJobCanceled

void printJobCanceled​(

PrintJobEvent

pje)

Called to notify the client that the job was canceled by a user or a
program.

printJobNoMoreEvents

```java
void printJobNoMoreEvents​(
PrintJobEvent
pje)
```

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

**Parameters:** pje

- the job generating this event

---

#### printJobNoMoreEvents

void printJobNoMoreEvents​(

PrintJobEvent

pje)

Called to notify the client that no more events will be delivered. One
cause of this event being generated is if the job has successfully
completed, but the printing system is limited in capability and cannot
verify this. This event is required to be delivered if none of the other
terminal events (completed/failed/canceled) are delivered.

printJobRequiresAttention

```java
void printJobRequiresAttention​(
PrintJobEvent
pje)
```

Called to notify the client that an error has occurred that the user
might be able to fix. One example of an error that can generate this
event is when the printer runs out of paper.

**Parameters:** pje

- the job generating this event

---

#### printJobRequiresAttention

void printJobRequiresAttention​(

PrintJobEvent

pje)

Called to notify the client that an error has occurred that the user
might be able to fix. One example of an error that can generate this
event is when the printer runs out of paper.

---

