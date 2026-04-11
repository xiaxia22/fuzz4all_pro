# Interface DocPrintJob

**Source:** `java.desktop\javax\print\DocPrintJob.html`

### Class Description

```java
public interface
DocPrintJob
```

This interface represents a print job that can print a specified document
with a set of job attributes. An object implementing this interface is
obtained from a print service.

**All Known Subinterfaces:** CancelablePrintJob

,

MultiDocPrintJob

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### PrintService
getPrintService()

Determines the

PrintService

object to which this print job object
is bound.

**Returns:**
- PrintService

object

---

#### PrintJobAttributeSet
getAttributes()

Obtains this Print Job's set of printing attributes. The returned
attribute set object is unmodifiable. The returned attribute set object
is a "snapshot" of this Print Job's attribute set at the time of the

getAttributes()

method call; that is, the returned attribute
set's object's contents will not be updated if this Print Job's attribute
set's contents change in the future. To detect changes in attribute
values, call

getAttributes()

again and compare the new attribute
set to the previous attribute set; alternatively, register a listener for
print job events. The returned value may be an empty set but should not
be

null

.

**Returns:**
- the print job attributes

---

#### void addPrintJobListener​(
PrintJobListener
listener)

Registers a listener for event occurring during this print job. If
listener is

null

, no exception is thrown and no action is
performed. If listener is already registered, it will be registered
again.

**Parameters:**
- listener

- the object implementing the listener interface

**See Also:**
- removePrintJobListener(javax.print.event.PrintJobListener)

---

#### void removePrintJobListener​(
PrintJobListener
listener)

Removes a listener from this print job. This method performs no function,
nor does it throw an exception, if the listener specified by the argument
was not previously added to this print job. If listener is

null

,
no exception is thrown and no action is performed. If a listener was
registered more than once only one of the registrations will be removed.

**Parameters:**
- listener

- the object implementing the listener interface

**See Also:**
- addPrintJobListener(javax.print.event.PrintJobListener)

---

#### void addPrintJobAttributeListener​(
PrintJobAttributeListener
listener,

PrintJobAttributeSet
attributes)

Registers a listener for changes in the specified attributes. If listener
is

null

, no exception is thrown and no action is performed. To
determine the attribute updates that may be reported by this job, a
client can call

getAttributes()

and identify the subset that are
interesting and likely to be reported to the listener. Clients expecting
to be updated about changes in a specific job attribute should verify it
is in that set, but updates about an attribute will be made only if it
changes and this is detected by the job. Also updates may be subject to
batching by the job. To minimize overhead in print job processing it is
recommended to listen on only that subset of attributes which are likely
to change. If the specified set is empty no attribute updates will be
reported to the listener. If the attribute set is

null

, then this
means to listen on all dynamic attributes that the job supports. This may
result in no update notifications if a job can not report any attribute
updates.

If listener is already registered, it will be registered again.

**Parameters:**
- listener

- the object implementing the listener interface
- attributes

- the attributes to listen on, or

null

to mean
all attributes that can change, as determined by the job

**See Also:**
- removePrintJobAttributeListener(javax.print.event.PrintJobAttributeListener)

---

#### void removePrintJobAttributeListener​(
PrintJobAttributeListener
listener)

Removes an attribute listener from this print job. This method performs
no function, nor does it throw an exception, if the listener specified by
the argument was not previously added to this print job. If the listener
is

null

, no exception is thrown and no action is performed. If a
listener is registered more than once, even for a different set of
attributes, no guarantee is made which listener is removed.

**Parameters:**
- listener

- the object implementing the listener interface

**See Also:**
- addPrintJobAttributeListener(javax.print.event.PrintJobAttributeListener, javax.print.attribute.PrintJobAttributeSet)

---

#### void print​(
Doc
doc,

PrintRequestAttributeSet
attributes)
throws
PrintException

Prints a document with the specified job attributes. This method should
only be called once for a given print job. Calling it again will not
result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
When the print method returns, printing may not yet have completed as
printing may happen asynchronously, perhaps in a different thread.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

**Parameters:**
- doc

- the document to be printed. It must be a flavor supported by
this PrintJob.
- attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.

**Throws:**
- PrintException

- the exception additionally may implement an
interface that more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

### Additional Sections

#### Interface DocPrintJob

**All Known Subinterfaces:** CancelablePrintJob

,

MultiDocPrintJob

```java
public interface
DocPrintJob
```

This interface represents a print job that can print a specified document
with a set of job attributes. An object implementing this interface is
obtained from a print service.

public interface

DocPrintJob

This interface represents a print job that can print a specified document
with a set of job attributes. An object implementing this interface is
obtained from a print service.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPrintJobAttributeListener

​(

PrintJobAttributeListener

listener,

PrintJobAttributeSet

attributes)

Registers a listener for changes in the specified attributes.

void

addPrintJobListener

​(

PrintJobListener

listener)

Registers a listener for event occurring during this print job.

PrintJobAttributeSet

getAttributes

()

Obtains this Print Job's set of printing attributes.

PrintService

getPrintService

()

Determines the

PrintService

object to which this print job object
is bound.

void

print

​(

Doc

doc,

PrintRequestAttributeSet

attributes)

Prints a document with the specified job attributes.

void

removePrintJobAttributeListener

​(

PrintJobAttributeListener

listener)

Removes an attribute listener from this print job.

void

removePrintJobListener

​(

PrintJobListener

listener)

Removes a listener from this print job.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPrintJobAttributeListener

​(

PrintJobAttributeListener

listener,

PrintJobAttributeSet

attributes)

Registers a listener for changes in the specified attributes.

void

addPrintJobListener

​(

PrintJobListener

listener)

Registers a listener for event occurring during this print job.

PrintJobAttributeSet

getAttributes

()

Obtains this Print Job's set of printing attributes.

PrintService

getPrintService

()

Determines the

PrintService

object to which this print job object
is bound.

void

print

​(

Doc

doc,

PrintRequestAttributeSet

attributes)

Prints a document with the specified job attributes.

void

removePrintJobAttributeListener

​(

PrintJobAttributeListener

listener)

Removes an attribute listener from this print job.

void

removePrintJobListener

​(

PrintJobListener

listener)

Removes a listener from this print job.

---

#### Method Summary

Registers a listener for changes in the specified attributes.

Registers a listener for event occurring during this print job.

Obtains this Print Job's set of printing attributes.

Determines the

PrintService

object to which this print job object
is bound.

Prints a document with the specified job attributes.

Removes an attribute listener from this print job.

Removes a listener from this print job.

============ METHOD DETAIL ==========

- Method Detail

- getPrintService

```java
PrintService
getPrintService()
```

Determines the

PrintService

object to which this print job object
is bound.

**Returns:** PrintService

object

- getAttributes

```java
PrintJobAttributeSet
getAttributes()
```

Obtains this Print Job's set of printing attributes. The returned
attribute set object is unmodifiable. The returned attribute set object
is a "snapshot" of this Print Job's attribute set at the time of the

getAttributes()

method call; that is, the returned attribute
set's object's contents will not be updated if this Print Job's attribute
set's contents change in the future. To detect changes in attribute
values, call

getAttributes()

again and compare the new attribute
set to the previous attribute set; alternatively, register a listener for
print job events. The returned value may be an empty set but should not
be

null

.

**Returns:** the print job attributes

- addPrintJobListener

```java
void addPrintJobListener​(
PrintJobListener
listener)
```

Registers a listener for event occurring during this print job. If
listener is

null

, no exception is thrown and no action is
performed. If listener is already registered, it will be registered
again.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** removePrintJobListener(javax.print.event.PrintJobListener)

- removePrintJobListener

```java
void removePrintJobListener​(
PrintJobListener
listener)
```

Removes a listener from this print job. This method performs no function,
nor does it throw an exception, if the listener specified by the argument
was not previously added to this print job. If listener is

null

,
no exception is thrown and no action is performed. If a listener was
registered more than once only one of the registrations will be removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobListener(javax.print.event.PrintJobListener)

- addPrintJobAttributeListener

```java
void addPrintJobAttributeListener​(
PrintJobAttributeListener
listener,

PrintJobAttributeSet
attributes)
```

Registers a listener for changes in the specified attributes. If listener
is

null

, no exception is thrown and no action is performed. To
determine the attribute updates that may be reported by this job, a
client can call

getAttributes()

and identify the subset that are
interesting and likely to be reported to the listener. Clients expecting
to be updated about changes in a specific job attribute should verify it
is in that set, but updates about an attribute will be made only if it
changes and this is detected by the job. Also updates may be subject to
batching by the job. To minimize overhead in print job processing it is
recommended to listen on only that subset of attributes which are likely
to change. If the specified set is empty no attribute updates will be
reported to the listener. If the attribute set is

null

, then this
means to listen on all dynamic attributes that the job supports. This may
result in no update notifications if a job can not report any attribute
updates.

If listener is already registered, it will be registered again.

**Parameters:** listener

- the object implementing the listener interface
**Parameters:** attributes

- the attributes to listen on, or

null

to mean
all attributes that can change, as determined by the job
**See Also:** removePrintJobAttributeListener(javax.print.event.PrintJobAttributeListener)

- removePrintJobAttributeListener

```java
void removePrintJobAttributeListener​(
PrintJobAttributeListener
listener)
```

Removes an attribute listener from this print job. This method performs
no function, nor does it throw an exception, if the listener specified by
the argument was not previously added to this print job. If the listener
is

null

, no exception is thrown and no action is performed. If a
listener is registered more than once, even for a different set of
attributes, no guarantee is made which listener is removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobAttributeListener(javax.print.event.PrintJobAttributeListener, javax.print.attribute.PrintJobAttributeSet)

- print

```java
void print​(
Doc
doc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Prints a document with the specified job attributes. This method should
only be called once for a given print job. Calling it again will not
result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
When the print method returns, printing may not yet have completed as
printing may happen asynchronously, perhaps in a different thread.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

**Parameters:** doc

- the document to be printed. It must be a flavor supported by
this PrintJob.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interface that more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

Method Detail

- getPrintService

```java
PrintService
getPrintService()
```

Determines the

PrintService

object to which this print job object
is bound.

**Returns:** PrintService

object

- getAttributes

```java
PrintJobAttributeSet
getAttributes()
```

Obtains this Print Job's set of printing attributes. The returned
attribute set object is unmodifiable. The returned attribute set object
is a "snapshot" of this Print Job's attribute set at the time of the

getAttributes()

method call; that is, the returned attribute
set's object's contents will not be updated if this Print Job's attribute
set's contents change in the future. To detect changes in attribute
values, call

getAttributes()

again and compare the new attribute
set to the previous attribute set; alternatively, register a listener for
print job events. The returned value may be an empty set but should not
be

null

.

**Returns:** the print job attributes

- addPrintJobListener

```java
void addPrintJobListener​(
PrintJobListener
listener)
```

Registers a listener for event occurring during this print job. If
listener is

null

, no exception is thrown and no action is
performed. If listener is already registered, it will be registered
again.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** removePrintJobListener(javax.print.event.PrintJobListener)

- removePrintJobListener

```java
void removePrintJobListener​(
PrintJobListener
listener)
```

Removes a listener from this print job. This method performs no function,
nor does it throw an exception, if the listener specified by the argument
was not previously added to this print job. If listener is

null

,
no exception is thrown and no action is performed. If a listener was
registered more than once only one of the registrations will be removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobListener(javax.print.event.PrintJobListener)

- addPrintJobAttributeListener

```java
void addPrintJobAttributeListener​(
PrintJobAttributeListener
listener,

PrintJobAttributeSet
attributes)
```

Registers a listener for changes in the specified attributes. If listener
is

null

, no exception is thrown and no action is performed. To
determine the attribute updates that may be reported by this job, a
client can call

getAttributes()

and identify the subset that are
interesting and likely to be reported to the listener. Clients expecting
to be updated about changes in a specific job attribute should verify it
is in that set, but updates about an attribute will be made only if it
changes and this is detected by the job. Also updates may be subject to
batching by the job. To minimize overhead in print job processing it is
recommended to listen on only that subset of attributes which are likely
to change. If the specified set is empty no attribute updates will be
reported to the listener. If the attribute set is

null

, then this
means to listen on all dynamic attributes that the job supports. This may
result in no update notifications if a job can not report any attribute
updates.

If listener is already registered, it will be registered again.

**Parameters:** listener

- the object implementing the listener interface
**Parameters:** attributes

- the attributes to listen on, or

null

to mean
all attributes that can change, as determined by the job
**See Also:** removePrintJobAttributeListener(javax.print.event.PrintJobAttributeListener)

- removePrintJobAttributeListener

```java
void removePrintJobAttributeListener​(
PrintJobAttributeListener
listener)
```

Removes an attribute listener from this print job. This method performs
no function, nor does it throw an exception, if the listener specified by
the argument was not previously added to this print job. If the listener
is

null

, no exception is thrown and no action is performed. If a
listener is registered more than once, even for a different set of
attributes, no guarantee is made which listener is removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobAttributeListener(javax.print.event.PrintJobAttributeListener, javax.print.attribute.PrintJobAttributeSet)

- print

```java
void print​(
Doc
doc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Prints a document with the specified job attributes. This method should
only be called once for a given print job. Calling it again will not
result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
When the print method returns, printing may not yet have completed as
printing may happen asynchronously, perhaps in a different thread.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

**Parameters:** doc

- the document to be printed. It must be a flavor supported by
this PrintJob.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interface that more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

#### Method Detail

getPrintService

```java
PrintService
getPrintService()
```

Determines the

PrintService

object to which this print job object
is bound.

**Returns:** PrintService

object

---

#### getPrintService

PrintService

getPrintService()

Determines the

PrintService

object to which this print job object
is bound.

getAttributes

```java
PrintJobAttributeSet
getAttributes()
```

Obtains this Print Job's set of printing attributes. The returned
attribute set object is unmodifiable. The returned attribute set object
is a "snapshot" of this Print Job's attribute set at the time of the

getAttributes()

method call; that is, the returned attribute
set's object's contents will not be updated if this Print Job's attribute
set's contents change in the future. To detect changes in attribute
values, call

getAttributes()

again and compare the new attribute
set to the previous attribute set; alternatively, register a listener for
print job events. The returned value may be an empty set but should not
be

null

.

**Returns:** the print job attributes

---

#### getAttributes

PrintJobAttributeSet

getAttributes()

Obtains this Print Job's set of printing attributes. The returned
attribute set object is unmodifiable. The returned attribute set object
is a "snapshot" of this Print Job's attribute set at the time of the

getAttributes()

method call; that is, the returned attribute
set's object's contents will not be updated if this Print Job's attribute
set's contents change in the future. To detect changes in attribute
values, call

getAttributes()

again and compare the new attribute
set to the previous attribute set; alternatively, register a listener for
print job events. The returned value may be an empty set but should not
be

null

.

addPrintJobListener

```java
void addPrintJobListener​(
PrintJobListener
listener)
```

Registers a listener for event occurring during this print job. If
listener is

null

, no exception is thrown and no action is
performed. If listener is already registered, it will be registered
again.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** removePrintJobListener(javax.print.event.PrintJobListener)

---

#### addPrintJobListener

void addPrintJobListener​(

PrintJobListener

listener)

Registers a listener for event occurring during this print job. If
listener is

null

, no exception is thrown and no action is
performed. If listener is already registered, it will be registered
again.

removePrintJobListener

```java
void removePrintJobListener​(
PrintJobListener
listener)
```

Removes a listener from this print job. This method performs no function,
nor does it throw an exception, if the listener specified by the argument
was not previously added to this print job. If listener is

null

,
no exception is thrown and no action is performed. If a listener was
registered more than once only one of the registrations will be removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobListener(javax.print.event.PrintJobListener)

---

#### removePrintJobListener

void removePrintJobListener​(

PrintJobListener

listener)

Removes a listener from this print job. This method performs no function,
nor does it throw an exception, if the listener specified by the argument
was not previously added to this print job. If listener is

null

,
no exception is thrown and no action is performed. If a listener was
registered more than once only one of the registrations will be removed.

addPrintJobAttributeListener

```java
void addPrintJobAttributeListener​(
PrintJobAttributeListener
listener,

PrintJobAttributeSet
attributes)
```

Registers a listener for changes in the specified attributes. If listener
is

null

, no exception is thrown and no action is performed. To
determine the attribute updates that may be reported by this job, a
client can call

getAttributes()

and identify the subset that are
interesting and likely to be reported to the listener. Clients expecting
to be updated about changes in a specific job attribute should verify it
is in that set, but updates about an attribute will be made only if it
changes and this is detected by the job. Also updates may be subject to
batching by the job. To minimize overhead in print job processing it is
recommended to listen on only that subset of attributes which are likely
to change. If the specified set is empty no attribute updates will be
reported to the listener. If the attribute set is

null

, then this
means to listen on all dynamic attributes that the job supports. This may
result in no update notifications if a job can not report any attribute
updates.

If listener is already registered, it will be registered again.

**Parameters:** listener

- the object implementing the listener interface
**Parameters:** attributes

- the attributes to listen on, or

null

to mean
all attributes that can change, as determined by the job
**See Also:** removePrintJobAttributeListener(javax.print.event.PrintJobAttributeListener)

---

#### addPrintJobAttributeListener

void addPrintJobAttributeListener​(

PrintJobAttributeListener

listener,

PrintJobAttributeSet

attributes)

Registers a listener for changes in the specified attributes. If listener
is

null

, no exception is thrown and no action is performed. To
determine the attribute updates that may be reported by this job, a
client can call

getAttributes()

and identify the subset that are
interesting and likely to be reported to the listener. Clients expecting
to be updated about changes in a specific job attribute should verify it
is in that set, but updates about an attribute will be made only if it
changes and this is detected by the job. Also updates may be subject to
batching by the job. To minimize overhead in print job processing it is
recommended to listen on only that subset of attributes which are likely
to change. If the specified set is empty no attribute updates will be
reported to the listener. If the attribute set is

null

, then this
means to listen on all dynamic attributes that the job supports. This may
result in no update notifications if a job can not report any attribute
updates.

If listener is already registered, it will be registered again.

If listener is already registered, it will be registered again.

removePrintJobAttributeListener

```java
void removePrintJobAttributeListener​(
PrintJobAttributeListener
listener)
```

Removes an attribute listener from this print job. This method performs
no function, nor does it throw an exception, if the listener specified by
the argument was not previously added to this print job. If the listener
is

null

, no exception is thrown and no action is performed. If a
listener is registered more than once, even for a different set of
attributes, no guarantee is made which listener is removed.

**Parameters:** listener

- the object implementing the listener interface
**See Also:** addPrintJobAttributeListener(javax.print.event.PrintJobAttributeListener, javax.print.attribute.PrintJobAttributeSet)

---

#### removePrintJobAttributeListener

void removePrintJobAttributeListener​(

PrintJobAttributeListener

listener)

Removes an attribute listener from this print job. This method performs
no function, nor does it throw an exception, if the listener specified by
the argument was not previously added to this print job. If the listener
is

null

, no exception is thrown and no action is performed. If a
listener is registered more than once, even for a different set of
attributes, no guarantee is made which listener is removed.

print

```java
void print​(
Doc
doc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Prints a document with the specified job attributes. This method should
only be called once for a given print job. Calling it again will not
result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
When the print method returns, printing may not yet have completed as
printing may happen asynchronously, perhaps in a different thread.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

**Parameters:** doc

- the document to be printed. It must be a flavor supported by
this PrintJob.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interface that more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

#### print

void print​(

Doc

doc,

PrintRequestAttributeSet

attributes)
throws

PrintException

Prints a document with the specified job attributes. This method should
only be called once for a given print job. Calling it again will not
result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
When the print method returns, printing may not yet have completed as
printing may happen asynchronously, perhaps in a different thread.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

Print service implementors should close any print data streams (ie

Reader

or

InputStream

implementations) that they obtain
from the client doc. Robust clients may still wish to verify this. An
exception is always generated if a

DocFlavor

cannot be printed.

FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

